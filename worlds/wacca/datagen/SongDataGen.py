from typing import List, Dict
import json, re

songList: Dict[str, Dict[str, any]] = {}
data = "";
waccaVer: Dict[int, str] = {
    100: "WACCA",
    150: "WACCA S",
    200: "LILY",
    250: "LILY R",
    300: "REVERSE",
    400: "PLUS",
}
categories: List[str] = []

with open("worlds/wacca/datagen/rawWaccaSongData.json", "r") as jsonData:
    data = json.load(jsonData)

    with open("worlds/wacca/datagen/SongData.py", "w") as file:
        file.write("from typing import Dict\n")
        file.write("from ..items import SongData\n\n")
        file.write("SONG_DATA: Dict[str, SongData] = {\n")

        for i, song in enumerate(data):
            title = re.sub("\"", "'",song["title"])
            id = song["id"]
            version = waccaVer[song["gameVersion"]]
            cat = song["category"]
            difficulties: List[int] = []

            for diff in song["sheets"]:
                difficulties.append(diff["difficulty"])

            if len(difficulties) < 5:
                difficulties.append(None)
        
            file.write(f"    \"{title}\":  SongData({i + 10}, \"{title}\", \"{version}\", \"{cat}\", {difficulties}),\n")
            songInfo = {
                "version": version,
                "category": cat,
                "difficulties": difficulties,
            }
            songList[title] = songInfo

            if(not cat in categories):
                categories.append(cat)

        file.write("}")

        file.write("\n\ngroups = {\n")
        for ver in waccaVer.values():
            file.write(f"    \"{ver}\": {{name for name, data, in SONG_DATA.items() if data.version == \"{ver}\"}},\n")
        
        for cat in categories:
            file.write(f"    \"{cat}\": {{name for name, data, in SONG_DATA.items() if data.category == \"{cat}\"}},\n")
        file.write("}")

with open("worlds/wacca/datagen/waccaSongData.json", "w") as file:
    file.write(json.dumps(songList))