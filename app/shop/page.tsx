import Link from "next/link";
import { getShopCategories } from "@/lib/content";

export const metadata = { title: "Shop & Unlocks" };

export default function Page() {
  const cats = getShopCategories();
  const total = cats.reduce((n, c) => n + c.items.length, 0);
  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-bold">
          Shop & Unlocks{" "}
          <span className="text-base font-normal text-muted">
            ({cats.length} categories · {total} items)
          </span>
        </h1>
        <p className="mt-1 max-w-3xl text-sm text-muted">
          Full datamined price tables — every purchasable character, costume, accessory, and item
          with its Zeni price and unlock condition.
        </p>
      </header>
      <div className="grid gap-3 sm:grid-cols-2">
        {cats.map((c) => (
          <Link
            key={c.slug}
            href={`/shop/${c.slug}`}
            className="rounded-xl border border-border bg-surface p-4 transition-colors hover:border-ki/60"
          >
            <div className="flex items-baseline justify-between">
              <div className="font-medium text-ki">{c.name}</div>
              <span className="text-sm tabular-nums text-muted">{c.items.length}</span>
            </div>
            {c.summary && <p className="mt-1 text-sm text-muted">{c.summary}</p>}
          </Link>
        ))}
      </div>
    </div>
  );
}
