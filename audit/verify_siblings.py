"""Confirm the blast 'Also exists as a separate ...' sibling cross-links (emitted as
[[slug\\|Label]]) now render as real <a> links (were 58/58 dead before the regex fix)."""
import re
from pathlib import Path

BUILT = Path(r"C:\vaults\sparking_zero\.next\server\app\blasts")
linked = dead = 0
dead_samples = []
for f in BUILT.glob("*.html"):
    t = f.read_text(encoding="utf-8", errors="ignore")
    # the human-readable HTML body is duplicated in an RSC script as \u003c… ; check the
    # plain <li> rendering near "for other fighters:"
    for m in re.finditer(r"for other fighters:\s*(.{0,120}?)</li>", t):
        seg = m.group(1)
        if "<a href=" in seg:
            linked += 1
        else:
            dead += 1
            if len(dead_samples) < 5:
                dead_samples.append((f.name, seg[:80]))
print(f"sibling cross-links rendered as <a>: {linked}")
print(f"sibling cross-links still plain text (dead): {dead}")
for n, s in dead_samples:
    print("  DEAD:", n, "->", s)
