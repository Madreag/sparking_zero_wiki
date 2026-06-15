import Link from "next/link";
import { getGameModes } from "@/lib/content";

export const metadata = { title: "Game Modes" };

export default function Page() {
  const modes = getGameModes();
  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-bold">
          Game Modes <span className="text-base font-normal text-muted">({modes.length})</span>
        </h1>
        <p className="mt-1 max-w-3xl text-sm text-muted">
          Rules, player counts, and reward payouts (in Zeni) for every mode.
        </p>
      </header>
      <div className="grid gap-3 sm:grid-cols-2">
        {modes.map((m) => (
          <Link
            key={m.slug}
            href={`/game-modes/${m.slug}`}
            className="rounded-xl border border-border bg-surface p-4 transition-colors hover:border-ki/60"
          >
            <div className="flex items-baseline justify-between">
              <div className="font-medium text-ki">{m.name}</div>
              <span className="text-xs uppercase text-muted">{m.category}</span>
            </div>
            {m.summary && <p className="mt-1 text-sm text-muted">{m.summary}</p>}
          </Link>
        ))}
      </div>
    </div>
  );
}
