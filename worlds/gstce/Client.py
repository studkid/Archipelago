import asyncio
import sys
import urllib.parse

import CommonClient
import NetUtils
import Utils

from typing import Any, Dict, List, Optional, Set
from .DataUtils import item_name_to_id, location_name_to_id, id_to_item_name, id_to_location_name

tracker_loaded = False
try:
    from worlds.tracker.TrackerClient import TrackerGameContext as Context
    from worlds.tracker.TrackerClient import TrackerCommandProcessor as CommandProcessor

    tracker_loaded = True
except ModuleNotFoundError:
    from CommonClient import CommonContext as Context
    from CommonClient import ClientCommandProcessor as CommandProcessor

class GuacameleeSTCECommandProcessor(CommandProcessor):
    ctx: "GuacameleeSTCEContext"

class GuacameleeSTCEContext(Context):
    tags: Set[str] = {"AP"}
    game: str = "Guacamelee Super Turbo Championship Edition"
    command_processor: CommonClient.ClientCommandProcessor = GuacameleeSTCECommandProcessor
    items_handling: int = 0b111
    want_slot_data = True

    item_name_to_id: Dict[str, int] = item_name_to_id()
    location_name_to_id: Dict[str, int] = location_name_to_id()

    id_to_item_name: Dict[int, str] = id_to_item_name()
    id_to_location_name: Dict[int, str] = id_to_location_name()

    def __init__(self, server_address: Optional[str], password: Optional[str]) -> None:
        super().__init__(server_address, password)

def main(*args) -> None:
    Utils.init_logging("GuacameleeSTCEClient", exception_logger="Client")

    parser = CommonClient.get_base_parser(description="Guacamelee Super Turbo Championship Edition Client")

    parser.add_argument("url", nargs="?", help="Archipelago Connection URL")
    parser.add_argument("--name", default=None, help="Archipelago Slot Name")
    
    args = parser.parse_args(args)

    if args.url:
        url = urllib.parse.urlparse(args.url)
        args.connect = url.netloc
        if url.username:
            args.none = urllib.parse.unquote(url.username)
        if url.password:
            args.password = urllib.parse.unquote(url.password)
        
    async def _main(_args):
        ctx: GuacameleeSTCEContext = GuacameleeSTCEContext(args.connect, args.password)

        ctx.server_task = asyncio.create_task(CommonClient.server_loop(ctx), name="server loop")
        # ctx.controller_task = asyncio.create_task(ctx.conntroller(), name="GuacameleeSTCEController")

        if tracker_loaded:
            ctx.run_generator()
        
        if CommonClient.gui_enabled:
            ctx.run_gui()

        ctx.run_cli()

        # await ctx.exit_event().wait()
        await ctx.shutdown()

    import colorama
    colorama.just_fix_windows_console()

    asyncio.run(_main(args))

    colorama.deinit()

if __name__ == "__main__":
    main(*sys.argv[1:])