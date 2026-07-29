from BaseClasses import CollectionState
from typing import TYPE_CHECKING

# Generic Logic
def can_bomba(state: CollectionState, player: int) -> bool:
    return state.has("Pollo Power", player) and state.has("Pollo Bomba", player)

def can_jump(state: CollectionState, player:int) -> bool:
    return state.has("Double Jump", player) or state.has("Rooster Uppercut", player) or can_fly(state, player)

def can_fly(state: CollectionState, player:int) -> bool:
    return state.has("Pollo Power", player) and state.has("Pollo Flight", player)

def can_goat_run(state: CollectionState, player: int) -> bool:
    return state.has("Goat Run") and state.has("Goat Jump")

def can_dodge(state: CollectionState, player: int, options):
    return not options.shuffle_dodge or state.has("Dodge", player)

# Zone Specific Logic
def can_climb_forest(state:CollectionState, player: int, options): # NOTE: Does not account for using pollo flight
    return (state.has("Dimension Swap", player) and can_jump(state, player)) or can_climb_jagged_walls(state, player, options)

def can_kill_xtabay(state: CollectionState, player: int) -> bool:
    return state.has("Frog Slam") and state.has("Rooster Uppercut") and state.has("Olmec Headbutt") and \
           (can_fly(state, player) or (state.has("Goat Jump")))

#Obscure Logic
def can_climb_jagged_walls(state: CollectionState, player: int, options):
    return options.obscure_logic and can_goat_run(state, player) and ((state.has("Double Jump", player) and state.has("Rooster Uppercut", player)) \
           or (can_jump(state, player) and (state.has("Olmec Headbutt", player) or state.has("Dashing Derp Derp", player))))

def set_rules(self, player: int):
    options = self.options

    # Misc
    self.get_location("AF: Juan House Chest").access_rule = \
        lambda state: can_bomba(state, player)
    self.get_location("ChacMool: Agave Field Orb").access_rule = \
        lambda state: state.has("Pollo Power", player) and state.has("Dimension Swap", player)
    self.get_location("LmdP: Plaform Chest",).access_rule = \
        lambda state: can_jump(state, player)
    
    # Peublucho
    self.get_location("Pb: Oustide Church Chest").access_rule = \
        lambda state: (can_jump(state, player) and self.options.obscure_logic) or state.has("Rooster Uppercut", player) or can_fly(state, player)
    self.get_location("Pb: Pollo Chest").access_rule = \
        lambda state: state.has("Pollo Power", player)
    self.get_location("Pb: X'tabay Chest").access_rule = \
        lambda state: state.has("Frog Slam", player) and (state.has("Goat Jump", player) and \
                      (state.has("Dashing Derp Derp", player) or can_jump(state, player)) or can_fly())
    self.get_location("Pb: Inside Church Chest").access_rule = \
        lambda state: (can_jump(state, player) and state.has("Goat Jump", player)) or can_fly(state, player) or can_goat_run(state, player)
    
    # Forest del Chivo
    self.get_location("FdC: Near Peubluch Chest").access_rule = \
        lambda state: state.has("Frog Slam", player)
    ## Add logic so dropping down to these checks in logical 
    self.get_location("FdC: Main Shaft Green Challenge Chest").access_rule = \
        lambda state: state.has("Frog Slam", player) and state.has("Rooster Uppercut", player) and can_dodge(state, player, options) and can_climb_forest(state, player, options) 
    self.get_location("FdC: Main Shaft Red Challenge Chest").access_rule = \
        lambda state: (state.has("Rooster Uppercut", player) or can_goat_run(state, player)) and (can_climb_forest(state, player, options) or \
                      (options.obscure_logic and state.has("Pollo Flight", player)))
    self.get_location("FdC: Main Shaft Yellow Challenge Chest").access_rule = \
        lambda state: state.has("Olmec Headbutt", player) and (can_climb_forest(state, player, options) or state.has("Pollo Flight", player))
    self.get_location("FdC: Main Shaft Blue Challenge Chest").access_rule = \
        lambda state: state.has("Dashing Derp Derp", player) and can_dodge(state, player, options) and (can_climb_forest(state, player, options) or \
                      (options.obscure_logic and state.has("Pollo Flight", player)))