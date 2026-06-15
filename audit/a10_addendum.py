"""Final addendum: DLC dp-under-datamined, null-HP prose summaries, grand tally."""
from pathlib import Path
import re
import yaml

CONTENT = Path(r"C:\vaults\sparking_zero\content")


def load(coll):
    out = []
    for f in sorted((CONTENT / coll).glob("*.md")):
        t = f.read_text(encoding="utf-8")
        parts = t.split("\n")
        end = next((i for i in range(1, len(parts)) if parts[i].strip() == "---"), None)
        fm = yaml.safe_load("\n".join(parts[1:end])) or {}
        body = "\n".join(parts[end + 1:]) if end else ""
        out.append((f.stem, fm, body))
    return out


# 1) DLC pages datamined w/ character dp
dlc_dm_dp = []
dlc_dp_entries = 0
for slug, fm, _ in load("dlc"):
    conf = fm.get("confidence", "community")
    chars = fm.get("characters") or []
    dpchars = [c for c in chars if isinstance(c, dict) and c.get("dp") is not None]
    if conf == "datamined" and dpchars:
        dlc_dm_dp.append((slug, len(dpchars)))
        dlc_dp_entries += len(dpchars)
print("DLC datamined pages carrying community DP values:", len(dlc_dm_dp))
for s, n in dlc_dm_dp:
    print(f"   content/dlc/{s}.md  ({n} chars w/ dp)")
print("  total DP entries under datamined DLC:", dlc_dp_entries)

# 2) null-HP prose summaries in characters
nullhp = []
for slug, fm, _ in load("characters"):
    summ = fm.get("summary") or ""
    if re.search(r"null[\s-]?HP|null HP|\(null HP\)", summ, re.I):
        nullhp.append(slug)
print("\ncharacter summaries containing 'null-HP' prose:", len(nullhp))
print("  ", nullhp)

# 3) grand tally datamined-stamped pages carrying a community DP value
chars_dp = sum(1 for slug, fm, _ in load("characters")
               if fm.get("confidence", "community") == "datamined" and fm.get("dp") is not None)
tf_dp = sum(1 for slug, fm, _ in load("transformations")
            if fm.get("confidence", "community") == "datamined"
            and (fm.get("dpFrom") is not None or fm.get("dpTo") is not None))
print("\n=== GRAND TALLY: datamined-stamped pages carrying community DP ===")
print("  characters (dp):           ", chars_dp)
print("  transformations (dpFrom/To):", tf_dp)
print("  dlc (character dp):        ", len(dlc_dm_dp))
print("  TOTAL pages:               ", chars_dp + tf_dp + len(dlc_dm_dp))

# 4) glossary datamined-but-research-only (sanity from earlier)
gl = []
for slug, fm, _ in load("glossary"):
    if fm.get("confidence", "community") == "datamined":
        srcs = " ".join(str(s).lower() for s in (fm.get("sources") or []))
        if not any(w in srcs for w in ["game file", "steam build", "cue4parse", "characterdata", "masterdata", "data-mined", "datamine"]):
            gl.append(slug)
print("\nglossary datamined w/ NO game-file source:", len(gl), gl)
