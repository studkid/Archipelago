from BaseClasses import Location
from .options import ItemPickups, ChestPickups, ShrinePickups
from typing import Dict, List, TypeVar, NamedTuple, Optional

class RoR1Location(Location):
    game: str = "Risk of Rain"

class RoR1LocationData(NamedTuple):
    category: str
    code: Optional[int] = None

startId = 1
stageId = startId + 5000

offsetChests = 0

map_orderedstage_1_table: Dict[str, int] = {
    "Desolate Forest":          0,
    "Dried Lake":               1,
}
map_orderedstage_2_table: Dict[str, int] = {
    "Damp Caverns":             2,
    "Sky Meadow":               3,
}
map_orderedstage_3_table: Dict[str, int] = {
    "Ancient Valley":           4,
    "Sunken Tombs":             5,
}
map_orderedstage_4_table: Dict[str, int] = {
    "Magma Barracks":           6,
    "Hive Cluster":             7,
}
map_orderedstage_5_table: Dict[str, int] = {
    "Temple of the Elders":     8,
}
map_special_table: Dict[str, int] = {
    # "Boar Beach":               9,
    "Risk of Rain":            10,
}

map_ss_orderedstage_1_table: Dict[str, int] = {
    "Stray Tarn":              11,
}

map_ss_orderedstage_2_table: Dict[str, int] = {
    "Whistling Basin":         12,
}

map_ss_orderedstage_3_table: Dict[str, int] = {
    "Torrid Wastelands":         13,
}

map_ss_orderedstage_4_table: Dict[str, int] = {
    "Verdant Woodland":         14,
}

map_ss_orderedstage_5_table: Dict[str, int] = {
    "Uncharted Mountain":         15,
}

X = TypeVar("X")
Y = TypeVar("Y")

#Taken from ror2environments.py
def compress_dict_list_horizontal(list_of_dict: List[Dict[X, Y]]) -> Dict[X, Y]:
    """Combine all dictionaries in a list together into one dictionary."""
    compressed: Dict[X, Y] = {}
    for individual in list_of_dict:
        compressed.update(individual)
    return compressed

map_orderedstages_table = \
    [map_orderedstage_1_table, map_orderedstage_2_table, map_orderedstage_3_table,
     map_orderedstage_4_table, map_orderedstage_5_table]
vanilla_map_table = \
    {**compress_dict_list_horizontal(map_orderedstages_table),
     **map_special_table}

map_ss_orderedstage_table = \
    [map_ss_orderedstage_1_table, map_ss_orderedstage_2_table, map_ss_orderedstage_3_table,
     map_ss_orderedstage_4_table, map_ss_orderedstage_5_table]
ss_map_table =\
    {**compress_dict_list_horizontal(map_ss_orderedstage_table)}

all_map_table = {**vanilla_map_table, **ss_map_table}


def shift_by_offset(dictionary: Dict[str, int], offset: int) -> Dict[str, int]:
    """Shift all indexes in a dictionary by an offset"""
    return {name: index+offset for name, index in dictionary.items()}

def get_map_locations(pickups: int, chests: int, shrines: int, map_name: str, map_index: int) -> Dict[str, int]:
    locations = {}

    mapStartId = map_index * ItemPickups.range_end + startId
    for n in range(pickups):
        locations.update({f"{map_name}: Item Pickup {n + 1}": n + offsetChests + mapStartId})
    for n in range(chests):
        locations.update({f"{map_name}: Chests {n + 1}": n + offsetChests + mapStartId})
    for n in range(shrines):
        locations.update({f"{map_name}: Shrines {n + 1}": n + offsetChests + mapStartId})
    return locations

def get_stage_locations(pickups: int, chests: int, shrines: int, stage: int) -> Dict[str, int]:
    locations = {}

    stageStartId = stage * ItemPickups.range_end + stageId
    for n in range(pickups):
        locations.update({f"Stage {stage + 1}: Item Pickup {n + 1}": n + offsetChests + stageStartId})
    for n in range(chests):
        locations.update({f"Stage {stage + 1}: Chests {n + 1}": n + offsetChests + stageStartId})
    for n in range(shrines):
        locations.update({f"Stage {stage + 1}: Shrines {n + 1}": n + offsetChests + stageStartId})
    return locations

def get_locations(pickups: int, chests: int, shrines: int, type: int = 0, ssSupport: bool = False) -> Dict[str, int]:
    locations = {}
    if type == 2:
        orderedstages = compress_dict_list_horizontal(map_orderedstages_table)
        if ssSupport:
            orderedstages.update(compress_dict_list_horizontal(map_ss_orderedstage_table))
        for map_name, map_index in orderedstages.items():
            locations.update(get_map_locations(
                pickups = pickups,
                chests = chests,
                shrines = shrines,
                map_name = map_name,
                map_index = map_index
            ))

    if type == 1:
        for stage in range(5):
            locations.update(get_stage_locations(
                pickups = pickups,
                chests = chests,
                shrines = shrines,
                stage = stage
            ))

    return locations

location_table = get_locations(
    pickups=ItemPickups.range_end,
    chests=ChestPickups.range_end,
    shrines=ShrinePickups.range_end,
    type=2,
    ssSupport=True
)

location_table.update(get_locations(
    pickups=ItemPickups.range_end,
    chests=ChestPickups.range_end,
    shrines=ShrinePickups.range_end,
    type=1,
    ssSupport=True
))