# Tokenomics — Positioning Document

---

## ONE-SENTENCE POSITIONING STATEMENT

Tokenomics is the usage intelligence layer for developers who run multiple AI coding tools and need to know — at a glance — whether they have headroom to start the next task.

---

## PRIMARY VALUE PROP

**One icon shows you all five AI tools and whether you're pacing toward a limit — before the API stops you.**

### Three Proof Points

1. **The pace dot:** A small dot on each ring shows where your fill would sit if usage were evenly distributed across the window. Ahead of the dot means burning fast. Behind means you have room. This converts a raw utilization number into a behavioral signal — something you can act on, not just read.

2. **Five providers, zero-friction:** Claude Code, GitHub Copilot, Cursor, Codex CLI, and Gemini CLI — all auto-detected, no token pasting. Credentials are read from where each tool already stores them. The self-healing OAuth retry means Claude Code's token rotations are invisible.

3. **Production-grade distribution:** Developer ID signed, notarized, auto-updating via Sparkle, on Homebrew. Not a weekend hack you'll forget to re-download. Install once, stay current.

---

## WHO THIS IS FOR (ICP)

### Primary: The Multi-Tool Power User

Runs Claude Code on Max plan plus at least one of: GitHub Copilot, Cursor, Codex. Has experienced the exact moment of being mid-task when an API returns a rate limit error. Has tried checking a provider dashboard and found the friction too high to do consistently. Installs menu bar utilities (iStat Menus, Bartender, or similar) — already trusts the category. On macOS. Probably a Mac developer, but increasingly a designer, PM, or anyone who codes with AI at the center of their workflow.

**Specific archetype:** The Cursor+Claude Code power user on a Max plan who starts agentic runs and wants to know before they start whether they have the quota to finish.

### Secondary: The Single-Provider Heavy User Who's Outgrown It

Uses Claude Code daily, has hit rate limits before, wants something better than claudeusagebar.com without switching to a paid tool. The "five providers" headline is future-proofing for them — they'll install for Claude, discover the pace dot, and stay.

### Tertiary: The Creative AI User (near-term)

Uses ElevenLabs, Runway, or Stability AI alongside coding tools. Once creative provider support ships, this is a meaningful market expansion. The "coming soon" on the landing page plants the flag.

---

## WHO THIS IS NOT FOR

- Windows or Linux users (macOS only, for now)
- Users who only care about one provider and prefer a free, MIT-licensed, no-frills tool — claudeusagebar.com serves them correctly
- Enterprise teams looking for shared dashboards, org-level spend aggregation, or SSO — Tokenomics is a personal utility
- Users who want a web app or mobile dashboard (not the category)

---

## DIFFERENTIATION MATRIX

| Feature / Quality | Tokenomics | claudeusagebar.com | TokenBar | Raw provider dashboard | Nothing |
|---|---|---|---|---|---|
| Providers supported | 5 (coding) + creative coming | 1 (Claude only) | 20+ (API key required) | 1 per tab | — |
| Auth friction | Zero — reads existing credentials | Manual cookie extraction | API key entry per provider | Log in per provider | — |
| Pace signal (are you burning fast?) | Yes — the pace dot | No | Yes (described, details unclear) | No | No |
| Menu bar rings (visual, not text) | Yes — concentric rings | Yes — percentage text + bar | Text/number display | No | No |
| Desktop widgets | Yes — small/medium/large | No | No | No | No |
| Distribution quality | Signed, notarized, Sparkle, Homebrew | GitHub DMG, unsigned or minimal signing | Website download | N/A | N/A |
| Price | Free | Free | $5–$10 one-time | Free | Free |
| Open source | Source-available (not MIT) | Yes (MIT) | No | N/A | N/A |
| macOS version requirement | 14 Sonoma+ | 13 Ventura+ | Not specified | Any browser | — |
| Self-healing OAuth (Claude Code token rotation) | Yes | No — shows error | Unknown | Shows error | — |
| Activity-aware polling (battery) | Yes — sleeps after 9 min idle | Unknown | Unknown | No | — |
| Exponential backoff on 429 | Yes — 5m→1h | Unknown | Unknown | No | — |

**Where claudeusagebar.com wins honestly:**
- macOS version support (13 vs 14)
- MIT license vs source-available
- "Pure" open source community signal
- Already has PH #1 badge (2024) — though that's stale

**Where TokenBar wins honestly:**
- Provider count (20+ vs 5)
- If a user already manages API keys for all their tools, TokenBar's model works
- Potentially more providers by the time users are reading this

**Our honest gap to acknowledge:** TokenBar's "20 providers" will look bigger than our "5" to a skimmer. Our answer: depth over breadth. TokenBar requires manual API key entry for every provider. Tokenomics reads your existing credentials. And "20 providers" includes services most developers don't use weekly. The five we ship are the five that matter.

---

## TOP 3 OBJECTIONS + RESPONSES

### Objection 1: "Why not use claudeusagebar.com? It's free and open source."

**Response:**
It is free and open source. If you only use Claude Code and you don't mind manually extracting a cookie to authenticate, it works. Two differences worth knowing about: Tokenomics supports five providers (so if you use Copilot or Cursor too, you're covered in one place), and the auth is automatic — no cookie hunting. There's also the pace dot, which shows whether your current usage is pacing toward a limit, not just how much you've used. If you want the simpler thing, use the simpler thing. Tokenomics is for people who've grown past it.

### Objection 2: "TokenBar does 20+ providers. Why only 5?"

**Response:**
TokenBar requires you to paste API keys for every provider. Tokenomics reads credentials from where your tools already store them. For the five coding tools that most developers actually use daily, that's a meaningfully better experience. We're not trying to integrate against every AI service that has an API endpoint — we're building depth on the ones developers run all day. Creative AI providers (ElevenLabs, Runway, Stability AI) are next in the pipeline, using the same zero-friction model where possible.

### Objection 3: "I can just check the dashboard."

**Response:**
You can. The problem is you don't know you need to check until you're mid-task. The pace dot is specifically designed for the decision you make *before* starting a long agentic run: do I have headroom to finish this, or should I wait for the window to reset? A dashboard answers "how much have I used?" — Tokenomics answers "am I about to run out?" Those are different questions, and the second one is the one that matters.

---

## POSITIONING NOTES

**The category risk:** This space is getting crowded fast. claudeusagebar.com, TokenBar, ClaudeBar, ClaudeMeter, Usage4Claude — there are at least five similar products. The window for "first mover" is closed. The positioning pivot is: we're not the first, we're the finished version. Signed, notarized, auto-updating, five providers, pace dot. Everything else is a prototype.

**The pace dot as the moat:** It's hard to copy well. It requires understanding both the time elapsed in the window and the current utilization, then rendering that relationship visually at a size where it's readable. Most competitors will add a percentage and call it done. The pace dot is a design decision, not a feature. That's defensible for longer.

**The "control plane" framing (from roadmap):** Phase 2 is agent approval notifications — the ability to approve a running agent from your watch or phone without returning to the desk. When that ships, Tokenomics stops being a usage monitor and becomes something more significant. The landing page copy should not promise this yet, but the hero copy ("your AI tools don't warn you") is compatible with this evolution. Don't paint yourself into a corner.
