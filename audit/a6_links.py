"""
Audit Agent 6 — internal [[wikilink]] resolution probe for the 12 guides.
Replicates lib/content.ts: normalizeSlug(s) = s.trim().lower().replace(/\\s+/,'-'),
resolved against the cross-collection slug index (all collection slugs + glossary aliases).
Unknown [[targets]] render as PLAIN TEXT (silent dead links) — this lists them.
Read-only.  Run: python audit/a6_links.py
"""
import os, re, glob

ROOT = r"c:\vaults\sparking_zero"
CONTENT = os.path.join(ROOT, "content")

def norm(s):
    return re.sub(r"\s+", "-", s.strip().lower())

def frontmatter(path):
    with open(path, encoding="utf-8") as f:
        txt = f.read()
    if not txt.startswith("---"):
        return "", txt
    end = txt.find("\n---", 3)
    return txt[3:end], txt[end+4:]

# ---- build slug index (keys) ----
keys = set()
COLLECTIONS = ["characters","skills","blasts","transformations","mechanics","game-modes",
               "episode-battles","patches","dlc","guides","stages","shop","glossary"]
for col in COLLECTIONS:
    for p in glob.glob(os.path.join(CONTENT, col, "*.md")):
        fm, _ = frontmatter(p)
        m = re.search(r'^slug:\s*"?([^"\n]+?)"?\s*$', fm, re.M)
        slug = m.group(1).strip() if m else os.path.basename(p)[:-3]
        keys.add(slug)
        if col == "glossary":
            # parse aliases (inline list or block list)
            am = re.search(r'^aliases:\s*\[(.*?)\]', fm, re.M | re.S)
            aliases = []
            if am:
                aliases = re.findall(r'"([^"]+)"', am.group(1))
            else:
                bm = re.search(r'^aliases:\s*\n((?:\s*-\s*.+\n?)+)', fm, re.M)
                if bm:
                    aliases = re.findall(r'-\s*"?([^"\n]+?)"?\s*$', bm.group(1), re.M)
            for a in aliases:
                keys.add(norm(a))

print(f"[index] {len(keys)} resolvable keys across {len(COLLECTIONS)} collections\n")

# ---- scan the 12 guides ----
WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")
total_links = 0
broken = []
for p in sorted(glob.glob(os.path.join(CONTENT, "guides", "*.md"))):
    _, body = frontmatter(p)
    lines = open(p, encoding="utf-8").read().splitlines()
    for ln_no, line in enumerate(lines, 1):
        for mm in WIKILINK.finditer(line):
            raw = mm.group(1)
            target = raw.split("|", 1)[0]
            target = target.replace("\\", "")  # table cells escape pipe as \|; strip stray backslashes
            total_links += 1
            if norm(target) not in keys:
                broken.append((os.path.basename(p), ln_no, raw, norm(target)))

print(f"[guides] scanned wikilinks: {total_links}")
print(f"[guides] UNRESOLVED (render as plain text): {len(broken)}\n")
for f, ln, raw, n in broken:
    print(f"  ** {f}:{ln}  [[{raw}]]  -> normalized '{n}' NOT in index")
if not broken:
    print("  (all wikilinks resolve)")
