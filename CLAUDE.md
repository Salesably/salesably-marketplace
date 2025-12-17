# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is **Salesably Marketplace**, a collection of Claude Code plugins for sales and marketing teams. It functions as a marketplace that users add to Claude Code, then install individual plugins from.

## Architecture

```
salesably-marketplace/
├── .claude-plugin/
│   └── marketplace.json     # Marketplace manifest - lists available plugins
├── marketing-skills/        # Marketing plugin (10 skills)
│   ├── .claude-plugin/
│   │   └── plugin.json      # Plugin manifest - declares skills path
│   ├── README.md            # Plugin documentation
│   └── skills/              # 10 marketing skills (each folder has SKILL.md)
│       ├── brand-voice/
│       ├── positioning-angles/
│       ├── keyword-research/
│       ├── lead-magnet/
│       ├── direct-response-copy/
│       ├── seo-content/
│       ├── newsletter/
│       ├── email-sequences/
│       ├── content-atomizer/
│       └── orchestrator/
├── sales-skills/            # Sales plugin (9 skills)
│   ├── .claude-plugin/
│   │   └── plugin.json
│   ├── README.md
│   └── skills/
│       ├── powerful-framework/
│       ├── prospect-research/
│       ├── account-qualification/
│       ├── company-intelligence/
│       ├── cold-call-scripts/
│       ├── call-analysis/
│       ├── follow-up-emails/
│       ├── multithread-outreach/
│       └── sales-orchestrator/
└── README.md                # Marketplace installation instructions
```

## Key Concepts

**Marketplace vs Plugin**: The root directory is a marketplace container. Individual plugins (like `marketing-skills`, `sales-skills`) live in subdirectories with their own `plugin.json`.

**Skills**: Each skill is a markdown file (`SKILL.md`) with YAML frontmatter containing `name` and `description`. The markdown body provides detailed instructions Claude uses when the skill is invoked.

**Marketing Skill Layers**:
- Foundation: brand-voice, positioning-angles
- Strategy: keyword-research, lead-magnet
- Execution: direct-response-copy, seo-content, newsletter, email-sequences
- Distribution: content-atomizer, orchestrator

**Sales Skill Layers**:
- Foundation: powerful-framework, prospect-research
- Strategy: account-qualification, company-intelligence
- Execution: cold-call-scripts, call-analysis, follow-up-emails, multithread-outreach
- Orchestration: sales-orchestrator

## Working with Skills

Skills follow this structure:
```markdown
---
name: skill-name
description: When to trigger this skill...
---

# Skill Name

[Detailed instructions, frameworks, and output formats]
```

The `description` field in frontmatter determines when Claude automatically suggests using the skill.

## Adding New Skills

1. Create a new directory under the appropriate plugin's `skills/` folder
   - Marketing skills: `marketing-skills/skills/`
   - Sales skills: `sales-skills/skills/`
2. Add a `SKILL.md` file with proper frontmatter
3. Skills are auto-discovered via the `"skills": "./skills"` path in `plugin.json`

## Adding New Plugins

1. Create a new directory at the repository root
2. Add `.claude-plugin/plugin.json` with plugin metadata
3. Register in `.claude-plugin/marketplace.json` under the `plugins` array

## MCP Tool Integrations

The sales-skills plugin includes optional MCP server integrations for enhanced research:

**Location:** `sales-skills/.mcp.json`

**Available Tools:**
- **Perplexity** - AI-powered web search
- **Exa** - Semantic search for companies/people
- **Apify** - Web scraping and data extraction
- **Hunter.io** - Email finding and verification

**Configuration:**
- All tools are disabled by default (`"disabled": true`)
- Users set API keys as environment variables
- Enable tools by changing `"disabled": false` in `.mcp.json`
- See `sales-skills/README.md` for detailed setup instructions
