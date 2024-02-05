# Most of this AP World is ripped 1:1 from RoR2's AP World

import string

from .items import RoR1Item, default_weights, item_table, offset
from .locations import RoR1Location, item_pickups, get_locations, map_orderedstages_table
from .options import ROROptions
from .regions import create_classic_regions

from worlds.AutoWorld import World, WebWorld
from BaseClasses import Item, ItemClassification, Tutorial
from typing import List, Dict, Any

class RiskOfWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Risk of Rain 1 integration for Archipelago multiworld games.",
        "English",
        "setup_en.md",
        "setup/en",
        ["studkid"]
    )]

class RoR1World(World):
    game = "Risk of Rain"
    options_dataclass = ROROptions
    options: ROROptions
    topology_present = False
    item_name_to_id = {name: data.code for name, data in item_table.items()}
    item_name_groups = {
        "Stages": {name for name, data in item_table.items() if data.category == "Stage"},
        "Maps": {name for name, data in item_table.items() if data.category == "Maps"},
        "Upgrades": {name for name, data in item_table.items() if data.category == "Upgrade"},
        "Fillers": {name for name, data in item_table.items() if data.category == "Filler"},
        "Traps": {name for name, data in item_table.items() if data.category == "Trap"},
    }
    location_name_to_id = item_pickups

    data_version = 8
    required_client_version = (0, 4, 4)

    def create_regions(self) -> None:
        create_classic_regions(self)
        self.create_events()

    def create_items(self) -> None:
        maps_pool = {}

        # unlock = self.random.choices(list(map_orderedstages_table[0].keys()), k=1)
        # self.multiworld.push_precollected(self.create_item(unlock[0]))
        # maps_pool.pop(unlock[0])
        
        itempool: List[str] = []

        for map_name, _ in maps_pool.items():
            itempool += [map_name]
        
        if self.options.goal == "classic":
            total_locations = self.options.total_locations.value
        
        junk_pool = self.create_junk_pool()
        filler = self.random.choices(*zip(*junk_pool.items()), k = total_locations - len(itempool))
        itempool.extend(filler)

        self.multiworld.itempool += map(self.create_item, itempool)

    def create_junk_pool(self) -> Dict[str, int]:
        # if presets are enabled generate junk_pool from the selected preset
        junk_pool: Dict[str, int] = {}
        junk_pool = {
            "Common Item": self.options.common_item.value,
            "Uncommon Item": self.options.uncommon_item.value,
            "Legendary Item": self.options.legendary_item.value,
            "Boss Item": self.options.boss_item.value,
            "Equipment": self.options.equipment.value,
            "Money": self.options.money.value,
            "1000 Exp": self.options.experience.value,
            "Time Warp Trap": self.options.time_warp_trap.value,
            "Combat Trap": self.options.combat_trap.value,
            "Meteor Trap": self.options.meteor_trap.value,
        }

        if not self.options.enable_trap:
            junk_pool.pop("Time Warp Trap")
            junk_pool.pop("Combat Trap")
            junk_pool.pop("Meteor Trap")

        return junk_pool

    def create_item(self, name: str) -> Item:
        data = item_table[name]
        return RoR1Item(name, data.item_type, data.code, self.player)
    
    def fill_slot_data(self) -> Dict[str, Any]:
        options_dict = self.options.as_dict("item_pickup_step", "goal", "total_locations", casing="camel")
        return {
            **options_dict,
            "seed": "".join(self.random.choice(string.digits) for _ in range(16)),
            "offset": offset
        }
    
    def create_events(self) -> None:
        total_locations = self.options.total_locations.value
        num_of_events = total_locations // 25
        if total_locations / 25 == num_of_events:
            num_of_events -= 1
        world_region = self.multiworld.get_region("Contact Light", self.player)
        if self.options.goal == "classic":
            # classic mode
            # only setup Pickups when using classic_mode
            for i in range(num_of_events):
                event_loc = RoR1Location(self.player, f"Pickup{(i + 1) * 25}", None, world_region)
                event_loc.place_locked_item(
                    RoR1Item(f"Pickup{(i + 1) * 25}", ItemClassification.progression, None,
                                   self.player))
                event_loc.access_rule = \
                    lambda state, i=i: state.can_reach(f"ItemPickup{((i + 1) * 25) - 1}", "Location", self.player)
                world_region.locations.append(event_loc)
        else:
            # explore mode
            event_region = self.multiworld.get_region("OrderedStage_5", self.player)
            event_loc = RoR1Location(self.player, "Stage 5", None, event_region)
            event_loc.place_locked_item(RoR1Item("Stage 5", ItemClassification.progression, None, self.player))
            event_loc.show_in_spoiler = False
            event_region.locations.append(event_loc)
            event_loc.access_rule = lambda state: state.has("Sky Meadow", self.player)

        victory_region = self.multiworld.get_region("Victory", self.player)
        victory_event = RoR1Location(self.player, "Victory", None, victory_region)
        victory_event.place_locked_item(RoR1Item("Victory", ItemClassification.progression, None, self.player))
        victory_region.locations.append(victory_event)