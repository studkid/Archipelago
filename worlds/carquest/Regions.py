from typing import Dict, List, NamedTuple, Optional

from BaseClasses import MultiWorld, Region
from .Locations import CarQuestLocation, location_table

class CarQuestRegionData(NamedTuple):
    locations: Optional[List[str]]
    exits: Optional[List[str]]

def create_regions(multiworld: MultiWorld, player: int):
    regions: Dict[str, CarQuestRegionData] = {
        # Hub
        "Menu":                              CarQuestRegionData(None, ["Hub Start"]),
        "Hub Start":                         CarQuestRegionData([], ["Hub Simple Portal Path", "Hub Throne Room Exterior"]),
        "Hub Simple Portal Path":            CarQuestRegionData([], ["Simple Square Area", "Hub Pool Area"]),
        "Hub Pool Area":                     CarQuestRegionData([], ["Hub Upper Uni Alleyway", "Hub South Pool Deadend Path",
                                                                     "Floating Cube Area", "Hub Cube Monument", "Hub South Portal",
                                                                     "Hub Vault", "Hub Drained Pool"]),
        "Hub Upper Uni Alleyway":            CarQuestRegionData([], None),
        "Hub South Pool Deadend Path":       CarQuestRegionData([], None),
        "Hub Museum":                        CarQuestRegionData([], None),
        "Hub Cube Monument":                 CarQuestRegionData([], None),
        "Hub South Portal":                  CarQuestRegionData([], ["Fixit Shop Main"]),
        "Hub Vault":                         CarQuestRegionData([], ["Slider Start"]),
        "Hub Drained Pool":                  CarQuestRegionData([], None),
        "Hub Throne Room Exterior":          CarQuestRegionData([], []),

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
    }