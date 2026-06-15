import Link from "next/link";
import { notFound } from "next/navigation";
import { getSkill, getSkills } from "@/lib/content";
import { renderMarkdown } from "@/lib/markdown";
import { fmtNum } from "@/lib/formulas";
import { StatStrip, ConfidenceBadge, VerifiedBadge, TierBadge } from "@/components/ui";

export function generateStaticParams() {
  return getSkills().map((s) => ({ slug: s.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const s = getSkill(slug);
  return { title: s ? s.name : "Skill" };
}

export default async function Page({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const s = getSkill(slug);
  if (!s) notFound();

  return (
    <article className="space-y-6">
      <div>
        <Link href="/skills" className="text-xs text-muted hover:text-ink">
          ← Skills
        </Link>
        <div className="mt-2 flex flex-wrap items-center gap-3">
          <h1 className="text-2xl font-bold">{s.name}</h1>
          <TierBadge tier={s.tier} />
          <ConfidenceBadge confidence={s.confidence} />
        </div>
      </div>

      <StatStrip
        items={[
          { label: "Skill cost", value: s.skillCost != null ? `${s.skillCost} stocks` : undefined, tone: "aura" },
          { label: "Duration", value: s.durationSec != null ? `${s.durationSec}s` : undefined, tone: "ki" },
          { label: "Magnitude", value: s.magnitude, tone: "good" },
          { label: "Users", value: s.users.length || s.userCount || undefined, tone: "muted" },
        ]}
      />

      {s.effect && <p className="max-w-3xl text-ink">{s.effect}</p>}
      {s.summary && <p className="max-w-3xl text-muted">{s.summary}</p>}

      {s.users.length > 0 && (
        <section>
          <h2 className="mb-2 text-lg font-semibold">Notable users</h2>
          <div className="flex flex-wrap gap-2 text-sm">
            {s.users.map((u, i) => (
              <span key={i} className="rounded border border-border bg-surface-2 px-2 py-1">
                {u}
              </span>
            ))}
          </div>
        </section>
      )}

      {s.changeHistory.length > 0 && (
        <section>
          <h2 className="mb-2 text-lg font-semibold">Patch history</h2>
          <div className="overflow-x-auto rounded-xl border border-border">
            <table className="w-full text-sm">
              <thead className="bg-surface-2 text-left text-xs uppercase tracking-wide text-muted">
                <tr>
                  <th className="px-3 py-2">Patch</th>
                  <th className="px-3 py-2">Change</th>
                </tr>
              </thead>
              <tbody>
                {s.changeHistory.map((c, i) => (
                  <tr key={i} className="border-t border-border">
                    <td className="px-3 py-2 whitespace-nowrap tabular-nums">
                      {c.version}
                      {c.date ? ` (${c.date})` : ""}
                    </td>
                    <td className="px-3 py-2">{c.change}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      )}

      {s.body && (
        <div className="prose max-w-none text-sm" dangerouslySetInnerHTML={{ __html: renderMarkdown(s.body) }} />
      )}

      <div className="flex flex-wrap items-center justify-between gap-2 border-t border-border pt-4 text-xs text-muted">
        <span className="flex items-center gap-1">
          As of {s.asOfVersion ?? "?"} · last verified <VerifiedBadge lastVerified={s.lastVerified} />
        </span>
        {s.sources.length > 0 && <span>Source: {s.sources.join("; ")}</span>}
      </div>
    </article>
  );
}
