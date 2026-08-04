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

    process_running = False
    process = Optional[Pymem]

    dl = 0xB2
    nop = 0x90

    base_address = 0x00400000

    dim_swap_offset = 0x1D4101

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

            self.process_running = True
            
        except Exception:
            return False
        
        return True

    def warpToLocation(self) -> None:
        tp_location: int = self.process.read_bytes(self.base_address + self.peublucho_id)

    def toggleDimSwap(self) -> bool:
        dim_bytes = self.process.read_bytes(self.base_address + self.dim_swap_offset, 3)
        print(dim_bytes.hex())

        if dim_bytes.hex() == "8a5218":
            to_write = b'\xB2\x01\x90'
            self.process.write_bytes(self.base_address + self.dim_swap_offset, to_write, len(to_write))
            print(self.process.read_bytes(self.base_address + self.dim_swap_offset, 3).hex())
            return True
        else:
            to_write = bytes.fromhex("8a5218")
            self.process.write_bytes(self.base_address + self.dim_swap_offset, to_write, len(to_write))
            print(self.process.read_bytes(self.base_address + self.dim_swap_offset, 3).hex())
            return False
