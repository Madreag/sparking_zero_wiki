"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { useRouter } from "next/navigation";

type Entry = { t: string; h: string; g: string; x: string };

const GROUP_TONE: Record<string, string> = {
  Fighter: "text-ki",
  Blast: "text-aura",
  Skill: "text-good",
  Transformation: "text-time",
  Mechanic: "text-danger",
  Guide: "text-aura",
  Patch: "text-muted",
  Mode: "text-good",
  "Episode Battle": "text-time",
  DLC: "text-aura",
  Stage: "text-ki",
  Shop: "text-good",
  Glossary: "text-muted",
};

export function SearchButton() {
  const [open, setOpen] = useState(false);
  const [q, setQ] = useState("");
  const [idx, setIdx] = useState<Entry[] | null>(null);
  const [sel, setSel] = useState(0);
  const inputRef = useRef<HTMLInputElement>(null);
  const triggerRef = useRef<HTMLButtonElement>(null);
  const router = useRouter();

  const close = useCallback(() => {
    setOpen(false);
    setTimeout(() => triggerRef.current?.focus(), 0);
  }, []);

  const load = useCallback(async () => {
    if (idx) return;
    try {
      const r = await fetch("/search-index.json");
      setIdx(await r.json());
    } catch {
      setIdx([]);
    }
  }, [idx]);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        setOpen((o) => !o);
        void load();
      } else if (e.key === "Escape") {
        close();
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [load, close]);

  useEffect(() => {
    if (open) {
      void load();
      setTimeout(() => inputRef.current?.focus(), 10);
    } else {
      setQ("");
      setSel(0);
    }
  }, [open, load]);

  const ql = q.trim().toLowerCase();
  const results = !ql || !idx
    ? []
    : idx
        .map((e) => {
          const tl = e.t.toLowerCase();
          let score = -1;
          if (tl === ql) score = 0;
          else if (tl.startsWith(ql)) score = 1;
          else if (tl.includes(ql)) score = 2;
          else if (e.x.toLowerCase().includes(ql)) score = 3;
          return { e, score };
        })
        .filter((r) => r.score >= 0)
        .sort((a, b) => a.score - b.score || a.e.t.length - b.e.t.length)
        .slice(0, 25)
        .map((r) => r.e);

  const go = (e: Entry) => {
    setOpen(false);
    router.push(e.h);
  };

  return (
    <>
      <button
        ref={triggerRef}
        onClick={() => setOpen(true)}
        aria-label="Open search (Command or Control + K)"
        aria-keyshortcuts="Meta+K Control+K"
        className="ml-auto flex items-center gap-2 rounded-lg border border-border bg-surface-2 px-3 py-1.5 text-xs text-muted transition-colors hover:border-ki/60 hover:text-ink"
      >
        <span>Search</span>
        <kbd className="rounded border border-border px-1 font-mono text-[10px]">⌘K</kbd>
      </button>
      {open && (
        <div
          className="fixed inset-0 z-[100] bg-void/70 p-4 backdrop-blur-sm sm:p-[10vh]"
          onClick={close}
        >
          <div
            role="dialog"
            aria-modal="true"
            aria-label="Search the wiki"
            className="mx-auto max-w-xl overflow-hidden rounded-xl border border-border bg-surface shadow-2xl"
            onClick={(e) => e.stopPropagation()}
          >
            <input
              ref={inputRef}
              value={q}
              onChange={(e) => {
                setQ(e.target.value);
                setSel(0);
              }}
              onKeyDown={(e) => {
                if (e.key === "ArrowDown") {
                  e.preventDefault();
                  setSel((s) => Math.min(s + 1, results.length - 1));
                } else if (e.key === "ArrowUp") {
                  e.preventDefault();
                  setSel((s) => Math.max(s - 1, 0));
                } else if (e.key === "Enter" && results[sel]) {
                  go(results[sel]);
                }
              }}
              aria-label="Search the wiki"
              placeholder="Search fighters, blasts, mechanics, guides… (e.g. 'vegito', 'super counter', 'dp')"
              className="w-full border-b border-border bg-transparent px-4 py-3 text-sm outline-none placeholder:text-muted"
            />
            <div className="max-h-[50vh] overflow-y-auto">
              {ql && results.length === 0 && (
                <div className="px-4 py-6 text-center text-sm text-muted">No matches for “{q}”.</div>
              )}
              {results.map((e, i) => (
                <button
                  key={e.h + i}
                  onClick={() => go(e)}
                  onMouseEnter={() => setSel(i)}
                  className={`flex w-full items-center gap-3 px-4 py-2 text-left text-sm ${
                    i === sel ? "bg-surface-2" : ""
                  }`}
                >
                  <span className={`w-28 shrink-0 text-[10px] font-medium uppercase tracking-wider ${GROUP_TONE[e.g] ?? "text-muted"}`}>
                    {e.g}
                  </span>
                  <span className="flex-1 truncate">{e.t}</span>
                  {e.x && <span className="shrink-0 text-xs tabular-nums text-muted">{e.x}</span>}
                </button>
              ))}
              {!ql && (
                <div className="px-4 py-6 text-center text-xs text-muted">
                  Type to search all {idx ? idx.length.toLocaleString() : "…"} pages · ↑↓ navigate · Enter to open · Esc to close
                </div>
              )}
            </div>
          </div>
        </div>
      )}
    </>
  );
}
