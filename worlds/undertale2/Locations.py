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
    "Ruins - Lake Monk Key":                                UT2LocationData("party", "Ruins Lake", 2),
    "Ruins - sans":                                         UT2LocationData("party", "Ruins Tree", 3),
    "Swamp - Save Monk Key":                                UT2LocationData("party", "Swamp", 4),
    "Prison - Nazrin":                                      UT2LocationData("party", "Prison Cells", 5),

    # Enemy Drops
    "Ruins - Scopestablook Drop":                           UT2LocationData("drop", "Scopestablook", 101),
    "Swamp - Friefit Drop":                                 UT2LocationData("drop", "Swamp", 102),
    "Slungy Scungle - Frogueslick Drop":                    UT2LocationData("drop", "Swamp", 103),
    "Archives Frogue Chamber - Froguelass Drop":            UT2LocationData("drop", "Frogue Chamber", 104),
    "Prison - Professormaster Cirno Drop #1":               UT2LocationData("drop", "Prison Office", 105),
    "Prison - Professormaster Cirno Drop #2":               UT2LocationData("drop", "Prison Office", 106),
    "Beach - Rouxian Rouxlette Drop":                       UT2LocationData("drop", "Beach Relax 1", 107),
    "Beach - DIE HARD Drop #1":                             UT2LocationData("drop", "Beach Relax 3", 108),
    "Beach - DIE HARD Drop #2":                             UT2LocationData("drop", "Beach Relax 3", 109),
    "Beach - Metal_Gnome Drop":                             UT2LocationData("drop", "Beach Relax 5", 110),
    "Beach - DIE HARD II Drop #1":                          UT2LocationData("drop", "Beach Relax 6", 111),
    "Beach - DIE HARD II Drop #2":                          UT2LocationData("drop", "Beach Relax 6", 112),
    "Beach - Travis Touchdown Drop #1":                     UT2LocationData("drop", "Beach Relax 7", 113),
    "Beach - Travis Touchdown Drop #2":                     UT2LocationData("drop", "Beach Relax 7", 114),

    # Shops
    "Nicky Coinflip Ruins - Paper hat Purchase":            UT2LocationData("shop", "Ruins Main", 201),
    "Nicky Coinflip Rest Stop - Lucky Crowbar Purchase":    UT2LocationData("shop", "Ruins Main", 202),
    "P-Capsule Ruins Seller - Soap-P Purchase":             UT2LocationData("shop", "Ruins Tree", 203),
    "P-Capsule Ruins Seller - Midnight-P Purchase":         UT2LocationData("shop", "Ruins Tree", 204),
    "P-Capsule Ruins Seller - Berry-P Purchase":            UT2LocationData("shop", "Ruins Tree", 205),
    "P-Capsule Ruins Seller - Spirulina-P Purchase":        UT2LocationData("shop", "Ruins Tree", 206),
    "P-Capsule Ruins Seller - Matcha-P Purchase":           UT2LocationData("shop", "Ruins Tree", 207),
    "P-Capsule Ruins Seller - Toby-P Purchase":             UT2LocationData("shop", "Ruins Tree", 208),
    
    "Archives Sewer Shop - Screamo-P":                      UT2LocationData("shop", "Archives Sewers", 209),
    "Wanda Hexagawns - Nutcracker Purchase":                UT2LocationData("shop", "Hotden", 210),
    "Wanda Hexagawns - Hawaiian shirt Puchase":             UT2LocationData("shop", "Hotden", 211),   
    "P-Capsule Hotden Seller - Kitty-P Purchase":           UT2LocationData("shop", "Hotden", 212),
    "P-Capsule Hotden Seller - Gurin-P Purchase":           UT2LocationData("shop", "Hotden", 213),
    "P-Capsule Hotden Seller - Baby-P Purchase":            UT2LocationData("shop", "Hotden", 214),
    "P-Capsule Hotden Seller - Yoko-P Purchase":            UT2LocationData("shop", "Hotden", 215),
    "P-Capsule Hotden Seller - Wadda-P Purchase":           UT2LocationData("shop", "Hotden", 216),
    
    "Nicky Coinflip Prison - Prison shank Purchase":        UT2LocationData("shop", "Prison Kitchen", 217),     
    "Nicky Coinflip Prison - Cool shades Purchase":         UT2LocationData("shop", "Prison Kitchen", 218),
    
    "P-Capsule Beach Seller - Yeller-P Purchase":           UT2LocationData("shop", "Beach Entry", 219),      
    "P-Capsule Beach Seller - Blues-P Purchase":            UT2LocationData("shop", "Beach Entry", 220),      
    "P-Capsule Beach Seller - DADADADADADA-P Purchase":     UT2LocationData("shop", "Beach Entry", 221),      
    "P-Capsule Beach Seller - Printa-P Purchase":           UT2LocationData("shop", "Beach Entry", 222),      

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
    "Intermission - sans' package":                         UT2LocationData("pickup", "Ruins Tree", 22),

    "Archives - Basement Bart":                             UT2LocationData("pickup", "Archives Pit", 23),
    "Archives - Broom Closet Lower Chest":                  UT2LocationData("pickup", "Archives Pit", 24),
    "Archives - Broom Closet Upper Chest":                  UT2LocationData("pickup", "Archives Pit", 25),
    "Archives Sewer - Shop Math Token":                     UT2LocationData("pickup", "Archives Sewers", 26),
    "Archives Chimeny - Magic Glass Chest":                 UT2LocationData("pickup", "Archives Back", 27),
    "Church - Chef Chest":                                  UT2LocationData("pickup", "Hotden", 28),
    "Archives Frogue Chamber - Odd Key":                    UT2LocationData("pickup", "Frogue Chamber", 29),

    "Swamp - Upper Chest":                                  UT2LocationData("pickup", "Swamp", 30),
    "Swamp - Lower Chest":                                  UT2LocationData("pickup", "Swamp", 31),

    "Prison - Corridor Chest Behind Spikes":                UT2LocationData("pickup", "Prison Cells", 32),
    "Prison - Puzzle Chest":                                UT2LocationData("pickup", "Prison Puzzle", 33),
    "Prison - Marylin Reward #1":                           UT2LocationData("pickup", "Prison Puzzle", 34),
    "Prison - Marylin Reward #2":                           UT2LocationData("pickup", "Prison Puzzle", 35),
    "Prison - Waiting Room Chest":                          UT2LocationData("pickup", "Prison Office", 36),
    "Prison - Explosion Chest":                             UT2LocationData("pickup", "Prison Office", 37),

    "Beach - Relax Hall Pass":                              UT2LocationData("pickup", "Beach Entry", 38),
    "Beach - Fishing Gear Bought":                          UT2LocationData("pickup", "Beach Entry", 39),

    # Enemies
    "#1 Flowey Card":                                       UT2LocationData("boss", "Landing", 301),
    "#2 Froggit Card":                                      UT2LocationData("enemy", "Ruins Main", 302),
    "#3 Bart Playing Rough Card":                           UT2LocationData("enemy", "Ruins Main", 303),
    "#4 Scopestablook Card":                                UT2LocationData("boss", "Scopestablook", 304),
    "#5 Peatrooper Card":                                   UT2LocationData("enemy", "Ruins Lake", 305),
    "#6 Helper Mimic Card":                                 UT2LocationData("enemy", "Archives Sewers", 306),
    "#7 Table Mimic Card":                                  UT2LocationData("boss", "Ruins Lake", 307),
    "#8 Dust Bunny Card":                                   UT2LocationData("enemy", "Archives Pit", 308),
    "#9 Minesweeper Card":                                  UT2LocationData("enemy", "Archives Pit", 309),
    "#10 Greater Guaglione Card":                           UT2LocationData("enemy", "Archives Pit", 310),   
    "#11 Lancer Card":                                      UT2LocationData("enemy", "Special Enemies", 311),
    "#12 Whimsoot Card":                                    UT2LocationData("enemy", "Archives Back", 312),
    "#13 Smolderpot Card":                                  UT2LocationData("enemy", "Archives Back", 313),
    "#14 Friefit Card":                                     UT2LocationData("boss", "Swamp", 314),
    "#15 Bog Cog Card":                                     UT2LocationData("enemy", "Swamp", 315),
    "#16 Frogueslick Card":                                 UT2LocationData("boss", "Swamp", 316),
    "#17 Froguelass Card":                                  UT2LocationData("boss", "Frogue Chamber", 317),
    "#18 Homer Guard Card":                                 UT2LocationData("enemy", "Special Enemies", 318),
    "#19 Prison Tick Card":                                 UT2LocationData("enemy", "Special Enemies", 319),
    "#20 Marylin Card":                                     UT2LocationData("boss", "Prison Puzzle", 320),
    "#21 Professormaster Cirno Card":                       UT2LocationData("boss", "Prison Office", 321),
    "#21 Prisonmaster Cirno Card":                          UT2LocationData("boss", "Special Enemies", 921),

    "#48 Rouxian Rouxlette Card":                           UT2LocationData("enemy", "Beach Relax 1", 348),
    "#49 Plami Card":                                       UT2LocationData("enemy", "Beach Relax 2", 349),
    "#50 DIE HARD Card":                                    UT2LocationData("enemy", "Beach Relax 3", 350),
    "#51 Excutie Card":                                     UT2LocationData("enemy", "Beach Relax 4", 351),
    "#52 Metal_Gnome Card":                                 UT2LocationData("enemy", "Beach Relax 5", 352),
    "#53 DIE HARD II Card":                                 UT2LocationData("enemy", "Beach Relax 6", 353),
    "#54 Travis Touchdown Card":                            UT2LocationData("enemy", "Beach Relax 7", 354),

    "#59 Gilded☆Bingus Card":                              UT2LocationData("enemy", "Ruins Lake", 359),

    # Special
    "Church - Play Cooking Minigame 1 Time":                UT2LocationData("minigame", "Hotden", 401),
    "Church - Play Cooking Minigame 5 Times":               UT2LocationData("minigame", "Hotden", 402), 

    "Beach - Relax Rank Up 1":                              UT2LocationData("minigame", "Beach Relax 1", 403),
    "Beach - Relax Rank Up 2":                              UT2LocationData("minigame", "Beach Relax 2", 404),
    "Beach - Relax Rank Up 3":                              UT2LocationData("minigame", "Beach Relax 3", 405),
    "Beach - Relax Rank Up 4":                              UT2LocationData("minigame", "Beach Relax 4", 406),
    "Beach - Relax Rank Up 5":                              UT2LocationData("minigame", "Beach Relax 5", 407),
    "Beach - Relax Rank Up 6":                              UT2LocationData("minigame", "Beach Relax 6", 408),
    "Beach - Relax Rank Up 7":                              UT2LocationData("minigame", "Beach Relax 7", 409),

    # Silly
    # "Rest Zone - PISS AND SHIT FM":                         UT2LocationData("silly", "Rest Zone", 1001),
    # "Hotden - Naughty Child Wiggler":                       UT2LocationData("silly", "Hotden", 1002),

    # Prison
    
}

event_location_table: Dict[str, UT2LocationData] = {
    "Lancer Encounter":                                     UT2LocationData("event", "Archives Back"),
    "Hotden Reached":                                       UT2LocationData("event", "Hotden"),
    "Cirno Defeated":                                       UT2LocationData("event", "Prison Office")
}
