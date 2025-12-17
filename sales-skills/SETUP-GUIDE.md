# Tool Setup Guide for Sales Professionals

This guide walks you through setting up the optional research tools step-by-step. **No coding experience required.**

## Table of Contents

- [Do I Need These Tools?](#do-i-need-these-tools)
- [Quick Start](#quick-start-the-easiest-option)
- [Getting Your API Keys](#getting-your-api-keys)
  - [Perplexity](#perplexity-recommended-first)
  - [Exa](#exa)
  - [Hunter.io](#hunterio)
  - [Apify](#apify)
- [Setting Up Your API Keys](#setting-up-your-api-keys)
  - [Mac Users](#for-mac-users)
  - [Windows Users](#for-windows-users)
- [Enabling the Tools](#enabling-the-tools)
- [Testing Your Setup](#testing-your-setup)
- [Troubleshooting](#troubleshooting)
- [Which Tools Should I Get?](#which-tools-should-i-get)
- [Claude Desktop Setup](#claude-desktop-setup) ← If you use Claude Desktop instead of Claude Code
- [Quick Reference Card](#quick-reference-card)

---

## Do I Need These Tools?

**No, they're optional.** The sales skills work without them—Claude will use its built-in knowledge and any information you provide.

**With tools enabled**, Claude can:
- Search the web in real-time for company news
- Find and verify email addresses
- Look up LinkedIn profiles
- Get current information instead of relying on training data

**Start without tools**, then add them later if you want enhanced research capabilities.

---

## Quick Start: The Easiest Option

If you just want one tool to start, **get Perplexity**. It's the most versatile:
- Real-time web search
- Works for company research, prospect research, and signal verification
- Simple API with clear pricing

---

## Getting Your API Keys

### Perplexity (Recommended First)

Perplexity is an AI-powered search engine. Their API lets Claude search the web for you.

**Cost:** ~$5 for 1,000 searches (pay as you go)

**Step 1:** Go to [perplexity.ai](https://www.perplexity.ai)

**Step 2:** Create an account (or sign in with Google)

**Step 3:** Click your profile icon → **Settings**

**Step 4:** Click **API** in the left sidebar

**Step 5:** Click **Generate API Key**

**Step 6:** Copy the key (starts with `pplx-`)

**Step 7:** Add a payment method (they charge per use, not monthly)

> 💡 **Tip:** Your key looks like: `pplx-a1b2c3d4e5f6...`

---

### Exa

Exa is a search engine built for AI. Great for finding companies, people, and specific content.

**Cost:** Free tier available (1,000 searches/month)

**Step 1:** Go to [exa.ai](https://exa.ai)

**Step 2:** Click **Get Started** or **Sign Up**

**Step 3:** Create an account

**Step 4:** Go to your Dashboard

**Step 5:** Find **API Keys** section

**Step 6:** Click **Create API Key**

**Step 7:** Copy the key

> 💡 **Tip:** The free tier is enough for most individual salespeople.

---

### Hunter.io

Hunter finds and verifies professional email addresses. Essential for prospecting.

**Cost:** Free tier (25 searches/month), paid plans from $49/month

**Step 1:** Go to [hunter.io](https://hunter.io)

**Step 2:** Click **Sign up free**

**Step 3:** Create an account (or sign in with Google)

**Step 4:** Click your profile icon → **API**

**Step 5:** Your API key is displayed on this page

**Step 6:** Copy the key

> 💡 **Tip:** 25 free searches/month is enough to test. Upgrade if you use it heavily.

---

### Apify

Apify runs web scrapers. Useful for extracting LinkedIn data and job postings.

**Cost:** Free tier ($5/month credit), paid plans from $49/month

**Step 1:** Go to [apify.com](https://apify.com)

**Step 2:** Click **Start free**

**Step 3:** Create an account

**Step 4:** Once logged in, click **Settings** (gear icon)

**Step 5:** Click **Integrations** in the left sidebar

**Step 6:** Find your **Personal API Token**

**Step 7:** Copy the token

> 💡 **Tip:** Apify is more technical. Start with the other tools first.

---

## Setting Up Your API Keys

### For Mac Users

**Step 1:** Open **Terminal** (press `Cmd + Space`, type "Terminal", press Enter)

**Step 2:** Type this command and press Enter:
```bash
open -e ~/.zshrc
```

If you see an error, try:
```bash
touch ~/.zshrc && open -e ~/.zshrc
```

**Step 3:** A text file will open. Add these lines at the bottom (only for keys you have):

```bash
# Salesably Sales Skills API Keys
export PERPLEXITY_API_KEY="pplx-your-key-here"
export EXA_API_KEY="your-exa-key-here"
export HUNTER_API_KEY="your-hunter-key-here"
export APIFY_API_TOKEN="your-apify-token-here"
```

**Step 4:** Replace `your-key-here` with your actual keys

**Step 5:** Save the file (`Cmd + S`) and close it

**Step 6:** Back in Terminal, type and press Enter:
```bash
source ~/.zshrc
```

**Step 7:** Restart Claude Code

---

### For Windows Users

#### Option A: Using System Environment Variables (Recommended)

**Step 1:** Press `Windows key + R` to open Run

**Step 2:** Type `sysdm.cpl` and press Enter

**Step 3:** Click the **Advanced** tab

**Step 4:** Click **Environment Variables** button at the bottom

**Step 5:** Under "User variables", click **New**

**Step 6:** Add each key:
- Variable name: `PERPLEXITY_API_KEY`
- Variable value: `pplx-your-key-here`

**Step 7:** Click OK, then repeat for each key you have:
- `EXA_API_KEY`
- `HUNTER_API_KEY`
- `APIFY_API_TOKEN`

**Step 8:** Click OK to close all windows

**Step 9:** **Restart your computer** (required for changes to take effect)

**Step 10:** Restart Claude Code

#### Option B: Using PowerShell Profile

**Step 1:** Open **PowerShell** (press `Windows key`, type "PowerShell", press Enter)

**Step 2:** Type this command and press Enter:
```powershell
notepad $PROFILE
```

**Step 3:** If asked to create a new file, click **Yes**

**Step 4:** Add these lines:
```powershell
# Salesably Sales Skills API Keys
$env:PERPLEXITY_API_KEY = "pplx-your-key-here"
$env:EXA_API_KEY = "your-exa-key-here"
$env:HUNTER_API_KEY = "your-hunter-key-here"
$env:APIFY_API_TOKEN = "your-apify-token-here"
```

**Step 5:** Save and close Notepad

**Step 6:** Restart PowerShell and Claude Code

---

## Enabling the Tools

After setting up your API keys, you need to enable the tools in the plugin.

**Step 1:** Find the file `sales-skills/.mcp.json`

**Step 2:** Open it in any text editor (Notepad, TextEdit, VS Code, etc.)

**Step 3:** Find the tool you want to enable. It looks like this:
```json
"perplexity": {
  "command": "npx",
  "args": ["-y", "@anthropic/mcp-server-perplexity"],
  "env": {
    "PERPLEXITY_API_KEY": "${PERPLEXITY_API_KEY}"
  },
  "disabled": true    ← Change this line
}
```

**Step 4:** Change `"disabled": true` to `"disabled": false`

**Step 5:** Save the file

**Step 6:** Restart Claude Code

---

## Testing Your Setup

After setup, test each tool in Claude Code:

**Test Perplexity:**
> "Use Perplexity to search for recent news about Salesforce"

**Test Exa:**
> "Use Exa to find the LinkedIn profile for Marc Benioff"

**Test Hunter:**
> "Use Hunter to find email addresses at Salesforce.com"

**Test Apify:**
> "Use Apify to find open sales jobs at Salesforce"

If it works, you'll see results. If not, check the troubleshooting section below.

---

## Troubleshooting

### "Tool not found" or "MCP server error"

1. Make sure you set the environment variable correctly
2. Make sure you changed `"disabled": true` to `"disabled": false`
3. Restart Claude Code completely (quit and reopen)

### "Invalid API key" or "Authentication failed"

1. Double-check you copied the full API key
2. Make sure there are no extra spaces before or after the key
3. Verify the key works by logging into the service's website

### "Rate limit exceeded"

You've used up your free tier or hit a usage limit. Either:
- Wait until your limit resets (usually monthly)
- Upgrade to a paid plan
- Use a different tool for now

### Windows: Environment variable not working

1. Make sure you restarted your computer after adding the variable
2. Open a new Command Prompt and type: `echo %PERPLEXITY_API_KEY%`
3. If it shows your key, it's working. Restart Claude Code.
4. If it's blank, redo the environment variable steps.

### Mac: Environment variable not working

1. Open Terminal and type: `echo $PERPLEXITY_API_KEY`
2. If it shows your key, it's working. Restart Claude Code.
3. If it's blank, make sure you ran `source ~/.zshrc`
4. If still blank, check you saved the file correctly

---

## Which Tools Should I Get?

| Your Main Need | Get This Tool |
|----------------|---------------|
| Company research before calls | Perplexity |
| Finding prospect email addresses | Hunter.io |
| Finding people on LinkedIn | Exa |
| Deep company research | Perplexity + Exa |
| Full prospecting workflow | All four |

### My Recommendation

1. **Start with Perplexity** - Most versatile, good free trial
2. **Add Hunter.io** - If you need email addresses
3. **Add Exa** - If you do a lot of LinkedIn research
4. **Add Apify** - Only if you need heavy data extraction

---

## Cost Summary

| Tool | Free Tier | Paid |
|------|-----------|------|
| Perplexity | Limited trial | ~$0.005/search |
| Exa | 1,000 searches/month | $99/month |
| Hunter.io | 25 searches/month | $49/month |
| Apify | $5/month credit | $49/month |

**Typical monthly cost for active salesperson:** $0-50 depending on usage

---

## Getting Help

If you're stuck:
- Check the troubleshooting section above
- Contact us at [https://www.salesably.ai/contact](https://www.salesably.ai/contact)
- Ask in your company's IT/support channel

---

## Claude Desktop Setup

**Using Claude Desktop instead of Claude Code?** The MCP research tools work there too! Here's how to set them up.

### Do Skills Work in Claude Desktop?

| Feature | Claude Code | Claude Desktop |
|---------|-------------|----------------|
| Skills auto-load | Yes | No |
| MCP Tools | Yes | Yes |

**Skills** (like the POWERFUL framework) won't automatically load in Claude Desktop, but you can:
- Add SKILL.md files to a **Project** as knowledge files
- Copy/paste skill content into your conversation
- Reference the frameworks manually

**MCP Tools** (Perplexity, Exa, Hunter, Apify) work in both, but need different configuration.

### Setting Up MCP Tools in Claude Desktop

#### Step 1: Set Your API Keys

Follow the same instructions above for [Mac](#for-mac-users) or [Windows](#for-windows-users) to set your environment variables. This step is the same.

#### Step 2: Find Your Claude Desktop Config File

**Mac:**
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

To open it:
1. Open **Finder**
2. Press `Cmd + Shift + G`
3. Paste: `~/Library/Application Support/Claude/`
4. Open `claude_desktop_config.json` in a text editor

**Windows:**
```
%APPDATA%\Claude\claude_desktop_config.json
```

To open it:
1. Press `Windows + R`
2. Type: `%APPDATA%\Claude`
3. Press Enter
4. Open `claude_desktop_config.json` in Notepad

#### Step 3: Add MCP Server Configuration

If the file is empty or doesn't exist, create it with this content. If it exists, add the `mcpServers` section.

**Add only the tools you have API keys for:**

```json
{
  "mcpServers": {
    "perplexity": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-perplexity"],
      "env": {
        "PERPLEXITY_API_KEY": "pplx-your-key-here"
      }
    },
    "exa": {
      "command": "npx",
      "args": ["-y", "exa-mcp-server"],
      "env": {
        "EXA_API_KEY": "your-exa-key-here"
      }
    },
    "hunter": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-fetch"],
      "env": {
        "HUNTER_API_KEY": "your-hunter-key-here"
      }
    },
    "apify": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-apify"],
      "env": {
        "APIFY_API_TOKEN": "your-apify-token-here"
      }
    }
  }
}
```

> **Important:** Replace `your-key-here` with your actual API keys, OR use environment variable references like `${PERPLEXITY_API_KEY}` if you set them in Step 1.

#### Step 4: Restart Claude Desktop

Completely quit Claude Desktop and reopen it. The tools should now be available.

#### Step 5: Test It

In a new Claude Desktop conversation, try:
> "Use Perplexity to search for recent news about Salesforce"

If it works, you'll see search results. If not, check troubleshooting below.

### Claude Desktop Troubleshooting

**"Tool not found" error:**
- Make sure `claude_desktop_config.json` is valid JSON (no trailing commas, proper quotes)
- Restart Claude Desktop completely (quit, not just close window)
- Check that Node.js is installed: open Terminal/Command Prompt and type `node --version`

**"Invalid API key" error:**
- Double-check your API key is correct in the config file
- Make sure there are no extra spaces or quotes

**Config file doesn't exist:**
- Create it yourself at the path shown above
- Make sure it's named exactly `claude_desktop_config.json`

**Node.js not installed:**
Claude Desktop MCP tools require Node.js. Install it from [nodejs.org](https://nodejs.org) (choose the LTS version).

### Using Skills in Claude Desktop Projects

While skills don't auto-load, you can add them to Projects:

1. Open Claude Desktop
2. Click **Projects** in the sidebar
3. Create a new project (e.g., "Sales Tools")
4. Click **Add Content** → **Add Files**
5. Navigate to the `sales-skills/skills/` folder
6. Add the SKILL.md files you want (e.g., `powerful-framework/SKILL.md`)
7. Start a conversation in that project—Claude will reference the skills

**Recommended skills to add:**
- `powerful-framework/SKILL.md` - Deal qualification
- `prospect-research/SKILL.md` - Research framework
- `company-intelligence/SKILL.md` - Company research
- `cold-call-scripts/SKILL.md` - Call preparation

---

## Quick Reference Card

**Your API Keys (fill in when you get them):**

```
PERPLEXITY_API_KEY: ____________________
EXA_API_KEY: ____________________
HUNTER_API_KEY: ____________________
APIFY_API_TOKEN: ____________________
```

**Checklist:**
- [ ] Got at least one API key
- [ ] Added key to environment variables
- [ ] Restarted computer (Windows) or ran `source ~/.zshrc` (Mac)
- [ ] Changed `"disabled": true` to `"disabled": false` in `.mcp.json`
- [ ] Restarted Claude Code
- [ ] Tested the tool with a sample query
