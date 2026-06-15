"""Scan all built HTML for leftover NUL bytes (the single-pass restore bug:
a protected span nested in another protected span is not fully restored)."""
from pathlib import Path

BUILT = Path(r"C:\vaults\sparking_zero\.next\server\app")
hits = []
for f in BUILT.rglob("*.html"):
    b = f.read_bytes()
    if b"\x00" in b:
        # collect short contexts around each NUL run
        idxs = [i for i, c in enumerate(b) if c == 0]
        ctxs = []
        seen = set()
        for i in idxs:
            start = max(0, i - 40)
            ctx = b[start:i + 8].replace(b"\x00", b"<NUL>")
            try:
                s = ctx.decode("utf-8", "replace")
            except Exception:
                s = str(ctx)
            if s not in seen:
                seen.add(s)
                ctxs.append(s)
        hits.append((str(f.relative_to(BUILT)), len(idxs), ctxs[:4]))

print(f"built HTML files containing NUL bytes: {len(hits)}")
for path, n, ctxs in hits[:40]:
    print(f"\n{path}  ({n} NUL bytes)")
    for c in ctxs:
        print("   …", c)
