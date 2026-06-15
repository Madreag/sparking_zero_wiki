import fs from "node:fs";
import path from "node:path";
import Link from "next/link";
import { MetaBoard } from "@/components/meta-board";
import { getCharacters } from "@/lib/content";

export const metadata = { title: "Current Meta — Tier Board" };

type TierBand = { tier: string; entries: { name: string; slug: string; score?: number }[] };
type Meta = {
  asOf: string;
  updated: string;
  sourceNote: string;
  singles: TierBand[];
  dp: TierBand[];
  counters: { slug: string; name: string; beats: string[]; losesTo: string[]; why: string }[];
  unmatched?: string[];
};

export default function Page() {
  const p = path.join(process.cwd(), "data-mined", "meta.json");
  if (!fs.existsSync(p)) {
    return <p className="text-muted">Meta data not generated yet — see the <Link className="text-ki underline" href="/guides/current-meta-tier-list">tier-list guide</Link>.</p>;
  }
  const meta = JSON.parse(fs.readFileSync(p, "utf8")) as Meta;
  const nameOf: Record<string, string> = {};
  for (const c of getCharacters()) nameOf[c.slug] = c.name;

  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-bold">Current Meta — Tier Board</h1>
        <p className="mt-1 max-w-3xl text-sm text-muted">
          As of <strong className="text-ink">{meta.asOf}</strong> · synthesized {meta.updated}.{" "}
          {meta.sourceNote} Singles ranks raw 1v1 power; DP ranks points-per-DP value. Read the{" "}
          <Link href="/guides/meta-analysis-june-2026" className="font-medium text-aura underline">
            full meta analysis (why these tiers — trait fingerprint, patterns, sleepers)
          </Link>
          . Full reasoning in the{" "}
          <Link href="/guides/current-meta-tier-list" className="text-ki underline">
            written tier list
          </Link>{" "}
          and{" "}
          <Link href="/guides/matchups-and-counterpicks" className="text-ki underline">
            matchup guide
          </Link>
          .
        </p>
      </header>
      <MetaBoard
        singles={meta.singles}
        dp={meta.dp}
        counters={meta.counters}
        unmatched={meta.unmatched}
        nameOf={nameOf}
      />
    </div>
  );
}
