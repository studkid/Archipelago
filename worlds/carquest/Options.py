from Options import Choice, Toggle, DefaultOnToggle, PerGameCommonOptions
from dataclasses import dataclass

class EndingGoal(Choice):
    """
    Choose goal:
    Museum - Collect all museum pieces and go through either ending portal
    Blockbeard - Defeat Captain Blockbeard and restore peace to Blockteria
    """
    display_name = "Ending Goal"
    option_museum = 0
    option_blockbeard = 1
    default = 1

@dataclass
class CarQuestOptions(PerGameCommonOptions):
    ending_goal: EndingGoal