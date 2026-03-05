from typing import Dict, List, NamedTuple, Optional

from BaseClasses import MultiWorld, Region
from .Locations import CarQuestLocationr, location_table

class CarQuestRegionData(NamedTuple):
    locations: Optional[List[str]]
    exits: Optional[List[str]]

def create_regions(multiworld: MultiWorld, player: int):
    regions: Dict[str, CarQuestRegionData] = {
        # Hub
        "Menu":                              CarQuestRegionData(None, ["Hub Start"]),
        "Hub Start":                         CarQuestRegionData([], ["Hub Simple Portal Path"]),
        "Hub Simple Portal Path":            CarQuestRegionData([], ["Simple Square Area", "Hub Pool Area"]),
        "Hub Pool Area":                     CarQuestRegionData([], ["Hub Upper Uni Alleyway", "Hub South Pool Deadend Path",
                                                                     "Floating Cube Area"]),
        "Hub Upper Uni Alleyway":            CarQuestRegionData([], None),
        "Hub South Pool Deadend Path":       CarQuestRegionData([], None),
        "Hub Museum":                        CarQuestRegionData([], None),

        # Simple
        "Simple Square Area":                CarQuestRegionData([], None),

        # Floating Cubes
        "Floating Cube Area":                CarQuestRegionData([], None),
    }