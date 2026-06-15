import os
from pathlib import Path

ROOT = Path(r"C:\vaults\sparking_zero")

def size(p: Path) -> int:
    total = 0
    for dp, dn, fn in os.walk(p):
        # don't descend into nested node_modules of node_modules etc; just sum all
        for f in fn:
            try:
                total += (Path(dp) / f).stat().st_size
            except OSError:
                pass
    return total

def human(n): 
    for u in ("B","KB","MB","GB"):
        if n < 1024: return f"{n:.1f}{u}"
        n /= 1024
    return f"{n:.1f}TB"

print("=== top-level entries ===")
for child in sorted(ROOT.iterdir()):
    if child.is_dir():
        try:
            n = sum(1 for _ in child.rglob("*") if _.is_file())
        except OSError:
            n = -1
        print(f"  {child.name+'/':28} {human(size(child)):>10}  ({n} files)")
    else:
        print(f"  {child.name:28} {human(child.stat().st_size):>10}")

print("\n=== tools/ contents ===")
tools = ROOT / "tools"
if tools.exists():
    for child in sorted(tools.iterdir()):
        if child.is_dir():
            print(f"  tools/{child.name}/  {human(size(child))}")
        else:
            print(f"  tools/{child.name}  {human(child.stat().st_size)}")

print("\n=== data-mined/ contents ===")
for child in sorted((ROOT/'data-mined').iterdir()):
    if child.is_dir():
        print(f"  data-mined/{child.name}/  {human(size(child))}")
    else:
        print(f"  data-mined/{child.name}  {human(child.stat().st_size)}")
