<p align="center">
  <img src="assets/logo.jpeg" alt="Salesably Marketplace" width="400">
</p>

# Salesably Marketplace

**Your unfair advantage in sales and marketing.**

Turn Claude into a seasoned sales strategist and marketing expert. These plugins bring battle-tested frameworks, proven methodologies, and systematic approaches that top performers use—now available at your fingertips.

Built by [Salesably.ai](https://salesably.ai).

## Available Plugins

| Plugin | Description |
|--------|-------------|
| **[marketing-skills](./marketing-skills)** | 10 specialized marketing skills: brand voice, positioning, content strategy, copywriting, and distribution |
| **[sales-skills](./sales-skills)** | 9 specialized sales skills: deal qualification, prospect research, call preparation, and stakeholder engagement |

## Installation

1. **Add the marketplace:**
   ```
   /plugin marketplace add Salesably/salesably-marketplace
   ```

2. **Install a plugin:**
   ```
   /plugin install marketing-skills
   /plugin install sales-skills
   ```

3. **Restart Claude Code** to load the new skills.

## Recommended: Core Document Skills

To get the most out of these sales and marketing plugins, we highly recommend adding Anthropic's core document skills. They are essential for generating and editing the actual files (decks, spreadsheets, PDFs) that these skills strategize:

- **DOCX**: Create and edit Word documents with formatting, comments, and tracked changes preserved.
- **PPTX**: Generate and modify PowerPoint decks, including layouts, charts, and structured slide sections.
- **XLSX**: Build and analyze Excel spreadsheets with formulas, tables, and charts.
- **PDF**: Extract text, split/merge files, fill forms, and create new PDFs.

## Important: Skill Limits

Claude Code has a token limit for displaying available skills. If you have many plugins installed, some skills may be truncated from the list and Claude won't automatically use them.

**Symptoms:**
- Claude uses generic approaches instead of your installed skills
- You see "Showing X of Y skills due to token limits" in skill listings

**Solutions:**
- Uninstall plugins you're not actively using
- Explicitly invoke skills by name: `use the sales-skills:powerful-framework skill`
- Keep your most important plugins installed and remove others

This marketplace adds 19 skills total (10 marketing + 9 sales). If you have many other plugins, consider which ones you need most.

## Claude Desktop Users

**Q: Do these work in Claude Desktop?**

Skills don't auto-load in Claude Desktop, but you can still use them:
- Add SKILL.md files to a **Project** as knowledge files
- Copy/paste skill content into conversations

The **MCP research tools** (Perplexity, Exa, Hunter, Apify) in the sales-skills plugin work in Claude Desktop with separate configuration. See the [sales-skills SETUP-GUIDE](./sales-skills/SETUP-GUIDE.md#claude-desktop-setup) for instructions.

## About Salesably

[Salesably.ai](https://salesably.ai) builds AI-powered tools for modern sales and marketing teams.

## Contact & Support

- Website: [Salesably.ai](https://salesably.ai)
- Contact: [https://www.salesably.ai/contact](https://www.salesably.ai/contact)

## License

MIT
