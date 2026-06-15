import Link from "next/link";
import { notFound } from "next/navigation";
import { getCharacter, getCharacters } from "@/lib/content";
import { renderMarkdown } from "@/lib/markdown";
import { fmtNum } from "@/lib/formulas";
import { linkifyText } from "@/lib/linkify";
import { StatStrip, ConfidenceBadge, VerifiedBadge, TierBadge } from "@/components/ui";

export function generateStaticParams() {
  return getCharacters().map((c) => ({ slug: c.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const c = getCharacter(slug);
  return { title: c ? c.name : "Fighter" };
}

const moveTypeLabel: Record<string, string> = {
  rush: "Rush",
  smash: "Smash",
  throw: "Throw",
  blast1: "Skill (S1/S2)",
  blast2: "Super (B2)",
  ultimate: "Ultimate",
  evasive: "Evasive",
  special: "Special",
};

function slugifyName(s: string): string {
  return s
    .toLowerCase()
    .replace(/['’!.]/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

function moveHref(name: string, type: string): string | null {
  const s = slugifyName(name);
  if (type === "blast2") return `/blasts/${s}-super`;
  if (type === "ultimate") return `/blasts/${s}-ultimate`;
  if (type === "blast1") return `/skills/${s}`;
  return null;
}

export default async function Page({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const c = getCharacter(slug);
  if (!c) notFound();
  const self = `/characters/${c.slug}`;

  const siblings = getCharacters().filter(
    (x) => x.baseCharacter === c.baseCharacter && x.slug !== c.slug,
  );

  const isAndroidNoCharge = c.kiChargeSpeed === 0;
  const params2: { label: string; value: string; note?: string }[] = [
    {
      label: "Health (Life)",
      value: fmtNum(c.hp),
      note: c.hpInherited
        ? "inherited from sibling form"
        : c.hp != null
          ? `${(c.hp / 10000).toLocaleString()} bars`
          : undefined,
    },
    {
      label: "Ki charge speed",
      value: fmtNum(c.kiChargeSpeed),
      note: isAndroidNoCharge ? "cannot charge manually (auto-recovery only)" : undefined,
    },
    {
      label: "Ki auto-recovery",
      value: c.kiAutoRecovery != null ? `${fmtNum(c.kiAutoRecovery)} /s` : "—",
      note: c.kiAutoRecoveryLimit != null ? `caps at ${fmtNum(c.kiAutoRecoveryLimit)}` : undefined,
    },
    {
      label: "Starting ki",
      value: c.initialKi != null ? fmtNum(c.initialKi) : "standard",
      note: c.initialKi != null ? `${(c.initialKi / 10000).toLocaleString()} bars at round start` : undefined,
    },
    {
      label: "Skill stocks",
      value:
        c.initialSkillStock != null || c.maxSkillStock != null
          ? `${c.initialSkillStock ?? "std"} start / ${c.maxSkillStock ?? "std"} max`
          : "standard",
    },
    {
      label: "Sparking! gauge drain",
      value: c.sparkingDrainPerSec != null ? `${fmtNum(c.sparkingDrainPerSec)} /s` : "—",
      note: "gauge drain while Sparking! is active",
    },
    { label: "Ki-blast volley", value: c.kiBlastShots != null ? `${c.kiBlastShots} shots` : "—" },
  ];

  const gaugeGainLabels: Record<string, string> = {
    vanishExchangeRate: "Vanish-exchange gain rate",
    attackBreak: "Attack break",
    fastAvoid: "Fast dodge",
    throwBreak: "Throw escape",
    hitFromBehind: "Hit from behind",
    lastHPGauge: "On last health bar",
    impactStart: "Impact start",
  };
  const gaugeGains = Object.entries(c.skillGaugeGains ?? {}).filter(([, v]) => v != null);

  return (
    <article className="space-y-6">
      <div>
        <Link href="/characters" className="text-xs text-muted hover:text-ink">
          ← Roster
        </Link>
        <div className="mt-2 flex flex-wrap items-center gap-3">
          <h1 className="text-2xl font-bold">{c.name}</h1>
          <TierBadge tier={c.tier} />
          {c.playstyle && (
            <span className="rounded border border-time/50 bg-time/10 px-1.5 py-0.5 text-xs text-time">
              {c.playstyle}
            </span>
          )}
          {!c.playable && (
            <span className="rounded border border-border bg-surface-2 px-1.5 py-0.5 text-xs uppercase text-muted">
              Story-only — not selectable in versus
            </span>
          )}
          <ConfidenceBadge confidence={c.confidence} />
        </div>
        {c.summary && <p className="mt-2 max-w-3xl text-muted">{linkifyText(c.summary, self)}</p>}
      </div>

      <StatStrip
        items={[
          { label: "DP cost", value: c.dp ?? (c.playable ? undefined : "n/a"), tone: "aura" },
          { label: "HP", value: fmtNum(c.hp), tone: "good" },
          { label: "Era", value: c.era !== "Story-only" ? c.era : undefined, tone: "muted" },
          { label: "Source", value: c.source, tone: c.source === "Base" ? "good" : "aura" },
          { label: "Classes", value: c.classes.length ? c.classes.join(", ") : undefined, tone: "time" },
          { label: "Unlock", value: c.unlock, tone: "muted" },
        ]}
      />

      <div className="grid gap-4 lg:grid-cols-2">
        <section className="rounded-xl border border-border bg-surface">
          <h2 className="border-b border-border px-4 py-2.5 text-xs font-semibold uppercase tracking-wider text-muted">
            Datamined battle parameters
          </h2>
          <table className="w-full text-sm" data-sortable-self>
            <tbody>
              {params2.map((p) => (
                <tr key={p.label} className="border-b border-border last:border-0">
                  <td className="px-4 py-2 text-muted">{p.label}</td>
                  <td className="px-4 py-2 text-right font-semibold tabular-nums text-aura">{p.value}</td>
                  <td className="px-4 py-2 text-right text-xs text-muted">{p.note ?? ""}</td>
                </tr>
              ))}
            </tbody>
          </table>
          {gaugeGains.length > 0 && (
            <>
              <h2 className="border-y border-border px-4 py-2.5 text-xs font-semibold uppercase tracking-wider text-muted">
                Skill-stock gauge gains (per action)
              </h2>
              <table className="w-full text-sm" data-sortable-self>
                <tbody>
                  {gaugeGains.map(([k, v]) => (
                    <tr key={k} className="border-b border-border last:border-0">
                      <td className="px-4 py-2 text-muted">{gaugeGainLabels[k] ?? k}</td>
                      <td className="px-4 py-2 text-right font-semibold tabular-nums text-good">
                        {k === "vanishExchangeRate" ? `×${v}` : `+${v}`}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </>
          )}
        </section>

        <div className="grid gap-4">
          {c.strengths.length > 0 && (
            <section className="rounded-xl border border-good/30 bg-surface p-4">
              <h2 className="text-xs font-semibold uppercase tracking-wider text-good">Strengths</h2>
              <ul className="mt-2 list-disc space-y-1.5 pl-4 text-sm leading-relaxed">
                {c.strengths.map((s, i) => (
                  <li key={i}>{linkifyText(s, self)}</li>
                ))}
              </ul>
            </section>
          )}
          {c.weaknesses.length > 0 && (
            <section className="rounded-xl border border-danger/30 bg-surface p-4">
              <h2 className="text-xs font-semibold uppercase tracking-wider text-danger">Weaknesses</h2>
              <ul className="mt-2 list-disc space-y-1.5 pl-4 text-sm leading-relaxed">
                {c.weaknesses.map((s, i) => (
                  <li key={i}>{linkifyText(s, self)}</li>
                ))}
              </ul>
            </section>
          )}
        </div>
      </div>

      {c.howToFight && (
        <section className="rounded-xl border border-aura/40 bg-aura/5 p-4">
          <h2 className="text-xs font-semibold uppercase tracking-wider text-aura">
            How to fight against {c.name}
          </h2>
          <p className="mt-2 max-w-4xl text-sm leading-relaxed">{linkifyText(c.howToFight, self)}</p>
        </section>
      )}

      {c.moveset.length > 0 && (
        <section className="space-y-2">
          <h2 className="text-lg font-semibold">
            Moveset <span className="text-sm font-normal text-muted">(costs datamined · click headers to sort)</span>
          </h2>
          <div className="overflow-x-auto rounded-xl border border-border">
            <table className="w-full text-sm">
              <thead className="bg-surface-2 text-left text-xs uppercase tracking-wide text-muted">
                <tr>
                  <th className="px-3 py-2">Move</th>
                  <th className="px-3 py-2">Type</th>
                  <th className="px-3 py-2 text-right">Ki cost</th>
                  <th className="px-3 py-2 text-right">Skill stocks</th>
                  <th className="px-3 py-2 text-right">Damage</th>
                  <th className="px-3 py-2">Properties</th>
                </tr>
              </thead>
              <tbody>
                {c.moveset.map((m, i) => {
                  const href = moveHref(m.name, m.type);
                  return (
                    <tr key={i} className="border-t border-border">
                      <td className="px-3 py-2 font-medium">
                        {href ? (
                          <Link href={href} className="text-ki hover:underline">
                            {m.name}
                          </Link>
                        ) : (
                          m.name
                        )}
                      </td>
                      <td className="px-3 py-2 text-muted">{moveTypeLabel[m.type] ?? m.type}</td>
                      <td className="px-3 py-2 text-right tabular-nums">{fmtNum(m.kiCost)}</td>
                      <td className="px-3 py-2 text-right tabular-nums">{fmtNum(m.skillCost)}</td>
                      <td className="px-3 py-2 text-right tabular-nums">{fmtNum(m.damage)}</td>
                      <td className="px-3 py-2 text-xs text-muted">
                        {[m.notes, ...(m.properties ?? [])].filter(Boolean).join(" · ") || "—"}
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
          <p className="text-xs text-muted">
            10,000 energy = 1 ki bar. Per-move damage lives in move blueprints, not parameter
            tables — community-labbed values appear where verified; see{" "}
            <Link href="/mechanics/health-and-damage" className="text-ki underline">
              Health &amp; Damage
            </Link>
            .
          </p>
        </section>
      )}

      {c.transformsTo.length > 0 && (
        <section className="space-y-2">
          <h2 className="text-lg font-semibold">Transformations & fusions</h2>
          <div className="flex flex-wrap gap-2">
            {c.transformsTo.map((t, i) => (
              <Link
                key={i}
                href={t.targetSlug ? `/characters/${t.targetSlug}` : "#"}
                className="rounded-lg border border-time/40 bg-time/10 px-2.5 py-1.5 text-sm transition-colors hover:bg-time/20"
              >
                {t.kind === "fusion" ? "⧉ " : "↑ "}
                {t.target}
                {t.cost != null && <span className="ml-1.5 text-xs text-muted">{t.cost} stocks</span>}
              </Link>
            ))}
          </div>
        </section>
      )}

      {c.body && (
        <div
          className="prose max-w-none text-sm"
          dangerouslySetInnerHTML={{ __html: renderMarkdown(c.body, { excludeHref: self }) }}
        />
      )}

      {siblings.length > 0 && (
        <section>
          <h2 className="mb-2 text-lg font-semibold">Other forms of {c.baseCharacter}</h2>
          <div className="flex flex-wrap gap-2 text-sm">
            {siblings.map((s) => (
              <Link
                key={s.slug}
                href={`/characters/${s.slug}`}
                className="rounded border border-border bg-surface-2 px-2 py-1 hover:border-ki/60"
              >
                {s.name}
                {s.dp != null && <span className="ml-1.5 text-xs text-aura">DP {s.dp}</span>}
              </Link>
            ))}
          </div>
        </section>
      )}

      <div className="flex flex-wrap items-center justify-between gap-2 border-t border-border pt-4 text-xs text-muted">
        <span className="flex items-center gap-1">
          As of {c.asOfVersion ?? "?"} · internal ID <code>{c.charId}</code> · last verified{" "}
          <VerifiedBadge lastVerified={c.lastVerified} />
        </span>
        {c.sources.length > 0 && <span>Source: {c.sources.join("; ")}</span>}
      </div>
    </article>
  );
}
