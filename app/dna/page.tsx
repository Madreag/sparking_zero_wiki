import Link from "next/link";
import { getCharacters } from "@/lib/content";
import { fmtNum } from "@/lib/formulas";
import { DnaExplorer, type DnaRow, type Badge } from "@/components/dna-explorer";

export const metadata = { title: "Roster DNA — what makes each fighter unique" };

const BASE = {
  hp: 40000,
  charge: 7,
  recovery: 1750,
  maxStocks: 6,
  supersKi: 30000,
  ultKi: 50000,
  sparkingDrain: 2800,
  kiBlastDmg: 200,
};

export default function Page() {
  const chars = getCharacters().filter((c) => c.playable);
  const groups = [
    "HP",
    "Android",
    "Giant",
    "Fusion",
    "Ki engine",
    "Skill stocks",
    "Unblockable",
    "Transforms",
  ];

  const rows: DnaRow[] = chars
    .map((c) => {
      const badges: Badge[] = [];
      if (c.hp != null && c.hp !== BASE.hp) {
        badges.push({
          label: `HP ${fmtNum(c.hp)} (${c.hp > BASE.hp ? "+" : ""}${fmtNum(c.hp - BASE.hp)})`,
          tone: c.hp > BASE.hp ? "good" : "bad",
          group: "HP",
        });
      }
      if (c.kiChargeSpeed === 0) {
        badges.push({ label: "cannot charge ki (Android engine)", tone: "time", group: "Android" });
      } else if (c.kiChargeSpeed != null && c.kiChargeSpeed !== BASE.charge) {
        badges.push({
          label: `ki charge ${c.kiChargeSpeed} (${c.kiChargeSpeed > BASE.charge ? "fast" : "slow"})`,
          tone: c.kiChargeSpeed > BASE.charge ? "good" : "bad",
          group: "Ki engine",
        });
      }
      if (c.kiAutoRecovery != null && c.kiAutoRecovery !== BASE.recovery) {
        badges.push({
          label: `recovery ${fmtNum(c.kiAutoRecovery)}/s`,
          tone: c.kiAutoRecovery > BASE.recovery ? "good" : "bad",
          group: "Ki engine",
        });
      }
      if (c.initialKi != null) {
        badges.push({
          label: `starts ${c.initialKi / 10000} bar${c.initialKi === 10000 ? "" : "s"} ki`,
          tone: c.initialKi >= 30000 ? "good" : "bad",
          group: "Ki engine",
        });
      }
      if (c.maxSkillStock != null && c.maxSkillStock !== BASE.maxStocks) {
        badges.push({
          label: `max ${c.maxSkillStock} stocks`,
          tone: c.maxSkillStock > BASE.maxStocks ? "good" : "bad",
          group: "Skill stocks",
        });
      }
      if (c.initialSkillStock != null) {
        badges.push({
          label: `starts ${c.initialSkillStock} stock${c.initialSkillStock === 1 ? "" : "s"}`,
          tone: c.initialSkillStock >= 2 ? "good" : "muted",
          group: "Skill stocks",
        });
      }
      for (const cls of c.classes) {
        if (["Giant", "Fusion", "Android"].includes(cls)) {
          badges.push({ label: cls, tone: "time", group: cls });
        }
      }
      const ub = c.moveset.filter(
        (m) => m.type === "blast1" && (m.properties ?? []).includes("unblockable"),
      );
      for (const m of ub) {
        badges.push({ label: `unblockable: ${m.name}`, tone: "aura", group: "Unblockable" });
      }
      const tf = c.transformsTo.filter((t) => t.kind === "transform");
      const fu = c.transformsTo.filter((t) => t.kind === "fusion");
      if (tf.length) {
        const min = Math.min(...tf.map((t) => t.cost ?? 99));
        badges.push({
          label: `transforms (${tf.length}) from ${min} stock${min === 1 ? "" : "s"}`,
          tone: "ki",
          group: "Transforms",
        });
      }
      if (fu.length) {
        badges.push({ label: `fusion access (${fu.length})`, tone: "ki", group: "Transforms" });
      }
      return {
        name: c.name,
        slug: c.slug,
        dp: c.dp,
        tier: c.tier,
        badges,
      };
    })
    .sort((a, b) => b.badges.length - a.badges.length || a.name.localeCompare(b.name));

  const standard = rows.filter((r) => r.badges.length === 0).length;

  return (
    <div className="space-y-8">
      <header>
        <h1 className="text-2xl font-bold">Roster DNA</h1>
        <p className="mt-1 max-w-3xl text-sm text-muted">
          Sparking! ZERO builds all {chars.length} fighters on one shared chassis — what makes a
          fighter unique is their <strong className="text-ink">deviations</strong> from it. This
          page shows only those deviations, so differences are scannable at a glance.{" "}
          {standard} fighters are the pure standard chassis (zero deviations). Grouped view:{" "}
          <Link href="/classes" className="text-ki underline">Class Exceptions</Link> · how traits
          decide tiers:{" "}
          <Link href="/guides/meta-analysis-june-2026" className="text-ki underline">Meta Analysis</Link>.
        </p>
      </header>

      <section className="rounded-xl border border-aura/40 bg-aura/5 p-4">
        <h2 className="text-xs font-semibold uppercase tracking-wider text-aura">
          The standard chassis (datamined baseline)
        </h2>
        <div className="mt-3 grid grid-cols-2 gap-x-6 gap-y-2 text-sm sm:grid-cols-4">
          <div><span className="text-muted">Health</span> <strong className="tabular-nums">{fmtNum(BASE.hp)}</strong> (4 bars)</div>
          <div><span className="text-muted">Ki charge</span> <strong className="tabular-nums">{BASE.charge}</strong></div>
          <div><span className="text-muted">Ki recovery</span> <strong className="tabular-nums">{fmtNum(BASE.recovery)}/s</strong></div>
          <div><span className="text-muted">Max skill stocks</span> <strong className="tabular-nums">{BASE.maxStocks}</strong></div>
          <div><span className="text-muted">Super cost</span> <strong className="tabular-nums">{fmtNum(BASE.supersKi)}</strong> ki</div>
          <div><span className="text-muted">Ultimate cost</span> <strong className="tabular-nums">{fmtNum(BASE.ultKi)}</strong> ki (all 207)</div>
          <div><span className="text-muted">Sparking! drain</span> <strong className="tabular-nums">{fmtNum(BASE.sparkingDrain)}/s</strong></div>
          <div><span className="text-muted">Ki blast</span> <strong className="tabular-nums">{BASE.kiBlastDmg}</strong> dmg / 2,000 ki</div>
        </div>
        <p className="mt-3 text-xs text-muted">
          77% of supers cost exactly 30,000 ki · 100% of ultimates cost 50,000 · 79% of fighters
          have exactly 40,000 HP · see{" "}
          <Link href="/stats" className="text-ki underline">
            Stats
          </Link>{" "}
          for full distributions.
        </p>
      </section>

      <DnaExplorer rows={rows} groups={groups} />
    </div>
  );
}
