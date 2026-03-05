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
    "Hub: Tree Slalom Unlock":                      CarQuestItemData("secret", 7, ItemClassification.progression),
    "Hub: Museum Unlock":                           CarQuestItemData("secret", 8, ItemClassification.progression),
    "Hub: North Pool Portal Access":                CarQuestItemData("secret", 9, ItemClassification.progression),
    "Hub: Cube Monument Access":                    CarQuestItemData("secret", 10, ItemClassification.progression),

    # Simple
    "Simple: Exit Bridge":                          CarQuestItemData("secret", 101, ItemClassification.progression),

    # Cubes
    "Cubes: Exit Bridge":                           CarQuestItemData("secret", 102, ItemClassification.progression),
}