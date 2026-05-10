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

@dataclass
class CarQuestOptions(PerGameCommonOptions):
    ending_goal: EndingGoal