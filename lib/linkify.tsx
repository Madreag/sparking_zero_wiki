import Link from "next/link";
import type { ReactNode } from "react";
import { getSlugIndex } from "./content";

/**
 * Entity auto-linking: any mention of a known page's display name becomes a link.
 * Built once per process from the cross-collection slug index.
 */

const STOP = new Set(["base", "story", "standard", "wish", "shop — other"]);

function escapeRe(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

let _idx: { map: Map<string, string>; regex: RegExp } | null = null;

export function getNameIndex() {
  if (_idx) return _idx;
  const map = new Map<string, string>();
  for (const [, { href, label }] of getSlugIndex()) {
    if (!label || label.length < 4) continue;
    if (STOP.has(label.toLowerCase())) continue;
    if (label.includes("→")) continue; // transformation edge names don't occur in prose
    const key = label.toLowerCase();
    if (!map.has(key)) map.set(key, href);
  }
  const names = [...map.keys()].sort((a, b) => b.length - a.length);
  const regex = new RegExp(
    `(?<![\\w/\\[])(${names.map(escapeRe).join("|")})(?![\\w\\]])`,
    "gi",
  );
  _idx = { map, regex };
  return _idx;
}

/**
 * Turn entity mentions in a plain string into links (first mention per entity).
 * Server-component safe. `excludeHref` prevents self-links.
 */
export function linkifyText(text: string, excludeHref?: string): ReactNode {
  const { map, regex } = getNameIndex();
  const nodes: ReactNode[] = [];
  const seen = new Set<string>();
  let last = 0;
  regex.lastIndex = 0;
  let m: RegExpExecArray | null;
  while ((m = regex.exec(text)) !== null) {
    const key = m[1].toLowerCase();
    const href = map.get(key);
    if (!href || href === excludeHref || seen.has(key)) continue;
    seen.add(key);
    nodes.push(text.slice(last, m.index));
    nodes.push(
      <Link key={`${m.index}-${key}`} href={href} className="text-ki hover:underline">
        {m[1]}
      </Link>,
    );
    last = m.index + m[1].length;
  }
  nodes.push(text.slice(last));
  return nodes;
}
