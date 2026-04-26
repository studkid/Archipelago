from typing import NamedTuple, Dict
from BaseClasses import Location, Optional

class CarQuestLocation(Location):
    game: str = "Car Quest"

class CarQuestLocationData(NamedTuple):
    category: str
    region: str
    code: Optional[int] = None


def get_locations_by_category(category: str) -> Dict[str, CarQuestLocationData]:
    location_dict: Dict[str, CarQuestLocationData] = {}
    for name, data in location_table.items():
        if data.category == category:
            location_dict.setdefault(name, data)

    return location_dict

simpleOffset = 600
cubesOffset = simpleOffset + 50
desertOffset = cubesOffset + 50
sliderOffset = desertOffset + 150
mazeOffset = sliderOffset + 50

location_table: Dict[str, CarQuestLocationData] = {
    # Hub
    # 52 Secrets
    # 10 Stained Glass
    # 371 Power Cells
    # 17 Mega Power Cells
    # 5 Tokens
    # 541 Total
    "Hub: Starting Area Artifact":                      CarQuestLocationData("Artifact", "Hub Start", 1),
    "Hub: University Alleyway Artifact":                CarQuestLocationData("Artifact", "Hub Pool Area", 2),
    "Hub: North Pool Secret Door Artifact":             CarQuestLocationData("Artifact", "Hub Pool Area", 3), # Needs "Hub: North Pool Small Secret Door"
    "Hub: North Pool Jump Ramp":                        CarQuestLocationData("Artifact", "Hub Pool Area", 4), # Needs "Hub: North Pool Jump Ramp"
    "Hub: Tree Slalom Start Artifact":                  CarQuestLocationData("Artifact", "Hub Pool Area", 5), # Needs "Hub: South Pool Artifact Block"
    "Hub: Upper University Alleyway Artifact":          CarQuestLocationData("Artifact", "Hub Pool Area", 6), 
    "Hub: South Pool Deadend Artifact":                 CarQuestLocationData("Artifact", "Hub South Pool Deadend Path", 7), 
    "Hub: Tree Slalom Reward Artifact":                 CarQuestLocationData("Artifact", "Hub Pool Area", 8), # Needs "Hub: Tree Slalom Unlock"
    "Hub: Museum Artifact":                             CarQuestLocationData("Artifact", "Hub Museum", 9),
    "Hub: Cube Monument Artifact":                      CarQuestLocationData("Artifact", "Hub Cube Monument", 10),
    "Hub: Ramp Near South Portal Artifact":             CarQuestLocationData("Artifact", "Hub South Portal", 11), 
    "Hub: North Pool Vault Room Artifact":              CarQuestLocationData("Artifact", "Hub Vault", 12), 
    "Hub: Inside Ramp Near South Portal Artifact":      CarQuestLocationData("Artifact", "Hub South Portal", 13), 
    "Hub: Pool Drain Artifact":                         CarQuestLocationData("Artifact", "Hub Pool Area", 14),
    "Hub: Drained Pool Jump Artifact":                  CarQuestLocationData("Artifact", "Hub Drained Pool", 15),
    "Hub: Throne Exterior Near Museum Piece Artifact":  CarQuestLocationData("Artifact", "Hub Throne Room East Exterior", 16),
    "Hub: Pool South West Artifact":                    CarQuestLocationData("Artifact", "Hub Pool Area", 17), # Needs Drained Pool
    "Hub: Pool South East Artifact":                    CarQuestLocationData("Artifact", "Hub Pool Area", 18), # Needs Drained Pool
    "Hub: Pool North West Artifact":                    CarQuestLocationData("Artifact", "Hub Pool Area", 19), # Needs Drained Pool
    "Hub: Pool Center Artifact":                        CarQuestLocationData("Artifact", "Hub Pool Area", 20), # Needs Refilled Pool
    "Hub: Throne Exterior Museum Piece":                CarQuestLocationData("Museum", "Hub Throne Room West Exterior", 21),
    "Hub: Throne Exterior Artifact":                    CarQuestLocationData("Artifact", "Hub Throne Room West Exterior", 22),
    "Hub: Lookout Artifact":                            CarQuestLocationData("Artifact", "Hub Central Bridge", 23),
    "Hub: Central Bridge East Ramp Artifact":           CarQuestLocationData("Artifact", "Hub Central Bridge", 24),
    "Hub: University Exterior Artifact":                CarQuestLocationData("Artifact", "Hub University Exterior", 25),
    "Hub: Central Bridge West Ramp Artifact":           CarQuestLocationData("Artifact", "Hub Central Bridge", 26),
    "Hub: Pool North East Artifact":                    CarQuestLocationData("Artifact", "Hub Pool Area", 27),

    # Simple
    # 2 Secrets
    # 30 Power Cells
    # 4 Mega Power Cells
    # 1 Token
    # 37 Total
    "Simple: Artifact Under Mound":                     CarQuestLocationData("Artifact", "Simple Square Area", simpleOffset + 1),
    "Simple: Artifact On Exit Ramp":                    CarQuestLocationData("Artifact", "Simple Square Area", simpleOffset + 2),

    # Cubes
    # 2 Secrets
    # 19 Power Cells
    # 2 Tokens
    # 22 Total
    "Cubes: Artifact Behind Start":                     CarQuestLocationData("Artifact", "Floating Cube Area", cubesOffset + 1),
    "Cubes: Artifact On Exit Ramp":                     CarQuestLocationData("Artifact", "Floating Cube Area", cubesOffset + 2),
    # "Cubes: Token Behind Start":                        CarQuestLocationData("Token", "Floating Cube Area", cubesOffset + 3), # Needs "Cubes: Exit Bridge"

    # Desert
    # 8 Secrets
    # 105 Power Cells
    # 2 Tokens
    # 115 Total
    "Desert: North East Mound Artifact":                CarQuestLocationData("Artifact", "Fixit Shop Main", desertOffset + 1),
    "Desert: South West Mound Artifact":                CarQuestLocationData("Artifact", "Fixit Shop Main", desertOffset + 2),
    "Desert: Shop Cave Artifact":                       CarQuestLocationData("Artifact", "Fixit Shop Cave", desertOffset + 3),
    "Desert: North West Mound Artifact":                CarQuestLocationData("Artifact", "Fixit Shop Main", desertOffset + 4),
    "Desert: South East Mound Artifact":                CarQuestLocationData("Artifact", "Fixit Shop Main", desertOffset + 5),
    "Desert: Fixit Shop Interior Artifact":             CarQuestLocationData("Artifact", "Fixit Shop Main", desertOffset + 6),
    "Desert: Fixit Shop Fence Artifact":                CarQuestLocationData("Artifact", "Fixit Shop Fence", desertOffset + 7),
    "Desert: Exit Reward Artifact":                     CarQuestLocationData("Artifact", "Fixit Shop Main", desertOffset + 8),

    # Slider
    # 6 Secrets
    # 32 Power Cells
    # 1 Token
    # 39 Total
    "Slider: Front Right Artifact":                     CarQuestLocationData("Artifact", "Slider Start", sliderOffset + 1),
    "Slider: Lower Back Artifact":                      CarQuestLocationData("Artifact", "Slider Lower Back", sliderOffset + 2),
    "Slider: Upper Left Artifact":                      CarQuestLocationData("Artifact", "Slider Upper Left", sliderOffset + 3),
    "Slider: Upper Right Artifact":                     CarQuestLocationData("Artifact", "Slider Upper Right", sliderOffset + 4),
    "Slider: Upper Upper Left Artifact":                CarQuestLocationData("Artifact", "Slider Upper Left", sliderOffset + 5),
    "Slider: Exit Reward Artifact":                     CarQuestLocationData("Artifact", "Slider Exit", sliderOffset + 6),

    # Maze
    "Maze: First Artifact":                             CarQuestLocationData("Artifact", "Maze Start", mazeOffset + 1),
    "Maze: On Wall Near Start Artifact":                CarQuestLocationData("Artifact", "Maze Exterior Walls", mazeOffset + 2),
    "Maze: Cave Artifact":                              CarQuestLocationData("Artifact", "Maze Cave", mazeOffset + 3),
    "Maze: Top of Mini Maze Artifact":                  CarQuestLocationData("Artifact", "Maze Interior Walls Upper", mazeOffset + 4),
    "Maze: Hidden Drop Off Artifact":                   CarQuestLocationData("Artifact", "Maze Interior Walls Upper", mazeOffset + 5),
    "Maze: On Wall Near Exit Artifact":                 CarQuestLocationData("Artifact", "Maze Interior Walls Bridge", mazeOffset + 6),
    "Maze: Exit Reward Artifact":                       CarQuestLocationData("Artifact", "Maze Interior Walls", mazeOffset + 7),
}