"""Confirm the restore regex + autolink return line use the NUL sentinel."""
from pathlib import Path

raw = Path(r"C:\vaults\sparking_zero\lib\markdown.ts").read_text(encoding="utf-8")
# show every line containing replace( with NUL visualized
for i, line in enumerate(raw.splitlines(), 1):
    if "replace(" in line or "protectedParts[" in line or "${protectedParts" in line:
        vis = line.replace("\x00", "<NUL>")
        print(f"{i:3}: {vis}")
