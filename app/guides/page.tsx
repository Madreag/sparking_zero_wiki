import Link from "next/link";
import { getGuides } from "@/lib/content";

export const metadata = { title: "Guides" };

export default function Page() {
  const guides = getGuides();
  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-bold">
          Guides <span className="text-base font-normal text-muted">({guides.length})</span>
        </h1>
        <p className="mt-1 max-w-3xl text-sm text-muted">
          Meta analysis, tier lists, and team math — built on the datamined numbers and current to
          the latest patch.
        </p>
      </header>
      <div className="grid gap-3 sm:grid-cols-2">
        {guides.map((g) => (
          <Link
            key={g.slug}
            href={`/guides/${g.slug}`}
            className="rounded-xl border border-border bg-surface p-4 transition-colors hover:border-ki/60"
          >
            <div className="flex items-baseline justify-between">
              <div className="font-medium text-ki">{g.title}</div>
              <span className="text-xs uppercase text-muted">{g.category}</span>
            </div>
            {g.summary && <p className="mt-1 text-sm text-muted">{g.summary}</p>}
          </Link>
        ))}
      </div>
    </div>
  );
}
