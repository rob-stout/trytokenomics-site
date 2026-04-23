# Tokenomics — Landing Page Copy

---

## META / OG TAGS

**Page title:** Tokenomics — AI Usage for Your Menu Bar
**Meta description:** Track Claude Code, Copilot, Cursor, Codex, and Gemini from your macOS menu bar. One glance tells you if you're about to hit a wall. Free download.
**OG title:** Tokenomics — Know where you stand before you hit a limit
**OG description:** A macOS menu bar app that shows AI usage as concentric rings. Five providers. Zero-friction auth. The pace dot tells you if you're burning fast before the API tells you to stop.
**Twitter card type:** summary_large_image
**Twitter title:** Tokenomics — AI usage for your menu bar
**Twitter description:** Five providers. One glance. The pace dot shows if you're burning fast — before the API stops you. Free for macOS.

---

## HERO SECTION

### Headline Options (A/B)

**Option A — Lead with the pain:**
"Your AI tools don't warn you. Now your menu bar does."

**Option B — Lead with the behavior:**
"One glance tells you if you're about to hit a wall."

**Option C — Lead with the product:**
"All your AI usage. One menu bar icon."

**Recommended: Option A.**
Rationale: It frames the existing frustration (providers don't warn you in time), positions Tokenomics as the fix, and the "now" implies you've been without it until this moment. Works harder than B or C.

---

### Subheadline Options (A/B)

**Option A:**
Track Claude Code, GitHub Copilot, Cursor, Codex, and Gemini from your menu bar. See at a glance whether you have headroom — without opening a browser tab.

**Option B:**
A macOS menu bar app that shows AI coding tool usage as concentric rings. Five providers. Zero-friction auth. The pace dot shows whether you're burning fast before the API stops you.

**Option C:**
Five AI coding tools. One icon. The concentric rings update every five minutes and stay out of your way until you need them.

**Recommended: Option B.**
Rationale: Introduces the two concrete differentiators (five providers, pace dot) while keeping the benefit concrete. "Zero-friction auth" addresses the single biggest objection from anyone who's tried a competitor.

---

### Above-the-Fold Supporting Line

(One sentence, appears below CTA, closes the deal for a scanner)

"Signed, notarized, and auto-updating — not a GitHub DMG you'll forget to re-download."

---

### Hero CTAs

**Primary:** Download Free (macOS 14+)
**Secondary:** Install with Homebrew

*(Secondary displays the command inline: `brew install rob-stout/tap/tokenomics`)*

---

## PROVIDER STRIP

### Framing

Headline: "Works with the tools you already use"

Display the five shipping providers as logos with names beneath them, in a horizontal row:
Claude Code — GitHub Copilot — Cursor — Codex CLI — Gemini CLI

Below the strip, a single line in a subdued treatment:
"ElevenLabs, Runway, and Stability AI coming soon."

Do NOT show Midjourney/Suno/Udio placeholders. Coming-soon credibility requires dates or near-term signals — vaporware logos hurt more than they help.

Design note for the designer: this strip should feel like a trust signal, not a feature. No checkmarks, no animation. Logo + name, one row, done.

---

## FEATURE SECTIONS — INFORMATION ARCHITECTURE

Recommended order and rationale:

1. **The Pace Dot** — lead with the signature idea. This is the thing nobody else has and nobody else could explain in one sentence. It converts the app from "usage meter" to "behavioral signal." Lead here.
2. **Five Providers, One Icon** — the wedge against claudeusagebar.com and TokenBar's complexity. Breadth without clutter.
3. **Zero-Friction Auth** — the objection killer. Anyone who has tried a competitor remembers pasting a cookie. Address this before they close the tab.
4. **Desktop Widgets** — visible differentiation. Competitor has nothing. This is a screenshot opportunity.
5. **Built to Last** — signed, notarized, auto-updating, Homebrew. Signals this is a product, not a weekend hack.
6. **Privacy** — developers will check. Make it easy to find and specific enough to trust.

---

## FEATURE COPY

### 1. The Pace Dot

**Section title:** Know if you're burning fast — before the API tells you to stop.

**Body:**
A ring at 60% means nothing on its own. Is that good or bad? It depends where you are in the window.

The pace dot shows where your fill would sit if you'd used quota evenly since the window opened. If your ring is ahead of the dot, you're moving fast. If it's behind, you have room.

That's the difference between data and signal. Tokenomics shows you both.

*(Designer note: this section needs a close-up illustration of the ring + pace dot relationship — the arc, the track, the dot, labeled. No screenshots. A diagram.)*

---

### 2. Five Providers, One Icon

**Section title:** Claude Code, Copilot, Cursor, Codex, Gemini — all in one place.

**Body:**
Most of us don't use just one AI tool. Tokenomics detects which ones you have installed and shows them all — usage rings in the menu bar, full detail in the popover, a dashboard on your desktop.

Drag to reorder. Hide the ones you're not using today. The menu bar shows the one you're closest to hitting.

---

### 3. Zero-Friction Auth

**Section title:** No token pasting. No cookie hunting.

**Body:**
Tokenomics reads credentials from the same places your AI tools already store them: macOS Keychain for Claude Code, `gh` CLI for Copilot, local session files for Cursor, Codex, and Gemini.

Sign in to your tools once. Tokenomics picks it up automatically.

If Claude Code rotates your OAuth token during a sleep/wake cycle — which it does — Tokenomics notices and re-reads Keychain silently. You won't see a logout screen.

---

### 4. Desktop Widgets

**Section title:** Your usage on the desktop. No clicks required.

**Body:**
Small, medium, and large widgets show your providers at a glance — right on your macOS desktop. The large widget fits up to seven providers with usage rings and reset timers.

Tap any widget to jump straight to Tokenomics.

*(Designer note: screenshot of large widget in context on a macOS desktop is the hero image for this section.)*

---

### 5. Built to Last

**Section title:** Signed, notarized, and auto-updating.

**Body:**
Tokenomics is distributed as a Developer ID-signed, notarized app — the same level of code signing Apple requires from paid apps on the Mac App Store. Sparkle handles silent background updates. Install once, stay current.

Available via Homebrew too, if that's how you roll.

```
brew install rob-stout/tap/tokenomics
```

No re-downloading from GitHub every time there's a new version.

---

### 6. Privacy

**Section title:** Your data doesn't leave your Mac.

**Body:**
Tokenomics reads credentials from local sources (Keychain, config files) and holds them in memory while running. No analytics. No telemetry. No third-party SDKs. No data collection of any kind.

Network calls go only to the providers whose data it's fetching: Anthropic, GitHub, OpenAI, Google. That's it.

Source code is available on GitHub. Check for yourself.

---

## COMPARISON FRAMING

**Recommendation: No direct comparison table. No naming claudeusagebar.com.**

The reasons:
1. Naming a smaller competitor elevates them — PH and HN audiences will visit it out of curiosity.
2. A comparison table in a launch context reads as defensive, not confident.
3. Tokenomics' advantages (pace dot, five providers, zero-friction auth, widgets, production distribution) are already in the product copy. Anyone who's used a single-provider app will self-select and understand the difference.

What to do instead: let the "Zero-Friction Auth" section do the work. The detail about OAuth token rotation and no cookie pasting is specific enough that anyone who's experienced competitor friction will recognize it immediately — without naming the competitor.

If a PH commenter asks "how is this different from claudeusagebar?" Rob has a crisp response ready (see launch-plan.md). That's where the comparison happens — in conversation, not on the page.

---

## FAQ

**Q: Is it free?**
Yes. Tokenomics is free to download and use. There's no subscription, no paid tier, and no feature gating. GitHub Sponsors link is in the app if you find it useful.

**Q: How does it authenticate? Do I need to paste any tokens?**
No manual setup required for most providers. Tokenomics reads credentials from where your AI tools already store them — macOS Keychain for Claude Code, the `gh` CLI for GitHub Copilot, and local config files for Cursor, Codex, and Gemini. Sign in to each tool once (as you normally would), and Tokenomics detects them automatically.

**Q: Does it send my API keys or credentials anywhere?**
No. Your credentials are read from local sources into memory. They're never written to disk by Tokenomics, never logged, and never transmitted to any server other than the provider you're fetching usage from. The only outbound calls Tokenomics makes are to Anthropic's API (for Claude Code usage), and to GitHub's appcast URL to check for app updates. Codex, Gemini, Copilot, and Cursor usage is read entirely from local files — no network calls.

**Q: Is it open source?**
Source is available on GitHub under a source-available license — you can read and share the code with attribution. It's not MIT: the license reserves commercial rights. This lets the project stay visible for portfolio and community purposes while preserving the option to monetize later.

**Q: macOS only? What about Windows/Linux?**
macOS only for now (14 Sonoma or later). The menu bar is a macOS-native concept and the auth paths (Keychain, `gh` CLI, local config files) are Mac-specific. A Windows/Linux version built on Tauri is on the roadmap, but it's behind Phase 2 work (agent approval notifications and a watch app). Cursor and Copilot users on Windows are a real audience — it's not forgotten, just sequenced correctly.

**Q: What about Midjourney / Suno / Udio?**
They're coming once those providers ship a public API with credit/usage endpoints. Tokenomics won't integrate against unofficial endpoints or scraping — that breaks with any platform update and it's against ToS. ElevenLabs, Runway, and Stability AI are next, because they have real APIs with documented quota endpoints.

**Q: Why not just open a browser tab and check the dashboard?**
You could. The problem is that you don't know you need to check until you're mid-task and something breaks. The pace dot is specifically useful here: it shows whether you're on track to hit a limit before you actually do, so you can make a call about whether to start a long agentic run. A dashboard answers "how much have I used?" — Tokenomics answers "am I about to run out?"

**Q: How is it different from other Claude/AI usage trackers?**
Two things: breadth and signal quality. Breadth: five providers in one place, without requiring a different app for each. Signal quality: the pace dot. Most usage meters show a percentage. Tokenomics shows whether that percentage is ahead of or behind where you'd expect given how much of the window has elapsed. That turns a number into an answer.

---

## FOOTER

**Tagline:** Know where you stand.

**Links:**
- GitHub (source code + releases)
- Homebrew (`brew install rob-stout/tap/tokenomics`)
- Changelog (GitHub Releases)
- Privacy Policy
- License
- Twitter / X (@robbystout or project handle — confirm with Rob)

**Copyright:** 2026 Rob Stout. Not affiliated with Anthropic, OpenAI, Google, GitHub, or Cursor.

---

## COPY NOT YET WRITTEN (depends on Rob's decisions)

- Pricing page (if ever added)
- Onboarding email (if email capture is added pre-launch)
- App Store description (not applicable — Mac App Store distribution not current plan)
