from .items import RoR1Item, item_table, map_offset
from .locations import RoR1Location, item_pickups, get_locations, map_orderedstages_table, map_table, shift_by_offset
from .options import ROROptions, ror_option_groups
from .rules import set_rules
from .regions import create_grouped_regions

from worlds.AutoWorld import World, WebWorld
from BaseClasses import Item, ItemClassification, Tutorial
from typing import List, Dict, Any

class RiskOfWeb(WebWorld):
    tutorials = [Tutorial(
        "Risk of Rain 2013 Setup Guide",
        "A guide to setting up the Risk of Rain 1 integration for Archipelago multiworld games.",
        "English",
        "setup_RoR1_en.md",
        "setup/en",
        ["studkid"]
    ),
    Tutorial(
        "Risk of Rain Returns Setup Guide",
        "A guide to setting up the Risk of Rain Returns integration for Archipelago multiworld games.",
        "English",
        "setup_RoRR_en.md",
        "setup/en",
        ["studkid"]
    )]

    option_groups = ror_option_groups

class RoR1World(World):
    game = "Risk of Rain"
    web = RiskOfWeb()
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
    required_client_version = (0, 6, 7)

    fragAmount = 0
    requiredFragAmount = 0

    def create_regions(self) -> None:
        create_grouped_regions(self)

        self.create_events()

    def create_items(self) -> None:
        maps_pool = {}

        if self.options.grouping == "map":
            maps_pool = shift_by_offset(map_table, map_offset)
            unlock = self.random.choices(list(map_orderedstages_table[0].keys()), k=1)
            self.multiworld.push_precollected(self.create_item(unlock[0]))
            maps_pool.pop(unlock[0])
            if not self.options.require_stage:
                self.multiworld.push_precollected(self.create_item("Stage 2"))
                self.multiworld.push_precollected(self.create_item("Stage 3"))
                self.multiworld.push_precollected(self.create_item("Stage 4"))
                self.multiworld.push_precollected(self.create_item("Stage 5"))
        
        itempool: List[str] = []

        for map_name, _ in maps_pool.items():
            itempool += [map_name]

        if self.options.require_stage:
            if not self.options.progressive_stages:
                itempool += ["Stage 2", "Stage 3", "Stage 4", "Stage 5"]
            else:
                itempool += ["Progressive Stage"] * 4

                
            total_locations = len(
                get_locations(
                    chests=self.options.total_pickups.value,
                )
            )

        if self.options.required_frags.value > 0 and self.options.available_frags.value > 0:
            fillerSize = total_locations - len(itempool)
            self.fragAmount = round(fillerSize * (self.options.available_frags.value / 100))
            self.requiredFragAmount = round(self.fragAmount * (self.options.required_frags.value / 100))
            itempool += ["Teleporter Fragment"] * self.fragAmount
            
        trapWeights = self.options.trap_weights
        itemWeights = self.options.item_weights
        print(trapWeights.values())
        traps = self.random.choices([trap for trap in trapWeights.keys()], [weight for weight in trapWeights.values()], 
                                    k = round((total_locations - len(itempool)) / self.options.trap_percentage.value))
        itempool.extend(traps)
        filler = self.random.choices([trap for trap in itemWeights.keys()], [weight for weight in itemWeights.values()], k = total_locations - len(itempool))
        itempool.extend(filler)

        self.multiworld.itempool += map(self.create_item, itempool)

    def get_filler_item_name(self):
        return self.random.choices([filler for filler in self.options.item_weights.keys()], [weight for weight in self.options.item_weights.values()], k=1)[0]

    def create_item(self, name: str) -> Item:
        data = item_table[name]
        return RoR1Item(name, data.item_type, data.code, self.player)
    
    def set_rules(self) -> None:
        set_rules(self)
    
    def fill_slot_data(self) -> Dict[str, Any]:
        options_dict = self.options.as_dict("grouping", "total_pickups", "item_pickup_step",
                                            "stage_five_tp", "strict_stage_prog", "progressive_stages", casing="camel")
        options_dict["requiredFrags"] = self.requiredFragAmount
        return {
            **options_dict,
        }
    
    def create_events(self) -> None:
        world_region = self.multiworld.get_region("Risk of Rain", self.player)
        victory_event = RoR1Location(self.player, "Victory", None, world_region)
        victory_event.place_locked_item(RoR1Item("Victory", ItemClassification.progression, None, self.player))
        world_region.locations.append(victory_event)