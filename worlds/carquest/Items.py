from typing import NamedTuple, Dict
from BaseClasses import Item, ItemClassification, Optional

class CarQuestItem(Item):
    game: str = "Car Quest"

class CarQuestItemData(NamedTuple):
    category: str
    code: Optional[int] = None
    classification: ItemClassification = ItemClassification.filler
    max_quantity: int = 1

def get_items_by_category(category: str) -> Dict[str, CarQuestItemData]:
    item_dict: Dict[str, CarQuestItemData] = {}
    for name, data in item_table.items():
        if data.category == category:
            item_dict.setdefault(name, data)

    return item_dict

simpleOffset = 100
cubesOffset = simpleOffset + 10
desertOffset = cubesOffset + 10
sliderOffset = desertOffset + 10
mazeOffset = sliderOffset + 10
glassOffset = mazeOffset + 10

item_table: Dict[str, CarQuestItemData] = {
    # Hub
    "Hub: Start Room Blocker":                      CarQuestItemData("secret", 1, ItemClassification.progression),
    "Hub: Simple Portal Bridge Wall":               CarQuestItemData("secret", 2, ItemClassification.progression),
    "Hub: North Pool Small Secret Door":            CarQuestItemData("secret", 3, ItemClassification.progression),
    "Hub: North Pool Jump Ramp":                    CarQuestItemData("secret", 4, ItemClassification.progression),
    "Hub: South Pool Artifact Block":               CarQuestItemData("secret", 5, ItemClassification.progression),
    "Hub: Upper University Alleyway Access":        CarQuestItemData("secret", 6, ItemClassification.progression),
    "Hub: South Pool Deadend Door":                 CarQuestItemData("secret", 7, ItemClassification.progression),
    "Hub: Tree Slalom Unlock":                      CarQuestItemData("secret", 8, ItemClassification.progression),
    "Hub: Museum Unlock":                           CarQuestItemData("secret", 9, ItemClassification.progression),
    "Hub: North Pool Portal Access":                CarQuestItemData("secret", 10, ItemClassification.progression),
    "Hub: Cube Monument Access":                    CarQuestItemData("secret", 11, ItemClassification.progression),
    "Hub: South Portal Ramp Door":                  CarQuestItemData("secret", 12, ItemClassification.progression),
    "Hub: North Pool Vault Door":                   CarQuestItemData("secret", 13, ItemClassification.progression),
    "Hub: South Portal Secondary Ramp":             CarQuestItemData("secret", 14, ItemClassification.progression),
    "Hub: South Portal Bridge":                     CarQuestItemData("secret", 15, ItemClassification.progression),
    "Hub: Pool Drain Door":                         CarQuestItemData("secret", 16, ItemClassification.progression),
    "Hub: Progressive Pool":                        CarQuestItemData("secret", 17, ItemClassification.progression, 2),
    "Hub: Start Room Right Door":                   CarQuestItemData("secret", 18, ItemClassification.progression),
    "Hub: Pool Push Block":                         CarQuestItemData("secret", 19, ItemClassification.progression),
    "Hub: Pool South East Blocker":                 CarQuestItemData("secret", 20, ItemClassification.progression),
    "Hub: Pool North West Blocker":                 CarQuestItemData("secret", 21, ItemClassification.progression),
    "Hub: Pool Vault Portal Unlock":                CarQuestItemData("secret", 22, ItemClassification.progression),
    "Hub: Throne Exterior Wall":                    CarQuestItemData("secret", 23, ItemClassification.progression),
    "Hub: Start Room Bridge":                       CarQuestItemData("secret", 24, ItemClassification.progression),
    "Hub: Central Bridge East Ramp":                CarQuestItemData("secret", 25, ItemClassification.progression),
    "Hub: Exterior University Ramp":                CarQuestItemData("secret", 26, ItemClassification.progression),
    "Hub: Central Bridge West Ramp":                CarQuestItemData("secret", 27, ItemClassification.progression),
    "Hub: Pool North East Blocker":                 CarQuestItemData("secret", 28, ItemClassification.progression),
    "Hub: Central Bridge Portal Bridge":            CarQuestItemData("secret", 29, ItemClassification.progression),
    "Hub: Exterior University Wall Door":           CarQuestItemData("secret", 30, ItemClassification.progression),
    "Hub: Ramp Near Simple Portal":                 CarQuestItemData("secret", 31, ItemClassification.progression),
    "Hub: Secondary Univery Wall Door":             CarQuestItemData("secret", 32, ItemClassification.progression),
    "Hub: Blocker Near Whale Bridge":               CarQuestItemData("secret", 33, ItemClassification.progression),
    "Hub: Whale Bridge":                            CarQuestItemData("secret", 34, ItemClassification.progression),
    "Hub: Colloseum Bridge":                        CarQuestItemData("secret", 35, ItemClassification.progression),
    "Hub: Colloseum Podeum Extension":              CarQuestItemData("secret", 36, ItemClassification.progression),
    "Hub: Start Area Back Removal":                 CarQuestItemData("secret", 37, ItemClassification.progression),
    "Hub: Colloseum Exterior Wall Doors":           CarQuestItemData("secret", 38, ItemClassification.progression),
    "Hub: Colloseum Push Block Unlock":             CarQuestItemData("secret", 39, ItemClassification.progression),
    "Hub: Colloseum Podoium Door":                  CarQuestItemData("secret", 40, ItemClassification.progression),
    "Hub: Colloseum Podium Ramp":                   CarQuestItemData("secret", 41, ItemClassification.progression),
    "Hub: Ramp to Light Puzzle":                    CarQuestItemData("secret", 42, ItemClassification.progression),

    "Hub: Sun Museum Glass":                        CarQuestItemData("museum", 90, ItemClassification.progression),

    # Simple
    "Simple: Exit Bridge":                          CarQuestItemData("secret",  simpleOffset + 1, ItemClassification.progression),

    # Cubes
    "Cubes: Exit Bridge":                           CarQuestItemData("secret", cubesOffset + 1, ItemClassification.progression),

    # Desert
    "Desert: South West Mound":                     CarQuestItemData("secret", desertOffset + 1, ItemClassification.progression),
    "Desert: Shop Cave Door":                       CarQuestItemData("secret", desertOffset + 2, ItemClassification.progression),
    "Desert: North West Mount":                     CarQuestItemData("secret", desertOffset + 3, ItemClassification.progression),
    "Desert: South East Mount":                     CarQuestItemData("secret", desertOffset + 4, ItemClassification.progression),
    "Desert: Fixit Shop Door":                      CarQuestItemData("secret", desertOffset + 5, ItemClassification.progression),
    "Desert: Fixit Shop Fence":                     CarQuestItemData("secret", desertOffset + 6, ItemClassification.progression),
    "Desert: Exit Ramp":                            CarQuestItemData("secret", desertOffset + 7, ItemClassification.progression),

    # Slider
    "Slider: Start Ramp":                           CarQuestItemData("secret", sliderOffset + 1, ItemClassification.progression),
    "Slider: Left Push Block Unlock":               CarQuestItemData("secret", sliderOffset + 2, ItemClassification.progression),
    "Slider: Right Push Block Unlock":              CarQuestItemData("secret", sliderOffset + 3, ItemClassification.progression),
    "Slider: Left Push Block Unlock":               CarQuestItemData("secret", sliderOffset + 4, ItemClassification.progression),
    "Slider: Exit Ramp Unlock":                     CarQuestItemData("secret", sliderOffset + 5, ItemClassification.progression),

    # Maze
    "Maze: Door to Big Ramp":                       CarQuestItemData("secret", mazeOffset + 1, ItemClassification.progression),
    "Maze: Hedge Ramp":                             CarQuestItemData("secret", mazeOffset + 2, ItemClassification.progression),
    "Maze: Raise Cave Wall":                        CarQuestItemData("secret", mazeOffset + 3, ItemClassification.progression),
    "Maze: Lower Artifact Wall":                    CarQuestItemData("secret", mazeOffset + 4, ItemClassification.progression),
    "Maze: Interior Wall Bridge":                   CarQuestItemData("secret", mazeOffset + 5, ItemClassification.progression),
    "Maze: Exit Door":                              CarQuestItemData("secret", mazeOffset + 6, ItemClassification.progression),

    # Glass Box
    "Glass Box: Useless Block":                     CarQuestItemData("secret", glassOffset + 1, ItemClassification.progression),
    "Glass Box: Exit Bridge":                       CarQuestItemData("secret", glassOffset + 2, ItemClassification.progression),

    # Filler
    "Energy Cell":                                  CarQuestItemData("filler", 10001, ItemClassification.filler),
}