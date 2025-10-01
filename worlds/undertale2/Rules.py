from typing import List
from BaseClasses import CollectionState, MultiWorld, Location, Region, Item
from .Options import UT2Options, CardSanity, RequireNazrin, AquariumSanity, ShuffleFishingMissions, RelaxRankNeedsPass, EndingGoal
from .Locations import location_table
from .MiscData import fish_data, fish_quests

def has_all(state: CollectionState, player: int, items: List[str]) -> bool:
    for _, item in enumerate(items):
        if not state.has(item, player):
            return False
        
    return True

def party_count(state: CollectionState, player: int) -> int:
    party = ["Fabio", "sans", "Nazrin", "Eclaire"]
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

def can_get_fish(state: CollectionState, name: str, player: int) -> bool:
    for _, region in enumerate(fish_data[name]):
        if state.can_reach(region, "Region", player):
            return True
        
    return False


def set_rules(multiworld: MultiWorld, player: int, options: UT2Options):
    # Card Sanity -----------------------------------------------------------------------
    if options.cardsanity == CardSanity.option_all and options.require_nazrin == RequireNazrin.option_true:
        for name, data in location_table.items():
            if data.category == "dig":
                multiworld.get_location(name, player).access_rule = \
                        lambda state: state.has("Joqua's Trowel", player)
            if name == "#59 Gilded☆Bingus Card":
                continue
            if data.category != "enemy":
                continue
            if name == "#11 Lancer Card":
                multiworld.get_location(name, player).access_rule = \
                        lambda state: state.has("Nazrin", player) and state.has("Lancer Encountered", player)
            if name == "#22 Angler Card":
                multiworld.get_location(name, player).access_rule = \
                        lambda state: state.has("Nazrin", player) and can_get_fish(state, "Angler", player)
            if name == "#23 Angeler Card":
                multiworld.get_location(name, player).access_rule = \
                        lambda state: state.has("Nazrin", player) and can_get_fish(state, "Angeler", player)
            
            multiworld.get_location(name, player).access_rule = \
                    lambda state: state.has("Nazrin", player)
    elif options.cardsanity == CardSanity.option_all:
        multiworld.get_location("#11 Lancer Card", player).access_rule = \
                lambda state: state.has("Lancer Encountered", player)
        multiworld.get_location(name, player).access_rule = \
                lambda state: can_get_fish(state, "Angler", player)
        multiworld.get_location(name, player).access_rule = \
                lambda state: can_get_fish(state, "Angeler", player)

    # Ruins -----------------------------------------------------------------------
    multiworld.get_entrance("Ruins Main -> Ruins Sewers", player).access_rule = \
            lambda state: state.has("Lucky Crowbar", player)
    multiworld.get_entrance("Ruins Main -> Scopestablook", player).access_rule = \
            lambda state: can_beat_snopestablook(state, player)
    multiworld.get_entrance("Ruins Lake -> Ruins Tree", player).access_rule = \
            lambda state: has_all(state, player, ["Gold Key", "Silver Key", "Bronze Key", "Progressive Monk Key"])\
                          or state.has("Progressive Key", player, 4)

    # Archives -----------------------------------------------------------------------
    multiworld.get_entrance("Archives Pit -> Archives Sewers", player).access_rule = \
            lambda state: state.has("Lucky Crowbar", player)
    multiworld.get_entrance("Archives Pit -> Archives Back", player).access_rule = \
            lambda state: state.has("Library Card", player)
    multiworld.get_entrance("Archives Pit -> Frogue Chamber", player).access_rule = \
            lambda state: (state.has("Progressive Monk Key", player, 2) or state.has("Progressive Key", player, 5)) and \
                          can_beat_froguelass(state, player)
    
    # Swamp -----------------------------------------------------------------------
    multiworld.get_entrance("Ruins Tree -> Swamp", player).access_rule =\
            lambda state: state.has("Hotden Reached", player)
    
    # Prison -----------------------------------------------------------------------
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
    
    # Beach -----------------------------------------------------------------------
    multiworld.get_entrance("Prison Office -> Beach Entry", player).access_rule =\
            lambda state: state.has("Prison Destroyed", player)    
            
    multiworld.get_entrance("Beach Entry -> Beach Relax 1", player).access_rule =\
            lambda state: state.has("Relax Pass", player, 1)
    if options.shuffle_relax == RelaxRankNeedsPass.option_true:
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
    
    multiworld.get_entrance("Beach Entry -> Greenhorn Shore", player).access_rule =\
            lambda state: state.has("Membership Card", player)
    if options.shuffle_fish_mission == ShuffleFishingMissions.option_true:
        multiworld.get_entrance("Greenhorn Shore -> Breadcrumb Bay", player).access_rule =\
                lambda state: state.has("Progressive Fishing Spot", player)
        multiworld.get_entrance("Breadcrumb Bay -> Melonbread Cove", player).access_rule =\
                lambda state: state.has("Progressive Fishing Spot", player, 3)
        multiworld.get_entrance("Melonbread Cove -> Pudding", player).access_rule =\
                lambda state: state.has("Progressive Fishing Spot", player, 5)
        multiworld.get_location("Beach - Piss and Shit FM HQ", player).access_rule =\
                lambda state: state.has("Progressive Fishing Spot", player, 6)
        multiworld.get_entrance("Greenhorn Shore -> Rust Gear Gulf", player).access_rule =\
                lambda state: state.has("Rust Ticket", player) and state.has("Progressive Fishing Spot", player, 4)
        multiworld.get_entrance("Greenhorn Shore -> Chemical Waste Zone", player).access_rule =\
                lambda state: state.has("Waste Ticket", player) and state.has("Progressive Fishing Spot", player, 4)
        multiworld.get_entrance("Greenhorn Shore -> Big Bone Bay", player).access_rule =\
                lambda state: state.has("Bone Ticket", player) and state.has("Progressive Fishing Spot", player, 4)
        multiworld.get_entrance("Greenhorn Shore -> Stardrop Tree", player).access_rule =\
                lambda state: state.has("Star Ticket", player) and state.has("Progressive Fishing Spot", player, 4)       
        
    else:    
        multiworld.get_entrance("Greenhorn Shore -> Rust Gear Gulf", player).access_rule =\
                lambda state: state.has("Rust Ticket", player)
        multiworld.get_entrance("Greenhorn Shore -> Chemical Waste Zone", player).access_rule =\
                lambda state: state.has("Waste Ticket", player)
        multiworld.get_entrance("Greenhorn Shore -> Big Bone Bay", player).access_rule =\
                lambda state: state.has("Bone Ticket", player)
        multiworld.get_entrance("Greenhorn Shore -> Stardrop Tree", player).access_rule =\
                lambda state: state.has("Star Ticket", player)
    
    multiworld.get_location("Beach - Greenhorn Shore Chest", player).access_rule =\
            lambda state: state.has("Progressive Fishing Spot", player, 2)
    multiworld.get_location("Beach - Melonbread Cove Chest", player).access_rule =\
            lambda state: can_get_fish(state, "Rubber Duckie", player)
    multiworld.get_location("Beach - Pudding Pond Can Trade", player).access_rule =\
            lambda state: can_get_fish(state, "Empty Can", player)
    multiworld.get_location("Stardrop Tree - Shyren Pisces Trade Chest", player).access_rule =\
            lambda state: state.can_reach("Big Bone Bay - Shyren Undyne Jr Trade", "Location", player)
    multiworld.get_location("Big Bone Bay - Shyren Undyne Jr Trade", player).access_rule =\
            lambda state: state.can_reach("Chemical Waste Zone - Shyren Pagliacci Chest", "Location", player)
    multiworld.get_location("Beach - Eclaire", player).access_rule =\
            lambda state: can_get_fish(state, "Taiyaki", player)
    multiworld.get_location("Beach - Helper Mimic Cave", player).access_rule = \
                        lambda state: state.has("Joqua's Trowel", player)
        
    if options.aqariumsanity == AquariumSanity.option_true:
        for name, data in fish_data.items():
            multiworld.get_location("Aquarium - " + name, player).access_rule =\
                lambda state: can_get_fish(state, name, player)
            
    if options.shuffle_fish_mission == ShuffleFishingMissions.option_true:
        for i, name in enumerate(fish_quests):
            multiworld.get_location("Beach - Fishing Mission " + str(i + 1), player).access_rule =\
                lambda state: can_get_fish(state, name, player)
            
    multiworld.get_entrance("Beach Entry -> Miku Zone", player).access_rule =\
            lambda state: state.has("Vocal Key", player)
    
    # Toriel ------------------------------------------------------------------------------
    multiworld.get_entrance("Toriel House -> Toriel Roof", player).access_rule =\
            lambda state: state.has("Tutariel Key", player, 3)
    multiworld.get_entrance("Toriel House -> Mario Zone", player).access_rule =\
            lambda state: state.has("Red Coin", player, 8) and state.has("Decision Chosen", player)
    
    # Exit ------------------------------------------------------------------------------
    multiworld.get_entrance("Beach Post Boss -> Exit", player).access_rule =\
            lambda state: state.has("Decision Chosen", player)
    multiworld.get_location("Fake Ending", player).access_rule =\
            lambda state: state.has("Fake Passport", player)
    
    # Win Condition -----------------------------------------------------------------------
    if options.ending_goal == EndingGoal.option_fake_ending:
        multiworld.completion_condition[player] = lambda state: state.can_reach("Fake Ending", "Location", player)
    