from Options import Choice, Toggle, DefaultOnToggle, PerGameCommonOptions
from dataclasses import dataclass

class EndingGoal(Choice):
    """
    Choose goal:
    Museum - Collect all museum pieces and go through either ending portal
    Bristles - Defeat Captain Brick Bristles and restore peace to Blockteria
    """
    display_name = "Ending Goal"
    option_museum = 0
    option_bristles = 1
    default = 0

class ReduceDoors(Toggle):
    """
    Start with most doors blocking single artifacts unlocked.
    Reduces number of 1:1 item to location requirements.
    """
    display_name = "Reduce Doors"

class EnergyCellSanity(Choice):
    """
    Shuffles energy cells as locations.
    Cells out of reach of the basic car are not included unless cars are shuffled.
    """
    diplay_name = "Energy Cell Sanity"
    option_false = 0
    option_big_only = 1
    option_small_only = 2
    option_all = 3
    default = 0

@dataclass
class CarQuestOptions(PerGameCommonOptions):
    ending_goal: EndingGoal
    reduce_doors: ReduceDoors
    # energy_cell_sanity: EnergyCellSanity