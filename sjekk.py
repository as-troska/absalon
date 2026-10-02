#!/usr/bin/env python3
"""Sjekkar postane i index.html: gyldig JS, sitat mot dagboka og avstand mellom postar.

Køyr: python3 sjekk.py   (krev node, og kjelder/dagbok.txt for sitatsjekken)
"""
import json, math, os, re, subprocess, sys, tempfile

RADIUS = 50
src = open("index.html", encoding="utf-8").read()
norm = lambda s: re.sub(r"\s+", " ", s).strip()
feil = 0

# 1. JS-syntaks og postdata via node
js = "\n".join(re.findall(r"<script>(.*?)</script>", src, re.S))
with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
    f.write(js)
if subprocess.run(["node", "--check", f.name]).returncode:
    sys.exit("FEIL: JavaScript-syntaks")
os.unlink(f.name)
arr = re.search(r"const POSTS = (\[[\s\S]*?\n\]);", src).group(1)
posts = json.loads(subprocess.check_output(["node", "-e", f"console.log(JSON.stringify({arr}))"]))
print(f"{len(posts)} postar: {' '.join(p['id'] for p in posts)}")

# 2. Felt som må vere med
for p in posts:
    for k in ["id", "name", "lat", "lon", "title", "intro", "orig", "modern", "date", "gloss", "task"]:
        if k not in p:
            print(f"FEIL {p.get('id')}: manglar {k}"); feil += 1
    if p.get("img") and not os.path.exists(f"bilete/{p['img'][1]}"):
        print(f"FEIL {p['id']}: finst ikkje bilete/{p['img'][1]}"); feil += 1

# 3. Sitat mot dagboka (utdrag skilde med (…); punktum kan vere lagt til mellom setningar)
if os.path.exists("kjelder/dagbok.txt"):
    d = norm(open("kjelder/dagbok.txt", encoding="utf-8").read())
    for p in posts:
        tekstar = [p["orig"]] + ([p["task"]["read"]] if p["task"].get("read") else [])
        for t in tekstar:
            for bit in re.split(r"\(…\)|(?<=\.) (?=[A-ZÆØÅW])", norm(t)):
                bit = bit.strip().rstrip(".,")
                if bit and bit not in d:
                    print(f"AVVIK {p['id']}: «{bit[:80]}…» står ikkje ordrett i dagboka"); feil += 1
else:
    print("(hoppar over sitatsjekk: kjelder/dagbok.txt manglar)")

# 4. Postar som ligg så tett at radiusane overlappar
def dist(a, b):
    r = math.pi / 180
    x = math.sin((b["lat"]-a["lat"])*r/2)**2 + math.cos(a["lat"]*r)*math.cos(b["lat"]*r)*math.sin((b["lon"]-a["lon"])*r/2)**2
    return 2 * 6371000 * math.asin(math.sqrt(x))
for i, a in enumerate(posts):
    for b in posts[i+1:]:
        if dist(a, b) < 2 * RADIUS:
            print(f"ÅTVARING: {a['id']} og {b['id']} ligg berre {dist(a, b):.0f} m frå kvarandre"); feil += 1

print("Alt ok" if not feil else f"{feil} problem")
sys.exit(1 if feil else 0)
