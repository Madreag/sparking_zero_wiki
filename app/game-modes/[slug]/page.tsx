import Link from "next/link";
import { notFound } from "next/navigation";
import { getGameMode, getGameModes } from "@/lib/content";
import { renderMarkdown } from "@/lib/markdown";
import { StatStrip, ConfidenceBadge, VerifiedBadge } from "@/components/ui";

export function generateStaticParams() {
  return getGameModes().map((m) => ({ slug: m.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const m = getGameMode(slug);
  return { title: m ? m.name : "Game Mode" };
}

export default async function Page({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const m = getGameMode(slug);
  if (!m) notFound();

  return (
    <article className="space-y-6">
      <div>
        <Link href="/game-modes" className="text-xs text-muted hover:text-ink">
          ← Game Modes
        </Link>
        <div className="mt-2 flex flex-wrap items-center gap-3">
          <h1 className="text-2xl font-bold">{m.name}</h1>
          <span className="rounded border border-border bg-surface-2 px-1.5 py-0.5 text-xs uppercase text-muted">
            {m.category}
          </span>
          <ConfidenceBadge confidence={m.confidence} />
        </div>
      </div>

      <StatStrip
        items={[
          { label: "Players", value: m.players, tone: "ki" },
          { label: "Access", value: m.access, tone: "muted" },
        ]}
      />

      {m.summary && <p className="max-w-3xl text-muted">{m.summary}</p>}

      {m.values.length > 0 && (
        <div className="overflow-x-auto rounded-xl border border-border">
          <table className="w-full text-sm">
            <thead className="bg-surface-2 text-left text-xs uppercase tracking-wide text-muted">
              <tr>
                <th className="px-3 py-2">Parameter</th>
                <th className="px-3 py-2 text-right">Value</th>
                <th className="px-3 py-2">Tag</th>
              </tr>
            </thead>
            <tbody>
              {m.values.map((v, i) => (
                <tr key={i} className="border-t border-border">
                  <td className="px-3 py-2">{v.label}</td>
                  <td className="px-3 py-2 text-right font-semibold tabular-nums text-aura">{v.value}</td>
                  <td className="px-3 py-2 text-muted">{v.tag ?? "—"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {m.rewards.length > 0 && (
        <section>
          <h2 className="mb-2 text-lg font-semibold">Rewards</h2>
          <ul className="list-disc space-y-1 pl-5 text-sm">
            {m.rewards.map((r, i) => (
              <li key={i}>{r}</li>
            ))}
          </ul>
        </section>
      )}

      {m.body && (
        <div className="prose max-w-none text-sm" dangerouslySetInnerHTML={{ __html: renderMarkdown(m.body) }} />
      )}

      <div className="flex flex-wrap items-center justify-between gap-2 border-t border-border pt-4 text-xs text-muted">
        <span className="flex items-center gap-1">
          As of {m.asOfVersion ?? "?"} · last verified <VerifiedBadge lastVerified={m.lastVerified} />
        </span>
        {m.sources.length > 0 && <span>Source: {m.sources.join("; ")}</span>}
      </div>
    </article>
  );
}
