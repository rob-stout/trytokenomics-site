# Marketer Notes — Round 1 Review

For Rob's eyes before Round 2.

---

## Top 3 Strategic Choices

### 1. The pace dot is the product's identity, not a feature

Every competitor either shows a percentage (claudeusagebar.com, ClaudeMeter) or a raw number (TokenBar). The pace dot is the only thing in this category that turns usage data into a behavioral answer: "should I start this next task, or wait?"

I led with it in every channel — the hero section, the first PH comment, the HN body, and post 2 of the Twitter thread. The instinct might be to lead with "five providers" because that's more immediately scannable. I didn't, because five providers is a comparative advantage (vs. single-provider tools) but the pace dot is an absolute advantage (vs. nothing). Nobody else has it. It's also the harder thing to copy, because it's a design decision that requires understanding the problem well.

The risk: "pace dot" is not self-explanatory. The landing page needs a diagram — not a screenshot — that shows the ring, the arc, and the dot with three labeled callouts. If that visual doesn't land, the pace dot section will get scrolled past. This is on the designer, but it's worth flagging explicitly.

### 2. Don't name claudeusagebar.com on the page

The instinct in a competitive launch is to run a comparison table and name the competitor. I chose not to, for two reasons.

First, naming them directs traffic to them. PH and HN audiences are curious — "let me check this other thing" is a real behavior, especially from people who are already using it.

Second, the comparison is implicit in the copy. The "Zero-Friction Auth" section describes no cookie extraction, self-healing OAuth, and automatic credential detection — anyone who has used a competitor that requires manual cookie paste will recognize the contrast without being told. Specificity does the work without the optics of punching at a smaller target.

The naming happens in conversation (PH comments, HN thread replies) where it's appropriate to be direct. That's where Rob has canned responses ready. On the page, the product speaks for itself.

### 3. TokenBar is the real threat, not claudeusagebar.com

By the time of a 2026 launch, the meaningful competitive question isn't "vs. a free single-provider tool" — it's "vs. TokenBar, which launched in March 2026 with 20+ providers and a $5 price point."

TokenBar's weakness is the same as all API-key-based aggregators: you have to do setup work for every provider, and if the user hasn't configured a provider, they get nothing. Tokenomics' zero-friction auth is a direct counter to this. The positioning matrix makes this explicit for Rob internally, so he can talk about it clearly in conversations without having to think it through on the fly.

The "depth over breadth" frame — 5 providers you actually run daily, all automatic, vs. 20 providers you have to configure — is the message.

---

## Hardest Call

**Whether to mention "source-available, not MIT" proactively.**

The FAQ includes this honest answer: "Source is available on GitHub under a source-available license — not MIT. The license reserves commercial rights." This is accurate and transparent.

The risk is that proactively surfacing this comparison to MIT triggers a "why should I trust a non-MIT tool?" response from a developer who might never have asked. Most users don't read licenses. Raising it in the FAQ surfaces a question that wouldn't otherwise come up.

The reason I kept it: the HN and PH developer audiences will find it anyway (the GitHub repo is linked, the LICENSE file is visible). Being proactively honest in the FAQ is better than appearing to hide it and having someone call it out in the comments. "Why didn't you mention the license?" is a worse thread to be in than "here's why the license is what it is."

The answer in the FAQ is also specific about the reason (Phase 2 monetization optionality) which turns a potential negative ("this is closed-source-ish") into a signal of honest business thinking. Developers generally respect founders who explain their reasoning over ones who bury the lede.

If Rob wants to test whether this objection actually surfaces, he could remove the license FAQ item and see what happens in the PH comments. My bet: it comes up within the first 10 comments on HN regardless. Better to be ready.
