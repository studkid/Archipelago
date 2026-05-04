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
        "Hub Central Bridge":                CarQuestRegionData([], ["Maze Start", "Hub Lookout Long Path", "Hub Tree"]),
        "Hub University Exterior":           CarQuestRegionData([], ["Hub Lower Whale Lookout", "Hub University Interior"]),
        "Hub Upper Pool Perimeter":          CarQuestRegionData([], ["Hub Light Puzzle Area", "Hub Throne Room East Exterior", "Hub Start Outlook", "Hub Ice Portal"]),
        "Hub Lower Whale Lookout":           CarQuestRegionData([], ["Hub Whale Bridge"]),
        "Hub Whale Bridge":                  CarQuestRegionData([], ["Ocean Main"]),
        "Hub Colloseum":                     CarQuestRegionData([], ["Hub Colloseum Exterior", "Hub Colloseum Podium"]),
        "Hub Colloseum Exterior":            CarQuestRegionData([], None),
        "Hub Colloseum Podium":              CarQuestRegionData([], ["Hub Colloseum Middle Level", "Rich Area"]),
        "Hub Colloseum Middle Level":        CarQuestRegionData([], ["Glass Box"]),
        "Hub Light Puzzle Area":             CarQuestRegionData([], []),
        "Hub Floating Islands Path":         CarQuestRegionData([], ["Sands Main"]),
        "Hub Lookout Long Path":             CarQuestRegionData([], []),
        "Hub Start Outlook":                 CarQuestRegionData([], None),
        "Hub University Interior":           CarQuestRegionData([], ["Hub University Second Floor"]),
        "Hub University Second Floor":       CarQuestRegionData([], ["Island Day"]),
        "Hub Ice Portal":                    CarQuestRegionData([], ["Ice Temple Main"]),
        "Hub Tree":                          CarQuestRegionData([], ["Sheep Patures Main"]),

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

        # Ocean
        "Ocean Main":                        CarQuestRegionData([], ["Ocean Inside Fort"]),
        "Ocean Inside Fort":                 CarQuestRegionData([], []),

        # Ice Temple
        "Ice Temple Main":                   CarQuestRegionData([], ["Ice Temple NE Ledge", "Ice Temple Lower East Ledge",
                                                                     "Ice Temple South Path Start", "Ice NE Perimeter Ledge"]),
        "Ice Temple South Path Start":       CarQuestRegionData([], ["Ice Temple South Ledge End"]),
        "Ice Temple South Ledge End":        CarQuestRegionData([], None),
        "Ice Temple NE Ledge":               CarQuestRegionData([], None),
        "Ice Temple Lower East Ledge":       CarQuestRegionData([], None),
        "Ice NE Perimeter Ledge":            CarQuestRegionData([], ["Ice SE Tower"]),
        "Ice SE Tower":                      CarQuestRegionData([], ["Ice South Bridge"]),
        "Ice SW Tower":                      CarQuestRegionData([], ["Ice South Bridge"]),
        "Ice South Bridge":                  CarQuestRegionData([], ["Ice SW Tower", "Ice Northern Towers"]),
        "Ice Northern Towers":               CarQuestRegionData([], ["Ice Tower Jump", "Ice Bridge Ramp To Monument", "Ice NE Tower Interior"]),
        "Ice Tower Jump":                    CarQuestRegionData([], []),
        "Ice Bridge Ramp To Monument":       CarQuestRegionData([], ["Ice Temple Lower East Ledge"]),
        "Ice NE Tower Interior":             CarQuestRegionData([], []),

        # Sheep Patures
        "Sheep Patures Main":                CarQuestRegionData([], ["Sheep Patures In Shed", "Sheep Patures Shed Raised"]),
        "Sheep Patures In Shed":             CarQuestRegionData([], []),
        "Sheep Patures Shed Raised":         CarQuestRegionData([], []),

        # Brick Bristle's Island
        "Island Day":                       CarQuestRegionData([], ["Island Day South Path", "Island Night",
                                                                    "Island North Lower Ledge", "Island North Upper Ledge",
                                                                    "Island East Path End", "Island Treetop"]),
        "Island Day South Path":            CarQuestRegionData([], []),
        "Island Night South Path":          CarQuestRegionData([], []),
        "Island Night":                     CarQuestRegionData([], ["Island Hut Ledge", "Island Night South Path", "Island East Path End"]),
        "Island North Lower Ledge":         CarQuestRegionData([], []),
        "Island North Upper Ledge":         CarQuestRegionData([], ["Island North Lower Ledge"]),
        "Island Hut Ledge":                 CarQuestRegionData([], ["Island Hut Inside"]),
        "Island Hut Inside":                CarQuestRegionData([], ["Island Treetop", "Island Hut Ledge"]),
        "Island East Path End":             CarQuestRegionData([], []),
        "Island Treetop":                   CarQuestRegionData([], ["Island Hut Inside"]),

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