from typing import List
from BaseClasses import CollectionState, MultiWorld, Location, Region, Item
from typing import TYPE_CHECKING

def has_all(state: CollectionState, player: int, items: List[str]) -> bool:
    for _, item in enumerate(items):
        if not state.has(item, player):
            return False
        
    return True

def set_rules(multiworld: MultiWorld, player: int):
    for entrance in multiworld.get_region("Sewers", player).entrances:
        entrance.access_rule = lambda state: state.has("Lucky Crowbar", player)

    for entrance in multiworld.get_region("Ruins Tree", player).entrances:
        entrance.access_rule = lambda state: has_all(state, player, ["Gold Key", "Silver Key", "Bronze Key", "Monk Key"])\
                                             or state.has("Progressive Key", player, 4)
    