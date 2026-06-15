"""Agent-07 shared probe lib: faithfully reconstruct the TS slug index + autolink name index.

Mirrors:
  - lib/content.ts  normalizeSlug() and getSlugIndex() first-wins priority
  - lib/markdown.ts  wikilink regex + autolink STOP set
  - lib/linkify.tsx  getNameIndex() STOP set
Read-only. Never mutates content.
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(r"C:\vaults\sparking_zero")
CONTENT = ROOT / "content"
BUILT = ROOT / ".next" / "server" / "app"

# getSlugIndex() add() order in lib/content.ts (first added wins on collisions)
PRIORITY = [
    "characters", "skills", "blasts", "transformations", "mechanics",
    "game-modes", "episode-battles", "patches", "dlc", "guides",
    "stages", "shop", "glossary",
]
# label field per collection (what getSlugIndex stores as `label`)
LABEL_FIELD = {
    "characters": "name", "skills": "name", "blasts": "name",
    "transformations": "name", "mechanics": "name", "game-modes": "name",
    "episode-battles": "name", "patches": "version", "dlc": "name",
    "guides": "title", "stages": "name", "shop": "name", "glossary": "term",
}


def normalize_slug(s: str) -> str:
    """lib/content.ts normalizeSlug: trim -> lowercase -> /\\s+/ -> '-'."""
    return re.sub(r"\s+", "-", s.strip().lower())


def load_fm(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---"):
        return {}
    parts = raw.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        data = yaml.safe_load(parts[1]) or {}
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def iter_files(coll: str):
    d = CONTENT / coll
    if not d.exists():
        return
    for f in sorted(d.glob("*.md")):
        yield f


def collection_items(coll: str):
    """Return list of dicts: slug (data.slug ?? filename), label, file."""
    out = []
    lf = LABEL_FIELD[coll]
    for f in iter_files(coll):
        fm = load_fm(f)
        slug = fm.get("slug") or f.stem
        slug = str(slug)
        label = fm.get(lf)
        out.append({"slug": slug, "label": str(label) if label is not None else "",
                    "file": f, "fm": fm, "stem": f.stem})
    return out


def build_index():
    """Reconstruct getSlugIndex(): key -> {href,label,collection,kind}.

    Returns (index, owners, alias_index) where:
      index   : faithful first-wins map (key -> entry)
      owners  : slug -> ordered list of collections that define that slug (priority order)
      alias_index: alias-key -> (glossary canonical slug, term) for reporting
    """
    index: dict[str, dict] = {}
    owners: dict[str, list] = {}
    alias_index: dict[str, tuple] = {}

    def add(key, href, label, collection, kind):
        if key not in index:
            index[key] = {"href": href, "label": label,
                          "collection": collection, "kind": kind}

    for coll in PRIORITY:
        if coll == "glossary":
            for it in collection_items("glossary"):
                slug = it["slug"]
                owners.setdefault(slug, []).append("glossary")
                add(slug, f"/glossary#{slug}", it["label"], "glossary", "slug")
                aliases = it["fm"].get("aliases") or []
                if isinstance(aliases, str):
                    aliases = [aliases]
                for a in aliases:
                    k = normalize_slug(str(a))
                    alias_index.setdefault(k, (slug, it["label"]))
                    add(k, f"/glossary#{slug}", it["label"], "glossary", "alias")
        else:
            prefix = f"/{coll}"
            for it in collection_items(coll):
                slug = it["slug"]
                owners.setdefault(slug, []).append(coll)
                add(slug, f"{prefix}/{slug}", it["label"], coll, "slug")
    return index, owners, alias_index


# ---- autolink name index (lib/markdown.ts autoIndex + lib/linkify.tsx getNameIndex) ----
STOP_MARKDOWN = {"base", "story", "standard"}
STOP_LINKIFY = {"base", "story", "standard", "wish", "shop — other"}


def build_name_index(index: dict, stop: set):
    """label.lower() -> href, len>=4, not in stop, no arrow, first-wins by index order."""
    name_map: dict[str, str] = {}
    # index dict preserves insertion order == priority order == getSlugIndex order
    for key, e in index.items():
        label = e["label"]
        if not label or len(label) < 4:
            continue
        if label.lower() in stop:
            continue
        if "\u2192" in label:  # arrow
            continue
        k = label.lower()
        if k not in name_map:
            name_map[k] = e["href"]
    return name_map


# faithful markdown.ts wikilink regex (backslash NOT excluded from target)
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")


def iter_wikilinks():
    """Yield (file, lineno, rawmatch, target, label) for every wikilink in content/,
    faithful to the markdown.ts regex (so escaped-pipe backslashes ARE captured)."""
    for f in sorted(CONTENT.rglob("*.md")):
        text = f.read_text(encoding="utf-8")
        for i, line in enumerate(text.splitlines(), 1):
            for m in WIKILINK_RE.finditer(line):
                yield f, i, m.group(0), m.group(1), m.group(2)


if __name__ == "__main__":
    idx, owners, aliases = build_index()
    print("index keys:", len(idx))
    print("aliases:", len(aliases))
    multi = {s: c for s, c in owners.items() if len(c) > 1}
    print("slug collisions (same slug in >1 collection):", len(multi))
    nm = build_name_index(idx, STOP_MARKDOWN)
    print("autolink names (markdown.ts):", len(nm))
    nl = build_name_index(idx, STOP_LINKIFY)
    print("autolink names (linkify.tsx):", len(nl))
