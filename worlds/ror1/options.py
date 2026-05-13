from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, Range, Choice, PerGameCommonOptions, OptionCounter, StartInventoryPool, OptionGroup
from .weights import trap_weights, default_weights

class Grouping(Choice):
    """
    Stages: Each stage will have location checks within each map variant on a given stage.
    Stages will be locked in the item pool until received.

    Maps: Each map will have location checks within each map on said stage.
    Both maps and stages will be locked in the item pool until received.
    """
    display_name = "Location Grouping"
    option_stage = 1
    option_map = 2
    default = 2

class ItemPickups(Range):
    """
    Number of item pickups locations each map/stage group will have.
    """
    display_name = "Total Locations"
    range_start = 10
    range_end = 50
    default = 20

class ProgressiveStage(DefaultOnToggle):
    """
    Changes stage items to be progressive.
    """
    display_name = "Progressive Stages"

class RequireStage(DefaultOnToggle):
    """
    Add Stage items to the pool that blocks maps of the type
    Does nothing unless on map grouping
    """
    display_name = "Require Stage"

class StrictStageProg(DefaultOnToggle):
    """
    Require both the prior stage and any corresponding map before having access to later stages
    Ex. You won't be able to access Stage 3 until you have Stage 2 and either Stage 2 map
    """
    display_name = "Strict Map Requirements"

class StageFiveTP(DefaultOnToggle):
    """
    Only allow access to teleport to final stage if you have at least visited a stage 5 map on your current run.
    Recommended if not shuffling teleporter fragments for goal.
    """
    display_name = "Divine Teleporter on Stage 5"

class MapShuffle(Toggle):
    """
    Shuffles map order to appear in different points of stage progression.
    Recommended to play with Strict Stage Progression enabled.
    """
    display_name = "Map Shuffle"

class AvailableFrags(Range):
    """
    Percentage of filler items to be replaced with teleporter fragments
    """
    display_name = "Teleporter Fragments Available"
    range_start = 0
    range_end = 100
    default = 0

class RequiredFrags(Range):
    """
    Percentage of teleporter fragments required to access the final stage
    """
    display_name = "Teleporter Fragments Required"
    range_start = 0
    range_end = 100
    default = 0

class ItemPickupStep(Range):
    """
    Number of items to pick up before an AP Check is completed.
    Setting to 1 means every other pickup.
    Setting to 2 means every third pickup. So on...
    """
    display_name = "Item Pickup Step"
    range_start = 0
    range_end = 5
    default = 1

class TrapPercentage(Range):
    """Percentage of filler to be replaced with traps."""
    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 0

class ItemWeights(OptionCounter):
    """
    Specify weight distribution of filler items.
    """
    display_name = "Item Weights"
    valid_keys = default_weights.keys()
    min = 0
    default = default_weights

class TrapWeights(OptionCounter):
    """
    Specify weight distribution of traps items.
    """
    display_name = "Trap Weights"
    valid_keys = trap_weights.keys()
    min = 0
    default = trap_weights

ror_option_groups = [
    OptionGroup("Location Settings", [
        Grouping,
        ItemPickups,
        ItemPickupStep,
    ]),
    OptionGroup("Logic Settings", [
        ProgressiveStage,
        RequireStage,
        StrictStageProg,
        StageFiveTP,
        MapShuffle
    ]),
    OptionGroup("Teleporter Frag Hunt Settings", [
        AvailableFrags,
        RequiredFrags,
    ]),
    OptionGroup("Item Pool Settings", [
        ItemWeights,
        TrapPercentage, 
        TrapWeights 
    ])
]

@dataclass
class ROROptions(PerGameCommonOptions):
    grouping: Grouping
    total_pickups: ItemPickups
    progressive_stages: ProgressiveStage
    require_stage: RequireStage
    stage_five_tp: StageFiveTP
    strict_stage_prog: StrictStageProg
    map_shuffle: MapShuffle
    available_frags: AvailableFrags
    required_frags: RequiredFrags
    item_pickup_step: ItemPickupStep
    trap_percentage: TrapPercentage
    item_weights: ItemWeights
    trap_weights: TrapWeights
    start_inventory_from_pool: StartInventoryPool