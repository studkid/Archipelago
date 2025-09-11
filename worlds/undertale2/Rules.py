from typing import List
from BaseClasses import CollectionState, MultiWorld, Location, Region, Item
from typing import TYPE_CHECKING

def has_all(state: CollectionState, player: int, items: List[str]) -> bool:
    for _, item in enumerate(items):
        if not state.has(item, player):
            return False
        
    return True

def set_rules(multiworld: MultiWorld, player: int):
    # Ruins
    multiworld.get_entrance("Ruins Main -> Ruins Sewers", player).access_rule = \
            lambda state: state.has("Lucky Crowbar", player)
    multiworld.get_entrance("Ruins Lake -> Ruins Tree", player).access_rule = \
            lambda state: has_all(state, player, ["Gold Key", "Silver Key", "Bronze Key", "Progressive Monk Key"])\
                          or state.has("Progressive Key", player, 4)

    # Archives
    multiworld.get_entrance("Archives Pit -> Archives Sewers", player).access_rule = \
            lambda state: state.has("Lucky Crowbar", player)
    multiworld.get_entrance("Archives Pit -> Archives Back", player).access_rule = \
            lambda state: state.has("Library Card", player)
    
    # Swamp
    multiworld.get_entrance("Ruins Tree -> Swamp", player).access_rule =\
            lambda state: state.has("Hotden Reached", player)
    
    # Special
    multiworld.get_location("Lancer Card", player).access_rule = \
            lambda state: state.has("Lancer Encountered", player)
    