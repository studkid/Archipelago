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
glassOffset = mazeOffset + 50
sandOffset = glassOffset + 60
oceanOffset = sandOffset + 140
iceOffset = oceanOffset + 140
sheepOffset = iceOffset + 200
islandOffset = sheepOffset + 120
throneOffset = islandOffset + 250
planetOffset = throneOffset + 200
powerOffset = planetOffset + 20
limboOffset = powerOffset + 230

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
    "Hub: Upper University Alleyway Artifact":          CarQuestLocationData("Artifact", "Hub Upper Uni Alleyway", 6), 
    "Hub: South Pool Dead End Artifact":                CarQuestLocationData("Artifact", "Hub South Pool Dead End Path", 7), 
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
    "Hub: Throne Exterior Artifact":                    CarQuestLocationData("Artifact", "Hub Throne Room West Exterior", 21),
    "Hub: Lookout Artifact":                            CarQuestLocationData("Artifact", "Hub Central Bridge", 22),
    "Hub: Central Bridge East Ramp Artifact":           CarQuestLocationData("Artifact", "Hub Central Bridge", 23),
    "Hub: University Exterior Artifact":                CarQuestLocationData("Artifact", "Hub University Exterior", 24),
    "Hub: Central Bridge West Ramp Artifact":           CarQuestLocationData("Artifact", "Hub Central Bridge", 25),
    "Hub: Pool North East Artifact":                    CarQuestLocationData("Artifact", "Hub Pool Area", 26),
    "Hub: Alley Push Ramp Artifact":                    CarQuestLocationData("Artifact", "Hub Uni Whale Bridge Connector", 27), # Needs "Hub: Exterior University Wall Door"
    "Hub: Upper Alley Bridge Near Throne Artifact":     CarQuestLocationData("Artifact", "Hub Upper Pool Perimeter", 28),
    "Hub: Lower Artifact Near Whale Bridge":            CarQuestLocationData("Artifact", "Hub Lower Whale Lookout", 29),
    "Hub: Upper Artifact Near Whale Bridge":            CarQuestLocationData("Artifact", "Hub Lower Whale Lookout", 30),
    "Hub: Whale Bridge Artifact":                       CarQuestLocationData("Artifact", "Hub Whale Bridge", 31),
    "Hub: Colloseum Hidden in Push Block Artifact":     CarQuestLocationData("Artifact", "Hub Colloseum", 32),
    "Hub: Colloseum Podium Artifact":                   CarQuestLocationData("Artifact", "Hub Colloseum", 33),
    "Hub: Start Area Jump Artifact":                    CarQuestLocationData("Artifact", "Hub South Portal", 34),
    "Hub: Behind Colloseum Artifact":                   CarQuestLocationData("Artifact", "Hub Colloseum Exterior", 35),
    "Hub: Near Rich Portal Artifact":                   CarQuestLocationData("Artifact", "Hub Colloseum Podium", 36),
    "Hub: Inside Podium Artifact":                      CarQuestLocationData("Artifact", "Hub Colloseum Podium", 37),
    "Hub: Upper Light Puzzle Artifact":                 CarQuestLocationData("Artifact", "Hub Light Puzzle Area", 38),
    "Hub: Floating Island Artifact":                    CarQuestLocationData("Artifact", "Hub Upper Pool Perimeter", 39),
    "Hub: Upper Pool Dead End Path Artifact":           CarQuestLocationData("Artifact", "Hub Upper Pool Perimeter", 40),
    "Hub: Long Lookout Alley Artifact":                 CarQuestLocationData("Artifact", "Hub Lookout Long Path", 41),
    "Hub: Central Path Dead End Artifact":              CarQuestLocationData("Artifact", "Hub Central Bridge", 42),
    "Hub: Start Lookout Artifact":                      CarQuestLocationData("Artifact", "Hub Start Lookout", 43),
    "Hub: University Podium Artifact":                  CarQuestLocationData("Artifact", "Hub University Interior", 44),
    "Hub: University Back Right Artifact":              CarQuestLocationData("Artifact", "Hub University Interior", 45),
    "Hub: University Second Row Artifact":              CarQuestLocationData("Artifact", "Hub University Interior", 46),
    "Hub: University Third Row Artifact":               CarQuestLocationData("Artifact", "Hub University Interior", 47),
    "Hub: University Fourth Row Artifact":              CarQuestLocationData("Artifact", "Hub University Interior", 48),
    "Hub: University First Row Artifact":               CarQuestLocationData("Artifact", "Hub University Interior", 49),
    "Hub: University Back Left Artifact":               CarQuestLocationData("Artifact", "Hub University Interior", 50),
    "Hub: Behind University Portal Artifact":           CarQuestLocationData("Artifact", "Hub University Second Floor", 51),
    "Hub: Power Room Entry Artifact":                   CarQuestLocationData("Artifact", "Hub Power Room", 52),

    "Hub: Throne Exterior Museum Piece":                CarQuestLocationData("Museum", "Hub Throne Room West Exterior", 55),
    "Hub: Ice Portal Drop Ledge Museum Piece":          CarQuestLocationData("Museum", "Hub Ice Portal", 56),
    "Hub: Hopscotch Museum Piece":                      CarQuestLocationData("Museum", "Hub Pool Area", 57),
    "Hub: South Pool Jump Museum Piece":                CarQuestLocationData("Museum", "Hub Pool Jump", 58),
    "Hub: Colloseum Museum Piece":                      CarQuestLocationData("Museum", "Hub Colloseum Top", 59),
    "Hub: Teleport Islands Museum Piece":               CarQuestLocationData("Museum", "Hub Teleport Island", 60),

    # Simple
    # 2 Secrets
    # 30 Power Cells
    # 4 Mega Power Cells
    # 1 Token
    # 37 Total
    "Simple: Artifact Under Mound":                     CarQuestLocationData("Artifact", "Simple Square Area", simpleOffset + 1),
    "Simple: Artifact On Exit Ramp":                    CarQuestLocationData("Artifact", "Simple Square Area", simpleOffset + 2),

    "Simple: Exterior Token":                           CarQuestLocationData("Token", "Simple Square Exterior", simpleOffset + 3),

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
    # 7 Secrets
    "Maze: First Artifact":                             CarQuestLocationData("Artifact", "Maze Start", mazeOffset + 1),
    "Maze: On Wall Near Start Artifact":                CarQuestLocationData("Artifact", "Maze Exterior Walls", mazeOffset + 2),
    "Maze: Cave Artifact":                              CarQuestLocationData("Artifact", "Maze Cave", mazeOffset + 3),
    "Maze: Top of Mini Maze Artifact":                  CarQuestLocationData("Artifact", "Maze Interior Walls Upper", mazeOffset + 4),
    "Maze: Hidden Drop Off Artifact":                   CarQuestLocationData("Artifact", "Maze Interior Walls Upper", mazeOffset + 5),
    "Maze: On Wall Near Exit Artifact":                 CarQuestLocationData("Artifact", "Maze Interior Walls Bridge", mazeOffset + 6),
    "Maze: Exit Reward Artifact":                       CarQuestLocationData("Artifact", "Maze Interior Walls", mazeOffset + 7),

    # Glass Cube
    # 3 Secrets
    # 40 Power Cells
    # 10 Mega Power Cells
    # 2 Tokens
    # 55 Total
    "Glass Cube: Top Artifact":                       CarQuestLocationData("Artifact", "Glass Box", glassOffset + 1),
    "Glass Cube: Bottom Artifact":                    CarQuestLocationData("Artifact", "Glass Box", glassOffset + 2),
    "Glass Cube: Exit Reward":                        CarQuestLocationData("Artifact", "Glass Box Exit", glassOffset + 3),

    # Sands of Fallen Kings
    # 11 Secrets
    # 100 Power Cells
    # 6 Mega Power Cells
    # 2 Tokens
    # 119 Total
    "Sands: Artifact Under South East Roof":          CarQuestLocationData("Artifact", "Sands Main", sandOffset + 1),
    "Sands: South West Tower Artifact":               CarQuestLocationData("Artifact", "Sands Main", sandOffset + 2),
    "Sands: Exterior Wall Artifact":                  CarQuestLocationData("Artifact", "Sands North Exterior Walls", sandOffset + 3),
    "Sands: Exterior Wall Tower Artifact":            CarQuestLocationData("Artifact", "Sands South Exterior Walls", sandOffset + 4),
    "Sands: Artifact Inside South East Tower":        CarQuestLocationData("Artifact", "Sands Main", sandOffset + 5),
    "Sands: Artifact Under Fallen Tower Roof":        CarQuestLocationData("Artifact", "Sands Main", sandOffset + 6),
    "Sands: North East Tower Artifact":               CarQuestLocationData("Artifact", "Sands Main", sandOffset + 7),
    "Sands: Artifact Under South West Roof":          CarQuestLocationData("Artifact", "Sands Main", sandOffset + 8),
    "Sands: North East Door Artifact":                CarQuestLocationData("Artifact", "Sands Main", sandOffset + 9),
    "Sands: King Head Artifact":                      CarQuestLocationData("Artifact", "Sands Main", sandOffset + 10),
    "Sands: Exit Reward Artifact":                    CarQuestLocationData("Artifact", "Sands Main", sandOffset + 11),

    # Ocean
    # 11 Secrets
    # 1 Museum
    # 103 Power Cells
    # 2 Tokens
    # 117 Total
    "Ocean: Shipwreck Artifact":                      CarQuestLocationData("Artifact", "Ocean Main", oceanOffset + 1),
    "Ocean: Top of Vulcano Artifact":                 CarQuestLocationData("Artifact", "Ocean Main", oceanOffset + 2),
    "Ocean: Outer Fort Bottom Artifact":              CarQuestLocationData("Artifact", "Ocean Main", oceanOffset + 3),
    "Ocean: Outer Fort Middle Artifact":              CarQuestLocationData("Artifact", "Ocean Main", oceanOffset + 4),
    "Ocean: Hill Near Portal Artifact":               CarQuestLocationData("Artifact", "Ocean Main", oceanOffset + 5),
    "Ocean: Inside Fort Artifact":                    CarQuestLocationData("Artifact", "Ocean Inside Fort", oceanOffset + 6),
    "Ocean: Artifact Near Bell":                      CarQuestLocationData("Artifact", "Ocean Main", oceanOffset + 7),
    "Ocean: Fish Circle Jump Artifact":               CarQuestLocationData("Artifact", "Ocean Main", oceanOffset + 8),
    "Ocean: Inside Pirate Ship Artifact":             CarQuestLocationData("Artifact", "Ocean Main", oceanOffset + 9),
    "Ocean: Inside Vulcano Artifact":                 CarQuestLocationData("Artifact", "Ocean Main", oceanOffset + 10),
    "Ocean: Whale Artifact":                          CarQuestLocationData("Artifact", "Ocean Main", oceanOffset + 11),
    "Ocean: Vulcano Museum Piece":                    CarQuestLocationData("Artifact", "Ocean Main", oceanOffset + 12),

    # Ice Temple
    # 12 Secrets
    # 159 Power Cells
    # 12 Mega Power Cells
    # 2 Tokens
    # 185 Total
    "Ice: South Jump Artifact":                      CarQuestLocationData("Artifact", "Ice Temple Main", iceOffset + 1),
    "Ice: North East Perimeter Artifact":            CarQuestLocationData("Artifact", "Ice Temple Main", iceOffset + 2),
    "Ice: Outside West Jump Artifact":               CarQuestLocationData("Artifact", "Ice Temple Main", iceOffset + 3),
    "Ice: North East Jump Artifact":                 CarQuestLocationData("Artifact", "Ice Temple Main", iceOffset + 4),
    "Ice: Lowest East Jump Artifact":                CarQuestLocationData("Artifact", "Ice Temple Lower East Ledge", iceOffset + 5),
    "Ice: South East Tower Artifact":                CarQuestLocationData("Artifact", "Ice SE Tower", iceOffset + 6),
    "Ice: East Top Jump Artifact":                   CarQuestLocationData("Artifact", "Ice Temple South Ledge End", iceOffset + 7),
    "Ice: South West Tower Artifact":                CarQuestLocationData("Artifact", "Ice SW Tower", iceOffset + 8),
    "Ice: North East Tower Artifact":                CarQuestLocationData("Artifact", "Ice Northern Towers", iceOffset + 9),
    "Ice: South East Tower Jump Artifact":           CarQuestLocationData("Artifact", "Ice Tower Jump", iceOffset + 10),
    "Ice: North East Bridge Ramp Artifact":          CarQuestLocationData("Artifact", "Ice Bridge Ramp To Monument", iceOffset + 11),
    "Ice: North East Tower Interior Artifact":       CarQuestLocationData("Artifact", "Ice NE Tower Interior", iceOffset + 12),
    "Ice: North East Tower Interior Museum Piece":   CarQuestLocationData("Museum", "Ice NE Tower Interior", iceOffset + 13),

    # Sheep Pastures
    # 6 Secrets
    # 103 Power Cells
    # 2 Tokens
    # 111 Total
    "Sheep: West Hidden Behind Tree Artifact":       CarQuestLocationData("Artifact", "Sheep Patures Main", sheepOffset + 1),
    "Sheep: In Sheep Shed Artifact":                 CarQuestLocationData("Artifact", "Sheep Patures In Shed", sheepOffset + 2),
    "Sheep: Sheep Herder Artifact":                  CarQuestLocationData("Artifact", "Sheep Patures Main", sheepOffset + 3),
    "Sheep: Inside Windmill Artifact":               CarQuestLocationData("Artifact", "Sheep Patures Main", sheepOffset + 4),
    "Sheep: Raised Shed Artifact":                   CarQuestLocationData("Artifact", "Sheep Patures Shed Raised", sheepOffset + 5),
    "Sheep: Inside Raised Shed Artifact":            CarQuestLocationData("Artifact", "Sheep Patures Shed Raised", sheepOffset + 6),

    # Brick Bristle's Island
    # 35 Artifacts
    # 199 Energy Cells
    # 5 Mega Energy Cells
    # 2 Tokens
    # 241 Total
    "Island: Spiral Island Artifact":                CarQuestLocationData("Artifact", "Island Day", islandOffset + 1),
    "Island: East Small Rock In Ocean Artifact":     CarQuestLocationData("Artifact", "Island Day", islandOffset + 2),
    "Island: Artifact Hidden Under East Path":       CarQuestLocationData("Artifact", "Island Day", islandOffset + 3),
    "Island: East Path First Artifact":              CarQuestLocationData("Artifact", "Island Day", islandOffset + 4),
    "Island: Raft Behind Start Artifact":            CarQuestLocationData("Artifact", "Island Day South Path", islandOffset + 5),
    "Island: South East Triange Island Artifact":    CarQuestLocationData("Artifact", "Island Day", islandOffset + 6),
    "Island: East Path Second Artifact":             CarQuestLocationData("Artifact", "Island Day", islandOffset + 7),
    "Island: East Path North Raft Artifact":         CarQuestLocationData("Artifact", "Island Day", islandOffset + 8),
    "Island: East Path South Raft Artifact":         CarQuestLocationData("Artifact", "Island Day", islandOffset + 9),
    "Island: East Path End Artifact":                CarQuestLocationData("Artifact", "Island East Path End", islandOffset + 10),
    "Island: Shark Island Artifact":                 CarQuestLocationData("Artifact", "Island Day", islandOffset + 11),
    "Island: West Island Ramp Artifact":             CarQuestLocationData("Artifact", "Island Day", islandOffset + 12),
    "Island: East Island Ledge Artifact":            CarQuestLocationData("Artifact", "Island Night", islandOffset + 13),
    "Island: South Path Jump Artifact":              CarQuestLocationData("Artifact", "Island Night", islandOffset + 14),
    "Island: South East Cave Artifact":              CarQuestLocationData("Artifact", "Island Day", islandOffset + 15),
    "Island: South Path Cave Artifact":              CarQuestLocationData("Artifact", "Island Day", islandOffset + 16),
    "Island: Clam Artifact":                         CarQuestLocationData("Artifact", "Island Day", islandOffset + 17),
    "Island: West Jump Artifact":                    CarQuestLocationData("Artifact", "Island Day", islandOffset + 18),
    "Island: North Wall Lower Artifact":             CarQuestLocationData("Artifact", "Island North Lower Ledge", islandOffset + 19),
    "Island: East Path Raft Cave Artifact":          CarQuestLocationData("Artifact", "Island Day", islandOffset + 20),
    "Island: North Wall Upper Artifact":             CarQuestLocationData("Artifact", "Island North Upper Ledge", islandOffset + 21),
    "Island: Back Serpant Hump Artifact":            CarQuestLocationData("Artifact", "Island Day", islandOffset + 22),
    "Island: Second South Path Cave Artifact":       CarQuestLocationData("Artifact", "Island Day", islandOffset + 23),
    "Island: Serpant Head Artifact":                 CarQuestLocationData("Artifact", "Island Day", islandOffset + 24),
    "Island: Hut Ledge Artifact":                    CarQuestLocationData("Artifact", "Island Hut Ledge", islandOffset + 25),
    "Island: Night South Path Artifact":             CarQuestLocationData("Artifact", "Island Night South Path", islandOffset + 26),
    "Island: Front Serpant Hump Artifact":           CarQuestLocationData("Artifact", "Island Night", islandOffset + 27),
    "Island: Balcony Hut Artifact":                  CarQuestLocationData("Artifact", "Island Hut Inside", islandOffset + 28),
    "Island: East Ocean Jump Artifact":              CarQuestLocationData("Artifact", "Island Night", islandOffset + 29),
    "Island: Treetop Near Flower Artifact":          CarQuestLocationData("Artifact", "Island Treetop", islandOffset + 30),
    "Island: Treetop Above Pond Ramp Artifact":      CarQuestLocationData("Artifact", "Island Treetop Pond", islandOffset + 31),
    "Island: Drained Pond Artifact":                 CarQuestLocationData("Artifact", "Island Day", islandOffset + 32),
    "Island: Treetop Inside Flower Artifact":        CarQuestLocationData("Artifact", "Island Treetop", islandOffset + 33),
    "Island: Inside Hut Artifact":                   CarQuestLocationData("Artifact", "Island Hut Inside", islandOffset + 34),
    "Island: Exit Reward Artifact":                  CarQuestLocationData("Artifact", "Island Night", islandOffset + 35),

    # Throne Room
    # 19 Secrets
    # 169 Power Cells
    # 7 Mega Power Cells
    # 1 Token
    # 1 Museum
    # 195 Total
    "Throne: Behind Throne Artifact":                CarQuestLocationData("Artifact", "Throne Interior", throneOffset + 1),
    "Throne: South West Trick Jump Artifact":        CarQuestLocationData("Artifact", "Throne Interior", throneOffset + 2),
    "Throne: South East Trick Jump Artifact":        CarQuestLocationData("Artifact", "Throne Interior", throneOffset + 3),
    "Throne: North East Window Artifact":            CarQuestLocationData("Artifact", "Throne Interior N Window", throneOffset + 4),
    "Throne: South West Window Artifact":            CarQuestLocationData("Artifact", "Throne Interior S Window", throneOffset + 5),
    "Throne: South East Window Artifact":            CarQuestLocationData("Artifact", "Throne Interior S Window", throneOffset + 5),
    "Throne: Lower Garden Artifact":                 CarQuestLocationData("Artifact", "Throne Garden", throneOffset + 6),
    "Throne: Hidden East Garden Artifact":           CarQuestLocationData("Artifact", "Throne Garden", throneOffset + 7),
    "Throne: Middle West Window Artifact":           CarQuestLocationData("Artifact", "Throne Interior", throneOffset + 8),
    "Throne: Hidden West Garden Artifact":           CarQuestLocationData("Artifact", "Throne Garden", throneOffset + 9),
    "Throne: Middle East Window Artifact":           CarQuestLocationData("Artifact", "Throne Interior", throneOffset + 10),
    "Throne: South West Window Artifact":            CarQuestLocationData("Artifact", "Throne Interior", throneOffset + 11),
    "Throne: South East Window Artifact":            CarQuestLocationData("Artifact", "Throne Interior", throneOffset + 12),
    "Throne: East Exterior Wall Artifact":           CarQuestLocationData("Artifact", "Throne East Exterior Wall", throneOffset + 13),
    "Throne: Exterior Corner Wall Artifact":         CarQuestLocationData("Artifact", "Throne West Exterior Wall", throneOffset + 14),
    "Throne: Upper Garden Artifact":                 CarQuestLocationData("Artifact", "Throne Garden", throneOffset + 15),
    "Throne: Hidden Throne Door Artifact":           CarQuestLocationData("Artifact", "Throne Interior N Window", throneOffset + 16),
    "Throne: Throne Ramp Artifact":                  CarQuestLocationData("Artifact", "Throne Interior", throneOffset + 17),
    "Throne: Exit Reward Artifact":                  CarQuestLocationData("Artifact", "Throne Garden", throneOffset + 18),
    "Throne: Brick Bristles' Museum Piece":          CarQuestLocationData("Artifact", "Throne Garden", throneOffset + 19),

    # Planetarium
    # 2 Artifacts
    # 1 Museum
    # 9 Power Cells
    # 1 Token
    # 13 Total
    "Planetarium: Top of Portal Artifact":           CarQuestLocationData("Artifact", "Planetarium", planetOffset + 1),
    "Planetarium: Top Path Artifact":                CarQuestLocationData("Artifact", "Planetarium", planetOffset + 2),
    "Planetarium: X Puzzle Museum Piece":            CarQuestLocationData("Artifact", "Planetarium", planetOffset + 3),

    # Power Room
    # 10 Artifacts
    # 201 Power Cells
    # 2 Tokens
    # 213 Total
    "Power Room: East Bottom Artifact":              CarQuestLocationData("Artifact", "Power Room", powerOffset + 1),
    "Power Room: Green Center Artifact":             CarQuestLocationData("Artifact", "Power Room", powerOffset + 2),
    "Power Room: Green Cable Artifact":              CarQuestLocationData("Artifact", "Power Room", powerOffset + 3),
    "Power Room: Blue Center Artifact":              CarQuestLocationData("Artifact", "Power Room", powerOffset + 4),
    "Power Room: Blue Cable Artifact":               CarQuestLocationData("Artifact", "Power Room", powerOffset + 5),
    "Power Room: Red Center Artifact":               CarQuestLocationData("Artifact", "Power Room", powerOffset + 6),
    "Power Room: Red Cable Artifact":                CarQuestLocationData("Artifact", "Power Room", powerOffset + 7),
    "Power Room: Yellow Center Artifact":            CarQuestLocationData("Artifact", "Power Room", powerOffset + 8),
    "Power Room: Book Artifact":                     CarQuestLocationData("Artifact", "Power Room", powerOffset + 9),
    "Power Room: Top Artifact Near Token":           CarQuestLocationData("Artifact", "Power Room", powerOffset + 10),

    # Limbo
    # 1 Artifact
    # 172 Power Cells
    # 2 Token
    # 175 Total
    "Limbo: Crown Artifact":                         CarQuestLocationData("Artifact", "Limbo", powerOffset + 11),
}