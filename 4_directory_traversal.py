import os
import re
import winshell
from pathlib import Path

desktop = Path(winshell.desktop())
pattern = r"\.[A-Za-z0-9]+$"
dirs = os.listdir()
dirs = [el for el in dirs if "." in el]
dirs = [el for el in sorted(dirs, key=str.casefold)]
keys_1 = set()
for el in dirs:
    keys_1.add(*re.findall(pattern, el))

coll = dict.fromkeys(keys_1)
for el in dirs:
    key = ''.join(re.findall(pattern, el))
    if coll[key] is None:
        coll[key] = [el]
    else:
        coll[key].append(el)

coll = {k: v for k, v in sorted(coll.items(), key=lambda x: x[0].lower())}
# desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
# with open(f"{desktop_path}\\report.txt", "a") as file:
with open(f"{desktop}\\report.txt", "w") as file:
    for k, val in coll.items():
        file.writelines(f"{k}\n")
        for v in val:
            file.writelines(f"- - - {v}\n")
