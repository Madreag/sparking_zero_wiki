import Link from "next/link";
import { CURRENT_VERSION } from "@/lib/version";
import {
  getCharacters,
  getBlasts,
  getSkills,
  getMechanics,
  getPatchNotes,
  getDLCs,
  getGuides,
  getStages,
  getShopCategories,
  getEpisodeBattles,
  getGameModes,
  getTransformations,
  getGlossary,
} from "@/lib/content";

export default function Home() {
  const guides = getGuides();
  const features = [
    {
      href: "/meta",
      title: "Current Meta Tier Board",
      desc: `Visual Z→D tiers for Singles & DP with counter-picks — as of ${CURRENT_VERSION.patch}.`,
      tone: "border-aura/50 hover:border-aura",
      tag: "PvP",
    },
    {
      href: "/guides/defense-bible",
      title: "Defense Bible",
      desc: "Every defensive option with its cost and window — what beats what, situation by situation.",
      tone: "border-ki/50 hover:border-ki",
      tag: "PvP",
    },
    {
      href: "/episode-battles",
      title: "Beat the hard fights",
      desc: "Full Episode Battle walkthroughs: every what-if trigger and boss strategies for the infamous walls.",
      tone: "border-time/50 hover:border-time",
      tag: "PvE",
    },
    {
      href: "/guides/beginner-numbers-guide",
      title: "Start here: the 10 numbers",
      desc: "Vanish ≈½ bar · 10k = 1 bar · ult 50k · Super Counter ~2f — the numbers that win games.",
      tone: "border-good/50 hover:border-good",
      tag: "New",
    },
  ];
  const sections = [
    { href: "/characters", label: "Roster", count: getCharacters().length, desc: "Datamined HP, DP, full kits, strengths & weaknesses" },
    { href: "/blasts", label: "Blasts & Ultimates", count: getBlasts().length, desc: "Every named attack with per-user ki costs" },
    { href: "/skills", label: "Skills", count: getSkills().length, desc: "Costs, users, and nerf histories" },
    { href: "/transformations", label: "Transformations", count: getTransformations().length, desc: "Exact stat deltas, stock costs, moveset diffs" },
    { href: "/mechanics", label: "Mechanics", count: getMechanics().length, desc: "Frame windows, ki costs, gauge rates" },
    { href: "/guides", label: "Guides", count: guides.length, desc: "Meta, matchups, ranked, economy, settings" },
    { href: "/episode-battles", label: "Episode Battle", count: getEpisodeBattles().length, desc: "Campaign walkthroughs + boss tactics" },
    { href: "/game-modes", label: "Game Modes", count: getGameModes().length, desc: "Rules and rewards per mode" },
    { href: "/stages", label: "Stages", count: getStages().length, desc: "Every map, variant, destructibility" },
    { href: "/shop", label: "Shop", count: getShopCategories().length, desc: "Full datamined Zeni price tables" },
    { href: "/patches", label: "Patches", count: getPatchNotes().length, desc: "Quantified buffs & nerfs per update" },
    { href: "/dlc", label: "DLC", count: getDLCs().length, desc: "Packs, prices, dates, contents" },
    { href: "/glossary", label: "Glossary", count: getGlossary().length, desc: "Terms with the numbers behind them" },
  ];
  return (
    <div className="space-y-10">
      <section className="space-y-3">
        <h1 className="text-3xl font-bold">
          DRAGON BALL: Sparking! ZERO — <span className="text-ki">numbers-first</span> knowledge base
        </h1>
        <p className="max-w-3xl text-muted">
          Every fighter&apos;s datamined health and ki economy, every transformation&apos;s exact cost
          and stat delta, every patch&apos;s nerf quantified, and the current meta — current to{" "}
          <strong className="text-ink">{CURRENT_VERSION.patch}</strong>. Next:{" "}
          {CURRENT_VERSION.nextContent}.
        </p>
        <div className="flex flex-wrap gap-x-8 gap-y-2 text-sm">
          <span>
            <span className="text-2xl font-bold tabular-nums text-aura">{CURRENT_VERSION.rosterSlots}</span>{" "}
            <span className="text-muted">roster slots</span>
          </span>
          <span>
            <span className="text-2xl font-bold tabular-nums text-aura">{CURRENT_VERSION.dpBudget}</span>{" "}
            <span className="text-muted">DP budget · {CURRENT_VERSION.teamSizeMax} fighters max</span>
          </span>
          <span>
            <span className="text-2xl font-bold tabular-nums text-aura">{CURRENT_VERSION.rankCount}</span>{" "}
            <span className="text-muted">ranked tiers (D5 → Z) · {CURRENT_VERSION.rankedSeason}</span>
          </span>
        </div>
      </section>

      <section className="space-y-3">
        <h2 className="text-sm font-semibold uppercase tracking-wider text-muted">Play smarter</h2>
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {features.map((f) => (
            <Link
              key={f.href}
              href={f.href}
              className={`rounded-xl border bg-surface p-4 transition-colors ${f.tone}`}
            >
              <div className="text-[10px] font-semibold uppercase tracking-wider text-muted">{f.tag}</div>
              <h3 className="mt-1 font-semibold">{f.title}</h3>
              <p className="mt-1 text-xs leading-relaxed text-muted">{f.desc}</p>
            </Link>
          ))}
        </div>
        <div className="flex flex-wrap gap-2 text-sm">
          {guides.map((g) => (
            <Link
              key={g.slug}
              href={`/guides/${g.slug}`}
              className="rounded-lg border border-border bg-surface-2 px-2.5 py-1 text-xs text-muted transition-colors hover:border-ki/60 hover:text-ink"
            >
              {g.title}
            </Link>
          ))}
        </div>
      </section>

      <section className="space-y-3">
        <h2 className="text-sm font-semibold uppercase tracking-wider text-muted">The database</h2>
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {sections.map((s) => (
            <Link
              key={s.href}
              href={s.href}
              className="rounded-xl border border-border bg-surface p-4 transition-colors hover:border-ki/60 hover:bg-surface-2"
            >
              <div className="flex items-baseline justify-between">
                <h3 className="font-semibold">{s.label}</h3>
                <span className="text-lg font-bold tabular-nums text-ki">{s.count}</span>
              </div>
              <p className="mt-1 text-sm text-muted">{s.desc}</p>
            </Link>
          ))}
        </div>
      </section>
    </div>
  );
}
