from typing import Dict, List, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Region, Entrance, MultiWorld
from .locations import location_table, RoR1Location, get_item_pickups

if TYPE_CHECKING:
    from . import RoR1World

class RoR1RegionData(NamedTuple):
    locations: Optional[List[str]]
    region_exits: Optional[List[str]]

def create_classic_regions(ror_world: "RoR1World") -> None:
    player = ror_world.player
    ror_options = ror_world.options
    multiworld = ror_world.multiworld

    menu = create_classic_region(multiworld, player, "Menu")
    multiworld.regions.append(menu)

    victory_region = create_classic_region(multiworld, player, "Victory")
    multiworld.regions.append(victory_region)
    contactLight = create_classic_region(multiworld, player, "Contact Light",
                                      get_item_pickups(ror_options.total_locations.value))
    multiworld.regions.append(contactLight)

    # classic mode can get to victory from the beginning of the game
    to_victory = Entrance(player, "beating game", contactLight)
    contactLight.exits.append(to_victory)
    to_victory.connect(victory_region)

    connection = Entrance(player, "Menu", menu)
    menu.exits.append(connection)
    connection.connect(contactLight)

def create_classic_region(multiworld: MultiWorld, player: int, name: str, locations: Dict[str, int] = {}) -> Region:
    ret = Region(name, player, multiworld)
    for location_name, location_id in locations.items():
        ret.locations.append(RoR1Location(player, location_name, location_id, ret))
    return ret