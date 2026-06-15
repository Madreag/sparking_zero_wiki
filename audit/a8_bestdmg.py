"""READ-ONLY probe: collision cids + best_damage chip/hits loss analysis."""
import json
from pathlib import Path

c = json.load(open(Path(r"C:\vaults\sparking_zero\data-mined\characters.json"), encoding="utf-8"))

print("---- collision cids ----")
for cid in ("0000_40", "0000_44", "0020_60", "0020_64"):
    x = c.get(cid, {})
    print(cid, "name=", repr(x.get("name")), "fullName=", repr(x.get("fullName")),
          "dlcPack=", repr(x.get("dlcPack")))


def best_damage(move):
    dmg = chip = hits = None
    for b in move.get("bullets") or []:
        cand = max(x for x in (b.get("beamPower"), b.get("power"), 0) if x is not None)
        if cand and (dmg is None or cand > dmg):
            dmg = cand
            chip = b.get("beamChip") or b.get("chip")
            hits = b.get("multiHit")
    melee = [p for p in (move.get("combatives") or {}).get("meleePowers", []) if p]
    pre_chip, pre_dmg, pre_hits = chip, dmg, hits
    if melee and (dmg is None or max(melee) > dmg):
        dmg = max(melee)
        chip = None
        hits = None
    return dmg, chip, hits, pre_chip, pre_dmg, pre_hits, bool(melee), len(move.get("bullets") or [])


print("\n---- best_damage: melee override discards a real beam chip/hits ----")
n = 0
multi_bullet_loss = 0
for cid, x in c.items():
    moves = list(x.get("supers") or [])
    if x.get("ultimate"):
        moves.append(x["ultimate"])
    for s in moves:
        if not s or not s.get("name"):
            continue
        dmg, chip, hits, pc, pd, ph, had_melee, nb = best_damage(s)
        if had_melee and (pc or ph) and chip is None and pd is not None:
            n += 1
            if n <= 12:
                print(f"  {cid} {s['name']!r}: beam dmg={pd} chip={pc} hits={ph} "
                      f"-> melee {dmg} wins, chip/hits DROPPED")
        if nb > 1:
            multi_bullet_loss += 1
print(f"  total moves where melee override discarded beam chip/hits: {n}")
print(f"  moves with >1 datamined bullet (only the single max bullet kept): {multi_bullet_loss}")
