from typing import NamedTuple, Dict
from BaseClasses import Item, ItemClassification, Optional

class CarQuestItem(Item):
    game: str = "Car Quest"

class CarQuestItemData(NamedTuple):
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
    "Start Room Blocker":               CarQuestItemData("secret", 1, ItemClassification.progression),
    "Start Room Blocker":               CarQuestItemData("secret", 2, ItemClassification.progression),
}