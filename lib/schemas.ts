import { z } from "zod";

/**
 * Version/provenance metadata mixed into every fact-bearing entity.
 * Spread as a raw shape (not a ZodObject) so it composes cleanly under Zod 4.
 */
const versionMetaShape = {
  asOfVersion: z.string().optional(),
  asOfDate: z.string().optional(),
  lastVerified: z.string().optional(),
  confidence: z
    .enum(["confirmed", "datamined", "community", "unverified"])
    .default("community"),
  sources: z.array(z.string()).default([]),
};

const changeEntry = z.object({
  version: z.string(),
  date: z.string().optional(),
  change: z.string(),
});

/** One move in a character's kit, numbers-first. */
const moveEntry = z.object({
  name: z.string(),
  // rush = basic chain, smash = heavy, blast1 = skill (S1), blast2 = super (S2),
  // ultimate = ult, evasive = signature evasion, throw, special = unique action
  type: z.enum(["rush", "smash", "throw", "blast1", "blast2", "ultimate", "evasive", "special"]),
  damage: z.number().nullable().optional(),
  hits: z.number().nullable().optional(),
  kiCost: z.number().nullable().optional(),
  skillCost: z.number().nullable().optional(),
  gauge: z.string().optional(),
  properties: z.array(z.string()).default([]),
  notes: z.string().optional(),
});

const transformEntry = z.object({
  target: z.string(), // roster name of the form transformed into
  targetSlug: z.string().optional(),
  cost: z.number().nullable().optional(), // skill-stock cost
  kind: z.enum(["transform", "fusion", "revert"]).default("transform"),
});

export const characterSchema = z.object({
  slug: z.string(),
  name: z.string(),
  charId: z.string().optional(), // internal id e.g. "0000_00"
  baseCharacter: z.string(),
  era: z.string().default("Unsorted"),
  dp: z.number().nullable().default(null),
  source: z.string().default("Base"),
  releaseDate: z.string().optional(),
  unlock: z.string().optional(),
  classes: z.array(z.string()).default([]),
  hp: z.number().nullable().optional(),
  hpInherited: z.boolean().default(false),
  kiChargeSpeed: z.number().nullable().optional(),
  kiAutoRecovery: z.number().nullable().optional(),
  kiAutoRecoveryLimit: z.number().nullable().optional(),
  initialKi: z.number().nullable().optional(),
  maxSkillStock: z.number().nullable().optional(),
  initialSkillStock: z.number().nullable().optional(),
  sparkingDrainPerSec: z.number().nullable().optional(),
  kiBlastShots: z.number().nullable().optional(),
  skillGaugeGains: z.record(z.string(), z.number().nullable()).optional(),
  transformsTo: z.array(transformEntry).default([]),
  moveset: z.array(moveEntry).default([]),
  tier: z.enum(["S", "A", "B", "C", "D", "unranked"]).optional(),
  playable: z.boolean().default(true),
  playstyle: z.string().optional(),
  strengths: z.array(z.string()).default([]),
  weaknesses: z.array(z.string()).default([]),
  howToFight: z.string().optional(),
  summary: z.string().optional(),
  changeHistory: z.array(changeEntry).default([]),
  ...versionMetaShape,
});

/** Blast Skills (S1) — Afterimage, Wild Sense, Instant Transmission, etc. */
export const skillSchema = z.object({
  slug: z.string(),
  name: z.string(),
  skillCost: z.number().nullable().default(null),
  effect: z.string().optional(),
  durationSec: z.number().nullable().optional(),
  magnitude: z.string().optional(),
  users: z.array(z.string()).default([]),
  userCount: z.number().optional(),
  tier: z.enum(["S", "A", "B", "C", "D", "situational"]).optional(),
  summary: z.string().optional(),
  changeHistory: z.array(changeEntry).default([]),
  ...versionMetaShape,
});

const blastUserEntry = z.object({
  character: z.string(),
  characterSlug: z.string().optional(),
  damage: z.number().nullable().optional(),
  chip: z.number().nullable().optional(),
  hits: z.number().nullable().optional(),
  kiCost: z.number().nullable().optional(),
  triggerKiCost: z.number().nullable().optional(),
  category: z.string().nullable().optional(),
  tags: z.array(z.string()).default([]),
  notes: z.string().optional(),
});

/** Blast 2 supers and Ultimate Blasts, one page per named attack. */
export const blastSchema = z.object({
  slug: z.string(),
  name: z.string(),
  class: z.enum(["super", "ultimate"]),
  category: z.string().optional(), // beam / rush / explosion / unblockable etc.
  users: z.array(blastUserEntry).default([]),
  tier: z.enum(["S", "A", "B", "C", "D", "situational"]).optional(),
  summary: z.string().optional(),
  changeHistory: z.array(changeEntry).default([]),
  ...versionMetaShape,
});

export const transformationSchema = z.object({
  slug: z.string(),
  name: z.string(),
  baseCharacter: z.string(),
  from: z.string(),
  to: z.string(),
  cost: z.number().nullable().optional(), // skill stocks
  kind: z.enum(["transform", "fusion", "awaken", "revert"]).default("transform"),
  hpRule: z.string().optional(),
  statChanges: z.string().optional(),
  dpFrom: z.number().optional(),
  dpTo: z.number().optional(),
  summary: z.string().optional(),
  changeHistory: z.array(changeEntry).default([]),
  ...versionMetaShape,
});

const numericValue = z.object({
  label: z.string(),
  value: z.string(), // keep as string so "6f", "12.5%", "2 stocks" all fit
  patch: z.string().optional(),
  tag: z.enum(["official", "datamined", "community"]).optional(),
});

/** Core combat mechanics: vanish, super counter, sparking, perception, etc. */
export const mechanicSchema = z.object({
  slug: z.string(),
  name: z.string(),
  category: z
    .enum(["offense", "defense", "movement", "resource", "system", "status"])
    .default("system"),
  input: z.string().optional(),
  values: z.array(numericValue).default([]),
  counters: z.array(z.string()).default([]),
  counteredBy: z.array(z.string()).default([]),
  summary: z.string().optional(),
  changeHistory: z.array(changeEntry).default([]),
  ...versionMetaShape,
});

export const gameModeSchema = z.object({
  slug: z.string(),
  name: z.string(),
  category: z.enum(["offline", "online", "pve", "pvp", "hub", "training"]).default("offline"),
  players: z.string().optional(),
  access: z.string().optional(),
  rewards: z.array(z.string()).default([]),
  values: z.array(numericValue).default([]),
  summary: z.string().optional(),
  ...versionMetaShape,
});

const episodeBattleEntry = z.object({
  id: z.string(),
  name: z.string(),
  vs: z.array(z.string()).default([]),
  altRoute: z.string().optional(), // exact trigger condition
  altResult: z.string().optional(),
  rewards: z.string().optional(),
});

export const episodeBattleSchema = z.object({
  slug: z.string(),
  name: z.string(),
  character: z.string(),
  order: z.number(),
  battleCount: z.number().optional(),
  sparkingEpisodes: z.number().optional(),
  battles: z.array(episodeBattleEntry).default([]),
  rewards: z.array(z.string()).default([]),
  summary: z.string().optional(),
  ...versionMetaShape,
});

const measuredChange = z.object({
  target: z.string(),
  metric: z.string(),
  old: z.string().optional(),
  new: z.string().optional(),
  note: z.string().optional(),
});

export const patchNoteSchema = z.object({
  slug: z.string(),
  version: z.string(),
  releaseDate: z.string(),
  order: z.number(),
  headline: z.string().optional(),
  type: z.enum(["launch", "major", "balance", "content", "hotfix"]).default("content"),
  changes: z.array(z.string()).default([]),
  measured: z.array(measuredChange).default([]),
  summary: z.string().optional(),
  ...versionMetaShape,
});

const dlcCharacterEntry = z.object({
  name: z.string(),
  dp: z.number().nullable().optional(),
  slug: z.string().optional(),
});

export const dlcSchema = z.object({
  slug: z.string(),
  name: z.string(),
  releaseDate: z.string(),
  order: z.number(),
  type: z.enum(["paid", "free", "preorder", "season-pass"]).default("paid"),
  priceUSD: z.number().nullable().optional(),
  characters: z.array(dlcCharacterEntry).default([]),
  adds: z.array(z.string()).default([]),
  upcoming: z.boolean().default(false),
  summary: z.string().optional(),
  ...versionMetaShape,
});

export const guideSchema = z.object({
  slug: z.string(),
  title: z.string(),
  category: z
    .enum(["meta", "pvp", "pve", "beginner", "tech", "economy", "tier-list"])
    .default("meta"),
  summary: z.string().optional(),
  ...versionMetaShape,
});

export const stageSchema = z.object({
  slug: z.string(),
  name: z.string(),
  source: z.string().default("Base"),
  destructible: z.string().optional(),
  variants: z.array(z.string()).default([]),
  notes: z.string().optional(),
  summary: z.string().optional(),
  ...versionMetaShape,
});

const shopItem = z.object({
  name: z.string(),
  price: z.number().nullable().optional(),
  currency: z.string().default("Zeni"),
  type: z.string().optional(),
  unlock: z.string().optional(),
});

/** One page per shop/unlock category, holding a full price table. */
export const shopCategorySchema = z.object({
  slug: z.string(),
  name: z.string(),
  items: z.array(shopItem).default([]),
  summary: z.string().optional(),
  ...versionMetaShape,
});

export const glossaryTermSchema = z.object({
  slug: z.string(),
  term: z.string(),
  definition: z.string(),
  aliases: z.array(z.string()).default([]),
  category: z.string().optional(),
  ...versionMetaShape,
});

export type Character = z.infer<typeof characterSchema>;
export type Skill = z.infer<typeof skillSchema>;
export type Blast = z.infer<typeof blastSchema>;
export type Transformation = z.infer<typeof transformationSchema>;
export type Mechanic = z.infer<typeof mechanicSchema>;
export type GameMode = z.infer<typeof gameModeSchema>;
export type EpisodeBattle = z.infer<typeof episodeBattleSchema>;
export type PatchNote = z.infer<typeof patchNoteSchema>;
export type DLC = z.infer<typeof dlcSchema>;
export type Guide = z.infer<typeof guideSchema>;
export type Stage = z.infer<typeof stageSchema>;
export type ShopCategory = z.infer<typeof shopCategorySchema>;
export type GlossaryTerm = z.infer<typeof glossaryTermSchema>;
