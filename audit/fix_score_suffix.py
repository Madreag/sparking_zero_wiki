"""One-off: strip the misleading 'k' from community model scores in the strengths/
weaknesses enrichment (e.g. '128.7k' -> '128.7'). These are ~150-point scores, not
thousands. Only decimal+k is touched; integer+k (40k ki, 50k-ki, 45k HP) is preserved."""
import re
import pathlib

ROOT = pathlib.Path(r"c:\vaults\sparking_zero")
for rel in ["data-mined/enrichment/sw_a.json", "data-mined/enrichment/sw_b.json"]:
    p = ROOT / rel
    t = p.read_text(encoding="utf-8")
    n = len(re.findall(r"\d+\.\d+k", t))
    p.write_text(re.sub(r"(\d+\.\d+)k", r"\1", t), encoding="utf-8")
    print(rel, "-> stripped", n, "score-k suffixes")
