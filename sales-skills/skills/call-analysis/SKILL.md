---
name: call-analysis
description: Analyzes sales call transcripts using the POWERFUL framework to extract insights and action items. Use this skill when reviewing call recordings, coaching reps, qualifying opportunities, or extracting deal intelligence from conversations.
---

# Call Analysis

This skill analyzes sales call transcripts to extract strategic insights, capture action items, and assess opportunity health using the POWERFUL deal qualification framework.

## Objective

Transform raw call transcripts into structured, actionable summaries that capture key discussion points, identify next steps, and provide objective opportunity assessments.

## Analysis Structure

### 1. Next Steps
Clear action items extracted from the conversation.

**Format:**
- **Action**: What needs to happen
- **Owner**: Who is responsible (us or them)
- **Timeline**: When it needs to happen
- **Priority**: High/Medium/Low

**Example:**
```
1. [Us] Send proposal with pricing options - by Friday - High
2. [Them] Get budget approval from finance - by next week - High
3. [Us] Schedule demo with technical team - within 2 weeks - Medium
```

### 2. POWERFUL Framework Analysis

Extract insights for each dimension:

#### Pain
- What challenges or frustrations did they mention?
- Include direct quotes when available
- Note the severity and impact

#### Opportunity Cost
- What happens if they don't solve this?
- Any timelines or deadlines mentioned?
- Financial or business impact of inaction?

#### Wants, Needs, Desires
- What outcomes are they looking for?
- What does success look like to them?
- Any specific requirements or criteria?

#### Executive Level Influence
- Who else is involved in the decision?
- What's the approval process?
- Any stakeholder dynamics revealed?

#### Resources/Budget
- Was budget discussed?
- What's their expected investment range?
- Any competing priorities for funds?

#### Fear of Failure
- What concerns or objections came up?
- Past negative experiences mentioned?
- Risk factors they're worried about?

#### Unequivocal Trust
- How did they hear about us?
- Were they transparent and open?
- Any trust-building moments?

#### Little Things
- Communication preferences mentioned?
- Scheduling constraints?
- Personal details or rapport builders?

### 3. Key Discussion Points
Important topics that don't fit neatly into the framework:
- Technical requirements discussed
- Competitive mentions
- Timeline drivers
- Internal politics
- Integration needs

### 4. Opportunity Rating
Objective assessment of deal health.

**Rating Scale:**
- **0-40%**: Early stage, significant unknowns
- **40-60%**: Developing, some validation
- **60-80%**: Promising, strong signals
- **80-100%**: High confidence, clear path

**Qualitative Assessment:**
One paragraph explaining the rating with evidence from the call.

### 5. Potential Concerns
Red flags or issues that might hinder the deal:
- Unresolved objections
- Missing stakeholders
- Competitive threats
- Timeline misalignment
- Budget constraints
- Technical gaps

### 6. Strategic Suggestions
3-5 actionable recommendations based on the analysis:
- What to do next
- What to clarify
- Who else to engage
- How to address concerns
- Ways to accelerate the deal

## Transcript Quality Requirements

### Minimum Standards
- At least 5 minutes of substantive conversation
- Identifiable speakers (not just one-sided notes)
- Readable/parseable format
- Contains actual sales dialogue (not just administrative chat)

### Information to Flag
- When something is unclear or ambiguous
- When important context seems missing
- When speakers are hard to distinguish
- When audio quality affected transcription

## Analysis Guidelines

### Be Objective
- Report what was actually said, not what you wish was said
- Include both positive and negative signals
- Don't over-interpret vague statements
- Flag uncertainty when present

### Be Specific
- Use direct quotes when possible
- Include specific numbers, dates, names
- Reference specific moments in the conversation
- Avoid generic summaries

### Be Actionable
- Every insight should connect to a potential action
- Prioritize what matters for deal advancement
- Focus on what can be verified or addressed
- Highlight time-sensitive items

### Be Honest About Gaps
- Note what wasn't discussed that should have been
- Identify questions that weren't asked
- Flag POWERFUL dimensions with no information
- Suggest what to cover in the next conversation

## Output Format

When analyzing a call, produce:

### Call Summary Header
```
Call: [Prospect Name] - [Company]
Date: [Date of call]
Duration: [Approximate length]
Participants: [List of participants]
Stage: [Pipeline stage]
```

### Structured Analysis
1. **Next Steps**: Action items with owners and timelines
2. **POWERFUL Analysis**: Findings for each dimension
3. **Other Key Notes**: Important points outside framework
4. **Opportunity Rating**: Percentage and qualitative assessment
5. **Potential Concerns**: Red flags and risks
6. **Strategic Suggestions**: 3-5 actionable recommendations

### Information Gaps
- POWERFUL dimensions with insufficient information
- Questions that should be asked next
- Stakeholders not yet engaged

## Cross-References

- Feed extracted POWERFUL data into `powerful-framework` scorecard
- Use insights to inform `follow-up-emails` content
- Guide `multithread-outreach` based on stakeholder mentions
- Update `prospect-research` profiles with new information
- Inform `account-qualification` tier adjustments
