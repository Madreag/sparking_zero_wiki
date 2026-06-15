import Link from "next/link";
import { notFound } from "next/navigation";
import { getTransformation, getTransformations } from "@/lib/content";
import { renderMarkdown } from "@/lib/markdown";
import { fmtNum } from "@/lib/formulas";
import { StatStrip, ConfidenceBadge, VerifiedBadge } from "@/components/ui";

export function generateStaticParams() {
  return getTransformations().map((t) => ({ slug: t.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const t = getTransformation(slug);
  return { title: t ? t.name : "Transformation" };
}

export default async function Page({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const t = getTransformation(slug);
  if (!t) notFound();

  return (
    <article className="space-y-6">
      <div>
        <Link href="/transformations" className="text-xs text-muted hover:text-ink">
          ← Transformations
        </Link>
        <div className="mt-2 flex flex-wrap items-center gap-3">
          <h1 className="text-2xl font-bold">{t.name}</h1>
          <ConfidenceBadge confidence={t.confidence} />
        </div>
      </div>

      <StatStrip
        items={[
          { label: "Cost", value: t.cost != null ? `${fmtNum(t.cost)} stocks` : undefined, tone: "aura" },
          { label: "From", value: t.from, tone: "muted" },
          { label: "To", value: t.to, tone: "ki" },
          { label: "DP", value: t.dpFrom != null && t.dpTo != null ? `${t.dpFrom} → ${t.dpTo}` : undefined, tone: "time" },
          { label: "Kind", value: t.kind, tone: "muted" },
        ]}
      />

      {t.hpRule && (
        <p className="max-w-3xl text-sm">
          <span className="font-semibold">HP rule:</span> {t.hpRule}
        </p>
      )}
      {t.statChanges && (
        <p className="max-w-3xl text-sm">
          <span className="font-semibold">Stat changes:</span> {t.statChanges}
        </p>
      )}
      {t.summary && <p className="max-w-3xl text-muted">{t.summary}</p>}

      {t.body && (
        <div className="prose max-w-none text-sm" dangerouslySetInnerHTML={{ __html: renderMarkdown(t.body, { excludeHref: `/transformations/${t.slug}` }) }} />
      )}

      <div className="flex flex-wrap items-center justify-between gap-2 border-t border-border pt-4 text-xs text-muted">
        <span className="flex items-center gap-1">
          As of {t.asOfVersion ?? "?"} · last verified <VerifiedBadge lastVerified={t.lastVerified} />
        </span>
        {t.sources.length > 0 && <span>Source: {t.sources.join("; ")}</span>}
      </div>
    </article>
  );
}
