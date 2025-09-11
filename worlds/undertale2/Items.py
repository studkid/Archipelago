from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification


class UT2Item(Item):
    game: str = "Undertale 2"


class UT2ItemData(NamedTuple):
    category: str
    code: Optional[int] = None
    classification: ItemClassification = ItemClassification.filler
    max_quantity: int = 1
    weight: int = 0


def get_items_by_category(category: str) -> Dict[str, UT2ItemData]:
    item_dict: Dict[str, UT2ItemData] = {}
    for name, data in item_table.items():
        if data.category == category:
            item_dict.setdefault(name, data)

    return item_dict

item_table: Dict[str, UT2ItemData] = {
    # Party Members
    # "Frisk":                    UT2ItemData("party", 1, ItemClassification.progression),
    "Fabio":                                UT2ItemData("party", 2, ItemClassification.progression),
    "Progressive Monk Key":                 UT2ItemData("key", 3, ItemClassification.progression, 2),
    "SANS":                                 UT2ItemData("party", 4, ItemClassification.progression),
    # "Nazrin":       UT2ItemData("party", 5, ItemClassification.progression),

    # Armor
    "Paper hat":                            UT2ItemData("head", 101, ItemClassification.progression_deprioritized),
    "Pinkeye scope":                        UT2ItemData("eyewear", 102, ItemClassification.progression_deprioritized),
    "Hawaiian shirt":                       UT2ItemData("body", 103, ItemClassification.progression_deprioritized),
    "Froggit Leg":                          UT2ItemData("trinket", 104, ItemClassification.progression_deprioritized),

    # Weapons
    "Lucky Crowbar":                        UT2ItemData("weapon", 201, ItemClassification.progression),
    "Baseball Bat":                         UT2ItemData("weapon", 202, ItemClassification.progression_deprioritized),
    "Nutcracker":                           UT2ItemData("weapon", 203, ItemClassification.progression_deprioritized),

    # Key Items
    "Gold Key":                             UT2ItemData("key", 301, ItemClassification.progression),
    "Silver Key":                           UT2ItemData("key", 302, ItemClassification.progression),
    "Bronze Key":                           UT2ItemData("key", 303, ItemClassification.progression),
    "Progressive Key":                      UT2ItemData("progkey", 304, ItemClassification.progression, 4),
    "Anime catboy transformation potion":   UT2ItemData("misc prog", 304, ItemClassification.progression),
    "Library Card":                         UT2ItemData("misc prog", 305, ItemClassification.progression),

    # Junk
    "EXP breeze badge!!!":                  UT2ItemData("trinket", 1001, ItemClassification.filler),
    "PEZ candy":                            UT2ItemData("filler", 1002, ItemClassification.filler, weight=6),
    "10 DOLLARS":                           UT2ItemData("filler", 1003, ItemClassification.filler, weight=5),
    "Soap-P":                               UT2ItemData("filler", 1004, ItemClassification.filler),
    "Midnight-P":                           UT2ItemData("filler", 1005, ItemClassification.filler),
    "Berry-P":                              UT2ItemData("filler", 1006, ItemClassification.filler),
    "Spirulina-P":                          UT2ItemData("filler", 1007, ItemClassification.filler),
    "Matcha-P":                             UT2ItemData("filler", 1008, ItemClassification.filler),
    "Toby-P":                               UT2ItemData("filler", 1009, ItemClassification.filler),
    "Tissue":                               UT2ItemData("filler", 1010, ItemClassification.filler, weight=3),
    "Dust Bomb":                            UT2ItemData("filler", 1011, ItemClassification.filler, weight=4),
    "Screamo-P":                            UT2ItemData("filler", 1012, ItemClassification.filler),
    "Mathtoken":                            UT2ItemData("filler", 1013, ItemClassification.filler, weight=1),
    "Kitty-P":                              UT2ItemData("filler", 1014, ItemClassification.filler),
    "Gurin-P":                              UT2ItemData("filler", 1015, ItemClassification.filler),
    "Baby-P":                               UT2ItemData("filler", 1016, ItemClassification.filler),
    "Yoko-P":                               UT2ItemData("filler", 1017, ItemClassification.filler),
    "Wadda-P":                              UT2ItemData("filler", 1018, ItemClassification.filler),
    "Scrumptious Stew":                     UT2ItemData("filler", 1019, ItemClassification.filler, weight=1),
    "Placebo":                              UT2ItemData("filler", 1020, ItemClassification.filler, weight=1),
}

event_item_table: Dict[str, UT2ItemData] = {
    "Lancer Encountered":                   UT2ItemData("event", classification=ItemClassification.progression),
    "Hotden Reached":                       UT2ItemData("event", classification=ItemClassification.progression),
}
