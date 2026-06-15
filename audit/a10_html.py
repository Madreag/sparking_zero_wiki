"""Agent 10 rendered-output QA: scan ALL built HTML for leaked artifacts.
READ-ONLY. Strips <script>/<style>/comments (React flight data legitimately
contains null/$undefined/[...]) then scans visible text nodes.
"""
import re
import json
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(r"C:\vaults\sparking_zero")
APP = ROOT / ".next" / "server" / "app"

html_files = sorted(APP.rglob("*.html"))
print("HTML files:", len(html_files))

SCRIPT = re.compile(r"<script\b[^>]*>.*?</script>", re.S | re.I)
STYLE = re.compile(r"<style\b[^>]*>.*?</style>", re.S | re.I)
COMMENT = re.compile(r"<!--.*?-->", re.S)
TEXTNODE = re.compile(r">([^<>]+)<")
TDCELL = re.compile(r"<td\b[^>]*>(.*?)</td>", re.S | re.I)
TAGSTRIP = re.compile(r"<[^>]+>")

# artifact patterns operating on VISIBLE text (post-strip)
patterns = {
    "gt_null_lt": re.compile(r">\s*null\s*<"),
    "gt_undefined_lt": re.compile(r">\s*undefined\s*<"),
    "gt_None_lt": re.compile(r">\s*None\s*<"),
    "gt_NaN_lt": re.compile(r">\s*NaN\s*<"),
    "object_Object": re.compile(r"\[object Object\]"),
    "leaked_wikilink": re.compile(r"\[\["),
    "leaked_pipe_escape": re.compile(r"\\\|"),
    "empty_td": re.compile(r"<td[^>]*>\s*</td>", re.I),
}
# word-in-text-node detection (looser; catches "HP: null" inside a cell)
WORDISH = {
    "null": re.compile(r"\bnull\b"),
    "undefined": re.compile(r"\bundefined\b"),
    "NaN": re.compile(r"\bNaN\b"),
    "None": re.compile(r"\bNone\b"),
}

counts = Counter()
samples = defaultdict(list)
# unformatted 5-7 digit numbers inside table cells
unformatted = []      # (relpath, cell_text_excerpt, number)
unformatted_pages = set()
# text-node word artifacts
word_hits = defaultdict(list)


def rel(p):
    return str(p.relative_to(APP)).replace("\\", "/")


for p in html_files:
    raw = p.read_text(encoding="utf-8", errors="replace")
    visible = COMMENT.sub(" ", STYLE.sub(" ", SCRIPT.sub(" ", raw)))

    for key, rx in patterns.items():
        n = len(rx.findall(visible))
        if n:
            counts[key] += n
            if len(samples[key]) < 12:
                samples[key].append(rel(p))

    # text-node word artifacts (null/undefined/NaN/None as standalone tokens in text)
    for txt in TEXTNODE.findall(visible):
        t = txt.strip()
        low = t.lower()
        for wk, rx in WORDISH.items():
            if rx.search(t):
                # ignore words embedded in normal prose like 'Nonexistent'? \b handles that.
                word_hits[wk].append((rel(p), t[:80]))

    # 5-7 digit numbers without thousands separators inside <td> cells
    for cell in TDCELL.findall(visible):
        celltext = TAGSTRIP.sub(" ", cell)
        for m in re.finditer(r"(?<![\d,])\d{5,7}(?![\d,])", celltext):
            num = m.group(0)
            unformatted.append((rel(p), celltext.strip()[:80], num))
            unformatted_pages.add(rel(p))

print("\n=== TAG-BOUNDED / STRUCTURAL ARTIFACTS (visible HTML) ===")
for key in patterns:
    print(f"  {key:22} count={counts[key]:5}  pages~{len(samples[key])} e.g. {samples[key][:4]}")

print("\n=== TEXT-NODE WORD ARTIFACTS (null/undefined/NaN/None as tokens) ===")
for wk in WORDISH:
    hits = word_hits[wk]
    print(f"  {wk:10} hits={len(hits)}  e.g. {hits[:4]}")

print("\n=== UNFORMATTED 5-7 DIGIT NUMBERS IN <td> CELLS ===")
print(f"  occurrences={len(unformatted)} across {len(unformatted_pages)} pages")
# tally by number to see what they are
bynum = Counter(n for _, _, n in unformatted)
print("  most common raw numbers:", bynum.most_common(15))
for s in unformatted[:25]:
    print("    ", s)

out = {
    "html_files": len(html_files),
    "structural": {k: counts[k] for k in patterns},
    "structural_samples": {k: samples[k] for k in patterns},
    "word_artifacts": {k: {"count": len(word_hits[k]), "samples": word_hits[k][:20]} for k in WORDISH},
    "unformatted_numbers": {
        "occurrences": len(unformatted),
        "pages": len(unformatted_pages),
        "by_number": bynum.most_common(40),
        "samples": unformatted[:60],
        "sample_pages": sorted(unformatted_pages)[:40],
    },
}
(ROOT / "audit" / "a10_html.json").write_text(json.dumps(out, indent=1, default=str), encoding="utf-8")
print("\nWROTE audit/a10_html.json")
