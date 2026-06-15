import Link from "next/link";
import { notFound } from "next/navigation";
import { getDLC, getDLCs } from "@/lib/content";
import { renderMarkdown } from "@/lib/markdown";
import { StatStrip, ConfidenceBadge, VerifiedBadge } from "@/components/ui";

export function generateStaticParams() {
  return getDLCs().map((d) => ({ slug: d.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const d = getDLC(slug);
  return { title: d ? d.name : "DLC" };
}

export default async function Page({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const d = getDLC(slug);
  if (!d) notFound();

  return (
    <article className="space-y-6">
      <div>
        <Link href="/dlc" className="text-xs text-muted hover:text-ink">
          ← DLC
        </Link>
        <div className="mt-2 flex flex-wrap items-center gap-3">
          <h1 className="text-2xl font-bold">{d.name}</h1>
          {d.upcoming && <span className="text-sm text-aura">upcoming</span>}
          <ConfidenceBadge confidence={d.confidence} />
        </div>
      </div>

      <StatStrip
        items={[
          { label: "Release", value: d.releaseDate, tone: "ki" },
          { label: "Price", value: d.priceUSD != null ? `$${d.priceUSD.toFixed(2)}` : undefined, tone: "aura" },
          { label: "Characters", value: d.characters.length || undefined, tone: "good" },
          { label: "Type", value: d.type, tone: "muted" },
        ]}
      />

      {d.summary && <p className="max-w-3xl text-muted">{d.summary}</p>}

      {d.characters.length > 0 && (
        <section>
          <h2 className="mb-2 text-lg font-semibold">Characters</h2>
          <div className="overflow-x-auto rounded-xl border border-border">
            <table className="w-full text-sm">
              <thead className="bg-surface-2 text-left text-xs uppercase tracking-wide text-muted">
                <tr>
                  <th className="px-3 py-2">Fighter</th>
                  <th className="px-3 py-2 text-right">DP</th>
                </tr>
              </thead>
              <tbody>
                {d.characters.map((c, i) => (
                  <tr key={i} className="border-t border-border">
                    <td className="px-3 py-2">
                      {c.slug ? (
                        <Link href={`/characters/${c.slug}`} className="text-ki hover:underline">
                          {c.name}
                        </Link>
                      ) : (
                        c.name
                      )}
                    </td>
                    <td className="px-3 py-2 text-right tabular-nums text-aura">{c.dp ?? "—"}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      )}

      {d.adds.length > 0 && (
        <section>
          <h2 className="mb-2 text-lg font-semibold">Also adds</h2>
          <ul className="list-disc space-y-1 pl-5 text-sm">
            {d.adds.map((a, i) => (
              <li key={i}>{a}</li>
            ))}
          </ul>
        </section>
      )}

      {d.body && (
        <div className="prose max-w-none text-sm" dangerouslySetInnerHTML={{ __html: renderMarkdown(d.body) }} />
      )}

      <div className="flex flex-wrap items-center justify-between gap-2 border-t border-border pt-4 text-xs text-muted">
        <span className="flex items-center gap-1">
          As of {d.asOfVersion ?? "?"} · last verified <VerifiedBadge lastVerified={d.lastVerified} />
        </span>
        {d.sources.length > 0 && <span>Sources: {d.sources.length} cited</span>}
      </div>
    </article>
  );
}
