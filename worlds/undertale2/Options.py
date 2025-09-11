from Options import Choice, Range, Toggle, DeathLink, DefaultOnToggle, OptionSet, PerGameCommonOptions

from dataclasses import dataclass

class ProgMonkKey(Choice):
    """
    Makes the gold, silver, bronze and monk key progressive.
    """
    display_name = "Progressive Monk Key"
    option_false = 0
    option_true = 1
    option_monk_key_only = 2

class CardSanity(Choice):
    """
    Turns card drops into locations.
    (You will need to interact with the card in your inventory to send the location)
    """
    display_name = "Cardsanity"
    option_false = 0
    option_bosses_only = 1
    option_all = 2

# class LancerSanity(Toggle):
#     """
#     Turns all lancer interactions into locations
#     """
#     display_name = "lancersanity"

@dataclass
class UT2Options(PerGameCommonOptions):
    progressive_monkkey: ProgMonkKey
    cardsanity: CardSanity
    # lancersanity: LancerSanity
