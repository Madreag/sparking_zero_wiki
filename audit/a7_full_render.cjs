// Faithful copy of lib/markdown.ts renderMarkdown (minus marked.parse) using the dumped maps.
const fs = require("fs");
const path = require("path");

const maps = JSON.parse(fs.readFileSync(path.join(__dirname, "a7_maps.json"), "utf8"));
const index = new Map(Object.entries(maps.index));
const nameMap = new Map(Object.entries(maps.nameMap));
const names = maps.names;

function escapeRe(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); }
const regex = new RegExp(`(?<![\\w/\\[])(${names.map(escapeRe).join("|")})(?![\\w\\]])`, "gi");

function autolink(md, excludeHref) {
  const protectedParts = [];
  const protect = (s) => { protectedParts.push(s); return ` ${protectedParts.length - 1} `; };
  let work = md
    .replace(/```[\s\S]*?```/g, protect)
    .replace(/`[^`\n]*`/g, protect)
    .replace(/!?\[[^\]]*\]\([^)]*\)/g, protect)
    .replace(/^#{1,6} .*$/gm, protect)
    .replace(/^\|[ :|-]+\|\s*$/gm, protect);
  const seen = new Set();
  work = work.replace(regex, (match) => {
    const key = match.toLowerCase();
    const entry = nameMap.get(key);
    if (!entry || entry === excludeHref || seen.has(key)) return match;
    seen.add(key);
    return `[${match}](${entry})`;
  });
  return work.replace(/ (\d+) /g, (_, i) => protectedParts[Number(i)]);
}

function renderMarkdownNoMarked(md, excludeHref) {
  const withLinks = md.replace(/\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g, (_m, target, label) => {
    const key = target.trim().toLowerCase().replace(/\s+/g, "-");
    const text = (label ?? target).trim();
    const entry = index.get(key);
    return entry ? `[${text}](${entry})` : text;
  });
  return autolink(withLinks, excludeHref);
}

function bodyOf(p) {
  const raw = fs.readFileSync(p, "utf8");
  const m = raw.match(/^---\r?\n[\s\S]*?\r?\n---\r?\n/);
  return m ? raw.slice(m[0].length).trim() : raw.trim();
}

const root = path.join(__dirname, "..", "content");
const cases = [
  ["game-modes/training.md", "10 / 15 / 20"],
  ["dlc/preorder-pack.md", "182 roster"],
  ["game-modes/player-match.md", "10 / 15 / 20"],
  ["episode-battles/episode-frieza.md", "chapters 2"],
];
for (const [rel, needle] of cases) {
  const out = renderMarkdownNoMarked(bodyOf(path.join(root, rel)));
  const i = out.indexOf(needle.slice(0, 5));
  console.log(`\n===== ${rel} =====`);
  console.log("  contains 'undefined':", out.includes("undefined"));
  if (i >= 0) console.log("  region:", JSON.stringify(out.slice(Math.max(0, i - 30), i + 50)));
}
