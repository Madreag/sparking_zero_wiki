import { getCharacters } from "@/lib/content";
import { CompareTool, type CompareChar } from "@/components/compare";

export const metadata = { title: "Compare Fighters" };

export default function Page() {
  const chars: CompareChar[] = getCharacters()
    .filter((c) => c.playable)
    .map((c) => ({
      name: c.name,
      slug: c.slug,
      dp: c.dp,
      hp: c.hp ?? null,
      kiCharge: c.kiChargeSpeed ?? null,
      kiRecovery: c.kiAutoRecovery ?? null,
      initialKi: c.initialKi ?? null,
      drain: c.sparkingDrainPerSec ?? null,
      stocksMax: c.maxSkillStock ?? null,
      tier: c.tier,
      playstyle: c.playstyle,
      classes: c.classes,
      era: c.era,
      source: c.source,
      moves: c.moveset.map((m) => ({
        name: m.name,
        type: m.type,
        kiCost: m.kiCost ?? null,
        skillCost: m.skillCost ?? null,
      })),
    }));
  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-bold">Compare Fighters</h1>
        <p className="mt-1 max-w-3xl text-sm text-muted">
          Side-by-side datamined parameters and kits for any two of the {chars.length} playable
          roster slots.
        </p>
      </header>
      <CompareTool chars={chars} />
    </div>
  );
}
