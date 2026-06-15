"use client";

import { useMemo, useState } from "react";
import Link from "next/link";

export type SkillRow = {
  name: string;
  slug: string;
  cost: number | null;
  duration: number | null;
  users: number;
  effect: string | null;
};

export function SkillsTable({ rows }: { rows: SkillRow[] }) {
  const [q, setQ] = useState("");
  const [verified, setVerified] = useState(false);
  const [sort, setSort] = useState<"name" | "users" | "cost">("name");

  const filtered = useMemo(() => {
    const ql = q.trim().toLowerCase();
    const out = rows.filter(
      (r) =>
        (!verified || r.cost != null || r.effect) &&
        (!ql || r.name.toLowerCase().includes(ql) || (r.effect ?? "").toLowerCase().includes(ql)),
    );
    out.sort((a, b) => {
      if (sort === "users") return b.users - a.users || a.name.localeCompare(b.name);
      if (sort === "cost") return (a.cost ?? 99) - (b.cost ?? 99) || a.name.localeCompare(b.name);
      return a.name.localeCompare(b.name);
    });
    return out;
  }, [rows, q, verified, sort]);

  const sel = "rounded-lg border border-border bg-surface-2 px-2 py-1.5 text-xs text-ink outline-none focus:border-ki/60";

  return (
    <div className="space-y-3">
      <div className="flex flex-wrap items-center gap-2">
        <input value={q} onChange={(e) => setQ(e.target.value)} placeholder={`Filter ${rows.length} skills…`} className={`${sel} w-56`} />
        <select value={sort} onChange={(e) => setSort(e.target.value as typeof sort)} className={sel}>
          <option value="name">Sort: name</option>
          <option value="users">Sort: most users</option>
          <option value="cost">Sort: cheapest</option>
        </select>
        <label className="flex items-center gap-1.5 text-xs text-muted">
          <input type="checkbox" checked={verified} onChange={(e) => setVerified(e.target.checked)} />
          with verified numbers only
        </label>
        <span className="ml-auto text-xs tabular-nums text-muted">{filtered.length} shown</span>
      </div>
      <div className="overflow-x-auto rounded-xl border border-border">
        <table className="w-full min-w-[680px] text-sm" data-sortable-self>
          <thead className="bg-surface-2 text-left text-xs uppercase tracking-wide text-muted">
            <tr>
              <th className="px-3 py-2">Skill</th>
              <th className="px-3 py-2 text-right">Cost (stocks)</th>
              <th className="px-3 py-2 text-right">Duration</th>
              <th className="px-3 py-2 text-right">Users</th>
              <th className="px-3 py-2">Effect</th>
            </tr>
          </thead>
          <tbody>
            {filtered.map((s) => (
              <tr key={s.slug} className="border-t border-border hover:bg-surface-2/50">
                <td className="px-3 py-2">
                  <Link href={`/skills/${s.slug}`} className="font-medium text-ki hover:underline">
                    {s.name}
                  </Link>
                </td>
                <td className="px-3 py-2 text-right tabular-nums text-aura">{s.cost ?? "—"}</td>
                <td className="px-3 py-2 text-right tabular-nums">{s.duration != null ? `${s.duration}s` : "—"}</td>
                <td className="px-3 py-2 text-right tabular-nums">{s.users || "—"}</td>
                <td className="px-3 py-2 text-muted">{s.effect ?? "—"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
