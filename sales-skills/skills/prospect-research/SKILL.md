---
name: prospect-research
description: Creates comprehensive prospect profiles and knowledge capsules for sales preparation. Use this skill when researching new prospects, preparing for calls, onboarding to new accounts, or updating prospect intelligence.
---

# Prospect Research

This skill creates comprehensive prospect profiles ("knowledge capsules") that give you everything you need to have relevant, personalized sales conversations.

## Objective

Build deep understanding of individual prospects-their background, role, priorities, and connection points-to enable personalized outreach and meaningful conversations.

## Research Dimensions

### 1. Professional Profile

**Basic Information:**
- Full name and preferred name
- Current title and company
- Location and time zone
- LinkedIn profile URL
- Email address (if available)

**Career Context:**
- How long in current role
- Previous roles and companies
- Career trajectory and progression
- Industry experience depth

### 2. Role & Responsibilities

**What They Own:**
- Department or function they lead
- Team size and structure
- Key metrics they're measured on
- Budget authority and scope

**Daily Reality:**
- What does their typical day look like?
- What tools and systems do they use?
- Who do they report to?
- Who reports to them?

### 3. Professional Interests

**LinkedIn Activity:**
- Topics they post about
- Content they engage with
- Groups they belong to
- Thought leadership themes

**Public Content:**
- Articles or blogs they've written
- Podcasts or webinars they've appeared on
- Conference presentations
- Published perspectives or opinions

### 4. Connection Points

**Mutual Connections:**
- Shared contacts on LinkedIn
- Common former employers
- Industry associations
- Alumni networks

**Shared Context:**
- Similar career paths
- Common interests or hobbies
- Geographic connections
- Industry events attended

### 5. Recent News & Activity

**Personal News:**
- Job changes or promotions
- Awards or recognition
- Public statements or interviews
- Social media activity

**Company Context:**
- Recent company announcements
- Industry trends affecting their role
- Competitive pressures
- Growth or challenges

## Knowledge Capsule Format

Create a condensed, actionable profile:

```
## [Name] - [Title] at [Company]

### Quick Facts
- Location: [City, Time Zone]
- Tenure: [X years at company, Y months in role]
- Background: [1-2 sentence career summary]

### Role Focus
[2-3 sentences on what they're responsible for and measured on]

### Recent Activity
- [Relevant recent event or news item]
- [Another relevant item]

### Connection Points
- [Mutual connection or shared context]
- [Common interest or background]

### Conversation Starters
1. [Specific talking point based on their interests]
2. [Reference to recent news or activity]
3. [Question about their priorities]

### Potential Pain Points
Based on role and industry:
- [Likely challenge #1]
- [Likely challenge #2]
- [Likely challenge #3]
```

## Research Sources

### Primary Sources
- LinkedIn profile and activity
- Company website (about page, team page)
- Professional bio from conferences or publications
- Personal website or blog

### Secondary Sources
- News articles mentioning the prospect
- Company press releases
- Industry publications
- Podcast appearances or interviews

### Social Intelligence
- Twitter/X presence
- LinkedIn posts and comments
- Published articles or thought leadership
- Conference presentations (SlideShare, YouTube)

## Research Process

### Step 1: Basic Profile (5 minutes)
1. Find LinkedIn profile
2. Capture basic info (title, company, location)
3. Note tenure and career history
4. Identify reporting structure

### Step 2: Deep Dive (10 minutes)
1. Review LinkedIn activity (posts, comments, shares)
2. Search for news mentions
3. Find any published content
4. Check for mutual connections

### Step 3: Synthesis (5 minutes)
1. Identify 2-3 key connection points
2. Draft conversation starters
3. Hypothesize likely pain points
4. Create knowledge capsule

## Personalization Guidelines

### What Makes Research Actionable

**Specific over generic:**
- Not: "They're a VP of Sales"
- But: "They've grown the sales team from 5 to 25 in 18 months"

**Recent over historical:**
- Not: "They worked at Salesforce"
- But: "They just posted about hitting 150% of quota last quarter"

**Relevant over interesting:**
- Not: "They went to Stanford"
- But: "They mentioned struggling with rep onboarding in a recent post"

### Red Flags to Note

- Very limited online presence (harder to personalize)
- Recent job change (may not be decision-maker yet)
- Negative company news (tread carefully)
- Previous bad experience with similar vendors

## Output Format

When researching a prospect, produce:

1. **Knowledge Capsule**: Condensed profile in standard format
2. **Research Confidence**: How complete is the picture (High/Medium/Low)
3. **Best Approach**: Recommended outreach strategy based on research
4. **Conversation Hooks**: 3-5 specific talking points
5. **Questions to Answer**: What we still need to learn

## Available Tools

When enabled, these MCP tools enhance research capabilities:

| Tool | What It Does | How to Use |
|------|-------------|------------|
| **Exa** | Find profiles and content by person | "Search Exa for [name]'s LinkedIn profile and recent posts" |
| **Apify** | Scrape LinkedIn profiles | "Use Apify LinkedIn scraper for [profile URL]" |
| **Hunter.io** | Find and verify email addresses | "Find email for [name] at [company] using Hunter" |
| **Perplexity** | Research person's public presence | "Use Perplexity to find recent mentions of [name]" |

**Note:** Tools must be enabled in `.mcp.json` and API keys configured. See README for setup instructions.

### Tool Usage Examples

```
"Use Hunter to find the email for John Smith at Acme Corp"
"Search Exa for John Smith VP Sales Acme Corp LinkedIn"
"Use Perplexity to find recent interviews or podcasts featuring John Smith"
"Use Apify to scrape this LinkedIn profile: [URL]"
```

## Cross-References

- Feed research into `cold-call-scripts` for personalized openers
- Use insights in `follow-up-emails` for relevant references
- Inform `multithread-outreach` with stakeholder context
- Update based on `call-analysis` findings
