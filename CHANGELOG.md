# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- New `CONTRIBUTING.md` guide for open-source contributors.
- GitHub Issue and Pull Request templates.
- Explicit "No Em-Dashes" and "Human-First" guidelines to marketing skills.
- Recommendations and instructions for Anthropic core document skills.
- Basic validation principles for marketplace maintenance.

### Fixed
- `sales-skills` MCP servers for Perplexity, Apify and Hunter pointed at npm packages that do not exist (`@anthropic/mcp-server-perplexity`, `@anthropic/mcp-server-apify`, and the generic `@anthropic/mcp-server-fetch` for Hunter), so they never connected. They now use each vendor's official server: `@perplexity-ai/mcp-server`, `@apify/actors-mcp-server` (still read from `APIFY_API_TOKEN`), and Hunter's hosted server at `https://mcp.hunter.io/mcp`.

### Changed
- Enhanced marketing skills with viral LinkedIn frameworks (2025).
- Improved SEO content instructions to prioritize human-led outlines and narrative arcs.
- Updated READMEs with Claude Code context and installation links.
- Replaced all em-dashes and en-dashes with hyphens in skill files.

## [1.0.0] - 2024-12-17

### Added
- Initial release of Salesably Marketplace.
- `marketing-skills` plugin with 10 specialized skills.
- `sales-skills` plugin with 9 specialized skills and MCP tool integrations.
