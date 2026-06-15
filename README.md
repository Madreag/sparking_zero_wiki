# Sparking! ZERO Codex

Numbers-first DRAGON BALL: Sparking! ZERO wiki. Datamined stats + quantified patch history +
current meta, rendered as a static Next.js site from typed markdown.

## Quick start

```bash
npm install
npm run dev    # http://localhost:3000
npm run build  # validates every content page against lib/schemas.ts
```

## Refresh data after a game patch

```bash
# 1. extract from the installed game (D:\SteamLibrary\...\DRAGON BALL Sparking! ZERO)
cd tools/extractor && dotnet run -c Release
# 2. rebuild reference tables + regenerate content
python scripts/parse_data.py
python scripts/gen_content.py
# 3. bump lib/version.ts CURRENT_VERSION, add the new content/patches page, rebuild
npm run build
```

See `PLAN.md` for architecture, data-gap notes (usmap), and the update workflow.
