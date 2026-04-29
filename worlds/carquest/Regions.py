from typing import Dict, List, NamedTuple, Optional

from BaseClasses import MultiWorld, Region
from .Locations import CarQuestLocation, location_table
from .Options import CarQuestOptions

class CarQuestRegionData(NamedTuple):
    locations: Optional[List[str]]
    exits: Optional[List[str]]

def create_regions(multiworld: MultiWorld, player: int, options: CarQuestOptions):
    regions: Dict[str, CarQuestRegionData] = {
        # Hub
        "Menu":                              CarQuestRegionData(None, ["Hub Start"]),
        "Hub Start":                         CarQuestRegionData([], ["Hub Simple Portal Path", "Hub Throne Room East Exterior",  
                                                                     "Hub Central Bridge", "Hub Upper Pool Perimeter"]),
        "Hub Simple Portal Path":            CarQuestRegionData([], ["Simple Square Area", "Hub Pool Area"]),
        "Hub Pool Area":                     CarQuestRegionData([], ["Hub Upper Uni Alleyway", "Hub South Pool Deadend Path",
                                                                     "Floating Cube Area", "Hub Cube Monument", "Hub South Portal",
                                                                     "Hub Vault", "Hub Drained Pool", "Hub University Exterior", "Hub Museum",
                                                                     "Hub Colloseum"]),
        "Hub Upper Uni Alleyway":            CarQuestRegionData([], None),
        "Hub South Pool Deadend Path":       CarQuestRegionData([], None),
        "Hub Museum":                        CarQuestRegionData([], None),
        "Hub Cube Monument":                 CarQuestRegionData([], None),
        "Hub South Portal":                  CarQuestRegionData([], ["Fixit Shop Main"]),
        "Hub Vault":                         CarQuestRegionData([], ["Slider Start"]),
        "Hub Drained Pool":                  CarQuestRegionData([], None),
        "Hub Throne Room East Exterior":     CarQuestRegionData([], ["Hub Throne Room West Exterior", "Hub Floating Islands Path"]),
        "Hub Throne Room West Exterior":     CarQuestRegionData([], None),
        "Hub Central Bridge":                CarQuestRegionData([], ["Maze Start"]),
        "Hub University Exterior":           CarQuestRegionData([], ["Hub Lower Whale Lookout"]),
        "Hub Upper Pool Perimeter":          CarQuestRegionData([], ["Hub Light Puzzle Area", "Hub Throne Room East Exterior"]),
        "Hub Lower Whale Lookout":           CarQuestRegionData([], ["Hub Whale Bridge"]),
        "Hub Whale Bridge":                  CarQuestRegionData([], []),
        "Hub Colloseum":                     CarQuestRegionData([], ["Hub Colloseum Exterior", "Hub Colloseum Podium"]),
        "Hub Colloseum Exterior":            CarQuestRegionData([], None),
        "Hub Colloseum Podium":              CarQuestRegionData([], ["Hub Colloseum Middle Level", "Rich Area"]),
        "Hub Colloseum Middle Level":        CarQuestRegionData([], ["Glass Box"]),
        "Hub Light Puzzle Area":             CarQuestRegionData([], []),
        "Hub Floating Islands Path":         CarQuestRegionData([], ["Sands Main"]),

        # Simple
        "Simple Square Area":                CarQuestRegionData([], None),

        # Floating Cubes
        "Floating Cube Area":                CarQuestRegionData([], None),

        # Fixit Shop
        "Fixit Shop Main":                   CarQuestRegionData([], ["Fixit Shop Cave", "Fixit Shop Fence"]),
        "Fixit Shop Cave":                   CarQuestRegionData([], None),
        "Fixit Shop Fence":                  CarQuestRegionData([], None),

        # Slider
        "Slider Start":                      CarQuestRegionData([], ["Slider Lower Back", "Slider Upper Left",
                                                                     "Slider Upper Right"]),
        "Slider Lower Back":                 CarQuestRegionData([], None),
        "Slider Upper Left":                 CarQuestRegionData([], None),
        "Slider Upper Right":                CarQuestRegionData([], ["Slider Exit"]),
        "Slider Exit":                       CarQuestRegionData([], None),

        # Maze
        "Maze Start":                        CarQuestRegionData([], ["Maze Exterior Walls", "Maze Cave"]),
        "Maze Exterior Walls":               CarQuestRegionData([], ["Maze Interior Walls"]),
        "Maze Interior Walls":               CarQuestRegionData([], ["Maze Cave", "Maze Interior Walls Upper"]),
        "Maze Cave":                         CarQuestRegionData([], []),
        "Maze Interior Walls Upper":         CarQuestRegionData([], ["Maze Interior Walls Bridge"]),
        "Maze Interior Walls Bridge":        CarQuestRegionData([], None),

        # Glass Box
        "Glass Box":                         CarQuestRegionData([], ["Glass Box Exit"]),
        "Glass Box Exit":                    CarQuestRegionData([], None),

        # Sands of Fallen Kings
        "Sands Main":                        CarQuestRegionData([], ["Sands North Exterior Walls", "Sands South Exterior Walls"]),
        "Sands North Exterior Walls":        CarQuestRegionData([], []),
        "Sands South Exterior Walls":        CarQuestRegionData([], ["Sands North Exterior Walls"]),

        # Rich
        "Rich Area":                         CarQuestRegionData([], None),
    }

    for name, data in location_table.items():
        regions[data.region].locations.append(name)

    for name, data in regions.items():
        multiworld.regions.append(create_region(multiworld, player, name, data))
        
    for name, data in regions.items():
        if(data.exits == None):
            continue
        connect_regions(multiworld, player, name, data)

def create_region(multiworld: MultiWorld, player: int, name: str, data: CarQuestRegionData):
    region = Region(name, player, multiworld)
    if data.locations:
        for loc_name in data.locations:
            loc_data = location_table.get(loc_name)
            location = CarQuestLocation(player, loc_name, loc_data.code if loc_data else None, region)
            region.locations.append(location)

    return region
    
def connect_regions(multiworld: MultiWorld, player: int, source: str, data: CarQuestRegionData, rule=None):
    for _, target in enumerate(data.exits):
        sourceRegion = multiworld.get_region(source, player)
        targetRegion = multiworld.get_region(target, player)
        sourceRegion.connect(targetRegion, rule=rule)