"""Check 1: enumerate EVERY [[wikilink]] and resolve via the faithful TS slug index.

Reports, grouped by target:
  - escaped-pipe victims  (target ends with '\\' from generator '\\|'; would resolve if fixed)
  - genuine unresolved    (silent plain-text dead-ends), split intentional vs real
"""
from __future__ import annotations

from collections import defaultdict

from a7_lib import (CONTENT, build_index, iter_wikilinks, normalize_slug)

idx, owners, aliases = build_index()

# Known-intentional unresolved targets (unreleased Season 2 names etc.)
INTENTIONAL = {
    "super-17",          # unreleased S2 character (audit.py whitelists this)
}
INTENTIONAL_PREFIX = ()  # none yet

resolved = 0
escaped_victim = defaultdict(list)   # clean target -> [(file,line,raw,label)]
escaped_broken = defaultdict(list)   # target(stripped) -> [...]
genuine = defaultdict(list)          # key -> [(file,line,raw,label)]
total = 0

for f, line, raw, target, label in iter_wikilinks():
    total += 1
    key = normalize_slug(target)
    if key in idx:
        resolved += 1
        continue
    rel = str(f.relative_to(CONTENT)).replace("\\", "/")
    # escaped-pipe artifact? target captured a trailing backslash from '\|'
    if target.endswith("\\"):
        clean = normalize_slug(target.rstrip("\\"))
        if clean in idx:
            escaped_victim[clean].append((rel, line, raw, label))
        else:
            escaped_broken[clean].append((rel, line, raw, label))
    else:
        genuine[key].append((rel, line, raw, label))

print(f"=== TOTAL wikilinks (faithful regex): {total}")
print(f"=== resolved cleanly: {resolved}")
print(f"=== escaped-pipe VICTIMS (markdown bug, would resolve if fixed): "
      f"{sum(len(v) for v in escaped_victim.values())} occurrences across {len(escaped_victim)} targets")
print(f"=== escaped-pipe + STILL broken: "
      f"{sum(len(v) for v in escaped_broken.values())} occurrences across {len(escaped_broken)} targets")
print(f"=== genuine unresolved (unescaped): "
      f"{sum(len(v) for v in genuine.values())} occurrences across {len(genuine)} targets")

print("\n----- ESCAPED-PIPE VICTIMS (top 40 targets by count) -----")
for tgt, occ in sorted(escaped_victim.items(), key=lambda kv: -len(kv[1]))[:40]:
    dest = idx[tgt]["href"]
    print(f"[[{tgt}\\|...]] x{len(occ)} -> {dest}   e.g. {occ[0][0]}:{occ[0][1]}")

print("\n----- ESCAPED-PIPE + STILL BROKEN (all) -----")
for tgt, occ in sorted(escaped_broken.items(), key=lambda kv: -len(kv[1])):
    print(f"[[{tgt}\\|...]] x{len(occ)}   e.g. {occ[0][0]}:{occ[0][1]}  raw={occ[0][2]!r} label={occ[0][3]!r}")

print("\n----- GENUINE UNRESOLVED (unescaped, silent plain-text) -----")
real = []
intentional = []
for key, occ in sorted(genuine.items(), key=lambda kv: -len(kv[1])):
    bucket = intentional if (key in INTENTIONAL or key.startswith(INTENTIONAL_PREFIX)) else real
    bucket.append((key, occ))
print(f"  REAL breaks: {len(real)} targets")
for key, occ in real:
    files = ", ".join(f"{o[0]}:{o[1]}" for o in occ[:6])
    print(f"  [[{key}]] x{len(occ)}  labels={sorted({str(o[3]) for o in occ})}  @ {files}")
print(f"\n  INTENTIONAL (S2/unreleased): {len(intentional)} targets")
for key, occ in intentional:
    print(f"  [[{key}]] x{len(occ)}  @ {occ[0][0]}:{occ[0][1]}")
