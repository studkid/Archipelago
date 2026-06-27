from typing import List, ClassVar

from BaseClasses import Tutorial, Region, ItemClassification, CollectionState
from worlds.AutoWorld import WebWorld, World
from .Items import CarQuestItem, CarQuestItemData, item_table
from .Locations import CarQuestLocation, location_table
from .Options import CarQuestOptions
from .Regions import create_regions
from .Rules import set_rules

class CarQuestWeb(WebWorld):
    theme = "stone"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Car Quest Deluxe Randomizer on your computer.",
        "English",
        "en_CarQuest.md",
        "setup/en",
        ["studkid"]
    )]

class CarQuestWorld(World):
    """
    Car Quest Deluxe is the PC re-release of the Switch game Car Quest.  Help Sir Blocksington collect artifacts to restore his realm. 
    """
    game = "Car Quest Deluxe"
    options_dataclass = CarQuestOptions
    options: CarQuestOptions
    topology_present = False
    required_client_version = (0, 6, 0)
    web = CarQuestWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items() if data.code is not None}
    location_name_to_id = {name: data.code for name, data in location_table.items() if data.code is not None}

    def create_items(self):
        item_pool: List[CarQuestItem] = []
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))

        precollected = ["Hub: Start Room Blocker"]
        self.push_precollected(self.create_item("Hub: Start Room Blocker"))
        starting_room = ["Hub: Simple Portal Bridge Wall", "Hub: Start Room Bridge"]
        self.random.shuffle(starting_room)
        self.push_precollected(self.create_item(starting_room[0]))
        precollected.append(starting_room[0])

        for name, data in item_table.items():
            quantity = data.max_quantity

            if name in precollected:
                continue

            if data.category == "car":
                continue

            item_pool += [self.create_item(name) for _ in range(0, quantity)]

        # Fill any empty locations with filler items.
        while len(item_pool) < total_locations:
            item_pool.append(self.create_item(self.get_filler_item_name()))

        self.multiworld.itempool += item_pool

    def get_filler_item_name(self):
        return "Energy Cell"
    
    def create_item(self, name: str) -> CarQuestItem:
        data = item_table[name]
        return CarQuestItem(name, data.classification, data.code, self.player)
    
    def create_regions(self):
        create_regions(self.multiworld, self.player, self.options)

        # self.multiworld.get_location("Hub: Starting Area Artifact", self.player).place_locked_item(
        #     self.create_item("Hub: Start Room Blocker"))

        from Utils import visualize_regions
        visualize_regions(self.multiworld.get_region("Menu", self.player), "carquest_world.puml")

    def set_rules(self):
        set_rules(self)