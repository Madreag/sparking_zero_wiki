"""Print RAW built-HTML bytes (unstripped) around target needles to see exact structure."""
from a7_lib import BUILT

targets = [
    ("game-modes/training.html", "15"),
    ("dlc/preorder-pack.html", "182"),
    ("game-modes/player-match.html", "selectable"),
]
for rel, needle in targets:
    f = BUILT / rel
    html = f.read_text(encoding="utf-8", errors="ignore")
    print(f"\n===== {rel}  (needle={needle!r}) =====")
    idx = 0
    shown = 0
    while shown < 3:
        i = html.find(needle, idx)
        if i < 0:
            break
        seg = html[max(0, i-80):i+80]
        if "script" not in seg.lower() and "_next" not in seg:
            print(repr(seg))
            shown += 1
        idx = i + len(needle)
