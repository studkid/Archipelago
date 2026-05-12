from worlds.generic.Rules import set_rule
from worlds.AutoWorld import World
from .locations import get_locations, map_orderedstages_table
from .options import Grouping
from rule_builder.rules import Has, HasAnyCount, OptionFilter, CanReachRegion, HasAllCounts

# Rule to see if it has access to the previous stage
def has_entrance_access_rule(world: World, stage: int, player: int) -> None:
    rule = HasAnyCount({f"Stage {stage + 1}": 1, "Progressive Stage": stage})
    for entrance in world.multiworld.get_region(f"OrderedStage_{stage+1}", player).entrances:
        world.set_rule(entrance, rule)

def has_stage_access_rule(world: World, stage: str, amount: int, region: str, player: int) -> None:
    rule = Has(region)
    for entrance in world.multiworld.get_region(region, player).entrances:
        world.set_rule(entrance, rule)

# Checks to see if chest/shrine are accessible
# def has_location_access_rule(world: World, map: str, player: int, item_number: int, item_type: str)\
#         -> None:
#     if item_number == 1:
#         multiworld.get_location(f"{map}: {item_type} {item_number}", player).access_rule = \
#             lambda state: state.has(map, player)
#     else:
#         multiworld.get_location(f"{map}: {item_type} {item_number}", player).access_rule = \
#             lambda state: check_location(state, map, player, item_number, item_type)

def check_location(state, map: str, player: int, item_number: int, item_name: str) -> bool:
    return state.can_reach(f"{map}: {item_name} {item_number - 1}", "Location", player)

def set_rules(self: World) -> None:
    player = self.player
    multiworld = self.multiworld
    ror_options = self.options
    if ror_options.grouping == "universal":
        # classic mode
        total_locations = ror_options.total_locations.value  # total locations for current player
    else:
        # explore mode
        total_locations = len(
            get_locations(
                chests=ror_options.total_locations.value,
            )
        )

    event_location_step = 25  # set an event location at these locations for "spheres"
    divisions = total_locations // event_location_step

    if ror_options.grouping == "universal":
        # universal mode
        if divisions:
            for i in range(1, divisions + 1):  # since divisions is the floor of total_locations / 25
                if i * event_location_step != total_locations:
                    event_loc = multiworld.get_location(f"Pickup{i * event_location_step}", player)
                    set_rule(event_loc,
                             lambda state, i=i: state.can_reach(f"ItemPickup{i * event_location_step - 1}",
                                                                "Location", player))
                    # we want to create a rule for each of the 25 locations per division
                for n in range(i * event_location_step, (i + 1) * event_location_step + 1):
                    if n > total_locations:
                        break
                    if n == i * event_location_step:
                        set_rule(multiworld.get_location(f"ItemPickup{n}", player),
                                 lambda state, event_item=event_loc.item.name: state.has(event_item, player))
                    else:
                        set_rule(multiworld.get_location(f"ItemPickup{n}", player),
                                 lambda state, n=n: state.can_reach(f"ItemPickup{n - 1}", "Location", player))
        set_rule(multiworld.get_location("Victory", player),
                 lambda state: state.can_reach(f"ItemPickup{total_locations}", "Location", player))

    else:
        # map mode
        chests = ror_options.total_locations

        for i in range(len(map_orderedstages_table)):
            if i > 0:
                has_entrance_access_rule(self, i, player)
            if ror_options.grouping == "map":
                for map_name, _ in map_orderedstages_table[i].items():
                    has_stage_access_rule(self, f"Stage {i + 1}", i, map_name, player)

        stageSixRule = Has("Teleporter Fragment", count=self.requiredFragAmount) & \
                       Has("Risk of Rain", options=[OptionFilter(Grouping, Grouping.option_map)], filtered_resolution=True)
        self.set_rule(multiworld.get_entrance("OrderedStage_6 -> Risk of Rain", player), stageSixRule)

    # Win Condition
    self.set_completion_rule(Has("Victory"))