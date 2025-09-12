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
    "sans":                                 UT2ItemData("party", 4, ItemClassification.progression),
    "Nazrin":                               UT2ItemData("party", 5, ItemClassification.progression),

    # Armor
    "Paper hat":                            UT2ItemData("head", 101, ItemClassification.progression_deprioritized),
    "Pinkeye scope":                        UT2ItemData("eyewear", 102, ItemClassification.progression_deprioritized),
    "Hawaiian shirt":                       UT2ItemData("body", 103, ItemClassification.progression_deprioritized),
    "Froggit Leg":                          UT2ItemData("trinket", 104, ItemClassification.progression_deprioritized),
    "Hatsune Miku Dice":                    UT2ItemData("trinket", 105, ItemClassification.progression_deprioritized),
    "Chef's Kiss":                          UT2ItemData("trinket", 106, ItemClassification.progression_deprioritized),
    "Chef's Hat":                           UT2ItemData("head", 107, ItemClassification.progression_deprioritized),
    "Cool Shades":                          UT2ItemData("eyewear", 108, ItemClassification.progression_deprioritized),
    "Ice crystals":                         UT2ItemData("body", 109, ItemClassification.progression_deprioritized),
    "Prisonmaster pauldrons":               UT2ItemData("trinket", 110, ItemClassification.progression_deprioritized),

    # Weapons
    "Lucky Crowbar":                        UT2ItemData("weapon", 201, ItemClassification.progression),
    "Baseball Bat":                         UT2ItemData("weapon", 202, ItemClassification.progression_deprioritized),
    "Nutcracker":                           UT2ItemData("weapon", 203, ItemClassification.progression_deprioritized),
    "Madame's Chalice":                     UT2ItemData("weapon", 204, ItemClassification.progression_deprioritized),
    "Prison Shank":                         UT2ItemData("weapon", 205, ItemClassification.progression_deprioritized),

    # Key Items
    "Gold Key":                             UT2ItemData("key", 301, ItemClassification.progression),
    "Silver Key":                           UT2ItemData("key", 302, ItemClassification.progression),
    "Bronze Key":                           UT2ItemData("key", 303, ItemClassification.progression),
    "Progressive Key":                      UT2ItemData("progkey", 304, ItemClassification.progression, 5),
    "Anime catboy transformation potion":   UT2ItemData("misc prog", 305, ItemClassification.progression),
    "Library Card":                         UT2ItemData("misc prog", 306, ItemClassification.progression),
    "Odd Key":                              UT2ItemData("misc prog", 307, ItemClassification.progression, 1),
    "Puzzle Key":                           UT2ItemData("misc prog", 308, ItemClassification.progression),
    "Prison Key":                           UT2ItemData("misc prog", 309, ItemClassification.progression),
    "Feelings Key":                         UT2ItemData("useful", 310, ItemClassification.useful),

    # Card
    "#18 Homer Guard Card":                 UT2ItemData("card", 401, ItemClassification.progression),
    "#19 Prison Tick Card":                 UT2ItemData("card", 402, ItemClassification.progression),

    # Junk
    "EXP breeze badge!!!":                  UT2ItemData("trinket", 1001, ItemClassification.filler),
    "PEZ candy":                            UT2ItemData("filler", 1002, ItemClassification.filler, 0, 6),
    "10 DOLLARS":                           UT2ItemData("filler", 1003, ItemClassification.filler, 0, 5),
    "Soap-P":                               UT2ItemData("filler", 1004, ItemClassification.filler),
    "Midnight-P":                           UT2ItemData("filler", 1005, ItemClassification.filler),
    "Berry-P":                              UT2ItemData("filler", 1006, ItemClassification.filler),
    "Spirulina-P":                          UT2ItemData("filler", 1007, ItemClassification.filler),
    "Matcha-P":                             UT2ItemData("filler", 1008, ItemClassification.filler),
    "Toby-P":                               UT2ItemData("filler", 1009, ItemClassification.filler),
    "Tissue":                               UT2ItemData("filler", 1010, ItemClassification.filler, 0, 3),
    "Dust Bomb":                            UT2ItemData("filler", 1011, ItemClassification.filler, 0, 4),
    "Screamo-P":                            UT2ItemData("filler", 1012, ItemClassification.filler),
    "Mathtoken":                            UT2ItemData("filler", 1013, ItemClassification.filler, 0, 1),
    "Kitty-P":                              UT2ItemData("filler", 1014, ItemClassification.filler),
    "Gurin-P":                              UT2ItemData("filler", 1015, ItemClassification.filler),
    "Baby-P":                               UT2ItemData("filler", 1016, ItemClassification.filler),
    "Yoko-P":                               UT2ItemData("filler", 1017, ItemClassification.filler),
    "Wadda-P":                              UT2ItemData("filler", 1018, ItemClassification.filler),
    "Horrible Hodgepodge":                  UT2ItemData("filler", 1019, ItemClassification.filler, 0, 1),
    "Below-average Broth":                  UT2ItemData("filler", 1020, ItemClassification.filler, 0, 3),
    "Steaming Soup":                        UT2ItemData("filler", 1021, ItemClassification.filler, 0, 5),
    "Scrumptious Stew":                     UT2ItemData("filler", 1022, ItemClassification.filler, 0, 3),
    "Pzuzu's Potpourri":                    UT2ItemData("filler", 1023, ItemClassification.filler, 0, 1),
    "Placebo":                              UT2ItemData("filler", 1024, ItemClassification.filler, 0, 1),
    "Gravy Granules":                       UT2ItemData("filler", 1025, ItemClassification.filler, 0, 1),
}

event_item_table: Dict[str, UT2ItemData] = {
    "Lancer Encountered":                   UT2ItemData("event", classification=ItemClassification.progression),
    "Hotden Reached":                       UT2ItemData("event", classification=ItemClassification.progression),
    "Prison Destroyed":                     UT2ItemData("event", classification=ItemClassification.progression),
}
