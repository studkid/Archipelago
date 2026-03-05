from typing import NamedTuple, Dict
from BaseClasses import Location, Optional

class CarQuestLocation(Location):
    game: str = "Car Quest"

class CarQuestLocationData(NamedTuple):
    category: str
    region: str
    code: Optional[int] = None


def get_locations_by_category(category: str) -> Dict[str, CarQuestLocationData]:
    location_dict: Dict[str, CarQuestLocationData] = {}
    for name, data in location_table.items():
        if data.category == category:
            location_dict.setdefault(name, data)

    return location_dict

location_table: Dict[str, CarQuestLocationData] = {
    # Hub
    "Hub: Starting Area Artifact":               CarQuestLocationData("Artifact", "Hub Start", 1),
    "Hub: University Alleyway Artifact":         CarQuestLocationData("Artifact", "Hub Pool Area", 2),
    "Hub: North Pool Secret Door Artifact":      CarQuestLocationData("Artifact", "Hub Pool Area", 3), # Needs "Hub: North Pool Small Secret Door"
    "Hub: North Pool Jump Ramp":                 CarQuestLocationData("Artifact", "Hub Pool Area", 4), # Needs "Hub: North Pool Jump Ramp"
    "Hub: Tree Slalom Start Artifact":           CarQuestLocationData("Artifact", "Hub Pool Area", 5), # Needs "Hub: South Pool Artifact Block"
    "Hub: Upper University Alleyway Artifact":   CarQuestLocationData("Artifact", "Hub Pool Area", 6), 
    "Hub: South Pool Deadend Artifact":          CarQuestLocationData("Artifact", "Hub South Pool Deadend Path", 7), 
    "Hub: Tree Slalom Reward Artifact":          CarQuestLocationData("Artifact", "Hub Pool Area", 8), # Needs "Hub: Tree Slalom Unlock"
    "Hub: Museum Artifact":                      CarQuestLocationData("Artifact", "Hub Museum", 9),
    "Hub: Cube Monument":                        CarQuestLocationData("Artifact", "Hub Museum", 10), # Needs "Hub: Cube Monument Access"

    # Simple
    "Simple: Artifact Under Mound":               CarQuestLocationData("Artifact", "Simple Square Area", 101),
    "Simple: Artifact On Exit Ramp":              CarQuestLocationData("Artifact", "Simple Square Area", 102),

    # Cubes
    "Cubes: Artifact Behind Start":              CarQuestLocationData("Artifact", "Floating Cube Area", 111),
    "Cubes: Artifact On Exit Ramp":              CarQuestLocationData("Artifact", "Floating Cube Area", 112),
}