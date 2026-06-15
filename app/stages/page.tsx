import Link from "next/link";
import { getStages } from "@/lib/content";

export const metadata = { title: "Stages" };

export default function Page() {
  const stages = getStages();
  const playable = stages.filter((s) => !s.notes?.includes("Story/menu"));
  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-bold">
          Stages{" "}
          <span className="text-base font-normal text-muted">
            ({stages.length} maps · {playable.length} battle stages)
          </span>
        </h1>
        <p className="mt-1 max-w-3xl text-sm text-muted">
          Every map in the game files with variant IDs and destructibility.
        </p>
      </header>
      <div className="overflow-x-auto rounded-xl border border-border">
        <table className="w-full min-w-[640px] text-sm">
          <thead className="bg-surface-2 text-left text-xs uppercase tracking-wide text-muted">
            <tr>
              <th className="px-3 py-2">Stage</th>
              <th className="px-3 py-2 text-right">Variants</th>
              <th className="px-3 py-2">Destructible</th>
              <th className="px-3 py-2">Source</th>
            </tr>
          </thead>
          <tbody>
            {stages.map((s) => (
              <tr key={s.slug} className="border-t border-border hover:bg-surface-2/50">
                <td className="px-3 py-2">
                  <Link href={`/stages/${s.slug}`} className="font-medium text-ki hover:underline">
                    {s.name}
                  </Link>
                  {s.notes?.includes("Story/menu") && (
                    <span className="ml-2 text-xs text-muted">(story/menu)</span>
                  )}
                </td>
                <td className="px-3 py-2 text-right tabular-nums">{s.variants.length}</td>
                <td className="px-3 py-2 text-muted">{s.destructible ?? "—"}</td>
                <td className="px-3 py-2">
                  {s.source === "Base" ? (
                    <span className="text-good">Base</span>
                  ) : (
                    <span className="text-aura">{s.source}</span>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
