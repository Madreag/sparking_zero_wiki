import "./globals.css";
import type { Metadata } from "next";
import type { ReactNode } from "react";
import Link from "next/link";
import { CURRENT_VERSION } from "@/lib/version";
import { SearchButton } from "@/components/search";
import { SortableTables } from "@/components/sortable-tables";

export const metadata: Metadata = {
  title: {
    default: "Sparking! ZERO Codex",
    template: "%s · Sparking! ZERO Codex",
  },
  description:
    "The numbers-first DRAGON BALL: Sparking! ZERO knowledge base — datamined HP and ki costs for every fighter, DP costs, patch-by-patch balance history, mechanics frame data, and the current meta.",
};

const navData = [
  { href: "/characters", label: "Roster" },
  { href: "/dna", label: "Roster DNA" },
  { href: "/classes", label: "Classes" },
  { href: "/compare", label: "Compare" },
  { href: "/blasts", label: "Blasts" },
  { href: "/skills", label: "Skills" },
  { href: "/transformations", label: "Transformations" },
  { href: "/stages", label: "Stages" },
  { href: "/shop", label: "Shop" },
  { href: "/stats", label: "Stats" },
];
const navPlay = [
  { href: "/meta", label: "Meta", hot: true },
  { href: "/guides", label: "Guides", hot: true },
  { href: "/mechanics", label: "Mechanics" },
  { href: "/episode-battles", label: "Episode Battle" },
  { href: "/game-modes", label: "Modes" },
  { href: "/patches", label: "Patches" },
  { href: "/dlc", label: "DLC" },
  { href: "/glossary", label: "Glossary" },
];

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen antialiased">
        <header className="sticky top-0 z-50 border-b border-border bg-surface/80 backdrop-blur">
          <div className="mx-auto max-w-6xl px-4 py-2.5">
            <div className="flex items-center gap-6">
              <Link href="/" className="shrink-0 font-semibold tracking-tight">
                <span className="text-aura">✦</span> <span className="text-ki">Sparking! ZERO Codex</span>
              </Link>
              <nav className="hidden flex-wrap gap-x-4 gap-y-1 text-sm text-muted md:flex">
                {navData.map((n) => (
                  <Link key={n.href} href={n.href} className="transition-colors hover:text-ink">
                    {n.label}
                  </Link>
                ))}
              </nav>
              <SearchButton />
            </div>
            <div className="mt-1.5 flex items-center gap-6">
              <nav className="flex flex-wrap gap-x-4 gap-y-1 text-sm">
                {navPlay.map((n) => (
                  <Link
                    key={n.href}
                    href={n.href}
                    className={n.hot ? "font-medium text-aura transition-colors hover:text-ink" : "text-muted transition-colors hover:text-ink"}
                  >
                    {n.label}
                  </Link>
                ))}
                <span className="flex flex-wrap gap-x-4 text-sm text-muted md:hidden">
                  {navData.map((n) => (
                    <Link key={n.href} href={n.href} className="transition-colors hover:text-ink">
                      {n.label}
                    </Link>
                  ))}
                </span>
              </nav>
              <span className="ml-auto hidden text-xs text-muted sm:inline">
                {CURRENT_VERSION.patch} · {CURRENT_VERSION.rosterSlots} fighters
              </span>
            </div>
          </div>
        </header>
        <main className="mx-auto max-w-6xl px-4 py-8">{children}</main>
        <SortableTables />
        <footer className="mx-auto max-w-6xl px-4 py-10 text-xs leading-relaxed text-muted">
          Data current as of {CURRENT_VERSION.patch} ({CURRENT_VERSION.releaseDate}). Stats are
          datamined from game files or re-derived from cited public sources. A fan project; not
          affiliated with Bandai Namco or Spike Chunsoft.
        </footer>
      </body>
    </html>
  );
}
