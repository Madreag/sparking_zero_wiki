"""Decisive check: is the markdown.ts autolink protect/restore sentinel a real
space (0x20) — which would corrupt prose numbers — or a control char (safe)?"""
from pathlib import Path

raw = Path(r"C:\vaults\sparking_zero\lib\markdown.ts").read_bytes()
text = raw.decode("utf-8")

# Show any non-ASCII / control bytes present (this is why it trips "binary" detection)
ctrl = sorted({b for b in raw if b < 0x09 or (0x0e <= b < 0x20)})
print("control bytes present (hex):", [hex(b) for b in ctrl])

for i, line in enumerate(text.splitlines(), 1):
    if "protectedParts.length" in line or "replace(/" in line or "return `" in line.strip()[:8] or "protect = (s" in line:
        # print exact repr so spaces vs control chars are visible
        print(f"L{i}: {line!r}")
