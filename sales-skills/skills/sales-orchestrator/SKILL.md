---
name: sales-orchestrator
description: Diagnoses sales needs and sequences appropriate skills for comprehensive deal execution. Use this skill when unsure which sales skill to use, planning multi-step deal strategies, coaching reps on process, or coordinating complex sales motions.
---

# Sales Orchestrator

This skill acts as a routing system for sales activities-diagnosing needs, recommending the right skills, and sequencing them for effective deal execution.

## Objective

Help users navigate the sales skills suite by identifying the right skill(s) for their situation and sequencing them effectively for multi-step sales motions.

## The 9 Sales Skills Available

### Foundation Layer
| Skill | Purpose | Use When |
|-------|---------|----------|
| `powerful-framework` | Qualify and assess deals | Evaluating opportunity health, identifying gaps, coaching on deal strategy |
| `prospect-research` | Build prospect profiles | Preparing for outreach, personalizing messages, understanding buyers |

### Strategy Layer
| Skill | Purpose | Use When |
|-------|---------|----------|
| `account-qualification` | Tier and prioritize accounts | Building target lists, prioritizing efforts, defining ICP |
| `company-intelligence` | Research companies deeply | Preparing for executive meetings, account planning, competitive research |

### Execution Layer
| Skill | Purpose | Use When |
|-------|---------|----------|
| `cold-call-scripts` | Create call frameworks | Prospecting prep, coaching on call structure, campaign templates |
| `call-analysis` | Extract insights from calls | Reviewing recordings, qualifying deals, capturing action items |
| `follow-up-emails` | Write post-call emails | After any sales conversation, confirming next steps, maintaining momentum |
| `multithread-outreach` | Engage multiple stakeholders | Account-based selling, executive outreach, deal acceleration |

## Diagnostic Questions

### 1. What's your primary goal right now?
- **Find new opportunities** → `account-qualification`, `prospect-research`
- **Prepare for outreach** → `prospect-research`, `cold-call-scripts`, `company-intelligence`
- **Qualify an opportunity** → `powerful-framework`, `call-analysis`
- **Advance an existing deal** → `follow-up-emails`, `multithread-outreach`
- **Coach a rep** → `call-analysis`, `powerful-framework`
- **Build account strategy** → `company-intelligence`, `account-qualification`

### 2. What stage is the opportunity?
- **Pre-outreach** → Start with `account-qualification` and `prospect-research`
- **Initial contact** → Use `cold-call-scripts` with `prospect-research`
- **Discovery/Qualification** → Apply `powerful-framework` via `call-analysis`
- **Evaluation/Demo** → Leverage `company-intelligence` and `multithread-outreach`
- **Negotiation/Close** → Focus on `powerful-framework` gaps and `multithread-outreach`

### 3. What do you have available?
- **Company name only** → Start with `company-intelligence`
- **Contact name only** → Start with `prospect-research`
- **Call transcript** → Start with `call-analysis`
- **Deal information** → Start with `powerful-framework`
- **Target account list** → Start with `account-qualification`

### 4. What's the primary challenge?
- **Don't know enough** → `company-intelligence`, `prospect-research`
- **Can't get meetings** → `cold-call-scripts`, `prospect-research`
- **Deals stalling** → `multithread-outreach`, `follow-up-emails`
- **Poor qualification** → `powerful-framework`, `call-analysis`
- **Wrong accounts** → `account-qualification`

## Skill Selection Matrix

Quick reference for common situations:

| Situation | Primary Skill | Supporting Skills |
|-----------|--------------|-------------------|
| "I need to find good prospects" | `account-qualification` | `company-intelligence` |
| "I have a call coming up" | `cold-call-scripts` | `prospect-research`, `company-intelligence` |
| "I just had a call, need to follow up" | `call-analysis` | `follow-up-emails` |
| "My deal is stuck" | `powerful-framework` | `multithread-outreach` |
| "I need to engage the executive" | `multithread-outreach` | `company-intelligence` |
| "I don't know enough about this company" | `company-intelligence` | `prospect-research` |
| "I need to send a follow-up email" | `follow-up-emails` | `call-analysis` |
| "Is this a good opportunity?" | `powerful-framework` | `account-qualification` |
| "I want to coach a rep on this call" | `call-analysis` | `powerful-framework` |
| "I don't know where to start" | This skill (`sales-orchestrator`) | Then `account-qualification` or `prospect-research` |

## Sequencing Playbooks

### Playbook 1: New Prospect Outreach
**Goal**: Make first contact with a new prospect
**Sequence**:
```
Step 1: account-qualification → Is this worth pursuing?
            ↓
Step 2: company-intelligence → Understand their business
            ↓
Step 3: prospect-research → Build knowledge capsule on contact
            ↓
Step 4: cold-call-scripts → Prepare personalized call script
            ↓
Step 5: follow-up-emails → Send follow-up if no answer/voicemail
```

### Playbook 2: Post-Call Processing
**Goal**: Capture insights and maintain momentum after a call
**Sequence**:
```
Step 1: call-analysis → Extract POWERFUL insights and next steps
            ↓
Step 2: powerful-framework → Score opportunity and identify gaps
            ↓
Step 3: follow-up-emails → Send summary to main contact
            ↓
Step 4: multithread-outreach → Engage other stakeholders mentioned
```

### Playbook 3: Deal Acceleration
**Goal**: Unstick a stalled deal
**Sequence**:
```
Step 1: powerful-framework → Diagnose where the deal is weak
            ↓
Step 2: company-intelligence → Find new angles or triggers
            ↓
Step 3: multithread-outreach → Engage additional stakeholders
            ↓
Step 4: follow-up-emails → Re-engage existing contacts with new value
```

### Playbook 4: Account Planning
**Goal**: Develop strategic approach to a key account
**Sequence**:
```
Step 1: company-intelligence → Deep research on the account
            ↓
Step 2: account-qualification → Score and tier the opportunity
            ↓
Step 3: prospect-research → Profile key stakeholders
            ↓
Step 4: multithread-outreach → Plan multi-stakeholder engagement
```

### Playbook 5: Call Preparation
**Goal**: Be fully prepared for an important call
**Sequence**:
```
Step 1: prospect-research → Update knowledge capsule
            ↓
Step 2: company-intelligence → Check for recent news/changes
            ↓
Step 3: powerful-framework → Review what we know/don't know
            ↓
Step 4: cold-call-scripts → Prepare questions and talking points
```

### Playbook 6: Rep Coaching
**Goal**: Coach a rep on deal strategy or call technique
**Sequence**:
```
Step 1: call-analysis → Review call transcript objectively
            ↓
Step 2: powerful-framework → Assess deal qualification
            ↓
Step 3: Identify specific coaching points based on analysis
            ↓
Step 4: Practice with cold-call-scripts for next call
```

## Handoff Guidance

When moving between skills, pass this context:

### From → To Context Transfer

**account-qualification → company-intelligence**
- Account tier and reasoning
- Key signals identified
- Priority stakeholders to research

**company-intelligence → prospect-research**
- Company strategic priorities
- Relevant news or triggers
- Organizational structure insights

**prospect-research → cold-call-scripts**
- Knowledge capsule highlights
- Best conversation hooks
- Likely pain points

**call-analysis → powerful-framework**
- Extracted POWERFUL data
- Gap assessment
- Recommended focus areas

**call-analysis → follow-up-emails**
- Key discussion points
- Agreed next steps
- Stakeholder mentions

**powerful-framework → multithread-outreach**
- Stakeholder map
- Individual priorities
- Deal risks to address

## Single-Skill Quick Start

If you know you need just one skill:

| "I want to..." | Go directly to |
|----------------|----------------|
| "...qualify and tier accounts" | `account-qualification` |
| "...research a company" | `company-intelligence` |
| "...research a specific person" | `prospect-research` |
| "...prepare for a cold call" | `cold-call-scripts` |
| "...analyze a call transcript" | `call-analysis` |
| "...assess deal health" | `powerful-framework` |
| "...write a follow-up email" | `follow-up-emails` |
| "...engage multiple stakeholders" | `multithread-outreach` |

## Output Format

When diagnosing needs, provide:

1. **Situation Assessment**: Summary of where the user is and what they're trying to do
2. **Recommended Skill(s)**: Primary and supporting skills
3. **Sequencing Plan**: Order of operations if multiple skills needed
4. **Quick Start**: First action to take

## How to Use This Skill

This skill (`sales-orchestrator`) is the starting point when:
- You're unsure which skill to use
- You have a complex, multi-step sales motion
- You want to build a comprehensive deal strategy
- You're planning account-based engagement
- You're coaching and need a diagnostic framework

After diagnosis, invoke the recommended skill(s) directly for detailed execution.
