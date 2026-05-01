from urllib import request
from typing import List, Dict
import json, re

songList: Dict[str, Dict[str, any]] = {}

with request.urlopen("https://dp4p6x0xfi5o9.cloudfront.net/chunithm/data.json") as url:
    data = json.loads(url.read().decode())

    with open("worlds/chunithm/datagen/SongData.py", "w") as file:
        file.write("from typing import Dict\n")
        file.write("from ..items import SongData\n\n")
        file.write("SONG_DATA: Dict[str, SongData] = {\n")

        for i, song in enumerate(data["songs"]):
            title = re.sub("\"", "'",song["title"])
            id = re.sub("\"", "'",song["songId"])
            version = song["version"]
            cat = song["category"]
            difficulties: List[int] = []
            regions: List[str] = []

            if cat == "WORLD'S END": continue

            for diff in song["sheets"]:
                if diff["type"] != "std": continue
                
                difficulties.append(diff["internalLevelValue"])

            if len(difficulties) < 5:
                difficulties.append(None)
            
            if song["sheets"][0]["regions"]["jp"]:
                regions.append("jp")
            
            if song["sheets"][0]["regions"]["intl"]:
                regions.append('intl')

            file.write(f"    \"{title}\":  SongData({i + 10}, \"{title}\", \"{version}\", \"{cat}\", {regions}, {difficulties}),\n")
            songInfo = {
                "version": version,
                "category": cat,
                "regions": regions,
                "difficulties": difficulties,
            }
            songList[title] = songInfo

        file.write("}")

        file.write("\n\ngroups = {\n")
        for ver in data["versions"]:
            file.write(f"    \"{ver["version"]}\": {{name for name, data, in SONG_DATA.items() if data.version == \"{ver["version"]}\"}},\n")
        
        for cat in data["categories"]:
            file.write(f"    \"{cat["category"]}\": {{name for name, data, in SONG_DATA.items() if data.category == \"{cat["category"]}\"}},\n")
        file.write("}")

with open("worlds/chunithm/datagen/chuniSongData.json", "w") as file:
    file.write(json.dumps(songList))