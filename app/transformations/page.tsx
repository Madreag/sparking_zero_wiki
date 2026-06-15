import Link from "next/link";
import { getTransformations } from "@/lib/content";
import { fmtNum } from "@/lib/formulas";

export const metadata = { title: "Transformations & Fusions" };

export default function Page() {
  const items = getTransformations();
  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-bold">
          Transformations & Fusions{" "}
          <span className="text-base font-normal text-muted">({items.length})</span>
        </h1>
        <p className="mt-1 max-w-3xl text-sm text-muted">
          In-battle form changes with skill-stock costs and what actually changes (HP pool, DP
          jump, new moveset).
        </p>
      </header>
      <div className="overflow-x-auto rounded-xl border border-border">
        <table className="w-full min-w-[700px] text-sm">
          <thead className="bg-surface-2 text-left text-xs uppercase tracking-wide text-muted">
            <tr>
              <th className="px-3 py-2">Transformation</th>
              <th className="px-3 py-2">From → To</th>
              <th className="px-3 py-2 text-right">Cost (stocks)</th>
              <th className="px-3 py-2 text-right">DP</th>
              <th className="px-3 py-2">Kind</th>
            </tr>
          </thead>
          <tbody>
            {items.map((t) => (
              <tr key={t.slug} className="border-t border-border hover:bg-surface-2/50">
                <td className="px-3 py-2">
                  <Link href={`/transformations/${t.slug}`} className="font-medium text-ki hover:underline">
                    {t.name}
                  </Link>
                </td>
                <td className="px-3 py-2 text-muted">
                  {t.from} → {t.to}
                </td>
                <td className="px-3 py-2 text-right tabular-nums text-aura">{fmtNum(t.cost)}</td>
                <td className="px-3 py-2 text-right tabular-nums">
                  {t.dpFrom != null && t.dpTo != null ? `${t.dpFrom} → ${t.dpTo}` : "—"}
                </td>
                <td className="px-3 py-2 text-muted">{t.kind}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
