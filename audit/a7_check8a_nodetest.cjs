// Exact port of lib/markdown.ts autolink protect/restore (no name map) to test on a real body.
const fs = require("fs");
const path = require("path");

function bodyOf(p) {
  const raw = fs.readFileSync(p, "utf8");
  const parts = raw.split("---");
  return parts.slice(2).join("---").trim();
}

function protectRestore(md) {
  const protectedParts = [];
  const protect = (s) => {
    protectedParts.push(s);
    return ` ${protectedParts.length - 1} `;
  };
  let work = md
    .replace(/```[\s\S]*?```/g, protect)
    .replace(/`[^`\n]*`/g, protect)
    .replace(/!?\[[^\]]*\]\([^)]*\)/g, protect)
    .replace(/^#{1,6} .*$/gm, protect)
    .replace(/^\|[ :|-]+\|\s*$/gm, protect);
  // NOTE: skipping name-regex replacement (irrelevant to the placeholder-collision question)
  const restored = work.replace(/ (\d+) /g, (_, i) => protectedParts[Number(i)]);
  return { protectedCount: protectedParts.length, work, restored };
}

const root = path.join(__dirname, "..", "content");
for (const rel of ["game-modes/training.md", "dlc/preorder-pack.md", "game-modes/player-match.md"]) {
  const md = bodyOf(path.join(root, rel));
  const r = protectRestore(md);
  console.log("=====", rel, "protectedCount=", r.protectedCount, "=====");
  // show the region around "10 / 15 / 20" or "182"
  for (const needle of ["10 / 15 / 20", "182 roster", "10 / 15 / 20"]) {
    const i = r.restored.indexOf(needle.slice(0, 4));
    if (i >= 0) {
      console.log("  RESTORED:", JSON.stringify(r.restored.slice(Math.max(0, i - 20), i + 40)));
      break;
    }
  }
  // also show whether 'undefined' appears
  console.log("  contains 'undefined':", r.restored.includes("undefined"));
}
