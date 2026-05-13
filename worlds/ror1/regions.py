from typing import Dict, List, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Region, MultiWorld
from .locations import location_table, map_orderedstage_2_table, map_orderedstage_3_table, map_orderedstage_4_table, map_orderedstages_table, RoR1Location
from worlds.AutoWorld import World

if TYPE_CHECKING:
    from . import RoR1World

class RoR1RegionData(NamedTuple):
    locations: Optional[List[str]]
    region_exits: Optional[List[str]]

def create_grouped_regions(self: World) -> List[List[str]]:
    ror_options = self.options
    multiworld = self.multiworld
    player = self.player

    mapProgression: List[List[str]] = [
        ["Desolate Forest", "Dried Lake"],
        ["Damp Caverns", "Sky Meadow"],
        ["Ancient Valley", "Sunken Tombs"],
        ["Magma Barracks", "Hive Cluster"],
        ["Temple of the Elders"]
    ]

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
    starstorm_map_regions: Dict[str, RoR1RegionData] = {
        "Stray Tarn":                       RoR1RegionData([], ["OrderedStage_2"]), # Make this loop only?
        "Whistling Basin":                  RoR1RegionData([], ["OrderedStage_3"]),
        "Torrid Wastelands":                RoR1RegionData([], ["OrderedStage_4"]),
        "Verdant Woodland":                 RoR1RegionData([], ["OrderedStage_5"]),
        "Uncharted Mountain":               RoR1RegionData([], ["OrderedStage_6"]),
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

    orderedMaps = {**map_regions, **starstorm_map_regions}

    if ror_options.starstorm:
        for i, map in enumerate(starstorm_map_regions.keys()):
            stage_regions[f"OrderedStage_{i + 1}"].region_exits.append(map)
            mapProgression[i].append(map)

    if not ror_options.map_shuffle:
        if not ror_options.strict_stage_prog:

            for stage, maps in enumerate(mapProgression):
                for map in maps:
                    for i in range(3 - stage):
                        orderedMaps[map].region_exits.append(f"OrderedStage_{stage + i + 3}")

        if not ror_options.stage_five_tp:
            for key in map_regions:
                if not key == "Menu" or not "OrderedStage_6" in map_regions[key].region_exits:
                    map_regions[key].region_exits.append("OrderedStage_6")

    else:
        mapList: List[str] = [map for map in map_regions.keys() if not map == "Menu"]
        if ror_options.starstorm:
            mapList.append([map for map in starstorm_map_regions.keys()])
        self.random.shuffle(mapList)
        shuffledMaps: List[str] = []

        for stage in range(5):
            selectedMaps = []
            stage_regions[f"OrderedStage_{stage + 1}"].region_exits.clear()

            for _ in range(len(mapProgression[stage])):
                map = mapList.pop()
                selectedMaps.append(map)
                map_regions[map].region_exits.clear()
                stage_regions[f"OrderedStage_{stage + 1}"].region_exits.append(map)
                map_regions[map].region_exits.append(f"OrderedStage_{stage + 2}")

                if not ror_options.strict_stage_prog:
                    for i in range(3 - stage):
                        map_regions[map].region_exits.append(f"OrderedStage_{stage + i + 3}")

                if not ror_options.stage_five_tp:
                    map_regions[map].region_exits.append("OrderedStage_6")
            
            shuffledMaps.append(selectedMaps)

        mapProgression = shuffledMaps


    pickups = int(ror_options.total_pickups)
    chests = int(ror_options.chest_locations)
    shrines = int(ror_options.shrine_locations)

    if ror_options.grouping == "map":
        for maps in mapProgression:
            for key in maps:
                if key == "Menu":
                    continue
                for i in range(0, pickups):
                    orderedMaps[key].locations.append(f"{key}: Item Pickup {i + 1}")
                for i in range(0, chests):
                    orderedMaps[key].locations.append(f"{key}: Chest {i + 1}")
                for i in range(0, shrines):
                    orderedMaps[key].locations.append(f"{key}: Shrine {i + 1}")

    elif ror_options.grouping == "stage":
        map_regions["Menu"].region_exits.append("OrderedStage_1")
        x = 1
        for key in stage_regions:
            if key == "OrderedStage_6":
                continue
            for i in range(0, pickups):
                stage_regions[key].locations.append(f"Stage {x}: Item Pickup {i + 1}")
            for i in range(0, chests):
                stage_regions[key].locations.append(f"Stage {x}: Chest {i + 1}")
            for i in range(0, shrines):
                stage_regions[key].locations.append(f"Stage {x}: Shrine {i + 1}")
            x += 1
    
    regions_pool: Dict = {**map_regions, **stage_regions, **other_regions}
    if ror_options.starstorm:
        regions_pool.update(starstorm_map_regions)

    for name, data, in regions_pool.items():
        multiworld.regions.append(create_region(multiworld, player, name, data))

    for name, data, in regions_pool.items():
        create_connections_in_regions(multiworld, player, name, data)

    return mapProgression

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