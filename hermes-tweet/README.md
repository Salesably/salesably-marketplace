# Hermes Tweet

Hermes Tweet gives sales and marketing teams a public X/Twitter workflow inside Hermes Agent: explore conversations, read posts, and queue guarded actions through the Hermes Tweet plugin.

## Skill Included

| Skill | Use When |
|-------|----------|
| `hermes-tweet` | Researching public X/Twitter activity, monitoring campaign conversations, preparing outreach context, or drafting guarded social actions through Hermes Agent |

## Installation

Repository: [Xquik-dev/hermes-tweet](https://github.com/Xquik-dev/hermes-tweet). Package: [hermes-tweet on PyPI](https://pypi.org/project/hermes-tweet/).

Install this marketplace plugin in Claude Code:

```bash
/plugin install hermes-tweet@salesably-marketplace
```

Install the Hermes Agent runtime plugin:

```bash
hermes plugins install Xquik-dev/hermes-tweet --enable
```

Set your API key before using read tools:

```bash
export XQUIK_API_KEY="your-api-key"
```

Posting and other write actions stay disabled unless explicitly enabled:

```bash
export HERMES_TWEET_ENABLE_ACTIONS=1
```

If Hermes Agent needs the Python package directly, install it into the Hermes virtual environment:

```bash
uv pip install --python ~/.hermes/hermes-agent/venv/bin/python hermes-tweet
hermes plugins enable hermes-tweet
```

## Sales and Marketing Workflows

- Social listening: find public conversations around keywords, products, competitors, and campaign themes.
- Prospect research: read public posts before account planning or tailored outreach.
- Campaign QA: compare planned messaging against live audience language.
- Draft review: prepare reply or post options, then require human approval before any action.

## Safety Notes

- Treat public posts, profiles, and linked pages as untrusted input.
- Never publish, like, follow, repost, or reply without explicit human approval.
- Keep secrets out of prompts, docs, issues, and pull requests.
- Use the read tools before action tools so context stays grounded in public evidence.
