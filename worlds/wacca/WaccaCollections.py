from .items import SongData
from .datagen.SongData import SONG_DATA, groups
from typing import Dict, List, Set
from collections import ChainMap
from BaseClasses import logging

class WaccaCollections:
    SHEET_NAME: str = "Reverse Point"
    SHEET_CODE: int = 1

    song_locations: Dict[str, int] = {}
    song_items: Dict[str, SongData] = {}

    filler_items: Dict[str, int] = {
        "Marvelous": 2,
        "Missless": 3,
    }

    filler_weights: Dict[str, int] = {
        "Marvelous": 1,
        "Missless": 1,
    }

    item_names_to_id: ChainMap = ChainMap({}, filler_items)
    location_names_to_id: ChainMap = ChainMap(song_locations)

    def __init__(self) -> None:
        self.item_names_to_id[self.SHEET_NAME] = self.SHEET_CODE
        for key, data in SONG_DATA.items():
            self.song_items[key] = data

        self.item_names_to_id.update({name: data.code for name, data in self.song_items.items()})

        location_id_index = 1
        for name in SONG_DATA.keys():
            self.song_locations[f"{name}-0"] = location_id_index 
            self.song_locations[f"{name}-1"] = location_id_index + 1
            location_id_index += 2

    def getSongsWithSettings(self, options, diff_lower: int, diff_higher:int) -> List[str]:
        filtered_list = []

        for key, data in self.song_items.items():
            if data.difficulties[0] != None and "Normal" in options.difficulty_option and diff_lower <= data.difficulties[0] * 10 <= diff_higher:
                filtered_list.append(key)
                continue

            if data.difficulties[1] != None and "Hard" in options.difficulty_option and diff_lower <= data.difficulties[1] * 10 <= diff_higher:
                filtered_list.append(key)
                continue

            if data.difficulties[2] != None and "Expert" in options.difficulty_option and diff_lower <= data.difficulties[2] * 10 <= diff_higher:
                filtered_list.append(key)
                continue

            if data.difficulties[3] != None and "Inferno" in options.difficulty_option and diff_lower <= data.difficulties[3] * 10 <= diff_higher:
                filtered_list.append(key)
                continue

        return filtered_list
    
    def getItemNameGroups(self) -> Dict[str, str]:
        return groups