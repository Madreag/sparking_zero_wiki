import { getBlasts } from "@/lib/content";
import { BlastsTable, type BlastRow } from "@/components/blasts-table";

export const metadata = { title: "Blasts & Ultimates" };

export default function Page() {
  const blasts = getBlasts();
  const rows: BlastRow[] = blasts.map((b) => {
    const dmgs = b.users.map((u) => u.damage).filter((x): x is number => x != null);
    return {
      name: b.name,
      slug: b.slug,
      cls: b.class,
      users: b.users.length,
      costs: [...new Set(b.users.map((u) => u.kiCost).filter((x): x is number => x != null))].sort(
        (a, b2) => a - b2,
      ),
      category: b.category ?? null,
      maxDamage: dmgs.length ? Math.max(...dmgs) : null,
    };
  });
  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-bold">
          Blasts & Ultimates <span className="text-base font-normal text-muted">({blasts.length})</span>
        </h1>
        <p className="mt-1 max-w-3xl text-sm text-muted">
          Every named Super (Blast 2) and Ultimate with datamined ki costs per user. 10,000 energy
          = 1 ki bar.
        </p>
      </header>
      <BlastsTable rows={rows} />
    </div>
  );
}
