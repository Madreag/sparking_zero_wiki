"""Fix broken [[wikilinks]] across content: wrong blast class-suffix guesses + known aliases."""

import re
from pathlib import Path

CONTENT = Path(r"C:\vaults\sparking_zero\content")

slug_set = {f.stem for d in CONTENT.iterdir() if d.is_dir() for f in d.glob("*.md")}

OVERRIDES = {
    "super-perception": "perception", "senzu": "senzu-bean",
}


def resolve(target: str) -> str | None:
    t = target.strip().lower().replace(" ", "-")
    if t in slug_set:
        return None  # fine as-is
    if t in OVERRIDES and OVERRIDES[t] in slug_set:
        return OVERRIDES[t]
    cands = []
    if t.endswith("-ultimate"):
        cands.append(t[: -len("-ultimate")] + "-super")
    if t.endswith("-super"):
        cands.append(t[: -len("-super")] + "-ultimate")
    # plain name -> try both suffixes
    cands += [t + "-super", t + "-ultimate"]
    hits = [c for c in cands if c in slug_set]
    return hits[0] if len(hits) >= 1 else None


wl = re.compile(r"\[\[([^\]|\\]+)")
fixed = unfixable = 0
for f in CONTENT.rglob("*.md"):
    txt = f.read_text(encoding="utf-8")
    out = txt
    for m in set(wl.findall(txt)):
        t = m.strip().lower().replace(" ", "-")
        if t in slug_set:
            continue
        r = resolve(m)
        if r:
            out = re.sub(r"\[\[" + re.escape(m) + r"(?=[\]|\\])", f"[[{r}", out)
            fixed += 1
        else:
            unfixable += 1
            print(f"  UNFIXABLE [[{m}]] in {f.relative_to(CONTENT)}")
    if out != txt:
        f.write_text(out, encoding="utf-8")
print(f"fixed={fixed} unfixable={unfixable}")
