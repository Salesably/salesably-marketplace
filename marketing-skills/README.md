# Marketing Skills Plugin

**Marketing that actually moves the needle.**

Stop churning out generic content. These 10 skills transform Claude into your strategic marketing partner—building brand foundations, crafting copy that converts, and distributing content that compounds.

Built on proven frameworks used to build audiences and drive revenue for modern businesses.

**Built by [Salesably.ai](https://salesably.ai)** — AI-powered sales and marketing tools for modern teams.

> **Inspired by [The Vibe Marketer](https://thevibemarketer.com)** — check them out for more marketing insights and strategies.

## What is this?

This is a plugin for **Claude Code**, Anthropic's agentic command-line interface. It adds 10 specialized marketing skills to Claude, allowing it to act as a strategic partner for your marketing team. 

If you are new to Claude Code, [start here](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview).

## Recommended: Core Document Skills

To get the most out of these marketing skills, we highly recommend adding Anthropic's core document skills. They are essential for generating and editing the actual files (briefs, slide decks, reports) that these skills help you create:

- **DOCX**: Create and edit Word documents with formatting, comments, and tracked changes preserved.
- **PPTX**: Generate and modify PowerPoint decks, including layouts, charts, and structured slide sections.
- **XLSX**: Build and analyze Excel spreadsheets with formulas, tables, and charts.
- **PDF**: Extract text, split/merge files, fill forms, and create new PDFs.

### How to install:
1. **Add the Anthropic marketplace:**
   ```
   /plugin marketplace add anthropics/skills
   ```
2. **Install the document skills:**
   - Run `/plugin install`
   - Select **Browse and install plugins**
   - Select **anthropic-agent-skills**
   - Select **document-skills**
   - Select **Install now**

## Installation

```bash
# Add this plugin to your Claude Code settings
claude plugin install ./marketing-skills
```

## Skills Overview

### Foundation Layer
Build the base everything else sits on.

| Skill | Purpose |
|-------|---------|
| **brand-voice** | Define consistent communication using 4 voice dimensions and the this-but-not-that framework |
| **positioning-angles** | Find market differentiation using 8 proven positioning frameworks |

### Strategy Layer
Plan before you execute.

| Skill | Purpose |
|-------|---------|
| **keyword-research** | Identify content opportunities using the 6 Circles Method |
| **lead-magnet** | Create high-converting opt-in offers with hooks, formats, and validation |

### Execution Layer
Create the actual marketing assets.

| Skill | Purpose |
|-------|---------|
| **direct-response-copy** | Write landing pages and sales copy using page architecture + persuasion principles |
| **seo-content** | Create search-optimized articles that rank AND read well |
| **newsletter** | Build recurring engagement with 9 proven newsletter formats |
| **email-sequences** | Automate customer journeys: welcome, nurture, conversion, launch |

### Distribution & Meta Layer
Maximize reach and orchestrate everything.

| Skill | Purpose |
|-------|---------|
| **content-atomizer** | Repurpose one piece into many formats across platforms |
| **orchestrator** | Route and sequence skills for comprehensive campaigns |

## Quick Start

### Not sure where to start?
Start with **orchestrator**—it will diagnose your needs and recommend the right skills:
- "Help me plan a product launch"
- "I need to build an email list"
- "What marketing should I focus on?"

### Know what you need?
Use skills directly:
- "Create a brand voice guide for my SaaS startup"
- "Find positioning angles for my consulting business"
- "Write a landing page for my online course"
- "Build a welcome email sequence"

## Common Workflows

### New Product Launch
```
brand-voice → positioning-angles → lead-magnet → direct-response-copy → email-sequences → content-atomizer
```

### Content Engine
```
keyword-research → seo-content → content-atomizer → newsletter
```

### Lead Generation System
```
lead-magnet → direct-response-copy → email-sequences (welcome → nurture → conversion)
```

### Brand Refresh
```
brand-voice → positioning-angles → update all existing content
```

## Skill Dependencies

Skills work together. Here's how they connect:

```
brand-voice ─────────────────────────────────────────┐
     │                                                │
     ▼                                                │
positioning-angles                                    │
     │                                                │
     ├─────────────┬────────────────┐                │
     ▼             ▼                ▼                │
keyword-research  lead-magnet  direct-response-copy  │
     │             │                │                │
     ▼             │                │                │
seo-content ◄──────┼────────────────┘                │
     │             │                                  │
     ├─────────────┤                                  │
     ▼             ▼                                  │
newsletter    email-sequences                         │
     │             │                                  │
     └─────┬───────┘                                  │
           ▼                                          │
   content-atomizer                                   │
           │                                          │
           ▼                                          │
     orchestrator ◄───────────────────────────────────┘
```

## Key Frameworks Included

- **4 Voice Dimensions** (brand-voice)
- **8 Positioning Frameworks** (positioning-angles)
- **6 Circles Method** (keyword-research)
- **Hook Formulas & Format Selection** (lead-magnet)
- **Page Architecture + Cialdini's 6 Principles** (direct-response-copy)
- **E-E-A-T & Intent Matching** (seo-content)
- **9 Newsletter Formats** (newsletter)
- **6 Sequence Types** (email-sequences)
- **Atomization Matrix** (content-atomizer)
- **Sequencing Playbooks** (orchestrator)

## Philosophy

These skills are designed to be:

1. **Actionable** — Frameworks and templates you can use immediately
2. **Interconnected** — Skills reference and build on each other
3. **Human-first** — Focus on genuinely good marketing, not tricks
4. **Distinctive** — Avoid generic AI output and templates

## Author

Created by [Vidal Graupera](https://salesably.ai) for modern marketing teams.

## More AI Tools

Check out [Salesably.ai](https://salesably.ai) for more AI-powered sales and marketing tools.

## License

MIT
