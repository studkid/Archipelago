from worlds.AutoWorld import World
from rule_builder.rules import Has, HasAll, CanReachRegion, HasAny
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
    world.set_rule(mw.get_entrance("Hub Start -> Hub Simple Portal Path", player), Has("Hub: Start Room Blocker"))
    world.set_rule(mw.get_entrance("Hub Start -> Hub South Portal", player), HasAll("Hub: Start Room Blocker", "Hub: Start Area Back Removal", "Hub: Start Room Bridge"))

    world.set_rule(mw.get_entrance("Hub Simple Portal Path -> Hub Pool Area", player), Has("Hub: Simple Portal Bridge Wall"))
    world.set_rule(mw.get_entrance("Hub Simple Portal Path -> Hub Throne Room East Exterior", player), Has("Hub: Start Room Right Door"))
    world.set_rule(mw.get_entrance("Hub Simple Portal Path -> Hub Central Bridge", player), Has("Hub: Start Room Right Door"))
    world.set_rule(mw.get_entrance("Hub Simple Portal Path -> Hub Upper Pool Perimeter", player), Has("Hub: Ramp Near Simple Portal"))

    world.set_rule(mw.get_entrance("Hub Pool Area -> Hub Upper Uni Alleyway", player), Has("Hub: Upper University Alleyway Access"))
    world.set_rule(mw.get_entrance("Hub Pool Area -> Hub South Pool Dead End Path", player), Has("Hub: South Pool Dead End Door"))
    world.set_rule(mw.get_entrance("Hub Pool Area -> Floating Cube Area", player), Has("Hub: North Pool Portal Access"))
    world.set_rule(mw.get_entrance("Hub Pool Area -> Hub Cube Monument", player), Has("Hub: Cube Monument Access"))
    world.set_rule(mw.get_entrance("Hub Pool Area -> Hub South Portal", player), Has("Hub: South Portal Ramp Door"))
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

    # Fixit Shop Entrances
    world.set_rule(mw.get_entrance("Fixit Shop Main -> Fixit Shop Cave", player), Has("Desert: Shop Cave Door"))
    world.set_rule(mw.get_entrance("Fixit Shop Main -> Fixit Shop Fence", player), Has("Desert: Fixit Shop Fence"))

    # Slider Entrances
    world.set_rule(mw.get_entrance("Slider Start -> Slider Lower Back", player), Has("Slider: Start Ramp"))
    world.set_rule(mw.get_entrance("Slider Start -> Slider Upper Left", player), Has("Slider: Left Push Block Unlock"))
    world.set_rule(mw.get_entrance("Slider Start -> Slider Upper Right", player), Has("Slider: Right Push Block Unlock"))

    world.set_rule(mw.get_entrance("Slider Upper Right -> Slider Exit", player), Has("Slider: Left Side Ramp"))

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