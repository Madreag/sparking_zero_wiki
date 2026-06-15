import Link from "next/link";
import { getMechanics } from "@/lib/content";

export const metadata = { title: "Combat Mechanics" };

const CATS = ["offense", "defense", "movement", "resource", "system", "status"] as const;
const catLabel: Record<string, string> = {
  offense: "Offense",
  defense: "Defense & Counters",
  movement: "Movement",
  resource: "Resources & Gauges",
  system: "Core Systems",
  status: "Status & Classes",
};

export default function Page() {
  const mechanics = getMechanics();
  return (
    <div className="space-y-8">
      <header>
        <h1 className="text-2xl font-bold">
          Combat Mechanics{" "}
          <span className="text-base font-normal text-muted">({mechanics.length})</span>
        </h1>
        <p className="mt-1 max-w-3xl text-sm text-muted">
          Every system quantified: input windows, ki costs, gauge rates, damage modifiers —
          tagged official / datamined / community-tested, with the patch they were measured on.
        </p>
      </header>
      {CATS.map((cat) => {
        const items = mechanics.filter((m) => m.category === cat);
        if (!items.length) return null;
        return (
          <section key={cat} className="space-y-2">
            <h2 className="text-lg font-semibold">{catLabel[cat]}</h2>
            <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
              {items.map((m) => (
                <Link
                  key={m.slug}
                  href={`/mechanics/${m.slug}`}
                  className="rounded-xl border border-border bg-surface p-3 transition-colors hover:border-ki/60"
                >
                  <div className="font-medium text-ki">{m.name}</div>
                  {m.values[0] && (
                    <div className="mt-1 text-xs text-muted">
                      {m.values[0].label}: <span className="text-aura">{m.values[0].value}</span>
                      {m.values.length > 1 ? ` · +${m.values.length - 1} more values` : ""}
                    </div>
                  )}
                </Link>
              ))}
            </div>
          </section>
        );
      })}
    </div>
  );
}
