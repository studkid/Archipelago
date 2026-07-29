from typing import Dict, List, NamedTuple, Optional, TYPE_CHECKING
from .Locations import location_table, GuacLocation
from BaseClasses import Region, Entrance, MultiWorld

class GuacRegionData(NamedTuple):
    locations: Optional[List[GuacLocation]]
    exits: Optional[List[str]]

def create_regions(self) -> None:
    regions: Dict[str, GuacRegionData] = {
        #Misc
        "Menu":                                     GuacRegionData(None, ["Peublucho"]),
        "Peublucho":                                GuacRegionData([], ["Mansion", "Agave Field", "Forest Upper Left"]),
        "Mansion":                                  GuacRegionData([], ["Peublucho"]),
        "Agave Field":                              GuacRegionData([], ["Peublucho"]),

        # Forest del Chivo
        "Forest Upper Left":                        GuacRegionData([], ["Peublucho", "Forest Shaft"]),
        "Forest Shaft":                             GuacRegionData([], ["Forest Upper Right", "Forest Upper Left", "Forest Bottom", "Forest Choozo"]),
        "Forest Upper Right":                       GuacRegionData([], ["Forest Shaft", "Forest Choozo"]),
        "Forest Bottom":                            GuacRegionData([], ["Forest Shaft", "Tule Tree"]),
        "Forest Choozo":                            GuacRegionData([], ["Forest Shaft", "Forest Bottom", "Forest Upper Right"]),

        "Temple of Rain":                           GuacRegionData([], ["Santa Luchita"]),
        "Tule Tree":                                GuacRegionData([], ["Forest Bottom", "Desierto Caliente"]),
        "Sierra Morena":                            GuacRegionData([], ["Santa Luchita", "Pico de Gallo", "Great Temple"]),
        "Great Temple":                             GuacRegionData([], ["Sierra Morena"]),
        "Temple of War":                            GuacRegionData([], ["Desierto Caliente"]),
        "Caverna del Pollo":                        GuacRegionData([], ["Santa Luchita"]),
        "Santa Luchita":                            GuacRegionData([], ["Forest Upper Right", "Temple of Rain", "Sierra Morena", "Desierto Caliente", "Caverna del Pollo", "El Infierno"]),
        "Canal":                                    GuacRegionData([], ["Forest Shaft", "Pico de Gallo"]),
        "Pico de Gallo":                            GuacRegionData([], ["Desierto Caliente", "Canal"]),
        "Desierto Caliente":                        GuacRegionData([], ["Santa Luchita", "Pico de Gallo", "Temple of War"]),
        "El Infierno":                              GuacRegionData([], ["Santa Luchita"]),
    }

    for key in location_table:
        if key.type == "orb" and not self.options.shuffle_orbs:
            continue

        regions[key.region].locations.append(key)

    for name, data in regions.items():
        self.multiworld.regions.append(create_region(self.multiworld, self.player, name, data))

    for name, data, in regions.items():
        create_connections_in_regions(self.multiworld, self.player, name, data)
    
def create_region(multiworld: MultiWorld, player: int, name: str, data: GuacRegionData):
    region = Region(name, player, multiworld)
    print(name)
    if data.locations:
        for loc in data.locations:
            print(loc.name)
            location = GuacLocation(player, f"{loc.area}: {loc.name}", loc.id if loc else None, region)
            region.locations.append(location)

    # if data.exits:
    #     for exit in data.exits:
    #         entrance = Entrance(player, exit, region)
    #         region.exits.append(entrance)

    return region

def create_connections_in_regions(multiworld: MultiWorld, player: int, name: str, data: GuacRegionData):
    region = multiworld.get_region(name, player)
    if data.exits:
        region.add_exits(data.exits)