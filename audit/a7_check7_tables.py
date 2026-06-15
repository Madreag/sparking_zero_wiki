"""Check 7: table pipe escaping + malformed GFM tables in built HTML.

- leaked literal '\\|' in rendered output (escape that wasn't consumed)
- stray '|' inside rendered <td>/<th> cells (broken cell / unescaped pipe)
- column-count consistency per rendered <table> (header cols vs body-row cols)
"""
from __future__ import annotations

import re
from collections import Counter

from a7_lib import BUILT

strip_scripts = lambda t: re.sub(r"<script[\s\S]*?</script>", "", t)

leaked_esc = Counter()          # pages with literal \|
leaked_esc_sample = None
cell_pipe = Counter()           # pages with '|' inside a td/th
cell_pipe_sample = []
malformed_tables = []           # (page, header_cols, bad_row_cols)
pages = 0

TD_RE = re.compile(r"<t[dh][^>]*>(.*?)</t[dh]>", re.S)
ROW_RE = re.compile(r"<tr[^>]*>(.*?)</tr>", re.S)
TABLE_RE = re.compile(r"<table[^>]*>(.*?)</table>", re.S)
TAG_RE = re.compile(r"<[^>]+>")

for f in BUILT.rglob("*.html"):
    pages += 1
    rel = str(f.relative_to(BUILT)).replace("\\", "/")
    html = strip_scripts(f.read_text(encoding="utf-8", errors="ignore"))

    if "\\|" in html:
        leaked_esc[rel] += html.count("\\|")
        if leaked_esc_sample is None:
            leaked_esc_sample = rel

    # stray pipe inside cells (ignore code cells which legitimately may show pipes)
    for cell in TD_RE.findall(html):
        text = TAG_RE.sub("", cell)
        if "|" in text and "<code" not in cell:
            cell_pipe[rel] += 1
            if len(cell_pipe_sample) < 12:
                cell_pipe_sample.append((rel, text.strip()[:60]))

    # column consistency per table
    for tbl in TABLE_RE.findall(html):
        rows = ROW_RE.findall(tbl)
        col_counts = []
        for r in rows:
            n = len(re.findall(r"<t[dh][^>]*>", r))
            if n:
                col_counts.append(n)
        if not col_counts:
            continue
        header = col_counts[0]
        bad = [c for c in col_counts[1:] if c != header]
        if bad:
            malformed_tables.append((rel, header, Counter(bad).most_common()))

print(f"=== scanned {pages} built HTML pages")
print(f"\n--- leaked literal '\\|' in output: {sum(leaked_esc.values())} occurrences on {len(leaked_esc)} pages ---")
for rel, c in leaked_esc.most_common(20):
    print(f"   {rel} x{c}")

print(f"\n--- '|' inside rendered table cells: {sum(cell_pipe.values())} cells on {len(cell_pipe)} pages ---")
for rel, txt in cell_pipe_sample:
    print(f"   {rel}: {txt!r}")

print(f"\n--- malformed tables (row col-count != header col-count): {len(malformed_tables)} ---")
for rel, header, bad in malformed_tables[:30]:
    print(f"   {rel}: header={header} cols, off-rows={bad}")
