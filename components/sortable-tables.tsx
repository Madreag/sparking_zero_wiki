"use client";

import { useEffect } from "react";
import { usePathname } from "next/navigation";

/**
 * Progressive enhancement: every statically-rendered table in <main> becomes
 * click-to-sort (numeric-aware, asc/desc toggle). Client tables that manage
 * their own sorting opt out with data-sortable-self on the <table>.
 */
export function SortableTables() {
  const path = usePathname();
  useEffect(() => {
    const tables = document.querySelectorAll<HTMLTableElement>(
      "main table:not([data-sortable-self])",
    );
    const cleanups: (() => void)[] = [];
    tables.forEach((table) => {
      const head = table.tHead?.rows[0];
      const tbody = table.tBodies[0];
      if (!head || !tbody || tbody.rows.length < 2) return;
      [...head.cells].forEach((th, idx) => {
        th.style.cursor = "pointer";
        th.title = "Click to sort";
        const handler = () => {
          const dir = th.dataset.dir === "asc" ? -1 : 1;
          [...head.cells].forEach((c) => {
            delete c.dataset.dir;
            c.querySelector(".sort-ind")?.remove();
          });
          th.dataset.dir = dir === 1 ? "asc" : "desc";
          const ind = document.createElement("span");
          ind.className = "sort-ind text-aura";
          ind.textContent = dir === 1 ? " ▲" : " ▼";
          th.appendChild(ind);
          const num = (s: string) => {
            const cleaned = s.replace(/[,%$]/g, "").replace(/^[—–-]$/, "");
            if (!cleaned || !/[\d]/.test(cleaned)) return null;
            const v = parseFloat(cleaned);
            return Number.isNaN(v) ? null : v;
          };
          const rows = [...tbody.rows];
          rows.sort((a, b) => {
            const ta = a.cells[idx]?.textContent?.trim() ?? "";
            const tb = b.cells[idx]?.textContent?.trim() ?? "";
            const na = num(ta);
            const nb = num(tb);
            if (na != null && nb != null) return (na - nb) * dir;
            if (na != null) return -1 * dir;
            if (nb != null) return 1 * dir;
            return ta.localeCompare(tb) * dir;
          });
          rows.forEach((r) => tbody.appendChild(r));
        };
        th.addEventListener("click", handler);
        cleanups.push(() => th.removeEventListener("click", handler));
      });
    });
    return () => cleanups.forEach((f) => f());
  }, [path]);
  return null;
}
