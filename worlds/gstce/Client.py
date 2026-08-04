import asyncio
import sys
import urllib.parse

import CommonClient
import NetUtils
import Utils

from typing import Any, Dict, List, Optional, Set
from .DataUtils import item_name_to_id, location_name_to_id, id_to_item_name, id_to_location_name
from .GameState import GameStateManager

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

    game_state_manager: GameStateManager

    process_not_found_msg_displayed: False
    process_found_msg_displayed: False

    def __init__(self, server_address: Optional[str], password: Optional[str]) -> None:
        super().__init__(server_address, password)

        self.game_state_manager = GameStateManager()

    async def controller(self):
        while not self.exit_event.is_set():
            await asyncio.sleep(0.2)

            if not self.game_state_manager.process_running:
                process_found = self.game_state_manager.openProcessHandle()

                if not process_found:
                    if not self.process_not_found_msg_displayed:
                        CommonClient.logger.info("Looking for Guacamelee STCE process...")

                        self.process_found_msg_displayed = False
                        self.process_not_found_msg_displayed = True

                if process_found:
                    CommonClient.logger.info("Guacamelee STCE process found!")

                    self.process_found_msg_displayed = True
                    self.process_not_found_msg_displayed = False

                    success = self.game_state_manager.toggleDimSwap()
                    if not success:
                        CommonClient.logger.info("Failed to give Dimension Swap.")

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
        ctx.controller_task = asyncio.create_task(ctx.controller(), name="GuacameleeSTCEController")

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