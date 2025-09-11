from typing import Dict, NamedTuple, Optional

from BaseClasses import Location


class UT2Location(Location):
    game: str = "Undertale 2"


class UT2LocationData(NamedTuple):
    category: str
    region: str
    code: Optional[int] = None


def get_locations_by_category(category: str) -> Dict[str, UT2LocationData]:
    location_dict: Dict[str, UT2LocationData] = {}
    for name, data in location_table.items():
        if data.category == category:
            location_dict.setdefault(name, data)

    return location_dict

location_table: Dict[str, UT2LocationData] = {
    # Party Members
    "Ruins - Fabio":                                        UT2LocationData("party", "Ruins Main", 1),
    "Ruins - Monk Key":                                     UT2LocationData("party", "Ruins Lake", 2),
    "Ruins - SANS":                                         UT2LocationData("party", "Ruins Tree", 3),

    # Enemy Drops
    "Ruins - Scopestablook Scope":                          UT2LocationData("boss", "Ruins Main", 101),

    # Shops
    "Ruins - Paper hat Purchase":                           UT2LocationData("shop", "Ruins Main", 201),
    "Ruins - Lucky Crowbar Purchase":                       UT2LocationData("shop", "Ruins Main", 202),
    "Ruins - Soap-P Purchase":                              UT2LocationData("shop", "Ruins Tree", 203),
    "Ruins - Midnight-P Purchase":                          UT2LocationData("shop", "Ruins Tree", 204),
    "Ruins - Berry-P Purchase":                             UT2LocationData("shop", "Ruins Tree", 205),
    "Ruins - Spirulina-P Purchase":                         UT2LocationData("shop", "Ruins Tree", 206),
    "Ruins - Matcha-P Purchase":                            UT2LocationData("shop", "Ruins Tree", 207),
    "Ruins - Toby-P Purchase":                              UT2LocationData("shop", "Ruins Tree", 208),

    # Item Pickups
    "Landing - In the Void":                                UT2LocationData("pickup", "Landing", 10),
    "Ruins - Corridor Homer PEZ Dispenser 1":               UT2LocationData("pickup", "Ruins Main", 11),
    "Ruins - Corridor Homer PEZ Dispenser 2":               UT2LocationData("pickup", "Ruins Main", 12),
    "Ruins - Corridor Homer PEZ Dispenser 3":               UT2LocationData("pickup", "Ruins Main", 13),
    "Ruins - Corridor Chest":                               UT2LocationData("pickup", "Ruins Main", 14),
    "Ruins - Rest Zone Homer PEZ Dispenser 1":              UT2LocationData("pickup", "Ruins Main", 15),
    "Ruins - Rest Zone Homer PEZ Dispenser 2":              UT2LocationData("pickup", "Ruins Main", 16),
    "Ruins - Rest Zone Homer PEZ Dispenser 3":              UT2LocationData("pickup", "Ruins Main", 17),
    "Ruins - Rest Zone Homer Puzzle":                       UT2LocationData("pickup", "Ruins Main", 18),
    "Ruins - Lake Gold Key":                                UT2LocationData("pickup", "Ruins Lake", 19),
    "Ruins - Lake Silver Key":                              UT2LocationData("pickup", "Ruins Lake", 20),
    "Ruins - Lake Bronze Key":                              UT2LocationData("pickup", "Ruins Lake", 21),

    # Enemies
    "Flowey Card":                                          UT2LocationData("boss", "Landing", 301),
    "Froggit Card":                                         UT2LocationData("enemy", "Ruins Main", 302),
    "Bart Playing Rough Card":                              UT2LocationData("enemy", "Ruins Main", 303),
    "Scopestablook Card":                                   UT2LocationData("boss", "Ruins Main", 304),
    "Peatrooper Card":                                      UT2LocationData("enemy", "Ruins Lake", 305),
    "Helper Mimic Card":                                    UT2LocationData("enemy", "Sewers", 306),
    "Table Mimic Card":                                     UT2LocationData("boss", "Ruins Lake", 307),

    "Gilded☆Bingus Card":                                  UT2LocationData("enemy", "Ruins Lake", 359),

    # Silly
    "Rest Zone - PISS AND SHIT FM":                         UT2LocationData("silly", "Rest Zone", 1001),
}

event_location_table: Dict[str, UT2LocationData] = {
    
}
