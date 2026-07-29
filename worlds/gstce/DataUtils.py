from .Items import item_table
from .Locations import location_table
from typing import Dict

def item_name_to_id() -> Dict[str, int]:
    return {item.name: (item.id) for _, item in enumerate(item_table)}

def location_name_to_id() -> Dict[str, int]:
    return {loc.area + ": " + loc.name: (loc.id) for _, loc in enumerate(location_table)}

def id_to_item_name() -> Dict[str, int]:
    return {item.id: (item.name) for _, item in enumerate(item_table)}

def id_to_location_name() -> Dict[int, str]:
    return {loc.id: (loc.area + ": " + loc.name) for _, loc in enumerate(location_table)}