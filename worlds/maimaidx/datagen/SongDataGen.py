from urllib import request
from typing import List, Dict
import json, re

songList: Dict[str, Dict[str, any]] = {}

with request.urlopen("https://dp4p6x0xfi5o9.cloudfront.net/maimai/data.json") as url:
    data = json.loads(url.read().decode())

    with open("worlds/maimaidx/datagen/SongData.py", "w") as file:
        file.write("from typing import Dict\n")
        file.write("from ..items import SongData\n\n")
        file.write("SONG_DATA: Dict[str, SongData] = {\n")
        id_offset = 0

        for i, song in enumerate(data["songs"]):
            title = re.sub("\"", "'",song["title"])
            id = re.sub("\"", "'",song["songId"])
            version = song["version"]
            cat = song["category"]
            std_difficulties: List[int] = []
            dx_difficulties: List[int] = []
            regions: List[str] = []

            if cat == "宴会場": continue

            for diff in song["sheets"]:
                if diff["type"] != "std": 
                    std_difficulties.append(diff["internalLevelValue"])
                
                if diff["type"] != "dx": 
                    dx_difficulties.append(diff["internalLevelValue"])

            if len(std_difficulties) < 5:
                std_difficulties.append(None)

            if len(dx_difficulties) < 5:
                dx_difficulties.append(None)
            
            if song["sheets"][0]["regions"]["jp"]:
                regions.append("jp")
            
            if song["sheets"][0]["regions"]["intl"]:
                regions.append('intl')
            
            if song["sheets"][0]["regions"]["usa"]:
                regions.append('usa')

            if song["sheets"][0]["regions"]["cn"]:
                regions.append('cn')

            if len(std_difficulties) == 5:
                if len(dx_difficulties) == 5:
                    file.write(f"    \"{title} (std)\":  SongData({i + 1 + id_offset}, \"{title}\", \"{version}\", \"{cat}\", \"std\", {regions}, {std_difficulties}),\n")
                    id_offset = id_offset + 1
                    file.write(f"    \"{title} (dx)\":  SongData({i + 1 + id_offset}, \"{title}\", \"{version}\", \"{cat}\", \"dx\", {regions}, {dx_difficulties}),\n")
                    
                    songInfoStd = {
                        "version": version,
                        "category": cat,
                        "regions": regions,
                        "difficulties": std_difficulties,
                    }
                    songInfoDx = {
                        "version": version,
                        "category": cat,
                        "regions": regions,
                        "difficulties": dx_difficulties,
                    }
                    songList[f"{title} (std)"] = songInfoStd
                    songList[f"{title} (dx)"] = songInfoDx
                    continue
                    
                else:
                    file.write(f"    \"{title}\":  SongData({i + 1 + id_offset}, \"{title}\", \"{version}\", \"{cat}\", \"std\", {regions}, {std_difficulties}),\n")
                    songInfo = {
                        "version": version,
                        "category": cat,
                        "regions": regions,
                        "difficulties": std_difficulties,
                    }
                    songList[title] = songInfo

            if len(dx_difficulties) == 5:
                file.write(f"    \"{title}\":  SongData({i + 1 + id_offset}, \"{title}\", \"{version}\", \"{cat}\", \"dx\", {regions}, {dx_difficulties}),\n")
                songInfo = {
                    "version": version,
                    "category": cat,
                    "regions": regions,
                    "difficulties": dx_difficulties,
                }
                songList[title] = songInfo

            
        file.write("}")

        file.write("\n\ngroups = {\n")
        for ver in data["versions"]:
            file.write(f"    \"{ver["version"]}\": {{name for name, data, in SONG_DATA.items() if data.version == \"{ver["version"]}\"}},\n")
        
        for cat in data["categories"]:
            file.write(f"    \"{cat["category"]}\": {{name for name, data, in SONG_DATA.items() if data.category == \"{cat["category"]}\"}},\n")

        file.write(f"    \"std\": {{name for name, data, in SONG_DATA.items() if data.type == \"std\"}},\n")
        file.write(f"    \"dx\": {{name for name, data, in SONG_DATA.items() if data.type == \"dx\"}},\n")
        file.write("}")

with open("worlds/maimaidx/datagen/maiSongData.json", "w") as file:
    file.write(json.dumps(songList))