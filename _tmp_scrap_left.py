from pathlib import Path
import re

samples = []
count = 0
for p in Path(".").rglob("*.html"):
    if ".git" in p.parts:
        continue
    t = p.read_text(encoding="utf-8", errors="ignore")
    if "-investments-group" not in t:
        continue
    count += 1
    if len(samples) < 5:
        for m in re.finditer(r".{0,60}-investments-group.{0,60}", t):
            samples.append((str(p), m.group(0).replace("\n", " ")[:140]))
            break
print("files", count)
for s in samples:
    print(s)
