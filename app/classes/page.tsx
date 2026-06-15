import Link from "next/link";
import { getCharacters } from "@/lib/content";
import { fmtNum } from "@/lib/formulas";

export const metadata = { title: "Class Exceptions — every deviation group" };

type C = ReturnType<typeof getCharacters>[number];

function Chips({ items }: { items: { c: C; note?: string }[] }) {
  return (
    <div className="mt-2 flex flex-wrap gap-1.5">
      {items
        .sort((a, b) => a.c.name.localeCompare(b.c.name))
        .map(({ c, note }) => (
          <Link
            key={c.slug}
            href={`/characters/${c.slug}`}
            className="rounded-lg border border-border bg-surface-2 px-2 py-1 text-xs transition-colors hover:border-ki/60"
          >
            {c.name}
            {note && <span className="ml-1 tabular-nums text-aura">{note}</span>}
            {c.dp != null && <span className="ml-1 text-muted">DP{c.dp}</span>}
          </Link>
        ))}
    </div>
  );
}

function Section({
  title,
  desc,
  items,
  tone = "border-border",
}: {
  title: string;
  desc: string;
  items: { c: C; note?: string }[];
  tone?: string;
}) {
  if (!items.length) return null;
  return (
    <section className={`rounded-xl border ${tone} bg-surface p-4`}>
      <div className="flex flex-wrap items-baseline gap-2">
        <h2 className="font-semibold">{title}</h2>
        <span className="text-sm tabular-nums text-ki">{items.length}</span>
      </div>
      <p className="mt-1 max-w-3xl text-sm text-muted">{desc}</p>
      <Chips items={items} />
    </section>
  );
}

export default function Page() {
  const chars = getCharacters().filter((c) => c.playable);
  const pick = (pred: (c: C) => boolean, note?: (c: C) => string) =>
    chars.filter(pred).map((c) => ({ c, note: note?.(c) }));

  return (
    <div className="space-y-5">
      <header>
        <h1 className="text-2xl font-bold">Class Exceptions</h1>
        <p className="mt-1 max-w-3xl text-sm text-muted">
          Every group that deviates from the standard chassis (40,000 HP · ki charge 7 · 1,750/s
          recovery · 6 skill stocks · 30k supers · 50k ultimates), with the exact datamined value.
          Per-fighter view: <Link href="/dna" className="text-ki underline">Roster DNA</Link> ·
          why these traits decide tiers:{" "}
          <Link href="/guides/meta-analysis-june-2026" className="text-ki underline">
            Meta Analysis
          </Link>
          .
        </p>
      </header>

      <Section
        title="Androids — cannot charge ki"
        desc="Manual charge speed is 0: they live on passive recovery only, and start with bonus resources to compensate."
        items={pick((c) => c.kiChargeSpeed === 0)}
        tone="border-time/40"
      />
      <Section
        title="Absorption engines — 4,500/s recovery"
        desc="The energy-absorption pair recovers ki at 2.6× the standard rate — the highest in the game."
        items={pick((c) => (c.kiAutoRecovery ?? 0) >= 4000, (c) => `${fmtNum(c.kiAutoRecovery)}/s`)}
        tone="border-good/40"
      />
      <Section
        title="Elite ki recovery (2,000–2,250/s)"
        desc="The 'angel engine' group — the single strongest meta predictor (46% of S-tier vs 6% of the unranked pool)."
        items={pick(
          (c) => (c.kiAutoRecovery ?? 0) >= 2000 && (c.kiAutoRecovery ?? 0) < 4000,
          (c) => `${fmtNum(c.kiAutoRecovery)}/s`,
        )}
        tone="border-good/40"
      />
      <Section
        title="Heavyweights — 45,000 HP"
        desc="One extra half-bar of health (4.5 bars total). 38% of S-tier comes from this group of 16."
        items={pick((c) => c.hp === 45000)}
        tone="border-good/40"
      />
      <Section
        title="Lightweights — 30,000 HP"
        desc="A full bar below standard — fragile by design; none reach above C tier."
        items={pick((c) => c.hp === 30000)}
        tone="border-danger/40"
      />
      <Section
        title="Mid-light — 35,000 HP"
        desc="Half a bar under standard (kids, teens, support casts)."
        items={pick((c) => c.hp === 35000)}
        tone="border-danger/30"
      />
      <Section
        title="Skill-stock cap: 4 (vs standard 6)"
        desc="A datamined hard ceiling — zero fighters with this cap reach S tier; 58% of C/D carries it."
        items={pick((c) => (c.maxSkillStock ?? 6) === 4)}
        tone="border-danger/40"
      />
      <Section
        title="Skill-stock cap: 7 — unique"
        desc="Babidi alone exceeds the standard cap."
        items={pick((c) => (c.maxSkillStock ?? 6) === 7)}
        tone="border-aura/40"
      />
      <Section
        title="Bonus starting stocks"
        desc="Start the round with skill resources already banked (standard fighters build from less)."
        items={pick((c) => (c.initialSkillStock ?? 0) >= 2, (c) => `starts ${c.initialSkillStock}`)}
        tone="border-good/40"
      />
      <Section
        title="4-bar ki starters"
        desc="Open the round with 40,000 ki — immediate super/pressure threat."
        items={pick((c) => c.initialKi === 40000)}
        tone="border-good/40"
      />
      <Section
        title="3-bar ki starters"
        desc="Open with 30,000 ki (54% of S-tier starts high)."
        items={pick((c) => c.initialKi === 30000)}
        tone="border-good/30"
      />
      <Section
        title="1-bar ki starters"
        desc="Open with only 10,000 ki — must charge before threatening supers."
        items={pick((c) => c.initialKi === 10000)}
        tone="border-danger/30"
      />
      <Section
        title="Giant class"
        desc="Super-armor bodies with bespoke rules: 2-bar dashes, throw immunity, post-nerf damage modifiers — see the giant-class mechanics page."
        items={pick((c) => c.classes.includes("Giant"))}
        tone="border-time/40"
      />
      <Section
        title="Fusion class"
        desc="Reached mid-battle via partners (3–5 stocks) or drafted directly — the Singles S-tier is dominated by them."
        items={pick((c) => c.classes.includes("Fusion"))}
        tone="border-time/40"
      />
      <Section
        title="Unblockable-skill owners"
        desc="Carry an S1/S2 flagged unguardable in the data — over-represented at LOW tiers (gimmick compensation, not power)."
        items={pick((c) =>
          c.moveset.some((m) => m.type === "blast1" && (m.properties ?? []).includes("unblockable")),
        )}
        tone="border-aura/40"
      />
    </div>
  );
}
