from test.bases import WorldTestBase
from .. import MaiWorld
from typing import cast

class RotNTestBase(WorldTestBase):
    game = "Rift of the Necrodancer"

    def get_world(self) -> MaiWorld:
        return cast(MaiWorld, self.multiworld.worlds[1])