from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification


class UT2Item(Item):
    game: str = "Undertale 2"


class UT2ItemData(NamedTuple):
    category: str
    code: Optional[int] = None
    classification: ItemClassification = ItemClassification.filler
    max_quantity: int = 1
    weight: int = 1


def get_items_by_category(category: str) -> Dict[str, UT2ItemData]:
    item_dict: Dict[str, UT2ItemData] = {}
    for name, data in item_table.items():
        if data.category == category:
            item_dict.setdefault(name, data)

    return item_dict

item_table: Dict[str, UT2ItemData] = {
    # Party Members
    # "Frisk":                    UT2ItemData("party", 1, ItemClassification.progression),
    "Fabio":                    UT2ItemData("party", 2, ItemClassification.progression),
    "Monk Key":                 UT2ItemData("party", 3, ItemClassification.progression),
    "SANS":                     UT2ItemData("party", 4, ItemClassification.progression),
    # "Nazrin":       UT2ItemData("party", 5, ItemClassification.progression),

    # Armor
    "Paper hat":                UT2ItemData("armor", 101, ItemClassification.progression_deprioritized),
    "Pinkeye scope":            UT2ItemData("armor", 102, ItemClassification.progression_deprioritized),

    # Weapons
    "Lucky Crowbar":            UT2ItemData("weapon", 201, ItemClassification.progression),
    "Baseball Bat":             UT2ItemData("weapon", 201, ItemClassification.progression_deprioritized),

    # Key Items
    "Gold Key":                 UT2ItemData("key", 301, ItemClassification.progression),
    "Silver Key":               UT2ItemData("key", 302, ItemClassification.progression),
    "Bronze Key":               UT2ItemData("key", 303, ItemClassification.progression),
    "Progressive Key":          UT2ItemData("progkey", 304, ItemClassification.progression, 4),

    # Junk
    "EXP breeze badge!!!":      UT2ItemData("filler", 1001, ItemClassification.filler),
    "PEZ candy":                UT2ItemData("filler", 1002, ItemClassification.filler, weight=6),
    "10 DOLLARS":               UT2ItemData("filler", 1003, ItemClassification.filler, weight=5),
    "Soap-P":                   UT2ItemData("filler", 1004, ItemClassification.filler),
    "Midnight-P":               UT2ItemData("filler", 1005, ItemClassification.filler),
    "Berry-P":                  UT2ItemData("filler", 1006, ItemClassification.filler),
    "Spirulina-P":              UT2ItemData("filler", 1007, ItemClassification.filler),
    "Matcha-P":                 UT2ItemData("filler", 1008, ItemClassification.filler),
    "Toby-P":                   UT2ItemData("filler", 1009, ItemClassification.filler),
}

event_item_table: Dict[str, UT2ItemData] = {
    
}
