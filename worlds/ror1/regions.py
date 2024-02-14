from typing import Dict, List, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Region, Entrance, MultiWorld
from .locations import location_table, RoR1Location, get_item_pickups

if TYPE_CHECKING:
    from . import RoR1World

class RoR1RegionData(NamedTuple):
    locations: Optional[List[str]]
    region_exits: Optional[List[str]]

def create_grouped_regions(ror_world: "RoR1World") -> None:
    ror_options = ror_world.options
    multiworld = ror_world.multiworld
    player = ror_world.player

    map_regions: Dict[str, RoR1Location] = {
        "Menu":                             RoR1RegionData(None, ["Desolate Forest", "Dried Lake"]),
        "Desolate Forest":                  RoR1RegionData([], ["Stage 1"]),
        "Dried Lake":                       RoR1RegionData([], ["Stage 1"]),
        "Damp Caverns":                     RoR1RegionData([], ["Stage 2"]),
        "Sky Meadow":                       RoR1RegionData([], ["Stage 2"]),
        "Ancient Valley":                   RoR1RegionData([], ["Stage 3"]),
        "Sunken Tomb":                      RoR1RegionData([], ["Stage 3"]),
        "Magma Barracks":                   RoR1RegionData([], ["Stage 4"]),
        "Hive Cluster":                     RoR1RegionData([], ["Stage 4"]),
        "Temple of the Elders":             RoR1RegionData([], ["Stage 5"]),
    }
    stage_regions: Dict[str, RoR1Location] = {
        "Stage 1":                          RoR1RegionData([], ["Desolate Forest", "Dried Lake"]),
        "Stage 2":                          RoR1RegionData([], ["Damp Caverns", "Sky Meadow"]),
        "Stage 3":                          RoR1RegionData([], ["Ancient Valley", "Sunken Tomb"]),
        "Stage 4":                          RoR1RegionData([], ["Magma Barracks", "Hive Cluster"]),
        "Stage 5":                          RoR1RegionData([], ["Temple of the Elders"]),
    }
    other_regions: Dict[str, RoR1Location] = {
        "Risk of Rain":                     RoR1RegionData(None, ["Victory"]),
        "Contact Light":                    RoR1RegionData(None, []),
        "Victory":                          RoR1RegionData(None, None)
    }

    pickups = int(ror_options.total_locations)

    if ror_options.grouping == "stage":
        for key in stage_regions:
            for i in range(0, pickups):
                map_regions[key].locations.append(f"{key}: Item Pickup {i + 1}")

    elif ror_options.grouping == "map":
        for key in map_regions:
            if key == "Menu":
                continue
            for i in range(0, pickups):
                map_regions[key].locations.append(f"{key}: Item Pickup {i + 1}")
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
        for region_exit in data.region_exits:
            r_exit_stage = Entrance(player, region_exit, region)
            exit_region = multiworld.get_region(region_exit, player)
            r_exit_stage.connect(exit_region)
            region.exits.append(r_exit_stage)

# TODO Refactor this code into the main create_regions method maybe?
def create_universal_regions(ror_world: "RoR1World") -> None:
    player = ror_world.player
    ror_options = ror_world.options
    multiworld = ror_world.multiworld

    menu = create_universal_region(multiworld, player, "Menu")
    multiworld.regions.append(menu)

    victory_region = create_universal_region(multiworld, player, "Victory")
    multiworld.regions.append(victory_region)
    contactLight = create_universal_region(multiworld, player, "Contact Light",
                                      get_item_pickups(ror_options.total_locations.value))
    multiworld.regions.append(contactLight)

    # classic mode can get to victory from the beginning of the game
    to_victory = Entrance(player, "beating game", contactLight)
    contactLight.exits.append(to_victory)
    to_victory.connect(victory_region)

    connection = Entrance(player, "Menu", menu)
    menu.exits.append(connection)
    connection.connect(contactLight)

def create_universal_region(multiworld: MultiWorld, player: int, name: str, locations: Dict[str, int] = {}) -> Region:
    ret = Region(name, player, multiworld)
    for location_name, location_id in locations.items():
        ret.locations.append(RoR1Location(player, location_name, location_id, ret))
    return ret