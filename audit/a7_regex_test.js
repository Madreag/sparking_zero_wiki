// Throwaway probe: test markdown.ts wikilink regex behavior on generator-emitted escaped-pipe links.
const re = /\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g;

const samples = [
  "From [[jiren\\|Jiren]] to [[jiren-full-power\\|Jiren, Full Power]].", // generator escaped pipe in prose
  "| [[goku-z-early\\|Goku (Z, Early)]] | 2 | — |",                      // generator escaped pipe in table cell
  "See [[health-and-damage]] and [[ki-and-charging]].",                  // plain wikilink, no pipe
  "[[goku-z-early|Goku (Z, Early)]]",                                    // UNescaped pipe (hand-written style)
];

for (const s of samples) {
  console.log("INPUT:", JSON.stringify(s));
  re.lastIndex = 0;
  let m;
  while ((m = re.exec(s)) !== null) {
    const target = m[1];
    const label = m[2];
    const key = target.trim().toLowerCase().replace(/\s+/g, "-"); // normalizeSlug
    console.log(`  match=${JSON.stringify(m[0])}  target=${JSON.stringify(target)}  label=${JSON.stringify(label)}  -> normalizeSlug=${JSON.stringify(key)}`);
  }
  console.log("");
}
