import Link from "next/link";
import { getPatchNotes } from "@/lib/content";

export const metadata = { title: "Patches" };

const typeTone: Record<string, string> = {
  launch: "text-time",
  major: "text-aura",
  balance: "text-danger",
  content: "text-ki",
  hotfix: "text-muted",
};

export default function Page() {
  const patches = getPatchNotes();
  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-bold">
          Patch History <span className="text-base font-normal text-muted">({patches.length} updates)</span>
        </h1>
        <p className="mt-1 max-w-3xl text-sm text-muted">
          Every update since launch with quantified balance changes — official notes plus
          community-measured numbers, clearly tagged.
        </p>
      </header>
      <div className="overflow-x-auto rounded-xl border border-border">
        <table className="w-full min-w-[680px] text-sm">
          <thead className="bg-surface-2 text-left text-xs uppercase tracking-wide text-muted">
            <tr>
              <th className="px-3 py-2">Version</th>
              <th className="px-3 py-2">Date</th>
              <th className="px-3 py-2">Type</th>
              <th className="px-3 py-2">Headline</th>
              <th className="px-3 py-2 text-right">Changes</th>
            </tr>
          </thead>
          <tbody>
            {patches.map((p) => (
              <tr key={p.slug} className="border-t border-border hover:bg-surface-2/50">
                <td className="px-3 py-2">
                  <Link href={`/patches/${p.slug}`} className="font-medium text-ki hover:underline">
                    {p.version}
                  </Link>
                </td>
                <td className="px-3 py-2 tabular-nums text-muted">{p.releaseDate}</td>
                <td className={`px-3 py-2 ${typeTone[p.type] ?? ""}`}>{p.type}</td>
                <td className="px-3 py-2 text-muted">{p.headline ?? "—"}</td>
                <td className="px-3 py-2 text-right tabular-nums">{p.changes.length + p.measured.length}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
