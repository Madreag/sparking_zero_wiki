"""Drill into the single >null< and the empty-<td> cells to classify them."""
import re
from pathlib import Path

APP = Path(r"C:\vaults\sparking_zero\.next\server\app")
SCRIPT = re.compile(r"<script\b[^>]*>.*?</script>", re.S | re.I)
STYLE = re.compile(r"<style\b[^>]*>.*?</style>", re.S | re.I)
COMMENT = re.compile(r"<!--.*?-->", re.S)


def visible(p):
    raw = p.read_text(encoding="utf-8", errors="replace")
    return COMMENT.sub(" ", STYLE.sub(" ", SCRIPT.sub(" ", raw)))


# 1) the >null< in vanish-z-counter
p = APP / "mechanics" / "vanish-z-counter.html"
v = visible(p)
for m in re.finditer(r">\s*null\s*<", v):
    s = max(0, m.start() - 220)
    print("=== >null< CONTEXT (vanish-z-counter) ===")
    print(v[s:m.end() + 60])
    print()

# 2) classify empty <td> on a character page + a listing page
for name in ["characters/android-13.html", "characters/all-members.html"]:
    p = APP / name
    v = visible(p)
    empties = [m.start() for m in re.finditer(r"<td[^>]*>\s*</td>", v, re.I)]
    print(f"=== {name}: {len(empties)} empty <td> ; first contexts ===")
    for st in empties[:3]:
        s = max(0, st - 160)
        print("   ...", re.sub(r"\s+", " ", v[s:st + 12]))
    print()

# 3) does android-13 summary contain 'null' prose? show its <p> summary
p = APP / "characters" / "anilaza.html"
v = visible(p)
m = re.search(r"null", v)
if m:
    s = max(0, m.start() - 120)
    print("=== anilaza 'null' context ===")
    print(re.sub(r"\s+", " ", v[s:m.start() + 40]))
