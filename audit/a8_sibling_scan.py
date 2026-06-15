"""READ-ONLY probe: count blast 'sibling' cross-links that render as plain text
(dead) vs as <a> anchors in the built HTML."""
import re
from pathlib import Path

BUILT = Path(r"C:\vaults\sparking_zero\.next\server\app\blasts")
strip = lambda t: re.sub(r"<script[\s\S]*?</script>", "", t)

total = dead = linked = 0
dead_examples = []
for f in sorted(BUILT.glob("*.html")):
    t = strip(f.read_text(encoding="utf-8", errors="ignore"))
    for m in re.finditer(r"Also exists as a separate.*?</li>", t):
        seg = m.group(0)
        total += 1
        if "<a " in seg:
            linked += 1
        else:
            dead += 1
            if len(dead_examples) < 12:
                # extract the trailing visible label
                lab = re.sub(r"<[^>]+>", "", seg).split(":")[-1].strip()
                dead_examples.append((f.stem, lab))

print(f"blast pages with a 'sibling' cross-link: {total}")
print(f"  rendered as <a> link: {linked}")
print(f"  rendered as PLAIN TEXT (dead cross-link): {dead}")
for stem, lab in dead_examples:
    print(f"    DEAD on /blasts/{stem}: '{lab}'")
