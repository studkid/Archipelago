from worlds.AutoWorld import World
from rule_builder.rules import Has, HasAll, CanReachRegion, HasAny, HasAllCounts
from rule_builder.options import OptionFilter
from .Options import EndingGoal

def set_rules(world: World) -> bool:
    mw = world.multiworld
    player = world.player
    options = world.options

    ##################
    # Entrance Rules #
    ##################
    # Hub Entrances
    world.set_rule(mw.get_entrance("Hub Start -> Hub Simple Portal Path", player), HasAny("Hub: Start Room Blocker", "Froggy Car"))
    world.set_rule(mw.get_entrance("Hub Start -> Hub South Portal", player), HasAll("Hub: Start Room Blocker", "Hub: Start Area Back Removal", "Hub: Start Room Bridge"))

    world.set_rule(mw.get_entrance("Hub Simple Portal Path -> Hub Pool Area", player), Has("Hub: Simple Portal Bridge Wall"))
    world.set_rule(mw.get_entrance("Hub Simple Portal Path -> Hub Throne Room East Exterior", player), Has("Hub: Start Room Right Door"))
    world.set_rule(mw.get_entrance("Hub Simple Portal Path -> Hub Central Bridge", player), HasAny("Hub: Start Room Right Door", "Froggy Car"))
    world.set_rule(mw.get_entrance("Hub Simple Portal Path -> Hub Upper Pool Perimeter", player), Has("Hub: Ramp Near Simple Portal"))

    world.set_rule(mw.get_entrance("Hub Pool Area -> Hub Upper Uni Alleyway", player), Has("Hub: Upper University Alleyway Access"))
    world.set_rule(mw.get_entrance("Hub Pool Area -> Hub South Pool Dead End Path", player), Has("Hub: South Pool Dead End Door"))
    world.set_rule(mw.get_entrance("Hub Pool Area -> Floating Cube Area", player), Has("Hub: North Pool Portal Access"))
    world.set_rule(mw.get_entrance("Hub Pool Area -> Hub Cube Monument", player), Has("Hub: Cube Monument Access"))
    world.set_rule(mw.get_entrance("Hub Pool Area -> Hub South Portal", player), HasAll("Hub: South Portal Ramp Door", "Froggy Car"))
    world.set_rule(mw.get_entrance("Hub Pool Area -> Hub Vault", player), Has("Hub: North Pool Vault Door"))
    world.set_rule(mw.get_entrance("Hub Pool Area -> Hub Drained Pool", player), Has("Hub: Progressive Pool"))
    world.set_rule(mw.get_entrance("Hub Pool Area -> Hub University Exterior", player), Has("Hub: Exterior University Ramp"))
    world.set_rule(mw.get_entrance("Hub Pool Area -> Hub Museum", player), Has("Hub: Museum Unlock"))
    world.set_rule(mw.get_entrance("Hub Pool Area -> Hub Colloseum", player), Has("Hub: Colloseum Bridge"))
    world.set_rule(mw.get_entrance("Hub Pool Area -> Hub Pool Jump", player), Has("Hub: World Peace"))

    world.set_rule(mw.get_entrance("Hub South Portal -> Fixit Shop Main", player), Has("Hub: South Portal Bridge"))
    
    world.set_rule(mw.get_entrance("Hub Vault -> Slider Start", player), Has("Hub: Pool Vault Portal Unlock"))
    
    world.set_rule(mw.get_entrance("Hub Throne Room East Exterior -> Hub Throne Room West Exterior", player), Has("Hub: Throne Exterior Wall"))
    world.set_rule(mw.get_entrance("Hub Throne Room East Exterior -> Hub Floating Islands Path", player), Has("Hub: Bottom Path Floating Islands"))

    world.set_rule(mw.get_entrance("Hub Throne Room West Exterior -> Throne Interior", player), Has("Hub: Throne Room Door"))

    world.set_rule(mw.get_entrance("Hub Central Bridge -> Maze Start", player), Has("Hub: Central Bridge Portal Bridge"))
    world.set_rule(mw.get_entrance("Hub Central Bridge -> Hub Lookout Long Path", player), HasAny("Hub: Power Room North Door", "Hub: Lookout Long Path Door"))
    world.set_rule(mw.get_entrance("Hub Central Bridge -> Hub Tree", player), Has("Hub: Tree Area Door"))
    world.set_rule(mw.get_entrance("Hub Central Bridge -> Hub Power Room", player), Has("Hub: Power Room North Door"))

    world.set_rule(mw.get_entrance("Hub University Exterior -> Hub Uni Whale Bridge Connector", player), Has("Hub: Exterior University Wall Door"))
    world.set_rule(mw.get_entrance("Hub University Exterior -> Hub University Interior", player), Has("Hub: University Doors"))

    world.set_rule(mw.get_entrance("Hub Uni Whale Bridge Connector -> Hub Lower Whale Lookout", player), Has("Hub: Secondary University Wall Door"))

    world.set_rule(mw.get_entrance("Hub Upper Pool Perimeter -> Hub Light Puzzle Area", player), HasAny("Hub: Ramp to Light Puzzle", "Hub: Upper Bridge Jump Walls"))
    world.set_rule(mw.get_entrance("Hub Upper Pool Perimeter -> Hub Throne Room East Exterior", player), Has("Hub: Top Path Floating Islands"))
    world.set_rule(mw.get_entrance("Hub Upper Pool Perimeter -> Hub Start Lookout", player), Has("Hub: Start Lookout Door"))
    world.set_rule(mw.get_entrance("Hub Upper Pool Perimeter -> Hub Ice Portal", player), Has("Hub: Upper Bridge Jump Walls"))

    world.set_rule(mw.get_entrance("Hub Lower Whale Lookout -> Hub Whale Bridge", player), Has("Hub: Whale Bridge"))

    world.set_rule(mw.get_entrance("Hub Whale Bridge -> Ocean Main", player), Has("Hub: Whales and Central Dead End Door"))

    world.set_rule(mw.get_entrance("Hub Colloseum -> Hub Colloseum Exterior", player), Has("Hub: Colloseum Exterior Wall Doors"))
    world.set_rule(mw.get_entrance("Hub Colloseum -> Hub Colloseum Podium", player), Has("Hub: Colloseum Push Block Unlock"))

    world.set_rule(mw.get_entrance("Hub Colloseum Exterior -> Hub Colloseum Top", player), Has("Hub: World Peace"))

    world.set_rule(mw.get_entrance("Hub Colloseum Podium -> Hub Colloseum Middle Level", player), Has("Hub: Colloseum Push Block Unlock"))
    
    world.set_rule(mw.get_entrance("Hub Colloseum Middle Level -> Glass Box", player), Has("Hub: Colloseum Podium Ramp"))

    world.set_rule(mw.get_entrance("Hub University Interior -> Hub University Second Floor", player), Has("Hub: University Second Floor Ramp"))
    
    world.set_rule(mw.get_entrance("Hub University Second Floor -> Island Day", player), Has("Hub: University Portal Buttons"))
    world.set_rule(mw.get_entrance("Hub University Second Floor -> Planetarium", player), Has("Hub: University Portal Planetarium Access"))

    world.set_rule(mw.get_entrance("Hub Ice Portal -> Hub Power Room", player), Has("Hub: Power Room South Door"))
    world.set_rule(mw.get_entrance("Hub Ice Portal -> Hub Teleport Island", player), HasAll("Hub: Power Room South Door", "Hub: Power Room North Door", "Hub: World Peace"))

    # Simple Square Entrances
    world.set_rule(mw.get_entrance("Simple Square Area -> Simple Square Exterior", player), HasAny("Hub: Power Room South Door", "Froggy Car", "Battery Rocket Car"))

    # Fixit Shop Entrances
    world.set_rule(mw.get_entrance("Fixit Shop Main -> Fixit Shop Cave", player), Has("Desert: Shop Cave Door"))
    world.set_rule(mw.get_entrance("Fixit Shop Main -> Fixit Shop Fence", player), Has("Desert: Fixit Shop Fence"))

    # Slider Entrances
    world.set_rule(mw.get_entrance("Slider Start -> Slider Lower Back", player), Has("Slider: Start Ramp"))
    world.set_rule(mw.get_entrance("Slider Start -> Slider Upper Left", player), Has("Slider: Left Push Block Unlock"))
    world.set_rule(mw.get_entrance("Slider Start -> Slider Upper Right", player), Has("Slider: Right Push Block Unlock"))

    world.set_rule(mw.get_entrance("Slider Upper Right -> Slider Exit", player), Has("Slider: Left Side Ramp"))

    # Maze
    world.set_rule(mw.get_entrance("Maze Start -> Maze Exterior Walls", player), Has("Maze: Door to Big Ramp"))
    world.set_rule(mw.get_entrance("Maze Start -> Maze Cave", player), Has("Maze: Raise Cave Wall"))

    world.set_rule(mw.get_entrance("Maze Exterior Walls -> Maze Interior Walls", player), Has("Maze: Hedge Ramp"))

    world.set_rule(mw.get_entrance("Maze Interior Walls -> Maze Interior Walls Upper", player), Has("Maze: Raise Cave Wall"))


    world.set_rule(mw.get_entrance("Maze Interior Walls Upper -> Maze Interior Walls Bridge", player), Has("Maze: Interior Wall Bridge"))

    # Glass Box
    world.set_rule(mw.get_entrance("Glass Box -> Glass Box Exit", player), Has("Glass Box: Exit Bridge"))

    # Sands of Fallen Kings
    world.set_rule(mw.get_entrance("Sands Main -> Sands North Exterior Walls", player), Has("Sands: Exterior Walls Access"))
    world.set_rule(mw.get_entrance("Sands Main -> Sands South Exterior Walls", player), Has("Sands: Lower South West Tower"))

    # Ocean
    world.set_rule(mw.get_entrance("Ocean Main -> Ocean Inside Fort", player), HasAll("Ocean: Fort Bottom Ramp", "Ocean: Fort Middle Ramp", "Ocean: Fort Top Ramp"))

    # Ice Temple
    world.set_rule(mw.get_entrance("Ice Temple Main -> Ice NE Perimeter Ledge", player), Has("Ice: Perimeter Wall Blocker"))
    world.set_rule(mw.get_entrance("Ice Temple Main -> Ice Temple Lower East Ledge", player), Has("Ice: South Ramp Blocker"))
    world.set_rule(mw.get_entrance("Ice Temple Main -> Ice Temple South Path Start", player), Has("Ice: South Ramp Blocker"))

    world.set_rule(mw.get_entrance("Ice Temple South Path Start -> Ice Temple South Ledge End", player), HasAll("Ice: South Jump Path Wall", "Ice: Ice Pillar Blocker"))

    world.set_rule(mw.get_entrance("Ice NE Perimeter Ledge -> Ice SE Tower", player), Has("Ice: Secondary Wall Ramp"))

    world.set_rule(mw.get_entrance("Ice SE Tower -> Ice SW Tower", player), Has("Ice: South Wall Bridge"))

    world.set_rule(mw.get_entrance("Ice SW Tower -> Ice Northern Towers", player), Has("Ice: Other Wall Bridges"))

    world.set_rule(mw.get_entrance("Ice Northern Towers -> Ice Tower Jump", player), Has("Ice: Wall Jump Ramp"))
    world.set_rule(mw.get_entrance("Ice Northern Towers -> Ice Bridge Ramp To Monument", player), Has("Ice: Wall Bridge Ramp to Monument"))
    world.set_rule(mw.get_entrance("Ice Northern Towers -> Ice NE Tower Interior", player), Has("Ice: Raise North East Tower"))

    # Sheep Pastures
    world.set_rule(mw.get_entrance("Sheep Patures Main -> Sheep Patures In Shed", player), HasAny("Sheep: Shed Ramp", "Sheep: Sheep Shed Door"))
    world.set_rule(mw.get_entrance("Sheep Patures Main -> Sheep Patures Shed Raised", player), Has("Sheep: Raise Shed"))

    # Island
    world.set_rule(mw.get_entrance("Island Day -> Island Day South Path", player), Has("Island: Lower Jump Blocker Behind Start"))
    world.set_rule(mw.get_entrance("Island Day -> Island Night", player), Has("Island: Night Portal"))
    world.set_rule(mw.get_entrance("Island Day -> Island North Lower Ledge", player), Has("Island: North Lower Wall Ramp"))
    world.set_rule(mw.get_entrance("Island Day -> Island North Upper Ledge", player), Has("Island: North Upper Wall Ramp"))
    # world.set_rule(mw.get_entrance("Island Day -> Island East Path End", player), Has("Sheep: Raise Shed")) Why was this an entrance?
    world.set_rule(mw.get_entrance("Island Day -> Island Treetop", player), HasAll("Island: Pond Treetop Ramp", "Island: Pond Treetop Ramp Blocker"))

    world.set_rule(mw.get_entrance("Island Night -> Island Hut Ledge", player), Has("Island: Lower Spiral Island"))
    world.set_rule(mw.get_entrance("Island Night -> Island Night South Path", player), Has("Island: South Path Cave Wall Removal")) #ig this is only needed for the artifact?
    world.set_rule(mw.get_entrance("Island Night -> Island East Path End", player), HasAll("Island: First East Path Bridge", "Island: Second East Path Bridge", "Island: Third East Path Bridge"))

    world.set_rule(mw.get_entrance("Island Hut Ledge -> Island Hut Inside", player), Has("Island: Hut Treetop Ramp"))

    world.set_rule(mw.get_entrance("Island Hut Inside -> Island Treetop", player), Has("Island: Treetop West Bridge"))
    world.set_rule(mw.get_entrance("Island Treetop -> Island Hut Inside", player), Has("Island: Treetop West Bridge"))

    # Throne Room
    world.set_rule(mw.get_entrance("Throne Interior -> Throne Interior N Window", player), Has("Throne: Open North Windows"))
    world.set_rule(mw.get_entrance("Throne Interior -> Throne Interior S Window", player), Has("Throne: Open South Windows"))
    world.set_rule(mw.get_entrance("Throne Interior -> Throne Garden", player), HasAll("Throne: Open Main Door", "Throne: Main Door Ramp"))
    
    world.set_rule(mw.get_entrance("Throne Garden -> Throne East Exterior Wall", player), Has("Throne: East Exterior Wall"))
    world.set_rule(mw.get_entrance("Throne Garden -> Throne West Exterior Wall", player), Has("Throne: West Exterior Wall"))

    world.set_rule(mw.get_entrance("Throne East Exterior Wall -> Throne West Exterior Wall", player), Has("Throne: Lower High Garden Artifact"))
    world.set_rule(mw.get_entrance("Throne West Exterior Wall -> Throne East Exterior Wall", player), Has("Throne: Lower High Garden Artifact"))

    # Power Room/Limbo
    world.set_rule(mw.get_entrance("Power Room -> Limbo", player), HasAll("Power Room: Green Cable Push", "Power Room: Green Cable Activate",
                                                                          "Power Room: Blue Cable Push", "Power Room: Blue Cable Activate",
                                                                          "Power Room: Red Cable Push", "Power Room: Red Cable Activate",
                                                                          "Power Room: Yellow Cable Push", "Power Room: Yellow Cable Activate",
                                                                          "Power Room: Exit Teleporter"))
    world.set_rule(mw.get_entrance("Limbo -> Throne Boss", player), Has("Limbo: Crown and Exit Portal"))

    ##################
    # Location Rules #
    ##################
    # Hub
    world.set_rule(mw.get_location("Hub: North Pool Secret Door Artifact", player), Has("Hub: North Pool Small Secret Door"))
    world.set_rule(mw.get_location("Hub: North Pool Jump Ramp", player), HasAny("Hub: North Pool Jump Ramp", "Froggy Car", "Battery Rocket Car"))
    world.set_rule(mw.get_location("Hub: Tree Slalom Start Artifact", player), Has("Hub: South Pool Artifact Block"))
    world.set_rule(mw.get_location("Hub: South Pool Dead End Artifact", player), HasAny("Hub: South Pool Dead End Door", "Froggy Car") | CanReachRegion("Hub South Portal"))
    world.set_rule(mw.get_location("Hub: Tree Slalom Reward Artifact", player), HasAny("Hub: Tree Slalom Unlock", "Froggy Car"))
    world.set_rule(mw.get_location("Hub: Pool Drain Artifact", player), Has("Hub: Progressive Pool")) # Unobtainable with filled pool
    world.set_rule(mw.get_location("Hub: Pool South West Artifact", player), HasAll("Hub: Progressive Pool", "Hub: Pool Push Block") |
                                                                             Has("Hub: Progressive Pool", 2))
    world.set_rule(mw.get_location("Hub: Pool South East Artifact", player), HasAll("Hub: Progressive Pool", "Hub: Pool Push Block", "Hub: Pool South East Blocker") | 
                                                                             Has("Hub: Progressive Pool", 2)) 
    world.set_rule(mw.get_location("Hub: Pool South West Artifact", player), HasAll("Hub: Progressive Pool", "Hub: Pool Push Block", "Hub: Pool North West Blocker") |
                                                                             Has("Hub: Progressive Pool", 2))
    world.set_rule(mw.get_location("Hub: Pool Center Artifact", player), Has("Hub: Progressive Pool", 2))
    world.set_rule(mw.get_location("Hub: Central Bridge West Ramp Artifact", player), Has("Hub: Central Bridge West Ramp"))
    world.set_rule(mw.get_location("Hub: Central Bridge East Ramp Artifact", player), Has("Hub: Central Bridge East Ramp"))
    world.set_rule(mw.get_location("Hub: Pool North East Artifact", player), HasAllCounts({"Hub: Progressive Pool": 2, "Hub: Pool North East Blocker": 1}))
    world.set_rule(mw.get_location("Hub: Alley Push Ramp Artifact", player), Has("Hub: Exterior University Wall Door"))
    world.set_rule(mw.get_location("Hub: Upper Artifact Near Whale Bridge", player), Has("Hub: Blocker Near Whale Bridge"))
    world.set_rule(mw.get_location("Hub: Colloseum Podium Artifact", player), HasAny("Hub: Colloseum Push Block Unlock", "Hub: Colloseum Podium Extension"))
    world.set_rule(mw.get_location("Hub: Start Area Jump Artifact", player), Has("Hub: Start Area Back Removal"))
    world.set_rule(mw.get_location("Hub: Inside Podium Artifact", player), Has("Hub: Colloseum Podium Door"))
    world.set_rule(mw.get_location("Hub: Floating Island Artifact", player), Has("Hub: Top Path Floating Islands"))
    world.set_rule(mw.get_location("Hub: Upper Pool Dead End Path Artifact", player), Has("Hub: Start Lookout Dead End Door"))
    world.set_rule(mw.get_location("Hub: Central Path Dead End Artifact", player), Has("Hub: Whales and Central Dead End Door"))
    world.set_rule(mw.get_location("Hub: University Back Right Artifact", player), Has("Hub: University Back Row Ramp"))
    world.set_rule(mw.get_location("Hub: University Back Left Artifact", player), HasAll("Hub: University Back Row Ramp", "Hub: University Lower Back Artifact Platform"))
    world.set_rule(mw.get_location("Hub: University Second Row Artifact", player), Has("Hub: University Lower Second Row Ramp"))
    world.set_rule(mw.get_location("Hub: University Third Row Artifact", player), Has("Hub: University Lower Third Row Ramp"))
    world.set_rule(mw.get_location("Hub: University Fourth Row Artifact", player), Has("Hub: University Lower Fourth Row Ramp"))
    world.set_rule(mw.get_location("Hub: University First Row Artifact", player), Has("Hub: University Lower Push Ramp"))

    world.set_rule(mw.get_location("Hub: Hopscotch Museum Piece", player), Has("Hub: World Peace"))

    ####################
    # Completion Rules #
    ####################
    if options.ending_goal == EndingGoal.option_bristles:
        world.set_completion_rule(CanReachRegion("Throne Boss"))
    elif options.ending_goal == EndingGoal.option_museum:
        world.set_completion_rule(CanReachRegion("Hub Museum") & 
                                  HasAll("Hub: Sun Museum Glass", "Hub: Block Museum Glass", "Hub: Book Museum Glass",
                                         "Hub: Energy Cell Museum Glass", "Hub: Tire Museum Glass", "Hub: Blockstar Museum Glass",
                                         "Hub: Tree Museum Glass", "Hub: Cube Museum Glass", "Hub: Portal Museum Glass",
                                         "Hub: Brick Bristles Museum Glass"))