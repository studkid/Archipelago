from typing import Any, Dict, List, NamedTuple, Optional, Set, Tuple, Union

import ctypes
import functools
import struct
import CommonClient

import psutil
import pymem.process
import pymem.ressources.structure

from pymem import Pymem

from .Enums import GameStates

class GameState(NamedTuple):
    state: GameStates

class GameStateManager:
    process_name: str = "Game.exe"
    game_state: GameStates.INVALID

    process_running = False
    process = Optional[Pymem]

    dl = 0xB2
    nop = 0x90
    eax = 0xB8

    dim_swap_offset = 0x1D4101

    tp_target_id = 0x25EACD
    tp_target_code = 0x25D800
    
    def __init__(self) -> None:
        self.process = None
        self.process_running = False
        self.game_state = GameStates.INVALID

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

    def update(self) -> bool:
        self.updateState()

        if self.game_state == GameStates.INGAME:
            self.waiting_msg_sent = False

            self.scanLocations()
            return True

        return False

    def updateState(self) -> None:
        address_bytes = self.process.read_bytes(self.process.base_address + 0x0051F3F0, 4)

        if address_bytes.hex() == "00000000":
            self.game_state = GameStates.MENU
        else:
            self.game_state = GameStates.INGAME

    def resolvePointers(self, address, offsets) -> int:
        pointer = self.process.read_uint(self.process.base_address + address)
        for offset in offsets:
            try:
                pointer = self.process.read_uint(pointer + offset)
            except Exception as e:
                # print(f"Failed to resolve pointer: {e}")
                return 0x0
        return pointer

    def scanLocations(self) -> None:
        offsets: List[int] = [0x11F0, 0x0C]
        
        while(True):
            pointer = self.resolvePointers(0x51F710, offsets)
            if pointer == 0x0:
                return
            value = self.process.read_string(pointer, 40)
            print(value)
            offsets[0] = offsets[0] + 0x10

    def warpToLocation(self) -> bool:
        tp_location = self.process.read_bytes(self.process.base_address + self.tp_target_id, 5)
        print(tp_location.hex())

        if tp_location.hex() == "e82eedffff":
            # print(self.process.pointer(self.process.base_address + self.tp_target_id, 3))
            return True

        return False

    def toggleDimSwap(self) -> bool:
        dim_bytes = self.process.read_bytes(self.process.base_address + self.dim_swap_offset, 3)

        if dim_bytes.hex() == "8a5218":
            to_write = b'\xB2\x01\x90'
            self.process.write_bytes(self.process.base_address + self.dim_swap_offset, to_write, len(to_write))
            return True
        else:
            to_write = bytes.fromhex("8a5218")
            self.process.write_bytes(self.process.base_address + self.dim_swap_offset, to_write, len(to_write))
            return False
