from typing import NamedTuple, Optional, List
from BaseClasses import Item, ItemClassification

class SongData(NamedTuple):
    code: Optional[int]
    song_id: str
    version: str
    category: str
    region: List[str]
    difficulties: List[int]

class ChuniSongItem(Item):
    game: str = "Chunithm"

    def __init__(self, name: str, player: int, data: SongData) -> None:
        super().__init__(name, ItemClassification.progression, data.code, player)

class ChuniFixedItem(Item):
    game: str = "Chunithm"

    def __init__(self, name: str, classification: ItemClassification, code: Optional[int], player: int) -> None:
        super().__init__(name, classification, code, player)