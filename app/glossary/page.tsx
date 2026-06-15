import { getGlossary } from "@/lib/content";

export const metadata = { title: "Glossary" };

export default function Page() {
  const terms = getGlossary();
  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-bold">
          Glossary <span className="text-base font-normal text-muted">({terms.length} terms)</span>
        </h1>
        <p className="mt-1 max-w-3xl text-sm text-muted">
          Community and in-game terminology, with the numbers behind each term where they exist.
        </p>
      </header>
      <dl className="space-y-4">
        {terms.map((t) => (
          <div key={t.slug} id={t.slug} className="rounded-xl border border-border bg-surface p-4">
            <dt className="flex flex-wrap items-baseline gap-2">
              <span className="font-semibold text-ki">{t.term}</span>
              {t.aliases.length > 0 && (
                <span className="text-xs text-muted">also: {t.aliases.join(", ")}</span>
              )}
              {t.category && <span className="ml-auto text-xs uppercase text-muted">{t.category}</span>}
            </dt>
            <dd className="mt-1 text-sm text-muted">{t.definition}</dd>
          </div>
        ))}
      </dl>
    </div>
  );
}
