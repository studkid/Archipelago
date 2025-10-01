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
    "Paper hat":                            UT2ItemData("head", 101, ItemClassification.useful),
    "Pinkeye scope":                        UT2ItemData("eyewear", 102, ItemClassification.useful),
    "Hawaiian shirt":                       UT2ItemData("body", 103, ItemClassification.useful),
    "Froggit Leg":                          UT2ItemData("trinket", 104, ItemClassification.useful),
    "Hatsune Miku Dice":                    UT2ItemData("trinket", 105, ItemClassification.useful),
    "Chef's Kiss":                          UT2ItemData("trinket", 106, ItemClassification.useful),
    "Chef's Hat":                           UT2ItemData("head", 107, ItemClassification.useful),
    "Cool Shades":                          UT2ItemData("eyewear", 108, ItemClassification.useful),
    "Ice crystals":                         UT2ItemData("body", 109, ItemClassification.useful),
    "Prisonmaster pauldrons":               UT2ItemData("trinket", 110, ItemClassification.useful),
    "Rouxian Lapel":                        UT2ItemData("trinket", 111, ItemClassification.useful),
    "Mimic's adieu":                        UT2ItemData("trinket", 112, ItemClassification.useful),
    "Sunflower":                            UT2ItemData("eyewear", 113, ItemClassification.useful),
    "Fisherman's hat":                      UT2ItemData("head", 114, ItemClassification.useful),
    "\"WOMEN WANT ME FISH FEAR ME\" hat":   UT2ItemData("head", 115, ItemClassification.useful),
    "Aluminum Visor":                       UT2ItemData("head", 116, ItemClassification.useful),
    "Funnypoo 69":                          UT2ItemData("trinket", 117, ItemClassification.useful),
    "Joqua's Box":                          UT2ItemData("trinket", 118, ItemClassification.useful),
    "Hector":                               UT2ItemData("trinket", 119, ItemClassification.useful),
    "Aluminum Shirt":                       UT2ItemData("body", 120, ItemClassification.useful),
    "Aluminum Hat":                         UT2ItemData("head", 121, ItemClassification.useful),
    "Aluminum Badge":                       UT2ItemData("trinket", 122, ItemClassification.useful),
    "Ra Men Abs":                           UT2ItemData("body", 123, ItemClassification.useful),

    # Weapons
    "Lucky Crowbar":                        UT2ItemData("weapon", 201, ItemClassification.progression),
    "Baseball Bat":                         UT2ItemData("weapon", 202, ItemClassification.useful),
    "Nutcracker":                           UT2ItemData("weapon", 203, ItemClassification.useful),
    "Madame's Chalice":                     UT2ItemData("weapon", 204, ItemClassification.useful),
    "Prison Shank":                         UT2ItemData("weapon", 205, ItemClassification.useful),
    "Empty Gun":                            UT2ItemData("weapon", 206, ItemClassification.useful),
    "Gun":                                  UT2ItemData("weapon", 207, ItemClassification.useful),
    "Blood Berry":                          UT2ItemData("weapon", 208, ItemClassification.useful),
    "Fishing rod":                          UT2ItemData("weapon", 209, ItemClassification.useful),
    "Joqua's Trowel":                       UT2ItemData("weapon", 210, ItemClassification.progression),
    "Aluminum Club":                        UT2ItemData("weapon", 211, ItemClassification.useful),
    "Scathach's Toothpick":                 UT2ItemData("weapon", 212, ItemClassification.useful),

    # Key Items
    "Gold Key":                             UT2ItemData("key", 301, ItemClassification.progression),
    "Silver Key":                           UT2ItemData("key", 302, ItemClassification.progression),
    "Bronze Key":                           UT2ItemData("key", 303, ItemClassification.progression),
    "Progressive Key":                      UT2ItemData("progkey", 304, ItemClassification.progression, 5),
    "Anime catboy transformation potion":   UT2ItemData("misc prog", 305, ItemClassification.progression),
    "Library Card":                         UT2ItemData("misc prog", 306, ItemClassification.progression),
    "Odd Key":                              UT2ItemData("misc prog", 307, ItemClassification.progression, 2),
    "Puzzle Key":                           UT2ItemData("misc prog", 308, ItemClassification.progression),
    "Prison Key":                           UT2ItemData("misc prog", 309, ItemClassification.progression),
    "Feelings Key":                         UT2ItemData("useful", 310, ItemClassification.useful),
    "Relax Pass":                           UT2ItemData("misc prog", 311, ItemClassification.progression, 7),
    "Membership Card":                      UT2ItemData("misc prog", 312, ItemClassification.progression),
    "Fisherman's haste":                    UT2ItemData("misc prog", 313, ItemClassification.useful),
    "Aquarium key":                         UT2ItemData("misc prog", 314, ItemClassification.progression),
    "Progressive Fishing Spot":             UT2ItemData("misc prog", 315, ItemClassification.progression, 6),
    "Rust Ticket":                          UT2ItemData("misc prog", 316, ItemClassification.progression),
    "Waste Ticket":                         UT2ItemData("misc prog", 317, ItemClassification.progression),
    "Bone Ticket":                          UT2ItemData("misc prog", 318, ItemClassification.progression),
    "Star Ticket":                          UT2ItemData("misc prog", 319, ItemClassification.progression),
    "Vocal Key":                            UT2ItemData("misc prog", 320, ItemClassification.progression),

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
    "Yeller-P":                             UT2ItemData("filler", 1026, ItemClassification.filler),
    "Blue-P":                               UT2ItemData("filler", 1027, ItemClassification.filler),
    "DADADADADADA-P":                       UT2ItemData("filler", 1028, ItemClassification.filler),
    "Printa-P":                             UT2ItemData("filler", 1029, ItemClassification.filler),
    "Flynn's diary":                        UT2ItemData("filler", 1030, ItemClassification.filler),
    "Knight's diary":                       UT2ItemData("filler", 1031, ItemClassification.filler),
    "Fishing Guide":                        UT2ItemData("filler", 1032, ItemClassification.filler),
    "50 DOLLARS":                           UT2ItemData("filler", 1033, ItemClassification.filler, 0, 4),
    "Frogueslab I":                         UT2ItemData("filler", 1034, ItemClassification.filler),
    "Frogueslab II":                        UT2ItemData("filler", 1035, ItemClassification.filler),
    "Frogueslab IV":                        UT2ItemData("filler", 1036, ItemClassification.filler),
    "Kiss on the Cheek":                    UT2ItemData("filler", 1037, ItemClassification.filler, 4, 1),
    "Apple Core":                           UT2ItemData("filler", 1038, ItemClassification.filler),

    # Settings
    "Relax Pass Off":                       UT2ItemData("filler", 90001, ItemClassification.filler, 0),
    "Fishing Mssion Off":                   UT2ItemData("filler", 90002, ItemClassification.filler, 0),
}

event_item_table: Dict[str, UT2ItemData] = {
    "Lancer Encountered":                   UT2ItemData("event", classification=ItemClassification.progression),
    "Hotden Reached":                       UT2ItemData("event", classification=ItemClassification.progression),
    "Prison Destroyed":                     UT2ItemData("event", classification=ItemClassification.progression),
}
