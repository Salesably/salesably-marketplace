# Contributing to Salesably Marketplace

We welcome contributions to the Salesably Marketplace! Whether you're adding new skills, improving existing ones, or suggesting new plugins, your help is appreciated.

## Ways to Contribute

### 1. Adding New Skills
Skills are the heart of this marketplace. To add a new skill to an existing plugin:

1. Create a new directory under the appropriate plugin's `skills/` folder:
   - Marketing: `marketing-skills/skills/`
   - Sales: `sales-skills/skills/`
2. Add a `SKILL.md` file with YAML frontmatter:
   ```markdown
   ---
   name: your-skill-name
   description: Brief description of when to use this skill.
   ---
   # Skill Name
   
   Detailed instructions, frameworks, and output formats.
   ```
3. Skills are automatically discovered by Claude Code via the `plugin.json` configuration.

### 2. Adding New Plugins
If you have a collection of related skills, you can create a new plugin:

1. Create a new directory at the repository root.
2. Add a `.claude-plugin/plugin.json` file with plugin metadata.
3. Register the plugin in the root `.claude-plugin/marketplace.json` under the `plugins` array.

### 3. Improving Existing Skills
Found a typo, a bug in an MCP integration, or a way to make a framework even more effective? Open a Pull Request!

## Guidelines

- **Human-First**: We aim for high-quality, non-generic output. Follow the "Human Content Principles" found in the `brand-voice` skill.
- **Punctuation**: We avoid em-dashes (—) and en-dashes (–) in skill content. Use standard hyphens (-) or colons instead.
- **Consistency**: Match the tone and structure of existing skills.
- **Testing**: If you add or modify a skill, test it in Claude Code to ensure it triggers correctly and provides useful output.

## Development Process

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes.
4. Verify changes in your local Claude Code environment.
5. Submit a Pull Request with a clear description of your changes.

---

Built with ❤️ by the team at [Salesably.ai](https://salesably.ai).
