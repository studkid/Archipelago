from typing import Dict, List, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Region, Entrance, MultiWorld
from .locations import location_table, map_orderedstage_2_table, map_orderedstage_3_table, map_orderedstage_4_table, RoR1Location

if TYPE_CHECKING:
    from . import RoR1World

class RoR1RegionData(NamedTuple):
    locations: Optional[List[str]]
    region_exits: Optional[List[str]]

def create_grouped_regions(self) -> None:
    ror_options = self.options
    multiworld = self.multiworld
    player = self.player

    map_regions: Dict[str, RoR1RegionData] = {
        "Menu":                             RoR1RegionData(None, ["OrderedStage_1"]),
        "Desolate Forest":                  RoR1RegionData([], ["OrderedStage_2"]),
        "Dried Lake":                       RoR1RegionData([], ["OrderedStage_2"]),
        "Damp Caverns":                     RoR1RegionData([], ["OrderedStage_3"]),
        "Sky Meadow":                       RoR1RegionData([], ["OrderedStage_3"]),
        "Ancient Valley":                   RoR1RegionData([], ["OrderedStage_4"]),
        "Sunken Tombs":                     RoR1RegionData([], ["OrderedStage_4"]),
        "Magma Barracks":                   RoR1RegionData([], ["OrderedStage_5"]),
        "Hive Cluster":                     RoR1RegionData([], ["OrderedStage_5"]),
        "Temple of the Elders":             RoR1RegionData([], ["OrderedStage_6"]),
    }
    stage_regions: Dict[str, RoR1RegionData] = {
        "OrderedStage_1":                   RoR1RegionData([], ["Desolate Forest", "Dried Lake"]),
        "OrderedStage_2":                   RoR1RegionData([], ["Damp Caverns", "Sky Meadow"]),
        "OrderedStage_3":                   RoR1RegionData([], ["Ancient Valley", "Sunken Tombs"]),
        "OrderedStage_4":                   RoR1RegionData([], ["Magma Barracks", "Hive Cluster"]),
        "OrderedStage_5":                   RoR1RegionData([], ["Temple of the Elders"]),
        "OrderedStage_6":                   RoR1RegionData([], ["Risk of Rain"]),
        
    }
    other_regions: Dict[str, RoR1RegionData] = {
        "Risk of Rain":                     RoR1RegionData([], [])
    }

    if not ror_options.strict_stage_prog:
        for key in map_orderedstage_2_table:
            map_regions[key].region_exits.append("OrderedStage_3")
            map_regions[key].region_exits.append("OrderedStage_4")
            map_regions[key].region_exits.append("OrderedStage_5")
        for key in map_orderedstage_3_table:
            map_regions[key].region_exits.append("OrderedStage_4")
            map_regions[key].region_exits.append("OrderedStage_5")
        for key in map_orderedstage_4_table:
            map_regions[key].region_exits.append("OrderedStage_5")

    if not ror_options.stage_five_tp:
        for key in map_regions:
            if not key == "Menu" or not key == "Temple of the Elders":
                map_regions[key].region_exits.append("OrderedStage_6")

    pickups = int(ror_options.total_pickups)

    if ror_options.grouping == "map":
        for key in map_regions:
            if key == "Menu":
                continue
            for i in range(0, pickups):
                map_regions[key].locations.append(f"{key}: Item Pickup {i + 1}")

    elif ror_options.grouping == "stage":
        map_regions["Menu"].region_exits.append("OrderedStage_1")
        x = 1
        for key in stage_regions:
            if key == "OrderedStage_6":
                continue
            for i in range(0, pickups):
                stage_regions[key].locations.append(f"Stage {x}: Item Pickup {i + 1}")
            x += 1
    
    regions_pool: Dict = {**map_regions, **stage_regions, **other_regions}

    for name, data, in regions_pool.items():
        multiworld.regions.append(create_region(multiworld, player, name, data))

    for name, data, in regions_pool.items():
        create_connections_in_regions(multiworld, player, name, data)
    

def create_region(multiworld:MultiWorld, player: int, name: str, data: RoR1RegionData) -> Region:
    region = Region(name, player, multiworld)
    if data.locations:
        for location_name in data.locations:
            location_data = location_table.get(location_name)
            location = RoR1Location(player, location_name, location_data, region)
            region.locations.append(location)

    return region

def create_connections_in_regions(multiworld: MultiWorld, player: int, name: str, data: RoR1RegionData):
    region = multiworld.get_region(name, player)
    if data.region_exits:
        region.add_exits(data.region_exits)