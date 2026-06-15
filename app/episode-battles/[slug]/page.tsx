import Link from "next/link";
import { notFound } from "next/navigation";
import { getEpisodeBattle, getEpisodeBattles } from "@/lib/content";
import { renderMarkdown } from "@/lib/markdown";
import { StatStrip, ConfidenceBadge, VerifiedBadge } from "@/components/ui";

export function generateStaticParams() {
  return getEpisodeBattles().map((e) => ({ slug: e.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const e = getEpisodeBattle(slug);
  return { title: e ? e.name : "Episode Battle" };
}

export default async function Page({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const e = getEpisodeBattle(slug);
  if (!e) notFound();

  return (
    <article className="space-y-6">
      <div>
        <Link href="/episode-battles" className="text-xs text-muted hover:text-ink">
          ← Episode Battle
        </Link>
        <div className="mt-2 flex flex-wrap items-center gap-3">
          <h1 className="text-2xl font-bold">{e.name}</h1>
          <ConfidenceBadge confidence={e.confidence} />
        </div>
      </div>

      <StatStrip
        items={[
          { label: "Protagonist", value: e.character, tone: "ki" },
          { label: "Battles", value: e.battleCount ?? e.battles.length, tone: "aura" },
          { label: "Sparking episodes", value: e.sparkingEpisodes, tone: "time" },
        ]}
      />

      {e.summary && <p className="max-w-3xl text-muted">{e.summary}</p>}

      {e.battles.length > 0 && (
        <div className="overflow-x-auto rounded-xl border border-border">
          <table className="w-full min-w-[760px] text-sm">
            <thead className="bg-surface-2 text-left text-xs uppercase tracking-wide text-muted">
              <tr>
                <th className="px-3 py-2">#</th>
                <th className="px-3 py-2">Battle</th>
                <th className="px-3 py-2">VS</th>
                <th className="px-3 py-2">What-if trigger</th>
                <th className="px-3 py-2">Rewards</th>
              </tr>
            </thead>
            <tbody>
              {e.battles.map((b, i) => (
                <tr key={i} className="border-t border-border">
                  <td className="px-3 py-2 tabular-nums text-muted">{b.id}</td>
                  <td className="px-3 py-2 font-medium">{b.name}</td>
                  <td className="px-3 py-2 text-muted">{b.vs.join(", ") || "—"}</td>
                  <td className="px-3 py-2">
                    {b.altRoute ? (
                      <span>
                        <span className="text-aura">{b.altRoute}</span>
                        {b.altResult && <span className="text-muted"> → {b.altResult}</span>}
                      </span>
                    ) : (
                      "—"
                    )}
                  </td>
                  <td className="px-3 py-2 text-muted">{b.rewards ?? "—"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {e.rewards.length > 0 && (
        <section>
          <h2 className="mb-2 text-lg font-semibold">Campaign rewards</h2>
          <ul className="list-disc space-y-1 pl-5 text-sm">
            {e.rewards.map((r, i) => (
              <li key={i}>{r}</li>
            ))}
          </ul>
        </section>
      )}

      {e.body && (
        <div className="prose max-w-none text-sm" dangerouslySetInnerHTML={{ __html: renderMarkdown(e.body) }} />
      )}

      <div className="flex flex-wrap items-center justify-between gap-2 border-t border-border pt-4 text-xs text-muted">
        <span className="flex items-center gap-1">
          As of {e.asOfVersion ?? "?"} · last verified <VerifiedBadge lastVerified={e.lastVerified} />
        </span>
        {e.sources.length > 0 && <span>Source: {e.sources.join("; ")}</span>}
      </div>
    </article>
  );
}
