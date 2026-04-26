from typing import NamedTuple, Dict
from BaseClasses import Item, ItemClassification, Optional

class CarQuestItem(Item):
    game: str = "Car Quest"

class       CarQuestItemData(NamedTuple):
    category: str
    code: Optional[int] = None
    classification: ItemClassification = ItemClassification.filler

def get_items_by_category(category: str) -> Dict[str, CarQuestItemData]:
    item_dict: Dict[str, CarQuestItemData] = {}
    for name, data in item_table.items():
        if data.category == category:
            item_dict.setdefault(name, data)

    return item_dict

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

    # Simple
    "Simple: Exit Bridge":                          CarQuestItemData("secret", 101, ItemClassification.progression),

    # Cubes
    "Cubes: Exit Bridge":                           CarQuestItemData("secret", 111, ItemClassification.progression),

    # Desert
    "Desert: South West Mound":                     CarQuestItemData("secret", 121, ItemClassification.progression),
    "Desert: Shop Cave Door":                       CarQuestItemData("secret", 122, ItemClassification.progression),
    "Desert: North West Mount":                     CarQuestItemData("secret", 123, ItemClassification.progression),
    "Desert: South East Mount":                     CarQuestItemData("secret", 124, ItemClassification.progression),
    "Desert: Fixit Shop Door":                      CarQuestItemData("secret", 125, ItemClassification.progression),
    "Desert: Fixit Shop Fence":                     CarQuestItemData("secret", 126, ItemClassification.progression),
    "Desert: Exit Ramp":                            CarQuestItemData("secret", 127, ItemClassification.progression),
}