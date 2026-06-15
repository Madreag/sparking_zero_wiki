"""Check 8a: autolink protect/restore prose-corruption detector.

markdown.ts autolink() shields code/links/headings/table-separators by replacing each with
" <n> " (space-digit-space), then restores with /  (\\d+) /g. A *prose* number surrounded by
spaces can collide with that placeholder pattern and get replaced by a shielded fragment (or
'undefined' if out of range). We detect this by running a faithful port AND a collision-proof
port (sentinel placeholders) on every rendered body and diffing the results.
"""
from __future__ import annotations

import re

from a7_lib import (CONTENT, build_index, build_name_index, normalize_slug,
                    STOP_MARKDOWN, WIKILINK_RE)

idx, owners, aliases = build_index()
name_map = build_name_index(idx, STOP_MARKDOWN)
names = sorted(name_map.keys(), key=lambda s: -len(s))


def esc(s):
    return re.sub(r"[.*+?^${}()|[\]\\]", lambda m: "\\" + m.group(0), s)


NAME_RE = re.compile(r"(?<![A-Za-z0-9_/\[])(" + "|".join(esc(n) for n in names) + r")(?![A-Za-z0-9_\]])",
                     re.IGNORECASE)

CODEFENCE = re.compile(r"```[\s\S]*?```")
INLINE = re.compile(r"`[^`\n]*`")
LINKIMG = re.compile(r"!?\[[^\]]*\]\([^)]*\)")
HEADING = re.compile(r"(?m)^#{1,6} .*$")
TBLSEP = re.compile(r"(?m)^\|[ :|-]+\|\s*$")


def wikilink_step(md):
    def repl(m):
        target, label = m.group(1), m.group(2)
        key = normalize_slug(target)
        text = (label if label is not None else target).strip()
        e = idx.get(key)
        return f"[{text}]({e['href']})" if e else text
    return WIKILINK_RE.sub(repl, md)


def autolink(md, sentinel: bool):
    parts = []

    def protect(m):
        parts.append(m.group(0))
        i = len(parts) - 1
        return f" \x01{i}\x01 " if sentinel else f" {i} "
    work = md
    for rx in (CODEFENCE, INLINE, LINKIMG, HEADING, TBLSEP):
        work = rx.sub(protect, work)
    seen = set()

    def repl(m):
        match = m.group(0)
        key = match.lower()
        href = name_map.get(key)
        if not href or key in seen:
            return match
        seen.add(key)
        return f"[{match}]({href})"
    work = NAME_RE.sub(repl, work)

    if sentinel:
        work = re.sub(r" \x01(\d+)\x01 ",
                      lambda m: parts[int(m.group(1))], work)
    else:
        def rest(m):
            i = int(m.group(1))
            return parts[i] if i < len(parts) else "undefined"
        work = re.sub(r" (\d+) ", rest, work)
    return work


corrupted = []
checked = 0
for f in sorted(CONTENT.rglob("*.md")):
    raw = f.read_text(encoding="utf-8")
    parts = raw.split("---", 2)
    body = parts[2] if len(parts) >= 3 else raw
    body = body.strip()
    if not body:
        continue
    checked += 1
    wl = wikilink_step(body)
    a_faithful = autolink(wl, sentinel=False)
    a_safe = autolink(wl, sentinel=True)
    if a_faithful != a_safe:
        rel = str(f.relative_to(CONTENT)).replace("\\", "/")
        # find first differing region
        for i, (cf, cs) in enumerate(zip(a_faithful, a_safe)):
            if cf != cs:
                ctx_f = a_faithful[max(0, i - 40):i + 40]
                ctx_s = a_safe[max(0, i - 40):i + 40]
                corrupted.append((rel, ctx_f, ctx_s))
                break

print(f"=== bodies checked: {checked}")
print(f"=== bodies with protect/restore CORRUPTION (faithful != collision-proof): {len(corrupted)}")
for rel, cf, cs in corrupted[:40]:
    print(f"\n  {rel}")
    print(f"    faithful: ...{cf!r}...")
    print(f"    correct : ...{cs!r}...")
