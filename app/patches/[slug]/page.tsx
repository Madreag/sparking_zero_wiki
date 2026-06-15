import Link from "next/link";
import { notFound } from "next/navigation";
import { getPatchNote, getPatchNotes } from "@/lib/content";
import { renderMarkdown } from "@/lib/markdown";
import { ConfidenceBadge, VerifiedBadge } from "@/components/ui";

export function generateStaticParams() {
  return getPatchNotes().map((p) => ({ slug: p.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const p = getPatchNote(slug);
  return { title: p ? p.version : "Patch" };
}

export default async function Page({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const p = getPatchNote(slug);
  if (!p) notFound();

  return (
    <article className="space-y-6">
      <div>
        <Link href="/patches" className="text-xs text-muted hover:text-ink">
          ← Patches
        </Link>
        <div className="mt-2 flex flex-wrap items-center gap-3">
          <h1 className="text-2xl font-bold">{p.version}</h1>
          <span className="rounded border border-border bg-surface-2 px-1.5 py-0.5 text-xs uppercase text-muted">
            {p.type}
          </span>
          <span className="text-sm tabular-nums text-muted">{p.releaseDate}</span>
          <ConfidenceBadge confidence={p.confidence} />
        </div>
        {p.headline && <p className="mt-2 max-w-3xl font-medium">{p.headline}</p>}
      </div>

      {p.summary && <p className="max-w-3xl text-muted">{p.summary}</p>}

      {p.measured.length > 0 && (
        <section>
          <h2 className="mb-2 text-lg font-semibold">Quantified changes</h2>
          <div className="overflow-x-auto rounded-xl border border-border">
            <table className="w-full min-w-[680px] text-sm">
              <thead className="bg-surface-2 text-left text-xs uppercase tracking-wide text-muted">
                <tr>
                  <th className="px-3 py-2">Target</th>
                  <th className="px-3 py-2">Metric</th>
                  <th className="px-3 py-2 text-right">Old</th>
                  <th className="px-3 py-2 text-right">New</th>
                  <th className="px-3 py-2">Note</th>
                </tr>
              </thead>
              <tbody>
                {p.measured.map((m, i) => (
                  <tr key={i} className="border-t border-border">
                    <td className="px-3 py-2 font-medium">{m.target}</td>
                    <td className="px-3 py-2">{m.metric}</td>
                    <td className="px-3 py-2 text-right tabular-nums text-danger">{m.old ?? "—"}</td>
                    <td className="px-3 py-2 text-right tabular-nums text-good">{m.new ?? "—"}</td>
                    <td className="px-3 py-2 text-muted">{m.note ?? "—"}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      )}

      {p.changes.length > 0 && (
        <section>
          <h2 className="mb-2 text-lg font-semibold">All changes</h2>
          <ul className="list-disc space-y-1 pl-5 text-sm">
            {p.changes.map((c, i) => (
              <li key={i}>{c}</li>
            ))}
          </ul>
        </section>
      )}

      {p.body && (
        <div className="prose max-w-none text-sm" dangerouslySetInnerHTML={{ __html: renderMarkdown(p.body, { excludeHref: `/patches/${p.slug}` }) }} />
      )}

      <div className="flex flex-wrap items-center justify-between gap-2 border-t border-border pt-4 text-xs text-muted">
        <span className="flex items-center gap-1">
          Last verified <VerifiedBadge lastVerified={p.lastVerified} />
        </span>
        {p.sources.length > 0 && <span>Sources: {p.sources.length} cited</span>}
      </div>
    </article>
  );
}
