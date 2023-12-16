import datetime
import os
import tempfile
from typing import List, Dict, Union

import flask
import yaml

import jinja2.exceptions
from flask import request, redirect, url_for, render_template, Response, session, abort, send_from_directory
from pony.orm import count, commit, db_session

from worlds.AutoWorld import AutoWorldRegister
import Options
from . import app, cache
from .models import Seed, Room, Command, UUID, uuid4


def get_world_theme(game_name: str):
    if game_name in AutoWorldRegister.world_types:
        return AutoWorldRegister.world_types[game_name].web.theme
    return 'grass'


@app.before_request
def register_session():
    session.permanent = True  # technically 31 days after the last visit
    if not session.get("_id", None):
        session["_id"] = uuid4()  # uniquely identify each session without needing a login


@app.errorhandler(404)
@app.errorhandler(jinja2.exceptions.TemplateNotFound)
def page_not_found(err):
    return render_template('404.html'), 404


# Start Playing Page
@app.route('/start-playing')
@cache.cached()
def start_playing():
    return render_template(f"startPlaying.html")


# TODO for back compat. remove around 0.4.5
@app.route("/weighted-settings")
def weighted_settings():
    return redirect("weighted-options", 301)


@app.route("/weighted-options")
@cache.cached()
def weighted_options():
    return render_template("weighted-options.html")


# TODO for back compat. remove around 0.4.5
@app.route("/games/<string:game>/player-settings")
def player_settings(game: str):
    return redirect(url_for("player_options", game=game), 301)


# Player options pages
@app.route("/games/<string:game>/player-options")
@cache.cached()
def player_options(game: str, message: str = None):
    world = AutoWorldRegister.world_types[game]
    all_options: Dict[str, Options.AssembleOptions] = world.options_dataclass.type_hints
    grouped_options = {}
    for option_name, option in all_options.items():
        if issubclass(option, (Options.ItemDict, Options.ItemSet)) and not option.verify_item_name:
            continue

        if issubclass(option, Options.LocationSet) and not option.verify_location_name:
            continue

        if issubclass(option, (Options.OptionList, Options.OptionSet)) and not hasattr(option, "valid_keys"):
            continue

        grouped_options.setdefault(getattr(option, "group_name", "Game Options"), {})[option_name] = option

    return render_template(
        "playerOptions/playerOptions.html",
        message=message,
        game=game,
        world=world,
        option_groups=grouped_options,
        issubclass=issubclass,
        Options=Options,
        theme=get_world_theme(game),
    )


# YAML generator for player-options
@app.route("/games/<string:game>/generate-yaml", methods=["POST"])
def generate_yaml(game):
    if request.method == "POST":
        options = {"game": game}
        for key, val in request.form.items(multi=True):
            if key in options:
                if not isinstance(options[key], list):
                    options[key] = [options[key]]
                options[key].append(val)
            else:
                options[key] = val

        # Detect and build ItemDict options from their name pattern
        for key, val in options.copy().items():
            key_parts = key.rsplit("||", 2)
            if key_parts[-1] == "qty":
                if key_parts[0] not in options:
                    options[key_parts[0]] = {}
                options[key_parts[0]][key_parts[1]] = val
                del options[key]

        # Error checking
        if not options["name"]:
            return "Player name is required."

        # Remove POST data irrelevant to YAML
        if "intent-generate" in options:
            del options["intent-generate"]
        if "intent-export" in options:
            del options["intent-export"]

        response = flask.Response(yaml.dump(options))
        response.headers["Content-Type"] = "text/yaml"
        response.headers["Content-Disposition"] = f"attachment; filename={options['name']}"
        return response


# Game Info Pages
@app.route('/games/<string:game>/info/<string:lang>')
@cache.cached()
def game_info(game, lang):
    return render_template('gameInfo.html', game=game, lang=lang, theme=get_world_theme(game))


# List of supported games
@app.route('/games')
@cache.cached()
def games():
    worlds = {}
    for game, world in AutoWorldRegister.world_types.items():
        if not world.hidden:
            worlds[game] = world
    return render_template("supportedGames.html", worlds=worlds)


@app.route('/tutorial/<string:game>/<string:file>/<string:lang>')
@cache.cached()
def tutorial(game, file, lang):
    return render_template("tutorial.html", game=game, file=file, lang=lang, theme=get_world_theme(game))


@app.route('/tutorial/')
@cache.cached()
def tutorial_landing():
    return render_template("tutorialLanding.html")


@app.route('/faq/<string:lang>/')
@cache.cached()
def faq(lang):
    return render_template("faq.html", lang=lang)


@app.route('/glossary/<string:lang>/')
@cache.cached()
def terms(lang):
    return render_template("glossary.html", lang=lang)


@app.route('/seed/<suuid:seed>')
def view_seed(seed: UUID):
    seed = Seed.get(id=seed)
    if not seed:
        abort(404)
    return render_template("viewSeed.html", seed=seed, slot_count=count(seed.slots))


@app.route('/new_room/<suuid:seed>')
def new_room(seed: UUID):
    seed = Seed.get(id=seed)
    if not seed:
        abort(404)
    room = Room(seed=seed, owner=session["_id"], tracker=uuid4())
    commit()
    return redirect(url_for("host_room", room=room.id))


def _read_log(path: str):
    if os.path.exists(path):
        with open(path, encoding="utf-8-sig") as log:
            yield from log
    else:
        yield f"Logfile {path} does not exist. " \
              f"Likely a crash during spinup of multiworld instance or it is still spinning up."


@app.route('/log/<suuid:room>')
def display_log(room: UUID):
    room = Room.get(id=room)
    if room is None:
        return abort(404)
    if room.owner == session["_id"]:
        file_path = os.path.join("logs", str(room.id) + ".txt")
        if os.path.exists(file_path):
            return Response(_read_log(file_path), mimetype="text/plain;charset=UTF-8")
        return "Log File does not exist."

    return "Access Denied", 403


@app.route('/room/<suuid:room>', methods=['GET', 'POST'])
def host_room(room: UUID):
    room: Room = Room.get(id=room)
    if room is None:
        return abort(404)
    if request.method == "POST":
        if room.owner == session["_id"]:
            cmd = request.form["cmd"]
            if cmd:
                Command(room=room, commandtext=cmd)
                commit()

    now = datetime.datetime.utcnow()
    # indicate that the page should reload to get the assigned port
    should_refresh = not room.last_port and now - room.creation_time < datetime.timedelta(seconds=3)
    with db_session:
        room.last_activity = now  # will trigger a spinup, if it's not already running

    return render_template("hostRoom.html", room=room, should_refresh=should_refresh)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static", "static"),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/discord')
def discord():
    return redirect("https://discord.gg/8Z65BR2")


@app.route('/datapackage')
@cache.cached()
def get_datapackage():
    """A pretty print version of /api/datapackage"""
    from worlds import network_data_package
    import json
    return Response(json.dumps(network_data_package, indent=4), mimetype="text/plain")


@app.route('/index')
@app.route('/sitemap')
@cache.cached()
def get_sitemap():
    available_games: List[Dict[str, Union[str, bool]]] = []
    for game, world in AutoWorldRegister.world_types.items():
        if not world.hidden:
            has_settings: bool = isinstance(world.web.options_page, bool) and world.web.options_page
            available_games.append({ 'title': game, 'has_settings': has_settings })
    return render_template("siteMap.html", games=available_games)
