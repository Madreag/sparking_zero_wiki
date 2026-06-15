import Link from "next/link";
import { getDLCs } from "@/lib/content";

export const metadata = { title: "DLC" };

export default function Page() {
  const dlcs = getDLCs();
  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-bold">
          DLC & Season Passes <span className="text-base font-normal text-muted">({dlcs.length})</span>
        </h1>
        <p className="mt-1 max-w-3xl text-sm text-muted">
          Every pack with release date, price, and full contents (characters with DP costs).
        </p>
      </header>
      <div className="overflow-x-auto rounded-xl border border-border">
        <table className="w-full min-w-[680px] text-sm">
          <thead className="bg-surface-2 text-left text-xs uppercase tracking-wide text-muted">
            <tr>
              <th className="px-3 py-2">Pack</th>
              <th className="px-3 py-2">Date</th>
              <th className="px-3 py-2 text-right">Price</th>
              <th className="px-3 py-2 text-right">Characters</th>
              <th className="px-3 py-2">Type</th>
            </tr>
          </thead>
          <tbody>
            {dlcs.map((d) => (
              <tr key={d.slug} className="border-t border-border hover:bg-surface-2/50">
                <td className="px-3 py-2">
                  <Link href={`/dlc/${d.slug}`} className="font-medium text-ki hover:underline">
                    {d.name}
                  </Link>
                  {d.upcoming && <span className="ml-2 text-xs text-aura">upcoming</span>}
                </td>
                <td className="px-3 py-2 tabular-nums text-muted">{d.releaseDate}</td>
                <td className="px-3 py-2 text-right tabular-nums">
                  {d.priceUSD != null ? `$${d.priceUSD.toFixed(2)}` : "—"}
                </td>
                <td className="px-3 py-2 text-right tabular-nums">{d.characters.length || "—"}</td>
                <td className="px-3 py-2 text-muted">{d.type}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
