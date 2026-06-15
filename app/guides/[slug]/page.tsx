import Link from "next/link";
import { notFound } from "next/navigation";
import { getGuide, getGuides } from "@/lib/content";
import { renderMarkdown } from "@/lib/markdown";
import { ConfidenceBadge, VerifiedBadge } from "@/components/ui";

export function generateStaticParams() {
  return getGuides().map((g) => ({ slug: g.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const g = getGuide(slug);
  return { title: g ? g.title : "Guide" };
}

export default async function Page({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const g = getGuide(slug);
  if (!g) notFound();

  return (
    <article className="space-y-6">
      <div>
        <Link href="/guides" className="text-xs text-muted hover:text-ink">
          ← Guides
        </Link>
        <div className="mt-2 flex flex-wrap items-center gap-3">
          <h1 className="text-2xl font-bold">{g.title}</h1>
          <span className="rounded border border-border bg-surface-2 px-1.5 py-0.5 text-xs uppercase text-muted">
            {g.category}
          </span>
          <ConfidenceBadge confidence={g.confidence} />
        </div>
      </div>

      {g.summary && <p className="max-w-3xl text-muted">{g.summary}</p>}

      <div className="prose max-w-none text-sm" dangerouslySetInnerHTML={{ __html: renderMarkdown(g.body, { excludeHref: `/guides/${g.slug}` }) }} />

      <div className="flex flex-wrap items-center justify-between gap-2 border-t border-border pt-4 text-xs text-muted">
        <span className="flex items-center gap-1">
          As of {g.asOfVersion ?? "?"} · last verified <VerifiedBadge lastVerified={g.lastVerified} />
        </span>
        {g.sources.length > 0 && <span>Sources: {g.sources.length} cited</span>}
      </div>
    </article>
  );
}
