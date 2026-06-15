import fs from "node:fs";
import path from "node:path";
import matter from "gray-matter";
import { z } from "zod";
import {
  characterSchema,
  skillSchema,
  blastSchema,
  transformationSchema,
  mechanicSchema,
  gameModeSchema,
  episodeBattleSchema,
  patchNoteSchema,
  dlcSchema,
  guideSchema,
  stageSchema,
  shopCategorySchema,
  glossaryTermSchema,
} from "./schemas";

const CONTENT_DIR = path.join(process.cwd(), "content");

export type WithBody<T> = T & { body: string };

function loadCollection<S extends z.ZodTypeAny>(
  dir: string,
  schema: S,
): WithBody<z.infer<S>>[] {
  const full = path.join(CONTENT_DIR, dir);
  if (!fs.existsSync(full)) return [];
  return fs
    .readdirSync(full)
    .filter((f) => f.endsWith(".md"))
    .map((file) => {
      const raw = fs.readFileSync(path.join(full, file), "utf8");
      const { data, content } = matter(raw);
      const slug = (data.slug as string) ?? file.replace(/\.md$/, "");
      try {
        const parsed = schema.parse({ ...data, slug }) as Record<string, unknown>;
        return { ...parsed, body: content.trim() } as WithBody<z.infer<S>>;
      } catch (err) {
        throw new Error(
          `Content validation failed for content/${dir}/${file}: ${
            err instanceof Error ? err.message : String(err)
          }`,
        );
      }
    });
}

export function getCharacters() {
  return loadCollection("characters", characterSchema).sort((a, b) =>
    a.name.localeCompare(b.name),
  );
}
export function getCharacter(slug: string) {
  return getCharacters().find((c) => c.slug === slug);
}

export function getSkills() {
  return loadCollection("skills", skillSchema).sort((a, b) => a.name.localeCompare(b.name));
}
export function getSkill(slug: string) {
  return getSkills().find((s) => s.slug === slug);
}

export function getBlasts() {
  return loadCollection("blasts", blastSchema).sort((a, b) => a.name.localeCompare(b.name));
}
export function getBlast(slug: string) {
  return getBlasts().find((b) => b.slug === slug);
}

export function getTransformations() {
  return loadCollection("transformations", transformationSchema).sort((a, b) =>
    a.name.localeCompare(b.name),
  );
}
export function getTransformation(slug: string) {
  return getTransformations().find((t) => t.slug === slug);
}

export function getMechanics() {
  return loadCollection("mechanics", mechanicSchema).sort((a, b) =>
    a.name.localeCompare(b.name),
  );
}
export function getMechanic(slug: string) {
  return getMechanics().find((m) => m.slug === slug);
}

export function getGameModes() {
  return loadCollection("game-modes", gameModeSchema).sort((a, b) =>
    a.name.localeCompare(b.name),
  );
}
export function getGameMode(slug: string) {
  return getGameModes().find((g) => g.slug === slug);
}

export function getEpisodeBattles() {
  return loadCollection("episode-battles", episodeBattleSchema).sort(
    (a, b) => a.order - b.order,
  );
}
export function getEpisodeBattle(slug: string) {
  return getEpisodeBattles().find((e) => e.slug === slug);
}

export function getPatchNotes() {
  return loadCollection("patches", patchNoteSchema).sort((a, b) => b.order - a.order);
}
export function getPatchNote(slug: string) {
  return getPatchNotes().find((p) => p.slug === slug);
}

export function getDLCs() {
  return loadCollection("dlc", dlcSchema).sort((a, b) => a.order - b.order);
}
export function getDLC(slug: string) {
  return getDLCs().find((d) => d.slug === slug);
}

export function getGuides() {
  return loadCollection("guides", guideSchema).sort((a, b) => a.title.localeCompare(b.title));
}
export function getGuide(slug: string) {
  return getGuides().find((g) => g.slug === slug);
}

export function getStages() {
  return loadCollection("stages", stageSchema).sort((a, b) => a.name.localeCompare(b.name));
}
export function getStage(slug: string) {
  return getStages().find((s) => s.slug === slug);
}

export function getShopCategories() {
  return loadCollection("shop", shopCategorySchema).sort((a, b) =>
    a.name.localeCompare(b.name),
  );
}
export function getShopCategory(slug: string) {
  return getShopCategories().find((s) => s.slug === slug);
}

export function getGlossary() {
  return loadCollection("glossary", glossaryTermSchema).sort((a, b) =>
    a.term.localeCompare(b.term),
  );
}
export function getGlossaryTerm(slug: string) {
  return getGlossary().find((t) => t.slug === slug);
}

export function normalizeSlug(s: string): string {
  // Must mirror scripts/gen_content.py `slugify` exactly, or [[wikilinks]] typed
  // with the display name (punctuation/accents) won't resolve to the generated slug.
  return s
    .toLowerCase()
    .replace(/['’!.]/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

/**
 * slug/alias -> canonical href, built once across every collection so that
 * Obsidian-style [[wikilinks]] in content resolve to real pages.
 */
let _slugIndex: Map<string, { href: string; label: string }> | null = null;

export function getSlugIndex() {
  if (_slugIndex) return _slugIndex;
  const m = new Map<string, { href: string; label: string }>();
  const add = (items: { slug: string }[], prefix: string, label: (i: never) => string) => {
    for (const i of items) {
      if (!m.has(i.slug)) m.set(i.slug, { href: `${prefix}/${i.slug}`, label: label(i as never) });
    }
  };
  add(getCharacters(), "/characters", (i: { name: string }) => i.name);
  add(getSkills(), "/skills", (i: { name: string }) => i.name);
  add(getBlasts(), "/blasts", (i: { name: string }) => i.name);
  add(getTransformations(), "/transformations", (i: { name: string }) => i.name);
  add(getMechanics(), "/mechanics", (i: { name: string }) => i.name);
  add(getGameModes(), "/game-modes", (i: { name: string }) => i.name);
  add(getEpisodeBattles(), "/episode-battles", (i: { name: string }) => i.name);
  add(getPatchNotes(), "/patches", (i: { version: string }) => i.version);
  add(getDLCs(), "/dlc", (i: { name: string }) => i.name);
  add(getGuides(), "/guides", (i: { title: string }) => i.title);
  add(getStages(), "/stages", (i: { name: string }) => i.name);
  add(getShopCategories(), "/shop", (i: { name: string }) => i.name);
  for (const t of getGlossary()) {
    if (!m.has(t.slug)) m.set(t.slug, { href: `/glossary#${t.slug}`, label: t.term });
    for (const a of t.aliases) {
      const k = normalizeSlug(a);
      if (!m.has(k)) m.set(k, { href: `/glossary#${t.slug}`, label: t.term });
    }
  }
  _slugIndex = m;
  return m;
}
