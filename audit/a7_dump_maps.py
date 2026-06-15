"""Dump the reconstructed slug index + autolink name map to JSON for the node faithful test."""
import json
from a7_lib import build_index, build_name_index, STOP_MARKDOWN

idx, owners, aliases = build_index()
name_map = build_name_index(idx, STOP_MARKDOWN)
out = {
    "index": {k: v["href"] for k, v in idx.items()},
    "nameMap": name_map,
    "names": sorted(name_map.keys(), key=lambda s: -len(s)),
}
import pathlib
pathlib.Path("a7_maps.json").write_text(json.dumps(out), encoding="utf-8")
print("index:", len(out["index"]), "names:", len(out["names"]))
