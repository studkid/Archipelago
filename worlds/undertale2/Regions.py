from typing import Dict, List, NamedTuple, Optional

from BaseClasses import MultiWorld, Region
from .Locations import UT2Location, location_table, get_locations_by_category
from Options import Choice
from .Options import UT2Options

class UT2RegionData(NamedTuple):
    locations: Optional[List[str]]
    exits: Optional[List[str]]

def create_regions(multiworld: MultiWorld, player: int, options: UT2Options):
    regions: Dict[str, UT2RegionData] = {
        "Menu":                     UT2RegionData(None, ["Landing"]),
        "Landing":                  UT2RegionData([], ["Ruins Main"]),
        "Ruins Main":               UT2RegionData([], ["Sewers", "Ruins Lake", "Rest Zone"]),
        "Sewers":                   UT2RegionData([], ["Ruins Lake"]),
        "Rest Zone":                UT2RegionData([], []),
        "Ruins Lake":               UT2RegionData([], ["Ruins Tree"]),
        "Ruins Tree":               UT2RegionData([], [])
    }

    for name, data in location_table.items():
        if data.category == "enemy" and options.cardsanity < 2:
            continue
        if data.category == "boss" and options.cardsanity < 1:
            continue

        regions[data.region].locations.append(name)

    for name, data in regions.items():
        multiworld.regions.append(create_region(multiworld, player, name, data))
        
    for name, data in regions.items():
        connect_regions(multiworld, player, name, data)

def create_region(multiworld: MultiWorld, player: int, name: str, data: UT2RegionData):
    region = Region(name, player, multiworld)
    if data.locations:
        for loc_name in data.locations:
            loc_data = location_table.get(loc_name)
            location = UT2Location(player, loc_name, loc_data.code if loc_data else None, region)
            region.locations.append(location)

    return region
    
def connect_regions(multiworld: MultiWorld, player: int, source: str, data: UT2RegionData, rule=None):
    for _, target in enumerate(data.exits):
        sourceRegion = multiworld.get_region(source, player)
        targetRegion = multiworld.get_region(target, player)
        sourceRegion.connect(targetRegion, rule=rule)