from typing import List
from BaseClasses import CollectionState, MultiWorld, Location, Region, Item
from .Options import UT2Options, CardSanity, RequireNazrin
from .Locations import location_table

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
    return party_count(state, player) >= 2

def can_beat_swamp(state: CollectionState, player: int) -> bool:
    return party_count(state, player) >= 2

def can_beat_froguelass(state: CollectionState, player: int) -> bool:
    return party_count(state, player) >= 3

def can_beat_cirno(state: CollectionState, player: int) -> bool:
    return party_count(state, player) >= 4

def set_rules(multiworld: MultiWorld, player: int, options: UT2Options):
    if options.cardsanity == CardSanity.option_all and options.requirenazrin == RequireNazrin.option_true:
        for name, data in location_table.items():
            if name == "#59 Gilded☆Bingus Card":
                continue
            if data.category != "enemy":
                continue
            
            multiworld.get_location(name, player).access_rule = \
                lambda state: state.has("Nazrin", player)

    # Ruins
    multiworld.get_entrance("Ruins Main -> Ruins Sewers", player).access_rule = \
            lambda state: state.has("Lucky Crowbar", player)
    multiworld.get_entrance("Ruins Main -> Scopestablook", player).access_rule = \
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
            lambda state: state.has("Hotden Reached", player)
    
    # Prison
    multiworld.get_entrance("Hotden -> Prison Cells", player).access_rule =\
            lambda state: has_all(state, player, ["sans", "Anime catboy transformation potion"]) and \
                          (state.has("Progressive Monk Key", player, 2) or state.has("Progressive Key", player, 5))
    
    multiworld.get_location("Prison - Marylin Reward #1", player).access_rule =\
            lambda state: has_all(state, player, ["Puzzle Key"])
    multiworld.get_location("Prison - Marylin Reward #2", player).access_rule =\
            lambda state: has_all(state, player, ["Puzzle Key"])
    multiworld.get_location("#20 Marylin Card", player).access_rule =\
            lambda state: has_all(state, player, ["Puzzle Key"])
    
    multiworld.get_entrance("Prison Cells -> Prison Kitchen", player).access_rule =\
            lambda state: state.has("Prison Key", player)
    
    multiworld.get_entrance("Prison Kitchen -> Prison Office", player).access_rule =\
            lambda state: can_beat_cirno(state, player)
    
    # Beach
    multiworld.get_entrance("Prison Office -> Beach Entry", player).access_rule =\
            lambda state: state.has("Prison Destroyed", player)    
            
    multiworld.get_entrance("Beach Entry -> Beach Relax 1", player).access_rule =\
            lambda state: state.has("Relax Pass", player, 1)
    multiworld.get_entrance("Beach Relax 1 -> Beach Relax 2", player).access_rule =\
            lambda state: state.has("Relax Pass", player, 2)
    multiworld.get_entrance("Beach Relax 2 -> Beach Relax 3", player).access_rule =\
            lambda state: state.has("Relax Pass", player, 3)
    multiworld.get_entrance("Beach Relax 3 -> Beach Relax 4", player).access_rule =\
            lambda state: state.has("Relax Pass", player, 4)
    multiworld.get_entrance("Beach Relax 4 -> Beach Relax 5", player).access_rule =\
            lambda state: state.has("Relax Pass", player, 5)
    multiworld.get_entrance("Beach Relax 5 -> Beach Relax 6", player).access_rule =\
            lambda state: state.has("Relax Pass", player, 6)
    multiworld.get_entrance("Beach Relax 6 -> Beach Relax 7", player).access_rule =\
            lambda state: state.has("Relax Pass", player, 7)
    
    # Special
    if options.cardsanity == CardSanity.option_all:
        multiworld.get_location("#11 Lancer Card", player).access_rule = \
                lambda state: state.has("Lancer Encountered", player)
        multiworld.get_location("#18 Homer Guard Card", player).access_rule = \
            lambda state: state.has("#18 Homer Guard Card", player)
        multiworld.get_location("#19 Prison Tick Card", player).access_rule = \
            lambda state: state.has("#19 Prison Tick Card", player)
    
    # Win Condition
    multiworld.completion_condition[player] = lambda state: state.can_reach("Cirno Defeated", "Location", player)
    