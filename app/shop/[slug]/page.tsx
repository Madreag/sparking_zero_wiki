import Link from "next/link";
import { notFound } from "next/navigation";
import { getShopCategory, getShopCategories } from "@/lib/content";
import { renderMarkdown } from "@/lib/markdown";
import { fmtNum } from "@/lib/formulas";
import { ConfidenceBadge, VerifiedBadge } from "@/components/ui";

export function generateStaticParams() {
  return getShopCategories().map((c) => ({ slug: c.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const c = getShopCategory(slug);
  return { title: c ? c.name : "Shop" };
}

export default async function Page({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const c = getShopCategory(slug);
  if (!c) notFound();

  const totalZeni = c.items.reduce((n, it) => n + (it.price ?? 0), 0);

  return (
    <article className="space-y-6">
      <div>
        <Link href="/shop" className="text-xs text-muted hover:text-ink">
          ← Shop
        </Link>
        <div className="mt-2 flex flex-wrap items-center gap-3">
          <h1 className="text-2xl font-bold">{c.name}</h1>
          <ConfidenceBadge confidence={c.confidence} />
        </div>
        <p className="mt-1 text-sm text-muted">
          {c.items.length} items{totalZeni > 0 && <> · total {fmtNum(totalZeni)} Zeni to buy everything</>}
        </p>
      </div>

      {c.summary && <p className="max-w-3xl text-muted">{c.summary}</p>}

      <div className="overflow-x-auto rounded-xl border border-border">
        <table className="w-full min-w-[640px] text-sm">
          <thead className="bg-surface-2 text-left text-xs uppercase tracking-wide text-muted">
            <tr>
              <th className="px-3 py-2">Item</th>
              <th className="px-3 py-2 text-right">Price</th>
              <th className="px-3 py-2">Currency</th>
              <th className="px-3 py-2">Unlock</th>
            </tr>
          </thead>
          <tbody>
            {c.items.map((it, i) => (
              <tr key={i} className="border-t border-border">
                <td className="px-3 py-2">{it.name}</td>
                <td className="px-3 py-2 text-right tabular-nums text-aura">{fmtNum(it.price)}</td>
                <td className="px-3 py-2 text-muted">{it.currency}</td>
                <td className="px-3 py-2 text-muted">{it.unlock ?? "—"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {c.body && (
        <div className="prose max-w-none text-sm" dangerouslySetInnerHTML={{ __html: renderMarkdown(c.body, { excludeHref: `/shop/${c.slug}` }) }} />
      )}

      <div className="flex flex-wrap items-center justify-between gap-2 border-t border-border pt-4 text-xs text-muted">
        <span className="flex items-center gap-1">
          As of {c.asOfVersion ?? "?"} · last verified <VerifiedBadge lastVerified={c.lastVerified} />
        </span>
        {c.sources.length > 0 && <span>Source: {c.sources.join("; ")}</span>}
      </div>
    </article>
  );
}
