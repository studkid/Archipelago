from typing import Any, Dict, List, NamedTuple, Optional, Set, Tuple, Union

import ctypes
import functools
import struct
import CommonClient
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
    game_state: GameStates.INVALID

    process_running = False
    process = Optional[Pymem]

    dl = 0xB2
    nop = 0x90
    eax = b'\xB8'

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
            # print(value)
            offsets[0] = offsets[0] + 0x10

    def warpToLocation(self) -> bool:
        tp_target_id = 0x25EACD
        tp_location = self.process.read_bytes(self.process.base_address + tp_target_id, 5)
        print(tp_location.hex())
        singleCall = self.process.allocate(0x4)
        regBackup = self.process.allocate(0x4)

        if tp_location.hex() == "e82eedffff":
            try:
                # Set world to living
                # mov dword ptr ["00400000"+4FB074],01
                # self.process.write_bytes(self.process.base_address + tp_target_id, 0x01, 1)

                self.process.write_int(singleCall, 0)

                # shellcode = b"\x83\x3d" + struct.pack("<I", singleCall) + b"\x00\x00\x00\x00" # cmp [singleCall],00000000
                # shellcode += b"\x0F\x85" + struct.pack("<I", )

                shellcode = b"\xC7\x05\x74\xB0\x51\x00\x01\x00\x00\x00" # mov dword ptr ["00400000"+4FB074],01

                shellcode += b"\xC7\x00\x4D\x61\x70\x5F"     # mov [eax],5F70614D    // Map_
                shellcode += b"\xC7\x40\x04\x0E\x14\xBC\x03" # mov [eax+8],6863756C  // luch
                shellcode += b"\xC7\x40\x08\x6C\x75\x63\x68" # mov [eax+4],62657550  // Pueb
                shellcode += b"\xC7\x40\x0C\x6F\x2E\x6C\x65" # mov [eax+C],656C2E6F  // o.le
                shellcode += b"\xC7\x40\x0A\x76\x65\x6C\x00" # mov [eax+10],006C6576 // vel
                shellcode += b"\xC7\x40\x0E\x00\x00\x00\x00" # mov [eax+14],00000000 //

                # shellcode += b"\x8B\x1D\xA4\xE7\x53\x00" # mov ebx,[00400000+5367716]
                # shellcode += b"\xC6\x83\x84\x00\x00\x00\x3E" # mov byte ptr [ebx+132],62

                shellcode += b'\xE8\x2E\xED\xFF\xFF'

                setTPTargetMem = self.process.allocate(len(shellcode))
                self.process.write_bytes(setTPTargetMem, shellcode, len(shellcode))

                # values = [
                #     # Change Current Map
                #     b"\xC7\x00\x4D\x61\x70\x5F",     # mov [eax],5F70614D    // Map_
                #     b"\xC7\x40\x04\x0E\x14\xBC\x03", # mov [eax+8],6863756C  // luch
                #     b"\xC7\x40\x08\x6C\x75\x63\x68", # mov [eax+4],62657550  // Pueb
                #     b"\xC7\x40\x0C\x6F\x2E\x6C\x65", # mov [eax+C],656C2E6F  // o.le
                #     b"\xC7\x40\x0A\x76\x65\x6C\x00", # mov [eax+10],006C6576 // vel
                #     b"\xC7\x40\x0E\x00\x00\x00\x00", # mov [eax+14],00000000 //

                #     # Reg Backup
                #     b"\x89\x1D\x00\x00\x00\x00", # mov [regbackup],ebx
                #     # Set player spawn checkpoint location
                #     b"\x8B\x1D\xA4\xE7\x53\x00", # mov ebx,[00400000+5367716]
                #     b"\xC6\x83\x84\x00\x00\x00\x3E", # mov byte ptr [ebx+132],62
                #     # Restore Reg State
                #     b"\x8B\x1D\x00\x00\x00\x00", # mov ebx,[regbackup]
                #     # Set Call
                #     b'\xE8\x2E\xED\xFF\xFF' # call 0065D800 
                # ]
                # for value in values:
                #     self.process.write_bytes(setTPTargetMem, value, len(value))
                #     tp_target_id = setTPTargetMem + (len(value) * 8)

                # # self.process.write_bytes(regBackup, )

                # Execute
                pointer = self.resolvePointers(self.process.read_uint(self.process.base_address + 0x51E7A4), [0x132])
                self.process.write_bytes(pointer, 0x17)
                return True
            except Exception as e:
                print(f"Failed to warp: {e}")
                return False

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
