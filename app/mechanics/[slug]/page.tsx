import Link from "next/link";
import { notFound } from "next/navigation";
import { getMechanic, getMechanics } from "@/lib/content";
import { renderMarkdown } from "@/lib/markdown";
import { linkifyText } from "@/lib/linkify";
import { ConfidenceBadge, VerifiedBadge } from "@/components/ui";

export function generateStaticParams() {
  return getMechanics().map((m) => ({ slug: m.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const m = getMechanic(slug);
  return { title: m ? m.name : "Mechanic" };
}

export default async function Page({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const m = getMechanic(slug);
  if (!m) notFound();

  return (
    <article className="space-y-6">
      <div>
        <Link href="/mechanics" className="text-xs text-muted hover:text-ink">
          ← Mechanics
        </Link>
        <div className="mt-2 flex flex-wrap items-center gap-3">
          <h1 className="text-2xl font-bold">{m.name}</h1>
          <span className="rounded border border-border bg-surface-2 px-1.5 py-0.5 text-xs uppercase text-muted">
            {m.category}
          </span>
          <ConfidenceBadge confidence={m.confidence} />
        </div>
        {m.input && (
          <p className="mt-1 text-sm text-muted">
            Input: <code className="text-ink">{m.input}</code>
          </p>
        )}
      </div>

      {m.summary && <p className="max-w-3xl text-muted">{m.summary}</p>}

      {m.values.length > 0 && (
        <div className="overflow-x-auto rounded-xl border border-border">
          <table className="w-full text-sm">
            <thead className="bg-surface-2 text-left text-xs uppercase tracking-wide text-muted">
              <tr>
                <th className="px-3 py-2">Value</th>
                <th className="px-3 py-2 text-right">Number</th>
                <th className="px-3 py-2">Measured on</th>
                <th className="px-3 py-2">Tag</th>
              </tr>
            </thead>
            <tbody>
              {m.values.map((v, i) => (
                <tr key={i} className="border-t border-border">
                  <td className="px-3 py-2">{v.label}</td>
                  <td className="px-3 py-2 text-right font-semibold tabular-nums text-aura">{v.value}</td>
                  <td className="px-3 py-2 text-muted">{v.patch ?? "—"}</td>
                  <td className="px-3 py-2 text-muted">{v.tag ?? "—"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {(m.counters.length > 0 || m.counteredBy.length > 0) && (
        <div className="grid gap-4 sm:grid-cols-2">
          {m.counters.length > 0 && (
            <div className="rounded-xl border border-border bg-surface p-3">
              <div className="text-xs uppercase tracking-wide text-good">Beats</div>
              <p className="mt-1 text-sm">{linkifyText(m.counters.join(", "), `/mechanics/${m.slug}`)}</p>
            </div>
          )}
          {m.counteredBy.length > 0 && (
            <div className="rounded-xl border border-border bg-surface p-3">
              <div className="text-xs uppercase tracking-wide text-danger">Loses to</div>
              <p className="mt-1 text-sm">{linkifyText(m.counteredBy.join(", "), `/mechanics/${m.slug}`)}</p>
            </div>
          )}
        </div>
      )}

      {m.changeHistory.length > 0 && (
        <section>
          <h2 className="mb-2 text-lg font-semibold">Patch history</h2>
          <ul className="space-y-1 text-sm">
            {m.changeHistory.map((c, i) => (
              <li key={i}>
                <span className="tabular-nums text-muted">
                  {c.version}
                  {c.date ? ` (${c.date})` : ""}:
                </span>{" "}
                {c.change}
              </li>
            ))}
          </ul>
        </section>
      )}

      {m.body && (
        <div className="prose max-w-none text-sm" dangerouslySetInnerHTML={{ __html: renderMarkdown(m.body, { excludeHref: `/mechanics/${m.slug}` }) }} />
      )}

      <div className="flex flex-wrap items-center justify-between gap-2 border-t border-border pt-4 text-xs text-muted">
        <span className="flex items-center gap-1">
          As of {m.asOfVersion ?? "?"} · last verified <VerifiedBadge lastVerified={m.lastVerified} />
        </span>
        {m.sources.length > 0 && <span>Sources: {m.sources.length} cited</span>}
      </div>
    </article>
  );
}
