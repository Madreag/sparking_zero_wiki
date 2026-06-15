import Link from "next/link";
import { notFound } from "next/navigation";
import { getStage, getStages } from "@/lib/content";
import { renderMarkdown } from "@/lib/markdown";
import { StatStrip, ConfidenceBadge, VerifiedBadge } from "@/components/ui";

export function generateStaticParams() {
  return getStages().map((s) => ({ slug: s.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const s = getStage(slug);
  return { title: s ? s.name : "Stage" };
}

export default async function Page({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const s = getStage(slug);
  if (!s) notFound();

  return (
    <article className="space-y-6">
      <div>
        <Link href="/stages" className="text-xs text-muted hover:text-ink">
          ← Stages
        </Link>
        <div className="mt-2 flex flex-wrap items-center gap-3">
          <h1 className="text-2xl font-bold">{s.name}</h1>
          <ConfidenceBadge confidence={s.confidence} />
        </div>
      </div>

      <StatStrip
        items={[
          { label: "Variants", value: s.variants.length, tone: "ki" },
          { label: "Destructible", value: s.destructible, tone: "aura" },
          { label: "Source", value: s.source, tone: s.source === "Base" ? "good" : "aura" },
        ]}
      />

      {s.summary && <p className="max-w-3xl text-muted">{s.summary}</p>}
      {s.notes && <p className="max-w-3xl text-sm text-muted">{s.notes}</p>}

      {s.body && (
        <div className="prose max-w-none text-sm" dangerouslySetInnerHTML={{ __html: renderMarkdown(s.body, { excludeHref: `/stages/${s.slug}` }) }} />
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
