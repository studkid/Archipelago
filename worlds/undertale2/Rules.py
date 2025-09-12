from typing import List
from BaseClasses import CollectionState, MultiWorld, Location, Region, Item
from typing import TYPE_CHECKING

def has_all(state: CollectionState, player: int, items: List[str]) -> bool:
    for _, item in enumerate(items):
        if not state.has(item, player):
            return False
        
    return True

def party_count(state: CollectionState, player: int) -> int:
    party = ["Fabio", "sans", "Nazrin"]
    count = 1

    for _, name in enumerate(party):
        if state.has(name, player):
            count += 1

        if count == 4:
            break

    return count

def can_beat_snopestablook(state: CollectionState, player: int) -> bool:
    return party_count(state, player) == 2

def can_beat_swamp(state: CollectionState, player: int) -> bool:
    return party_count(state, player) == 2

def can_beat_froguelass(state: CollectionState, player: int) -> bool:
    return party_count(state, player) == 3

def set_rules(multiworld: MultiWorld, player: int):
    # Ruins
    multiworld.get_entrance("Ruins Main -> Ruins Sewers", player).access_rule = \
            lambda state: state.has("Lucky Crowbar", player)
    multiworld.get_entrance("Ruins Main -> Ruins Lake", player).access_rule = \
            lambda state: can_beat_snopestablook(state, player)
    multiworld.get_entrance("Ruins Lake -> Ruins Tree", player).access_rule = \
            lambda state: has_all(state, player, ["Gold Key", "Silver Key", "Bronze Key", "Progressive Monk Key"])\
                          or state.has("Progressive Key", player, 4)

    # Archives
    multiworld.get_entrance("Archives Pit -> Archives Sewers", player).access_rule = \
            lambda state: state.has("Lucky Crowbar", player)
    multiworld.get_entrance("Archives Pit -> Archives Back", player).access_rule = \
            lambda state: state.has("Library Card", player)
    multiworld.get_entrance("Archives Pit -> Frogue Chamber", player).access_rule = \
            lambda state: (state.has("Progressive Monk Key", player, 2) or state.has("Progressive Key", player, 5)) and \
                          can_beat_froguelass(state, player)
    
    # Swamp
    multiworld.get_entrance("Ruins Tree -> Swamp", player).access_rule =\
            lambda state: state.has("Hotden Reached", player) and can_beat_swamp(state, player)
    
    # Prison
    multiworld.get_entrance("Hotden -> Prison Cells", player).access_rule =\
            lambda state: has_all(state, player, ["sans", "Anime catboy transformation potion"]) and \
                          (state.has("Progressive Monk Key", player, 2) or state.has("Progressive Key", player, 5))
    
    # Special
    multiworld.get_location("#11 Lancer Card", player).access_rule = \
            lambda state: state.has("Lancer Encountered", player)
    
    # Win Condition
    multiworld.completion_condition[player] = lambda state: state.can_reach("Goal Region", "Region", player)
    