"""Quantify NUL-leak headings + self-link breakdown for the report."""
import re
from collections import Counter
from a7_lib import BUILT, CONTENT, iter_files

print("=== NUL-pair (broken heading/inline) counts in built HTML ===")
for rel in ["guides/matchups-and-counterpicks.html", "guides/offense-and-pressure.html"]:
    html = (BUILT / rel).read_text(encoding="utf-8", errors="ignore")
    n = html.count("\x00")
    # extract the broken headings
    heads = re.findall(r"<h[1-6][^>]*>([^<]*\x00[^<]*)</h[1-6]>", html)
    print(f"  {rel}: {n} NUL chars (~{n//2} broken placeholders), {len(heads)} broken headings")

# how many content headings contain a wikilink or inline code (the trigger), site-wide
trigger = []
for f in sorted(CONTENT.rglob("*.md")):
    for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
        if re.match(r"^#{1,6} ", line) and ("[[" in line or "`" in line or re.search(r"\]\(", line)):
            trigger.append((str(f.relative_to(CONTENT)).replace("\\","/"), i, line.strip()[:70]))
print(f"\n=== content headings containing [[wikilink]]/inline-code/link (NUL-leak trigger): {len(trigger)}")
for rel, i, txt in trigger:
    print(f"   {rel}:{i}  {txt}")
