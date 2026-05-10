from worlds.AutoWorld import World
from rule_builder.rules import Has, HasAll, CanReachRegion
from rule_builder.options import OptionFilter
from .Options import EndingGoal

def set_rules(world: World) -> bool:
    mw = world.multiworld
    player = world.player
    options = world.options

    # Entrance Rules
    world.set_rule(mw.get_entrance("Hub Start -> Hub Simple Portal Path", player), Has("Hub: Start Room Blocker"))
    world.set_rule(mw.get_entrance("Hub Start -> Hub South Portal", player), HasAll("Hub: Start Room Blocker", "Hub: Start Area Back Removal", "Hub: Start Room Bridge"))

    world.set_rule(mw.get_entrance("Hub Simple Portal Path -> Hub Pool Area", player), Has("Hub: Simple Portal Bridge Wall"))
    world.set_rule(mw.get_entrance("Hub Simple Portal Path -> Hub Throne Room East Exterior", player), Has("Hub: Start Room Right Door"))
    world.set_rule(mw.get_entrance("Hub Simple Portal Path -> Hub Central Bridge", player), Has("Hub: Start Room Right Door"))
    world.set_rule(mw.get_entrance("Hub Simple Portal Path -> Hub Upper Pool Perimeter", player), Has("Hub: Ramp Near Simple Portal"))

    # Completion Rules
    if options.ending_goal == EndingGoal.option_bristles:
        world.set_completion_rule(CanReachRegion("Throne Boss"))
    elif options.ending_goal == EndingGoal.option_museum:
        world.set_completion_rule(CanReachRegion("Hub Museum") & 
                                  HasAll("Hub: Sun Museum Glass", "Hub: Block Museum Glass", "Hub: Book Museum Glass",
                                         "Hub: Energy Cell Museum Glass", "Hub: Tire Museum Glass", "Hub: Blockstar Museum Glass",
                                         "Hub: Tree Museum Glass", "Hub: Cube Museum Glass", "Hub: Portal Museum Glass",
                                         "Hub: Brick Bristles Museum Glass"))