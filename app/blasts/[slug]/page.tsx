import Link from "next/link";
import { notFound } from "next/navigation";
import { getBlast, getBlasts } from "@/lib/content";
import { renderMarkdown } from "@/lib/markdown";
import { fmtNum } from "@/lib/formulas";
import { StatStrip, ConfidenceBadge, VerifiedBadge } from "@/components/ui";

export function generateStaticParams() {
  return getBlasts().map((b) => ({ slug: b.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const b = getBlast(slug);
  return { title: b ? b.name : "Blast" };
}

export default async function Page({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const b = getBlast(slug);
  if (!b) notFound();
  const self = `/blasts/${b.slug}`;

  const costs = b.users.map((u) => u.kiCost).filter((x): x is number => x != null);
  const dmgs = b.users.map((u) => u.damage).filter((x): x is number => x != null);
  const hasTrigger = b.users.some((u) => u.triggerKiCost != null && u.triggerKiCost !== u.kiCost);
  const hasDamage = dmgs.length > 0;
  const hasTags = b.users.some((u) => u.tags.length > 0);

  return (
    <article className="space-y-6">
      <div>
        <Link href="/blasts" className="text-xs text-muted hover:text-ink">
          ← Blasts & Ultimates
        </Link>
        <div className="mt-2 flex flex-wrap items-center gap-3">
          <h1 className="text-2xl font-bold">{b.name}</h1>
          <span className="rounded border border-border bg-surface-2 px-1.5 py-0.5 text-xs uppercase text-muted">
            {b.class}
          </span>
          {b.category && (
            <span className="rounded border border-time/50 bg-time/10 px-1.5 py-0.5 text-xs text-time">
              {b.category}
            </span>
          )}
          <ConfidenceBadge confidence={b.confidence} />
        </div>
      </div>

      <StatStrip
        items={[
          { label: "Users", value: b.users.length, tone: "ki" },
          {
            label: "Ki cost",
            value: costs.length
              ? [...new Set(costs)].sort((x, y) => x - y).map((c) => fmtNum(c)).join(" / ")
              : undefined,
            tone: "aura",
          },
          {
            label: "Datamined power",
            value: hasDamage
              ? [...new Set(dmgs)].sort((x, y) => x - y).map((d) => fmtNum(d)).join(" / ")
              : undefined,
            tone: "good",
          },
          { label: "Category", value: b.category ?? undefined, tone: "time" },
        ]}
      />

      {b.summary && <p className="max-w-3xl text-muted">{b.summary}</p>}

      <div className="overflow-x-auto rounded-xl border border-border">
        <table className="w-full text-sm">
          <thead className="bg-surface-2 text-left text-xs uppercase tracking-wide text-muted">
            <tr>
              <th className="px-3 py-2">Character</th>
              <th className="px-3 py-2 text-right">Ki</th>
              {hasTrigger && <th className="px-3 py-2 text-right">Trigger ki</th>}
              {hasDamage && <th className="px-3 py-2 text-right">Power</th>}
              {hasDamage && <th className="px-3 py-2 text-right">Chip</th>}
              {hasDamage && <th className="px-3 py-2 text-right">Hits</th>}
              <th className="px-3 py-2">Slot</th>
              {hasTags && <th className="px-3 py-2">Tags</th>}
            </tr>
          </thead>
          <tbody>
            {b.users.map((u, i) => (
              <tr key={i} className="border-t border-border">
                <td className="px-3 py-2">
                  {u.characterSlug ? (
                    <Link href={`/characters/${u.characterSlug}`} className="text-ki hover:underline">
                      {u.character}
                    </Link>
                  ) : (
                    u.character
                  )}
                </td>
                <td className="px-3 py-2 text-right tabular-nums">{fmtNum(u.kiCost)}</td>
                {hasTrigger && (
                  <td className="px-3 py-2 text-right tabular-nums">
                    {u.triggerKiCost != null && u.triggerKiCost !== u.kiCost ? fmtNum(u.triggerKiCost) : "—"}
                  </td>
                )}
                {hasDamage && (
                  <td className="px-3 py-2 text-right font-semibold tabular-nums text-aura">
                    {fmtNum(u.damage)}
                  </td>
                )}
                {hasDamage && <td className="px-3 py-2 text-right tabular-nums">{fmtNum(u.chip)}</td>}
                {hasDamage && <td className="px-3 py-2 text-right tabular-nums">{fmtNum(u.hits)}</td>}
                <td className="px-3 py-2 text-muted">{u.notes ?? "—"}</td>
                {hasTags && (
                  <td className="px-3 py-2 text-xs text-muted">{u.tags.join(", ") || "—"}</td>
                )}
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {b.body && (
        <div
          className="prose max-w-none text-sm"
          dangerouslySetInnerHTML={{ __html: renderMarkdown(b.body, { excludeHref: self }) }}
        />
      )}

      <div className="flex flex-wrap items-center justify-between gap-2 border-t border-border pt-4 text-xs text-muted">
        <span className="flex items-center gap-1">
          As of {b.asOfVersion ?? "?"} · last verified <VerifiedBadge lastVerified={b.lastVerified} />
        </span>
        {b.sources.length > 0 && <span>Source: {b.sources.join("; ")}</span>}
      </div>
    </article>
  );
}
