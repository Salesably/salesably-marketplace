# Sales Skills Plugin

**Stop winging it. Start winning.**

Transform your sales prep from guesswork into a systematic advantage. These 9 skills turn Claude into your personal sales strategist—qualifying deals, researching prospects, crafting calls, and engaging stakeholders with the rigor of a top performer.

Built on proven methodologies including the POWERFUL framework, used by elite sales teams to consistently close complex deals.

**Built by [Salesably.ai](https://salesably.ai)** — AI-powered sales and marketing tools for modern teams.

> **Inspired by [Prep5](https://prep5.salesably.ai/)**, our AI-powered sales preparation platform. Visit [prep5.salesably.ai](https://prep5.salesably.ai/) for the full product with integrated research tools, CRM sync, and more.

## What is this?

This is a plugin for **Claude Code**, Anthropic's agentic command-line interface. It adds 9 specialized sales skills to Claude, allowing it to act as your personal sales strategist—qualifying deals, researching prospects, and preparing for calls with the rigor of a top performer.

If you are new to Claude Code, [start here](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview).

## Installation

```bash
# Add this plugin to your Claude Code settings
claude plugin install ./sales-skills
```

## Skills Overview

### Foundation Layer
Build the knowledge base for effective selling.

| Skill | Purpose |
|-------|---------|
| **powerful-framework** | Qualify deals using the POWERFUL framework (Pain, Opportunity Cost, Wants, Executive Influence, Resources, Fear, Trust, Little Things) |
| **prospect-research** | Create comprehensive prospect profiles and knowledge capsules for personalized outreach |

### Strategy Layer
Plan before you execute.

| Skill | Purpose |
|-------|---------|
| **account-qualification** | Tier and prioritize accounts based on signals, fit, and potential |
| **company-intelligence** | Generate 11-section company research reports for strategic selling |

### Execution Layer
Create the actual sales assets.

| Skill | Purpose |
|-------|---------|
| **cold-call-scripts** | Build personalized cold call scripts using the 5-step framework |
| **call-analysis** | Extract POWERFUL insights, action items, and opportunity ratings from call transcripts |
| **follow-up-emails** | Write professional post-call emails that capture key points and drive next steps |
| **multithread-outreach** | Create role-specific messages for multiple stakeholders in a deal |

### Orchestration Layer
Navigate and sequence skills effectively.

| Skill | Purpose |
|-------|---------|
| **sales-orchestrator** | Diagnose needs and sequence skills for comprehensive deal execution |

## Quick Start

### Not sure where to start?
Start with **sales-orchestrator**—it will diagnose your needs and recommend the right skills:
- "Help me prepare for a sales call"
- "I have a deal that's stuck"
- "What should I do after this call?"

### Know what you need?
Use skills directly:
- "Analyze this call transcript using POWERFUL framework"
- "Create a cold call script for this prospect"
- "Research this company for my upcoming meeting"
- "Write a follow-up email after my discovery call"

## Common Workflows

### New Prospect Outreach
```
account-qualification → company-intelligence → prospect-research → cold-call-scripts → follow-up-emails
```

### Post-Call Processing
```
call-analysis → powerful-framework → follow-up-emails → multithread-outreach
```

### Deal Acceleration
```
powerful-framework → company-intelligence → multithread-outreach → follow-up-emails
```

### Account Planning
```
company-intelligence → account-qualification → prospect-research → multithread-outreach
```

## Skill Dependencies

Skills work together. Here's how they connect:

```
account-qualification ──────────────────────────────┐
        │                                            │
        ▼                                            │
company-intelligence                                 │
        │                                            │
        ├──────────────┐                             │
        ▼              ▼                             │
prospect-research    powerful-framework              │
        │              │                             │
        ▼              ▼                             │
cold-call-scripts    call-analysis                   │
        │              │                             │
        └──────┬───────┘                             │
               ▼                                     │
        follow-up-emails                             │
               │                                     │
               ▼                                     │
      multithread-outreach                           │
               │                                     │
               ▼                                     │
       sales-orchestrator ◄──────────────────────────┘
```

## Key Frameworks Included

- **POWERFUL Framework** (powerful-framework, call-analysis)
- **5-Step Cold Call Framework** (cold-call-scripts)
- **Account Tiering System** (account-qualification)
- **11-Section Company Intelligence Report** (company-intelligence)
- **Knowledge Capsule Format** (prospect-research)
- **Role-Based Stakeholder Messaging** (multithread-outreach)
- **Structured Follow-Up Templates** (follow-up-emails)

## Tool Integrations (Optional)

This plugin includes optional MCP server integrations that supercharge your research capabilities. **All tools are disabled by default**—you enable only the ones you need.

> **New to this?** See the **[SETUP-GUIDE.md](./SETUP-GUIDE.md)** for beginner-friendly, step-by-step instructions with screenshots for both Mac and Windows.

### Available Tools

| Tool | Purpose | Best For |
|------|---------|----------|
| **Perplexity** | AI-powered web search and research | company-intelligence, prospect-research, account-qualification |
| **Exa** | Semantic search for companies and people | prospect-research, company-intelligence |
| **Apify** | Web scraping and data extraction | prospect-research (LinkedIn), company-intelligence |
| **Hunter.io** | Email finding and verification | prospect-research, multithread-outreach |

### Quick Setup (3 Steps)

1. **Get an API key** from one of the services above
2. **Set the environment variable** on your computer
3. **Enable the tool** in `.mcp.json` by changing `"disabled": true` to `"disabled": false`

**Detailed instructions:** See **[SETUP-GUIDE.md](./SETUP-GUIDE.md)** for:
- Step-by-step instructions for getting each API key
- Mac setup instructions
- Windows setup instructions
- Troubleshooting common problems
- Cost breakdown and recommendations

### Which Tools to Enable?

| If you mainly need... | Enable these |
|-----------------------|--------------|
| Company research | Perplexity, Exa |
| Prospect research | Exa, Apify, Hunter.io |
| Finding email addresses | Hunter.io |
| LinkedIn data | Apify |
| General research | Perplexity |

### How Tools Work With Skills

When tools are enabled, just ask Claude to use them:

```
"Use Perplexity to research Acme Corp's recent news"
"Use Hunter to find the email for John Smith at Acme Corp"
"Search Exa for the VP of Sales at Acme Corp"
```

Skills like **company-intelligence**, **prospect-research**, and **account-qualification** will automatically suggest using available tools when relevant.

**Having trouble?** See the troubleshooting section in [SETUP-GUIDE.md](./SETUP-GUIDE.md).

## Claude Desktop Compatibility

**Q: Do these skills work in Claude Desktop?**

| Feature | Claude Code | Claude Desktop |
|---------|-------------|----------------|
| Skills (auto-loaded) | Yes | No |
| MCP Tools (Perplexity, etc.) | Yes | Yes |

### Using Skills in Claude Desktop

The skills won't auto-load, but you can still use them:

1. **Projects Method (Recommended):** Create a Project in Claude Desktop and add the SKILL.md files you want as knowledge files. Claude will reference them in that project.

2. **Copy/Paste Method:** Open a SKILL.md file, copy its contents, and paste into your conversation. Ask Claude to follow those instructions.

3. **Reference Method:** Keep the skill files open and manually reference the frameworks (e.g., "Use the POWERFUL framework to analyze this deal").

### Using MCP Tools in Claude Desktop

The research tools (Perplexity, Exa, Hunter, Apify) **do work** in Claude Desktop with separate configuration.

See **[SETUP-GUIDE.md](./SETUP-GUIDE.md#claude-desktop-setup)** for Claude Desktop MCP setup instructions.

## Philosophy

These skills are designed to be:

1. **Research-Driven** — Quality selling starts with quality intelligence
2. **Framework-Based** — Proven methodologies, not guesswork
3. **Interconnected** — Skills build on each other naturally
4. **Human-Centered** — Focus on genuine value, not tricks

## Author

Created by [Vidal Graupera](https://salesably.ai) for modern sales teams.

## Contact & Support

- Website: [Salesably.ai](https://salesably.ai)
- Contact: [https://www.salesably.ai/contact](https://www.salesably.ai/contact)

## More AI Tools

Check out [Salesably.ai](https://salesably.ai) for more AI-powered sales and marketing tools.

## License

MIT
