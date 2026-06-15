"""Inspect raw bytes of markdown.ts around protect()/restore to detect hidden placeholder chars."""
from pathlib import Path

p = Path(r"C:\vaults\sparking_zero\lib\markdown.ts")
raw = p.read_text(encoding="utf-8")
for marker in ["protectedParts.length - 1", "work.replace(/ (", "return ` ", ".replace(/ ("]:
    i = raw.find(marker)
    if i < 0:
        print(f"NOT FOUND: {marker!r}")
        continue
    seg = raw[i-10:i+40]
    print(f"\n--- around {marker!r} ---")
    print("repr:", repr(seg))
    print("codes:", [hex(ord(c)) for c in seg])
