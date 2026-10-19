# Agent skills for the SEO glossary

One skill, packaged for three coding agents. Each folder holds a `SKILL.md` with the same body: locate the glossary, read it before writing, use only its terms, run the checker before delivering, propose missing terms as rows.

| Agent | Copy the folder to | Install |
|---|---|---|
| Claude Code | `~/.claude/skills/seo-glossary/` (or `.claude/skills/` inside a project) | `cp -r skills/claude/seo-glossary ~/.claude/skills/` |
| OpenAI Codex | `~/.codex/skills/seo-glossary/` | `cp -r skills/codex/seo-glossary ~/.codex/skills/` |
| Gemini CLI and Antigravity | `~/.gemini/config/skills/seo-glossary/` (or `.gemini/skills/` inside a project) | `cp -r skills/gemini/seo-glossary ~/.gemini/config/skills/` |

The skill finds the glossary through `$SEO_GLOSSARY_DIR`, a `seo-glossary.md` in the current repository, or `~/seo-glossary/`. Set the variable when the clone lives elsewhere:

```bash
export SEO_GLOSSARY_DIR=/path/to/seo-glossary
```

Invoke it with `/seo-glossary`, or let it trigger on any task that produces an SEO document.
