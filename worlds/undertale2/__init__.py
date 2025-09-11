from typing import List

from BaseClasses import Tutorial, Region
from worlds.AutoWorld import WebWorld, World
from .Items import UT2Item, UT2ItemData, event_item_table, get_items_by_category, item_table
from .Locations import UT2Location, location_table
from .Options import UT2Options
from .Regions import create_regions
# from .Rules import set_rules


class UT2Web(WebWorld):
    theme = "stone"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Undertale 2 Randomizer on your computer.",
        "English",
        "",
        "",
        ["studkid"]
    )]

class UT2World(World):
    """
    
    """
    game = "Undertale 2"
    options_dataclass = UT2Options
    options: UT2Options
    topology_present = True
    required_client_version = (0, 5, 0)
    web = UT2Web()

    item_name_to_id = {name: data.code for name, data in item_table.items() if data.code is not None}
    location_name_to_id = {name: data.code for name, data in location_table.items() if data.code is not None}

    # def fill_slot_data(self) -> dict:
    #     return self.options.as_dict(*[name for name in self.options_dataclass.type_hints.keys()])

    def create_items(self):
        item_pool: List[UT2Item] = []
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        for name, data in item_table.items():
            quantity = data.max_quantity

            # Ignore filler, it will be added in a later stage.
            if data.category == "Filler":
                continue

            if data.category == "key" and self.options.progressive_monkkey == 1:
                continue
            elif data.category == "progkey" and self.options.progressive_monkkey != 1:
                continue

            item_pool += [self.create_item(name) for _ in range(0, quantity)]

        # Fill any empty locations with filler items.
        while len(item_pool) < total_locations:
            item_pool.append(self.create_item(self.get_filler_item_name()))

        self.multiworld.itempool += item_pool

    def get_filler_item_name(self) -> str:
        fillers = get_items_by_category("filler")
        weights = [data.weight for data in fillers.values()]
        return self.random.choices([filler for filler in fillers.keys()], weights, k=1)[0]

    def create_item(self, name: str) -> UT2Item:
        data = item_table[name]
        return UT2Item(name, data.classification, data.code, self.player)

    def create_event(self, name: str) -> UT2Item:
        data = event_item_table[name]
        return UT2Item(name, data.classification, data.code, self.player)

    # def set_rules(self):
    #     set_rules(self, self.player)

    def create_regions(self):
        create_regions(self.multiworld, self.player, self.options)
        from Utils import visualize_regions
        visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml")
        # self._place_events()

    # def _place_events(self):
    #     # Fountain
    #     self.multiworld.get_location("Fountain Room", self.player).place_locked_item(
    #         self.create_event("Defeat The Fountain"))

    #     # Khidr / Neo Khidr
    #     if self.options.khidr == "vanilla":
    #         self.multiworld.get_location("Castle Hamson Boss Room", self.player).place_locked_item(
    #             self.create_event("Defeat Khidr"))
    #     else:
    #         self.multiworld.get_location("Castle Hamson Boss Room", self.player).place_locked_item(
    #             self.create_event("Defeat Neo Khidr"))

    #     # Alexander / Alexander IV
    #     if self.options.alexander == "vanilla":
    #         self.multiworld.get_location("Forest Abkhazia Boss Room", self.player).place_locked_item(
    #             self.create_event("Defeat Alexander"))
    #     else:
    #         self.multiworld.get_location("Forest Abkhazia Boss Room", self.player).place_locked_item(
    #             self.create_event("Defeat Alexander IV"))

    #     # Ponce de Leon / Ponce de Freon
    #     if self.options.leon == "vanilla":
    #         self.multiworld.get_location("The Maya Boss Room", self.player).place_locked_item(
    #             self.create_event("Defeat Ponce de Leon"))
    #     else:
    #         self.multiworld.get_location("The Maya Boss Room", self.player).place_locked_item(
    #             self.create_event("Defeat Ponce de Freon"))

    #     # Herodotus / Astrodotus
    #     if self.options.herodotus == "vanilla":
    #         self.multiworld.get_location("Land of Darkness Boss Room", self.player).place_locked_item(
    #             self.create_event("Defeat Herodotus"))
    #     else:
    #         self.multiworld.get_location("Land of Darkness Boss Room", self.player).place_locked_item(
    #             self.create_event("Defeat Astrodotus"))
