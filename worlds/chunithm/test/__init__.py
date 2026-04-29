from test.bases import WorldTestBase
from .. import ChuniWorld
from typing import cast

class RotNTestBase(WorldTestBase):
    game = "Rift of the Necrodancer"

    def get_world(self) -> ChuniWorld:
        return cast(ChuniWorld, self.multiworld.worlds[1])