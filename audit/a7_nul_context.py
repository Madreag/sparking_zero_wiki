"""Show context around leaked NUL (\\x00) in the two guide pages, and locate the source cause."""
from pathlib import Path
from a7_lib import BUILT, CONTENT

for rel in ["guides/matchups-and-counterpicks.html", "guides/offense-and-pressure.html"]:
    html = (BUILT / rel).read_text(encoding="utf-8", errors="ignore")
    print(f"\n===== BUILT {rel} =====")
    start = 0
    while True:
        i = html.find("\x00", start)
        if i < 0:
            break
        seg = html[max(0, i-90):i+40].replace("\x00", "[NUL]")
        print("  ", repr(seg))
        start = i + 1

# look at the source guide bodies for the likely trigger (adjacent protected patterns)
for rel in ["guides/matchups-and-counterpicks.md", "guides/offense-and-pressure.md"]:
    raw = (CONTENT / rel).read_text(encoding="utf-8")
    print(f"\n===== SOURCE {rel} (lines with backtick+link or adjacency) =====")
    for i, line in enumerate(raw.splitlines(), 1):
        # heuristics for protect-adjacency: inline code immediately followed by a link or another code
        if "`[" in line or "`](" in line or "](`" in line or "``" in line.replace("``",""):
            print(f"  {i}: {line[:160]}")
