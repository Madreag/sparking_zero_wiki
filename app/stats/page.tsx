import Link from "next/link";
import { fmtNum } from "@/lib/formulas";
import { CURRENT_VERSION } from "@/lib/version";
import constantsData from "@/data-mined/system_constants.json";
import ranksData from "@/data-mined/ranks.json";

export const metadata = { title: "Stats & System Constants" };

type DistRow = { value: number; count: number; examples: string[] };
type HpRow = { hp: number; count: number; examples: string[] };
type GenericBullet = {
  action: string;
  power: number | null;
  chip: number | null;
  beamPower: number | null;
  beamChip: number | null;
  kiCost: number | null;
};
type Constants = {
  hpDistribution: HpRow[];
  kiChargeSpeedDistribution: DistRow[];
  kiAutoRecoveryDistribution: DistRow[];
  sparkingDrainDistribution: DistRow[];
  maxSkillStockDistribution: DistRow[];
  initialSkillStockDistribution: DistRow[];
  initialKiDistribution: DistRow[];
  kiBlastShotsDistribution: DistRow[];
  genericKiBlasts: GenericBullet[];
};
type Rank = { id: string; name: string | null };

function DistTable({
  title,
  rows,
  unit,
  note,
}: {
  title: string;
  rows: DistRow[];
  unit?: string;
  note?: string;
}) {
  if (!rows?.length) return null;
  return (
    <section className="space-y-2">
      <h2 className="text-lg font-semibold">{title}</h2>
      {note && <p className="max-w-3xl text-sm text-muted">{note}</p>}
      <div className="overflow-x-auto rounded-xl border border-border">
        <table className="w-full min-w-[560px] text-sm">
          <thead className="bg-surface-2 text-left text-xs uppercase tracking-wide text-muted">
            <tr>
              <th className="px-3 py-2 text-right">Value{unit ? ` (${unit})` : ""}</th>
              <th className="px-3 py-2 text-right">Fighters</th>
              <th className="px-3 py-2">Examples</th>
            </tr>
          </thead>
          <tbody>
            {rows.map((r) => (
              <tr key={r.value} className="border-t border-border">
                <td className="px-3 py-2 text-right font-semibold tabular-nums text-aura">{fmtNum(r.value)}</td>
                <td className="px-3 py-2 text-right tabular-nums">{r.count}</td>
                <td className="px-3 py-2 text-muted">{r.examples.slice(0, 7).join(", ")}…</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}

export default function Page() {
  // Static imports keep Next's file-tracer from conservatively bundling the whole
  // project (incl. data-mined/raw/) the way a process.cwd()+dynamic-path read did.
  const c = constantsData as unknown as Constants;
  const ranks = ranksData as unknown as Rank[];

  return (
    <div className="space-y-8">
      <header>
        <h1 className="text-2xl font-bold">Stats & System Constants</h1>
        <p className="mt-1 max-w-3xl text-sm text-muted">
          Datamined from the live game build ({CURRENT_VERSION.patch}). Units:{" "}
          <strong className="text-ink">10,000 energy = 1 ki bar</strong>; health bars hold 10,000
          HP each. Field semantics verified by value-matching against the current-patch schema
          dump.
        </p>
      </header>

      <section className="space-y-2">
        <h2 className="text-lg font-semibold">Health (HP) tiers — entire cast</h2>
        <div className="overflow-x-auto rounded-xl border border-border">
          <table className="w-full min-w-[560px] text-sm">
            <thead className="bg-surface-2 text-left text-xs uppercase tracking-wide text-muted">
              <tr>
                <th className="px-3 py-2 text-right">HP</th>
                <th className="px-3 py-2 text-right">Bars</th>
                <th className="px-3 py-2 text-right">Fighters</th>
                <th className="px-3 py-2">Examples</th>
              </tr>
            </thead>
            <tbody>
              {c.hpDistribution.map((r) => (
                <tr key={r.hp} className="border-t border-border">
                  <td className="px-3 py-2 text-right font-semibold tabular-nums text-aura">{fmtNum(r.hp)}</td>
                  <td className="px-3 py-2 text-right tabular-nums">{r.hp / 10000}</td>
                  <td className="px-3 py-2 text-right tabular-nums">{r.count}</td>
                  <td className="px-3 py-2 text-muted">{r.examples.slice(0, 7).join(", ")}…</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      <DistTable
        title="Manual ki-charge speed"
        rows={c.kiChargeSpeedDistribution}
        note="0 = cannot charge manually (Androids — they rely on auto-recovery only). Standard cast charges at 7."
      />
      <DistTable
        title="Passive ki auto-recovery"
        rows={c.kiAutoRecoveryDistribution}
        unit="energy/s"
        note="Energy per second recovered passively. 1,750 standard; elite angels/androids reach 2,000–2,250."
      />
      <DistTable
        title="Starting ki"
        rows={c.initialKiDistribution}
        unit="energy"
        note="Fighters with a non-standard opening ki pool (30,000 = 3 bars at round start)."
      />
      <DistTable
        title="Max skill stocks"
        rows={c.maxSkillStockDistribution}
        note="Skill-count capacity. Standard maximum is 6; entries here are explicit per-character overrides."
      />
      <DistTable
        title="Starting skill stocks"
        rows={c.initialSkillStockDistribution}
        note="Stocks at round start where overridden (e.g. Androids start with extra; nerfed stallers start at 0)."
      />
      <DistTable
        title="Sparking! Mode gauge drain"
        rows={c.sparkingDrainDistribution}
        unit="gauge/s"
        note="How fast the Sparking! gauge empties while Sparking is active — 2,800/s standard. (This is the field the launch-era schema mislabeled; it is NOT a vanish cost.)"
      />
      <DistTable
        title="Ki-blast volley size"
        rows={c.kiBlastShotsDistribution}
        unit="shots"
        note="Maximum rapid-fire ki blasts per volley."
      />

      <section className="space-y-2">
        <h2 className="text-lg font-semibold">Generic ki-blast & shared projectile defaults</h2>
        <p className="max-w-3xl text-sm text-muted">
          Datamined defaults shared across the cast (per-move overrides appear on each{" "}
          <Link href="/blasts" className="text-ki underline">
            blast page
          </Link>
          ). Power is per hit vs a 40,000-HP fighter; chip is damage through guard.
        </p>
        <div className="overflow-x-auto rounded-xl border border-border">
          <table className="w-full min-w-[640px] text-sm">
            <thead className="bg-surface-2 text-left text-xs uppercase tracking-wide text-muted">
              <tr>
                <th className="px-3 py-2">Projectile (action)</th>
                <th className="px-3 py-2 text-right">Power</th>
                <th className="px-3 py-2 text-right">Chip</th>
                <th className="px-3 py-2 text-right">Beam power</th>
                <th className="px-3 py-2 text-right">Beam chip</th>
                <th className="px-3 py-2 text-right">Ki cost</th>
              </tr>
            </thead>
            <tbody>
              {c.genericKiBlasts.map((b) => (
                <tr key={b.action} className="border-t border-border">
                  <td className="px-3 py-2 font-mono text-xs">{b.action}</td>
                  <td className="px-3 py-2 text-right tabular-nums text-aura">{fmtNum(b.power)}</td>
                  <td className="px-3 py-2 text-right tabular-nums">{fmtNum(b.chip)}</td>
                  <td className="px-3 py-2 text-right tabular-nums">{fmtNum(b.beamPower)}</td>
                  <td className="px-3 py-2 text-right tabular-nums">{fmtNum(b.beamChip)}</td>
                  <td className="px-3 py-2 text-right tabular-nums">{fmtNum(b.kiCost)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      <section className="space-y-2">
        <h2 className="text-lg font-semibold">Ranked ladder — {ranks.length} tiers</h2>
        <p className="text-sm text-muted">{CURRENT_VERSION.rankedSeason}.</p>
        <div className="flex flex-wrap gap-1.5">
          {ranks.map((r) => (
            <span
              key={r.id}
              className={`rounded border px-2 py-1 text-xs font-medium tabular-nums ${
                r.name === "Z"
                  ? "border-aura/50 bg-aura/15 text-aura"
                  : r.name?.startsWith("S")
                    ? "border-ki/50 bg-ki/10 text-ki"
                    : "border-border bg-surface-2 text-muted"
              }`}
            >
              {r.name}
            </span>
          ))}
        </div>
      </section>
    </div>
  );
}
