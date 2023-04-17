import os, json, re
from collections import defaultdict


path = r"D:\Downloads\SS"

# default_value = {"name": "", "desc": "", "added": False}

d = []

for i in range(1,145):
    d.append({"number": i, "name": f"Episode {i}", "desc": "Shrimaan Shrimati, a famous sitcom by Adhikari Brothers, reflects the notion of loving one's neighbor's wife.", "added": False})

print(d)

def get_description(filepath):
    with open(filepath, "r") as fi:
        tet = fi.read()
        # print(tet)
        return tet.split("SUBSCRIBE")[0].split("Click")[0].strip()


for filename in os.listdir(path):
    print(filename)
    if filename.lower().endswith(".txt"):
        epno = int(re.findall("Shrimaan Shrimati.*\s+(\d+)", filename)[0])
        print(epno)
        d[epno-1]["desc"] = get_description(os.path.join(path, filename))

epfi = "SS_epinfo.json"

with open(epfi, "w") as fu:
    fu.write(json.dumps(d, indent=3))
