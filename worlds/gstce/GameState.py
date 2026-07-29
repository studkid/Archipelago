from typing import Any, Dict, List, NamedTuple, Optional, Set, Tuple, Union

import ctypes
import functools
import struct

import psutil
import pymem.process
import pymem.ressources.structure

from pymem import Pymem

from .Enums import GameStates

class GameState(NamedTuple):
    state: GameStates

class GameStateManager:
    process_name: str = "Game.exe"

    base_address = 0x00400000
    peublucho_id = 0x25D800
    
    def __init__(self) -> None:
        self.process = None
        self.process_running = False

    def openProcessHandle(self) -> bool:
        try:
            process_pid: Optional[int] = None
            process_memory_usage: int = 0

            process: psutil.Process
            for process in psutil.process_iter(["pid", "name", "memory_info"]):
                process_data: Dict[str, Any] = process.info

                if process_data["name"] != self.process_name:
                    continue

                memory_usage: int = process_data["memory_info"].rss

                if memory_usage > process_memory_usage:
                    process_pid = process_data["pid"]
                    process_memory_usage = memory_usage
            
            if process_pid is None:
                return False
            
            self.process = Pymem(process_pid)

            module: pymem.ressources.structure.MODULEINFO = pymem.process.module_from_name(
                self.process.process_handle, self.process_name
            )

            self.process_running = True
            
        except Exception:
            return False
        
        return True

    def warpToLocation(self) -> None:
        tp_location: int = self.process.read_bytes(self.base_address + self.peublucho_id)
        