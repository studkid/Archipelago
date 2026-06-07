from typing import NamedTuple, Dict
from BaseClasses import Item, ItemClassification, Optional

class CarQuestItem(Item):
    game: str = "Secret Game"

class CarQuestItemData(NamedTuple):
    category: str
    code: Optional[int] = None
    classification: ItemClassification = ItemClassification.filler
    max_quantity: int = 1

def get_items_by_category(category: str) -> Dict[str, CarQuestItemData]:
    item_dict: Dict[str, CarQuestItemData] = {}
    for name, data in item_table.items():
        if data.category == category:
            item_dict.setdefault(name, data)

    return item_dict

simpleOffset = 100
cubesOffset = simpleOffset + 10
desertOffset = cubesOffset + 10
sliderOffset = desertOffset + 10
mazeOffset = sliderOffset + 10
glassOffset = mazeOffset + 10
sandsOffset = glassOffset + 10
oceanOffset = sandsOffset + 10
iceOffset = oceanOffset + 10
sheepOffset = iceOffset + 15
islandOffset = sheepOffset + 5
throneOffset = islandOffset + 40
planetOffset = throneOffset + 20
powerOffset = planetOffset + 10

item_table: Dict[str, CarQuestItemData] = {
    # Hub
    "Hub: Start Room Blocker":                      CarQuestItemData("secret", 1, ItemClassification.progression),
    "Hub: Simple Portal Bridge Wall":               CarQuestItemData("secret", 2, ItemClassification.progression),
    "Hub: North Pool Small Secret Door":            CarQuestItemData("secret", 3, ItemClassification.progression),
    "Hub: North Pool Jump Ramp":                    CarQuestItemData("secret", 4, ItemClassification.progression),
    "Hub: South Pool Artifact Block":               CarQuestItemData("secret", 5, ItemClassification.progression),
    "Hub: Upper University Alleyway Access":        CarQuestItemData("secret", 6, ItemClassification.progression),
    "Hub: South Pool Dead End Door":                CarQuestItemData("secret", 7, ItemClassification.progression),
    "Hub: Tree Slalom Unlock":                      CarQuestItemData("secret", 8, ItemClassification.progression),
    "Hub: Museum Unlock":                           CarQuestItemData("secret", 9, ItemClassification.progression),
    "Hub: North Pool Portal Access":                CarQuestItemData("secret", 10, ItemClassification.progression),
    "Hub: Cube Monument Access":                    CarQuestItemData("secret", 11, ItemClassification.progression),
    "Hub: South Portal Ramp Door":                  CarQuestItemData("secret", 12, ItemClassification.progression),
    "Hub: North Pool Vault Door":                   CarQuestItemData("secret", 13, ItemClassification.progression),
    "Hub: South Portal Secondary Ramp":             CarQuestItemData("secret", 14, ItemClassification.progression),
    "Hub: South Portal Bridge":                     CarQuestItemData("secret", 15, ItemClassification.progression),
    "Hub: Pool Drain Door":                         CarQuestItemData("secret", 16, ItemClassification.progression),
    "Hub: Progressive Pool":                        CarQuestItemData("secret", 17, ItemClassification.progression, 2),
    "Hub: Start Room Right Door":                   CarQuestItemData("secret", 18, ItemClassification.progression),
    "Hub: Pool Push Block":                         CarQuestItemData("secret", 19, ItemClassification.progression),
    "Hub: Pool South East Blocker":                 CarQuestItemData("secret", 20, ItemClassification.progression),
    "Hub: Pool North West Blocker":                 CarQuestItemData("secret", 21, ItemClassification.progression),
    "Hub: Pool Vault Portal Unlock":                CarQuestItemData("secret", 22, ItemClassification.progression),
    "Hub: Throne Exterior Wall":                    CarQuestItemData("secret", 23, ItemClassification.progression),
    "Hub: Start Room Bridge":                       CarQuestItemData("secret", 24, ItemClassification.progression),
    "Hub: Central Bridge East Ramp":                CarQuestItemData("secret", 25, ItemClassification.progression),
    "Hub: Exterior University Ramp":                CarQuestItemData("secret", 26, ItemClassification.progression),
    "Hub: Central Bridge West Ramp":                CarQuestItemData("secret", 27, ItemClassification.progression),
    "Hub: Pool North East Blocker":                 CarQuestItemData("secret", 28, ItemClassification.progression),
    "Hub: Central Bridge Portal Bridge":            CarQuestItemData("secret", 29, ItemClassification.progression),
    "Hub: Exterior University Wall Door":           CarQuestItemData("secret", 30, ItemClassification.progression),
    "Hub: Ramp Near Simple Portal":                 CarQuestItemData("secret", 31, ItemClassification.progression),
    "Hub: Secondary University Wall Door":          CarQuestItemData("secret", 32, ItemClassification.progression),
    "Hub: Blocker Near Whale Bridge":               CarQuestItemData("secret", 33, ItemClassification.progression),
    "Hub: Whale Bridge":                            CarQuestItemData("secret", 34, ItemClassification.progression),
    "Hub: Colloseum Bridge":                        CarQuestItemData("secret", 35, ItemClassification.progression),
    "Hub: Colloseum Podium Extension":              CarQuestItemData("secret", 36, ItemClassification.progression),
    "Hub: Start Area Back Removal":                 CarQuestItemData("secret", 37, ItemClassification.progression),
    "Hub: Colloseum Exterior Wall Doors":           CarQuestItemData("secret", 38, ItemClassification.progression),
    "Hub: Colloseum Push Block Unlock":             CarQuestItemData("secret", 39, ItemClassification.progression),
    "Hub: Colloseum Podium Door":                   CarQuestItemData("secret", 40, ItemClassification.progression),
    "Hub: Colloseum Podium Ramp":                   CarQuestItemData("secret", 41, ItemClassification.progression),
    "Hub: Ramp to Light Puzzle":                    CarQuestItemData("secret", 42, ItemClassification.progression),
    "Hub: Top Path Floating Islands":               CarQuestItemData("secret", 43, ItemClassification.progression),
    "Hub: Start Lookout Dead End Door":             CarQuestItemData("secret", 44, ItemClassification.progression),
    "Hub: Bottom Path Floating Islands":            CarQuestItemData("secret", 45, ItemClassification.progression),
    "Hub: Lookout Long Path Door":                  CarQuestItemData("secret", 46, ItemClassification.progression),
    "Hub: Whales and Central Dead End Door":        CarQuestItemData("secret", 47, ItemClassification.progression),
    "Hub: Start Lookout Door":                      CarQuestItemData("secret", 48, ItemClassification.progression),
    "Hub: University Doors":                        CarQuestItemData("secret", 49, ItemClassification.progression),
    "Hub: University Back Row Ramp":                CarQuestItemData("secret", 50, ItemClassification.progression),
    "Hub: University Lower Second Row Ramp":        CarQuestItemData("secret", 51, ItemClassification.progression),
    "Hub: University Lower Third Row Ramp":         CarQuestItemData("secret", 52, ItemClassification.progression),
    "Hub: University Lower Fourth Row Ramp":        CarQuestItemData("secret", 53, ItemClassification.progression),
    "Hub: University Lower Push Ramp":              CarQuestItemData("secret", 54, ItemClassification.progression),
    "Hub: University Lower Back Artifact Platform": CarQuestItemData("secret", 55, ItemClassification.progression),
    "Hub: University Second Floor Ramp":            CarQuestItemData("secret", 56, ItemClassification.progression),
    "Hub: Upper Bridge Jump Walls":                 CarQuestItemData("secret", 57, ItemClassification.progression),
    "Hub: Tree Area Door":                          CarQuestItemData("secret", 58, ItemClassification.progression),
    "Hub: University Portal Buttons":               CarQuestItemData("secret", 59, ItemClassification.progression),
    "Hub: Throne Room Door":                        CarQuestItemData("secret", 60, ItemClassification.progression),
    "Hub: Power Room South Door":                   CarQuestItemData("secret", 61, ItemClassification.progression),
    "Hub: University Portal Planetarium Access":    CarQuestItemData("secret", 62, ItemClassification.progression),
    "Hub: Power Room North Door":                   CarQuestItemData("secret", 63, ItemClassification.progression),

    "Hub: Sun Museum Glass":                        CarQuestItemData("museum", 90, ItemClassification.progression),
    "Hub: Block Museum Glass":                      CarQuestItemData("museum", 91, ItemClassification.progression),
    "Hub: Book Museum Glass":                       CarQuestItemData("museum", 92, ItemClassification.progression),
    "Hub: Energy Cell Museum Glass":                CarQuestItemData("museum", 93, ItemClassification.progression),
    "Hub: Tire Museum Glass":                       CarQuestItemData("museum", 94, ItemClassification.progression),
    "Hub: Blockstar Museum Glass":                  CarQuestItemData("museum", 95, ItemClassification.progression),
    "Hub: Tree Museum Glass":                       CarQuestItemData("museum", 96, ItemClassification.progression),
    "Hub: Cube Museum Glass":                       CarQuestItemData("museum", 97, ItemClassification.progression),
    "Hub: Portal Museum Glass":                     CarQuestItemData("museum", 98, ItemClassification.progression),
    "Hub: Brick Bristles Museum Glass":             CarQuestItemData("museum", 99, ItemClassification.progression),

    # Simple
    "Simple: Exit Bridge":                          CarQuestItemData("secret",  simpleOffset + 1, ItemClassification.progression),

    # Cubes
    "Cubes: Exit Bridge":                           CarQuestItemData("secret", cubesOffset + 1, ItemClassification.progression),

    # Desert
    "Desert: South West Mound":                     CarQuestItemData("secret", desertOffset + 1, ItemClassification.progression),
    "Desert: Shop Cave Door":                       CarQuestItemData("secret", desertOffset + 2, ItemClassification.progression),
    "Desert: North West Mound":                     CarQuestItemData("secret", desertOffset + 3, ItemClassification.progression),
    "Desert: South East Mound":                     CarQuestItemData("secret", desertOffset + 4, ItemClassification.progression),
    "Desert: Fixit Shop Door":                      CarQuestItemData("secret", desertOffset + 5, ItemClassification.progression),
    "Desert: Fixit Shop Fence":                     CarQuestItemData("secret", desertOffset + 6, ItemClassification.progression),
    "Desert: Exit Ramp":                            CarQuestItemData("secret", desertOffset + 7, ItemClassification.progression),

    # Slider
    "Slider: Start Ramp":                           CarQuestItemData("secret", sliderOffset + 1, ItemClassification.progression),
    "Slider: Left Push Block Unlock":               CarQuestItemData("secret", sliderOffset + 2, ItemClassification.progression),
    "Slider: Right Push Block Unlock":              CarQuestItemData("secret", sliderOffset + 3, ItemClassification.progression),
    "Slider: Left Side Ramp":                       CarQuestItemData("secret", sliderOffset + 4, ItemClassification.progression),
    "Slider: Exit Ramp Unlock":                     CarQuestItemData("secret", sliderOffset + 5, ItemClassification.progression),

    # Maze
    "Maze: Door to Big Ramp":                       CarQuestItemData("secret", mazeOffset + 1, ItemClassification.progression),
    "Maze: Hedge Ramp":                             CarQuestItemData("secret", mazeOffset + 2, ItemClassification.progression),
    "Maze: Raise Cave Wall":                        CarQuestItemData("secret", mazeOffset + 3, ItemClassification.progression),
    "Maze: Lower Artifact Wall":                    CarQuestItemData("secret", mazeOffset + 4, ItemClassification.progression),
    "Maze: Interior Wall Bridge":                   CarQuestItemData("secret", mazeOffset + 5, ItemClassification.progression),
    "Maze: Exit Door":                              CarQuestItemData("secret", mazeOffset + 6, ItemClassification.progression),

    # Glass Box
    "Glass Box: Useless Block":                     CarQuestItemData("secret", glassOffset + 1, ItemClassification.progression),
    "Glass Box: Exit Bridge":                       CarQuestItemData("secret", glassOffset + 2, ItemClassification.progression),

    # Sands of Fallen Kings
    "Sands: Exterior Walls Access":                 CarQuestItemData("secret", sandsOffset + 1, ItemClassification.progression),
    "Sands: Lower South West Tower":                CarQuestItemData("secret", sandsOffset + 2, ItemClassification.progression),
    "Sands: Lower Exterior Wall Tower":             CarQuestItemData("secret", sandsOffset + 3, ItemClassification.progression),
    "Sands: South East Tower Access":               CarQuestItemData("secret", sandsOffset + 4, ItemClassification.progression),
    "Sands: Move Fallen Tower Roof":                CarQuestItemData("secret", sandsOffset + 5, ItemClassification.progression),
    "Sands: Raise Exit Platform":                   CarQuestItemData("secret", sandsOffset + 6, ItemClassification.progression),
    "Sands: North East Door":                       CarQuestItemData("secret", sandsOffset + 7, ItemClassification.progression),
    "Sands: Reveal King Artifact":                  CarQuestItemData("secret", sandsOffset + 8, ItemClassification.progression),
    "Sands: Exit Reward Reveal":                    CarQuestItemData("secret", sandsOffset + 9, ItemClassification.progression),
    "Sands: Lower North West Tower":                CarQuestItemData("secret", sandsOffset + 10, ItemClassification.progression),

    # Ocean
    "Ocean: Vulcano Slope":                         CarQuestItemData("secret", oceanOffset + 1, ItemClassification.progression),
    "Ocean: Fort Bottom Ramp":                      CarQuestItemData("secret", oceanOffset + 2, ItemClassification.progression),
    "Ocean: Fort Middle Ramp":                      CarQuestItemData("secret", oceanOffset + 3, ItemClassification.progression),
    "Ocean: Raise Hill Near Exit":                  CarQuestItemData("secret", oceanOffset + 4, ItemClassification.progression),
    "Ocean: Fort Top Ramp":                         CarQuestItemData("secret", oceanOffset + 5, ItemClassification.progression),
    "Ocean: Raise Fish Ring Rock":                  CarQuestItemData("secret", oceanOffset + 6, ItemClassification.progression),
    "Ocean: Raise Fish Ring Ramp":                  CarQuestItemData("secret", oceanOffset + 7, ItemClassification.progression),
    "Ocean: Pirate Ship Repair":                    CarQuestItemData("secret", oceanOffset + 8, ItemClassification.progression),
    "Ocean: Shoot Cannon":                          CarQuestItemData("secret", oceanOffset + 9, ItemClassification.progression),
    "Ocean: Ring Bell":                             CarQuestItemData("secret", oceanOffset + 10, ItemClassification.progression),

    # Ice Temple
    "Ice: West Artifact Blocker":                   CarQuestItemData("secret", iceOffset + 1, ItemClassification.progression),
    "Ice: South Ramp Blocker":                      CarQuestItemData("secret", iceOffset + 2, ItemClassification.progression),
    "Ice: Secondary Wall Ramp":                     CarQuestItemData("secret", iceOffset + 3, ItemClassification.progression),
    "Ice: Ice Pillar Blocker":                      CarQuestItemData("secret", iceOffset + 4, ItemClassification.progression),
    "Ice: Perimeter Wall Blocker":                  CarQuestItemData("secret", iceOffset + 5, ItemClassification.progression),
    "Ice: South Jump Path Wall":                    CarQuestItemData("secret", iceOffset + 6, ItemClassification.progression),
    "Ice: South Wall Bridge":                       CarQuestItemData("secret", iceOffset + 7, ItemClassification.progression),
    "Ice: Other Wall Bridges":                      CarQuestItemData("secret", iceOffset + 8, ItemClassification.progression),
    "Ice: Wall Jump Ramp":                          CarQuestItemData("secret", iceOffset + 9, ItemClassification.progression),
    "Ice: Wall Bridge Ramp to Monument":            CarQuestItemData("secret", iceOffset + 10, ItemClassification.progression),
    "Ice: Raise North East Tower":                  CarQuestItemData("secret", iceOffset + 11, ItemClassification.progression),

    # Sheep Pastrues
    "Sheep: Shed Ramp":                             CarQuestItemData("secret", sheepOffset + 1, ItemClassification.progression),
    "Sheep: Sheep Shed Door":                       CarQuestItemData("secret", sheepOffset + 2, ItemClassification.progression),
    "Sheep: Windmill Activation":                   CarQuestItemData("secret", sheepOffset + 3, ItemClassification.progression),
    "Sheep: Raise Shed":                            CarQuestItemData("secret", sheepOffset + 4, ItemClassification.progression),
    "Sheep: Raised Shed Hidden Wall":               CarQuestItemData("secret", sheepOffset + 5, ItemClassification.progression),

    # Brick Bristle's Island
    "Island: East Long Path Start Wall":            CarQuestItemData("secret", islandOffset + 1, ItemClassification.progression),
    "Island: Artifact Blocker Under East Path":     CarQuestItemData("secret", islandOffset + 2, ItemClassification.progression),
    "Island: First East Path Bridge":               CarQuestItemData("secret", islandOffset + 3, ItemClassification.progression),
    "Island: Lower Jump Blocker Behind Start":      CarQuestItemData("secret", islandOffset + 4, ItemClassification.progression),
    "Island: Lower South East Triangle Island":     CarQuestItemData("secret", islandOffset + 5, ItemClassification.progression),
    "Island: Second East Path Bridge":              CarQuestItemData("secret", islandOffset + 6, ItemClassification.progression),
    "Island: East Path Ocean Ramp":                 CarQuestItemData("secret", islandOffset + 7, ItemClassification.progression),
    "Island: Third East Path Bridge":               CarQuestItemData("secret", islandOffset + 8, ItemClassification.progression),
    "Island: Night Portal":                         CarQuestItemData("secret", islandOffset + 9, ItemClassification.progression),
    "Island: West Shark Island Ramp":               CarQuestItemData("secret", islandOffset + 10, ItemClassification.progression),
    "Island: West Island Artifact Ramp":            CarQuestItemData("secret", islandOffset + 11, ItemClassification.progression),
    "Island: East Ledge Artifact Ramp":             CarQuestItemData("secret", islandOffset + 12, ItemClassification.progression),
    "Island: South Path Artifact Jump Ramp":        CarQuestItemData("secret", islandOffset + 13, ItemClassification.progression),
    "Island: East Ledge Cave Entrance":             CarQuestItemData("secret", islandOffset + 14, ItemClassification.progression),
    "Island: South Path Cave Entrance":             CarQuestItemData("secret", islandOffset + 15, ItemClassification.progression),
    "Island: Open Clam":                            CarQuestItemData("secret", islandOffset + 16, ItemClassification.progression),
    "Island: Shark Pinnacle":                       CarQuestItemData("secret", islandOffset + 17, ItemClassification.progression),
    "Island: North Lower Wall Ramp":                CarQuestItemData("secret", islandOffset + 18, ItemClassification.progression),
    "Island: East Path Raft Cave Door":             CarQuestItemData("secret", islandOffset + 19, ItemClassification.progression),
    "Island: North Upper Wall Ramp":                CarQuestItemData("secret", islandOffset + 20, ItemClassification.progression),
    "Island: Lower Serpant Hump":                   CarQuestItemData("secret", islandOffset + 21, ItemClassification.progression),
    "Island: South Path Cave Wall Removal":         CarQuestItemData("secret", islandOffset + 22, ItemClassification.progression),
    "Island: Lower Serpant Head":                   CarQuestItemData("secret", islandOffset + 23, ItemClassification.progression),
    "Island: Lower Spiral Island":                  CarQuestItemData("secret", islandOffset + 24, ItemClassification.progression),
    "Island: Pond Treetop Ramp":                    CarQuestItemData("secret", islandOffset + 25, ItemClassification.progression),
    "Island: Serpant Head Jump Ramp":               CarQuestItemData("secret", islandOffset + 26, ItemClassification.progression),
    "Island: Hut Entrance Ramp":                    CarQuestItemData("secret", islandOffset + 27, ItemClassification.progression),
    "Island: East Ocean Jump Ramp":                 CarQuestItemData("secret", islandOffset + 28, ItemClassification.progression),
    "Island: Hut Treetop Ramp":                     CarQuestItemData("secret", islandOffset + 29, ItemClassification.progression),
    "Island: Treetop West Bridge":                  CarQuestItemData("secret", islandOffset + 30, ItemClassification.progression),
    "Island: Pond Drain":                           CarQuestItemData("secret", islandOffset + 31, ItemClassification.progression),
    "Island: Pond Treetop Ramp Blocker":            CarQuestItemData("secret", islandOffset + 32, ItemClassification.progression),
    "Island: Open Hut Door":                        CarQuestItemData("secret", islandOffset + 33, ItemClassification.progression),
    "Island: Exit Ramp":                            CarQuestItemData("secret", islandOffset + 34, ItemClassification.progression),

    # Throne Room
    "Throne: Interior South West Ramp":             CarQuestItemData("secret", throneOffset + 1, ItemClassification.progression),
    "Throne: Interior South East Ramp":             CarQuestItemData("secret", throneOffset + 2, ItemClassification.progression),
    "Throne: Open North Windows":                   CarQuestItemData("secret", throneOffset + 3, ItemClassification.progression),
    "Throne: Open South Windows":                   CarQuestItemData("secret", throneOffset + 4, ItemClassification.progression),
    "Throne: Open Main Door":                       CarQuestItemData("secret", throneOffset + 5, ItemClassification.progression),
    "Throne: Main Door Ramp":                       CarQuestItemData("secret", throneOffset + 6, ItemClassification.progression),
    "Throne: West Middle Window":                   CarQuestItemData("secret", throneOffset + 7, ItemClassification.progression),
    "Throne: West Push Ramp":                       CarQuestItemData("secret", throneOffset + 8, ItemClassification.progression),
    "Throne: East Middle Window":                   CarQuestItemData("secret", throneOffset + 9, ItemClassification.progression),
    "Throne: East Push Ramp":                       CarQuestItemData("secret", throneOffset + 10, ItemClassification.progression),
    "Throne: West South Window":                    CarQuestItemData("secret", throneOffset + 11, ItemClassification.progression),
    "Throne: East South Window":                    CarQuestItemData("secret", throneOffset + 12, ItemClassification.progression),
    "Throne: East Exterior Wall":                   CarQuestItemData("secret", throneOffset + 13, ItemClassification.progression),
    "Throne: West Exterior Wall":                   CarQuestItemData("secret", throneOffset + 14, ItemClassification.progression),
    "Throne: Lower High Garden Exit Ledge":         CarQuestItemData("secret", throneOffset + 15, ItemClassification.progression),
    "Throne: North Throne Hidden Door":             CarQuestItemData("secret", throneOffset + 16, ItemClassification.progression),
    "Throne: Throne Ramp":                          CarQuestItemData("secret", throneOffset + 17, ItemClassification.progression),
    "Throne: Exit Portal":                          CarQuestItemData("secret", throneOffset + 18, ItemClassification.filler),

    # Planetarium
    "Planetarium: Elevator Access":                 CarQuestItemData("secret", planetOffset + 1, ItemClassification.progression),

    # Power Room
    "Power Room: Green Cable Push":                 CarQuestItemData("secret", powerOffset + 1, ItemClassification.progression),
    "Power Room: Green Cable Activate":             CarQuestItemData("secret", powerOffset + 2, ItemClassification.progression),
    "Power Room: Blue Cable Push":                  CarQuestItemData("secret", powerOffset + 3, ItemClassification.progression),
    "Power Room: Blue Cable Activate":              CarQuestItemData("secret", powerOffset + 4, ItemClassification.progression),
    "Power Room: Red Cable Push":                   CarQuestItemData("secret", powerOffset + 5, ItemClassification.progression),
    "Power Room: Red Cable Activate":               CarQuestItemData("secret", powerOffset + 6, ItemClassification.progression),
    "Power Room: Yellow Cable Push":                CarQuestItemData("secret", powerOffset + 7, ItemClassification.progression),
    "Power Room: Yellow Cable Activate":            CarQuestItemData("secret", powerOffset + 8, ItemClassification.progression),
    "Hub: Power Restore":                           CarQuestItemData("secret", powerOffset + 9, ItemClassification.progression),
    "Power Room: Exit Teleporter":                  CarQuestItemData("secret", powerOffset + 10, ItemClassification.progression),

    # Limbo
    "Limbo: Crown and Exit Portal":                 CarQuestItemData("secret", powerOffset + 11, ItemClassification.progression),
 
    # Cars
    "x2 Battery Car":                               CarQuestItemData("car", 501, ItemClassification.useful),
    "Super Boost Car":                              CarQuestItemData("car", 502, ItemClassification.progression),
    "Froggy Car":                                   CarQuestItemData("car", 503, ItemClassification.progression),
    "Higher Torque Car":                            CarQuestItemData("car", 504, ItemClassification.useful),
    "Battery Rocket Car":                           CarQuestItemData("car", 505, ItemClassification.progression),
    "Nitro Car":                                    CarQuestItemData("car", 506, ItemClassification.progression),
    "Spider Car":                                   CarQuestItemData("car", 507, ItemClassification.progression),

    # Filler
    "Energy Cell":                                  CarQuestItemData("filler", 10001, ItemClassification.filler, 0),
    "Mega Energy Cell (25)":                        CarQuestItemData("filler", 10002, ItemClassification.filler, 0),
    "Mega Energy Cell (50)":                        CarQuestItemData("filler", 10003, ItemClassification.filler, 0),
}