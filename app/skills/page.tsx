import { getSkills } from "@/lib/content";
import { SkillsTable, type SkillRow } from "@/components/skills-table";

export const metadata = { title: "Skills (Blast Skills)" };

export default function Page() {
  const skills = getSkills();
  const rows: SkillRow[] = skills.map((s) => ({
    name: s.name,
    slug: s.slug,
    cost: s.skillCost,
    duration: s.durationSec ?? null,
    users: s.users.length || s.userCount || 0,
    effect: s.effect ?? null,
  }));
  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-bold">
          Skills{" "}
          <span className="text-base font-normal text-muted">
            ({skills.length} datamined skill names)
          </span>
        </h1>
        <p className="mt-1 max-w-3xl text-sm text-muted">
          Blast Skills (S1/S2 stock skills) — buffs, evasives, heals. User lists are datamined per
          character; costs are datamined where serialized, community-verified otherwise.
        </p>
      </header>
      <SkillsTable rows={rows} />
    </div>
  );
}
