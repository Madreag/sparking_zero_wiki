import subprocess
from pathlib import Path

ROOT = Path(r"C:\vaults\sparking_zero")
out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True).stdout
files = [f for f in out.splitlines() if f]
print(f"tracked files: {len(files)}")
sized = []
for f in files:
    p = ROOT / f
    try:
        sized.append((p.stat().st_size, f))
    except OSError:
        pass
sized.sort(reverse=True)
print("\nlargest 15 tracked files:")
for s, f in sized[:15]:
    print(f"  {s/1024:9.1f} KB  {f}")
total = sum(s for s, _ in sized)
print(f"\ntotal tracked size: {total/1024/1024:.1f} MB")
# sanity: confirm none are in ignored areas
bad = [f for _, f in sized if f.startswith("data-mined/raw/") or f.startswith("node_modules/") or "/bin/" in f or "/obj/" in f or f.endswith(".usmap") or f.endswith(".dll")]
print(f"leaked-ignored files staged: {len(bad)}  {bad[:5]}")
