from typing import Dict, NamedTuple, Optional

from BaseClasses import Location


class UT2Location(Location):
    game: str = "Undertale 2"


class UT2LocationData(NamedTuple):
    category: str
    code: Optional[int] = None


def get_locations_by_category(category: str) -> Dict[str, UT2LocationData]:
    location_dict: Dict[str, UT2LocationData] = {}
    for name, data in location_table.items():
        if data.category == category:
            location_dict.setdefault(name, data)

    return location_dict

location_table: Dict[str, UT2LocationData] = {
    # Party Members
    "Ruins - Fabio":                                         UT2LocationData("party", 1),
    "Ruins - Monk Key":                                      UT2LocationData("party", 2),
    "Ruins - SANS":                                          UT2LocationData("party", 3),

    # Enemy Drops
    "Ruins - Scopestablook Scope":                          UT2LocationData("boss", 101),

    # Shops
    "Ruins - Paper hat Purchase":                           UT2LocationData("shop", 201),
    "Ruins - Lucky Crowbar Purchase":                       UT2LocationData("shop", 202),
    "Ruins - Soap-P Purchase":                              UT2LocationData("shop", 203),
    "Ruins - Midnight-P Purchase":                          UT2LocationData("shop", 204),
    "Ruins - Berry-P Purchase":                             UT2LocationData("shop", 205),
    "Ruins - Spirulina-P Purchase":                         UT2LocationData("shop", 206),
    "Ruins - Matcha-P Purchase":                            UT2LocationData("shop", 207),
    "Ruins - Toby-P Purchase":                              UT2LocationData("shop", 208),

    # Item Pickups
    "Landing - In the Void":                                UT2LocationData("pickup", 10),
    "Ruins - Corridor Homer PEZ Dispenser 1":               UT2LocationData("pickup", 11),
    "Ruins - Corridor Homer PEZ Dispenser 2":               UT2LocationData("pickup", 12),
    "Ruins - Corridor Homer PEZ Dispenser 3":               UT2LocationData("pickup", 13),
    "Ruins - Corridor Chest":                               UT2LocationData("pickup", 14),
    "Ruins - Rest Zone Homer PEZ Dispenser 1":              UT2LocationData("pickup", 15),
    "Ruins - Rest Zone Homer PEZ Dispenser 2":              UT2LocationData("pickup", 16),
    "Ruins - Rest Zone Homer PEZ Dispenser 3":              UT2LocationData("pickup", 17),
    "Ruins - Rest Zone Homer Puzzle":                       UT2LocationData("pickup", 18),
    "Ruins - Lake Gold Key":                                UT2LocationData("pickup", 19),
    "Ruins - Lake Silver Key":                              UT2LocationData("pickup", 20),
    "Ruins - Lake Bronze Key":                              UT2LocationData("pickup", 21),

    # Silly
    "Rest Zone - PISS AND SHIT FM":                         UT2LocationData("silly", 1001),
}

event_location_table: Dict[str, UT2LocationData] = {
    
}
