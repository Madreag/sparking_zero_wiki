import Link from "next/link";
import { getEpisodeBattles } from "@/lib/content";

export const metadata = { title: "Episode Battle" };

export default function Page() {
  const eps = getEpisodeBattles();
  const battles = eps.reduce((n, e) => n + (e.battleCount ?? e.battles.length), 0);
  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-bold">
          Episode Battle{" "}
          <span className="text-base font-normal text-muted">
            ({eps.length} campaigns · {battles} battles)
          </span>
        </h1>
        <p className="mt-1 max-w-3xl text-sm text-muted">
          Every campaign with battle lists, exact what-if route triggers, and reward payouts.
        </p>
      </header>
      <div className="grid gap-3 sm:grid-cols-2">
        {eps.map((e) => (
          <Link
            key={e.slug}
            href={`/episode-battles/${e.slug}`}
            className="rounded-xl border border-border bg-surface p-4 transition-colors hover:border-ki/60"
          >
            <div className="flex items-baseline justify-between">
              <div className="font-medium text-ki">{e.name}</div>
              <span className="text-sm tabular-nums text-muted">
                {(e.battleCount ?? e.battles.length) || "?"} battles
              </span>
            </div>
            {e.summary && <p className="mt-1 text-sm text-muted">{e.summary}</p>}
          </Link>
        ))}
      </div>
    </div>
  );
}
