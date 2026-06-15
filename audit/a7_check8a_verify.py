"""Verify Check 8a corruption against the REAL built HTML (ground truth)."""
from __future__ import annotations

import re
from a7_lib import BUILT

probes = [
    ("dlc/preorder-pack.html", ["roster slot", "base game"]),
    ("game-modes/training.html", ["DP-format", "toggle"]),
    ("game-modes/player-match.html", ["selectable at", "DP total"]),
    ("episode-battles/episode-frieza.html", ["chapters 2", "campaign"]),
    ("dlc/season-pass-1.html", ["bundle", "Season"]),
    ("game-modes/world-tournament.html", ["bracket", "fighters"]),
    ("glossary.html", ["roster slots", "base game"]),  # glossary BODY is NOT rendered -> control
]

strip_scripts = lambda t: re.sub(r"<script[\s\S]*?</script>", "", t)
tags = re.compile(r"<[^>]+>")

for rel, needles in probes:
    f = BUILT / rel
    if not f.exists():
        print(f"MISSING {rel}")
        continue
    html = strip_scripts(f.read_text(encoding="utf-8", errors="ignore"))
    text = tags.sub("", html)
    text = text.replace("<!-- -->", "")
    print(f"\n===== {rel} =====")
    print("  contains 'undefined':", "undefined" in text)
    for n in needles:
        i = text.find(n)
        if i >= 0:
            print(f"  …{text[max(0,i-50):i+70]}…")
            break
