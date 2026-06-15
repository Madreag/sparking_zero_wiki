import { getCharacters } from "@/lib/content";
import { hpPerDp } from "@/lib/formulas";
import { RosterTable, type RosterRow } from "@/components/roster-table";

export const metadata = { title: "Roster" };

export default function Page() {
  const chars = getCharacters();
  const playable = chars.filter((c) => c.playable);
  const bases = new Set(playable.map((c) => c.baseCharacter)).size;
  const rows: RosterRow[] = chars.map((c) => ({
    name: c.name,
    slug: c.slug,
    dp: c.dp,
    hp: c.hp ?? null,
    hpVal: hpPerDp(c.hp, c.dp),
    kiCharge: c.kiChargeSpeed ?? null,
    kiRecovery: c.kiAutoRecovery ?? null,
    stocksInit: c.initialSkillStock ?? null,
    stocksMax: c.maxSkillStock ?? null,
    era: c.era,
    source: c.source,
    tier: c.tier,
    dpTier: c.dpTier,
    classes: c.classes,
    playstyle: c.playstyle,
    playable: c.playable,
  }));
  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-bold">
          Roster{" "}
          <span className="text-base font-normal text-muted">
            ({playable.length} playable slots · {bases} base fighters · {chars.length - playable.length} story-only)
          </span>
        </h1>
        <p className="mt-1 max-w-3xl text-sm text-muted">
          Every roster slot with datamined HP, community-verified DP, tier, and playstyle. Filter,
          sort, and click through for full kits, strengths/weaknesses, and counter-strategies.
        </p>
      </header>
      <RosterTable rows={rows} />
    </div>
  );
}
