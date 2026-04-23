# Tokenomics — Product Hunt Launch Plan

---

## PRODUCT HUNT CORE COPY

### Tagline (60 char max)

"Track five AI tools from your menu bar. Never get rate-limited mid-task."

Character count: 60. Use as-is.

Backup option (if 60 is hard): "AI usage for your menu bar. Five tools. One glance."

---

### PH Description (260 char max)

Tokenomics shows Claude Code, Copilot, Cursor, Codex, and Gemini as concentric rings in your macOS menu bar. The pace dot tells you if you're burning fast before the API stops you. Zero-friction auth. Free. Signed and auto-updating.

Character count: 237. Room for minor edits.

---

### PH First Comment — Rob's Founder Post

Hey everyone — I'm Rob, the designer/developer behind Tokenomics.

I built this because I kept getting rate-limited mid-task. Not because I was careless — I just had no idea where I stood. The only option was to break flow, open a browser, find a dashboard, and then decide whether to keep going. That friction compounds when you're deep in an agentic run.

The thing I'm most proud of isn't the multi-provider support. It's the pace dot — a small marker on each ring that shows where your fill would sit if you'd consumed quota evenly across the window. If your arc is ahead of the dot, you're burning fast. Behind, you have room. It converts a raw number into a signal you can act on before the API acts on you.

A few things worth knowing:
- Auth is zero-friction. It reads credentials from where Claude Code, Copilot, Cursor, Codex, and Gemini already store them. No token pasting, no cookie extraction.
- Self-healing OAuth: when Claude Code rotates your token during sleep/wake, Tokenomics re-reads Keychain silently. You won't see a logout screen.
- It's signed, notarized, and auto-updating via Sparkle. Available on Homebrew too. This is a product, not a GitHub DMG.
- Desktop widgets (small, medium, large) for macOS 14+. The large widget fits seven providers.
- Creative AI providers (ElevenLabs, Runway, Stability AI) are next.

It's free. Source available on GitHub.

Happy to answer questions — especially about the pace dot design, auth mechanics, or the rings renderer (CoreGraphics, not SwiftUI — there's a reason for that).

---

## PH GALLERY SHOT LIST

Order matters. PH galleries are left-to-right; most people see shots 1–3.

**Shot 1 — Hero (the icon + popover)**
The menu bar icon with both rings filled to a meaningful value (not 0%, not 100%) with the popover open showing 2–3 providers tabbed. Pace dots visible and ahead/behind the arc on at least one ring. This is the money shot. Dark menu bar. macOS desktop context visible but blurred or minimal.

**Shot 2 — The Pace Dot (close-up diagram or annotated screenshot)**
A close-up of a single ring with callout labels: "Fill arc = what you've used," "Pace dot = where you'd be at average pace," "Ahead = burning fast." This is the one screenshot that explains the signature idea. Can be a designed diagram rather than a pure screenshot — probably should be.

**Shot 3 — Five Providers (the popover, multi-provider state)**
The popover open with all five provider tabs visible at the top, one active, showing its rings and usage bars. This visually answers "does it support my tools?" in one glance.

**Shot 4 — Desktop Widgets**
Large widget on a macOS desktop showing 5–7 providers with usage rings and reset timers. Should feel like ambient information, not a dashboard crammed into a widget. Natural desktop context (wallpaper, icons) rather than a blank background.

**Shot 5 — Auth / Setup (optional but strong)**
The onboarding or "first run" state showing zero configuration required — detected providers appearing automatically. One screenshot that makes "zero-friction auth" concrete without requiring the viewer to read about it.

**Shot 6 — Settings (optional)**
The settings view with providers in reorder state, showing drag handles and toggle controls. Shows depth without requiring a feature walkthrough.

Design note: all shots should be @2x / Retina. If using a real MacBook Pro screenshot, make sure menu bar items aren't cluttered. Crop to focus on Tokenomics.

---

## MAKER COMMENTS STRATEGY

**The goal:** be the developer who knows their product deeply and answers questions specifically, not the founder who repeats marketing copy.

**Rules:**
1. Answer every question in the first 6 hours. PH voting is front-loaded; engaged founders get more upvotes.
2. Never get defensive about competitors. "It's a good app too" and redirect to what makes yours different.
3. One specific detail per response. Not bullet lists — one concrete thing. Example: "The pace dot computes elapsed / total window and renders as a CoreGraphics arc endpoint — it's the same math the rings use, just inverted."
4. Ask follow-up questions. "What tools are you currently using?" draws people in and generates real feedback publicly visible on the page.
5. If someone asks something you can't answer well yet, say so: "That's on the roadmap — agent approval notifications are Phase 2. Here's why I sequenced it that way..."

**Pre-planned responses to likely comments:**

"How is this different from claudeusagebar?" → "Two things: five providers with zero-friction auth (no cookie extraction needed), and the pace dot — a marker that shows if your current usage is trending toward a limit, not just how much you've used. If you only use Claude and want MIT-licensed, that app works great. This is for people who've grown past single-provider."

"TokenBar does 20+ providers" → "TokenBar needs an API key for each one. Tokenomics reads credentials from where your tools already store them. For the coding tools most of us run daily, that's a better experience. 20 providers sounds more impressive than it is if 15 of them require manual setup."

"Why not free/open source like competitors?" → "Source is available on GitHub — you can read every line. The license is source-available rather than MIT, which keeps commercial rights open for later. Free to use, forever. I'm not trying to build a SaaS out of this."

"Why macOS only?" → "The menu bar, Keychain, and `gh` CLI auth paths are Mac-specific. Windows/Linux is on the roadmap once macOS is mature — building on Tauri, probably. Cursor and Copilot users on Windows are a real audience and it's not forgotten."

---

## TIMING RECOMMENDATION

**Day:** Tuesday
**Time:** 12:01 AM PST (Pacific Time)

**Rationale:**
Tuesday is the peak traffic day on Product Hunt. Developer tools historically perform well mid-week when developers are at their desks, encountering the problem the tool solves. Weekend launches see higher developer-to-total-visitor ratios but lower absolute traffic.

For a zero-budget launch with no pre-existing PH following, absolute traffic matters more than ratio. Tuesday maximizes the pool of people who could see and upvote.

**Season:** Avoid major US holidays and the week between Christmas and New Year. April–May 2026 is clean. Avoid launching the same week as a major Apple event (WWDC is typically early June) — developer attention goes elsewhere.

**Do not** try to launch on a Monday. Mondays have historically underperformed for developer tools, and the PH audience is slowest to engage on day-of.

---

## PRE-LAUNCH CHECKLIST

### 7 Days Out

- [ ] Create a Product Hunt account if Rob doesn't have one (need at least some activity before launch — even a few upvotes on other products signals you're real)
- [ ] Finalize all 6 gallery screenshots. No placeholder images.
- [ ] Draft the PH description, tagline, and first comment. Have someone else read it cold.
- [ ] Confirm trytokenomics.com is live with working download/Homebrew links
- [ ] Prepare a v2.7.x build that's clean: no known bugs, no broken states, installer works on a fresh macOS 14 machine
- [ ] Post the LinkedIn origin story (this exists — it's in `/Users/jarvis/projects/Tokenomics/linkedin-post.md`). Do this 3–5 days before PH to warm up the network.
- [ ] Identify 5–10 developers in your network to ask for honest early feedback (not "please upvote" — "I'd love your reaction to this"). Real engagement beats coordinated upvoting.
- [ ] Set up the PH page (can be done in draft before going live)

### 3 Days Out

- [ ] Post a "shipping soon" note on Twitter/X with a screenshot of the pace dot. Don't explain everything — one concrete detail that creates curiosity.
- [ ] Post in r/MacApps: "I built a menu bar app to track AI coding usage across five providers. Soft launch before PH — looking for feedback." Link to trytokenomics.com, not PH (avoid vote brigading optics).
- [ ] Confirm the PH gallery images look good in the preview. Retina screenshots only.
- [ ] Write a short HN Show HN post (see below). Don't post yet.
- [ ] Ping 2–3 developer friends to download and test on the morning of launch.

### Day Of

- [ ] Submit to PH at 12:01 AM PST
- [ ] Post first comment (the founder post above) within the first 5 minutes
- [ ] Do NOT share a direct "upvote me" link anywhere. PH has gotten good at detecting this and it can backfire.
- [ ] Share the PH page link organically: Twitter, LinkedIn, the Slack/Discord communities you're actually in. Frame it as "I launched today and would love feedback" — not "please upvote."
- [ ] Post the HN Show HN at ~8–9 AM PST (HN traffic peaks later in the morning Pacific Time)
- [ ] Check PH every 30–60 minutes. Respond to comments quickly. Engagement velocity matters to the PH algorithm in the first few hours.
- [ ] Block your calendar for the morning. This is a half-day of community engagement, not a press-release-and-walk-away.

---

## ADJACENT CHANNELS

### Hacker News — Show HN

**Title:**
Show HN: Tokenomics – macOS menu bar app for AI coding tool usage (Claude, Copilot, Cursor, Codex, Gemini)

**Body:**
I kept getting rate-limited mid-task. The only way to check was to break focus and open a browser dashboard — which I wouldn't do until it was already too late.

So I built Tokenomics: a menu bar app that shows AI coding tool usage as concentric activity rings. Five providers (Claude Code, GitHub Copilot, Cursor, Codex CLI, Gemini CLI), auto-detected from credentials already on your machine — no token pasting.

The thing I ended up caring most about is the pace dot: a small marker on each ring that shows where your fill would sit if you'd consumed quota evenly. If your arc is ahead of it, you're burning fast. Behind it, you have room. Turns a percentage into a signal you can act on before the API acts on you.

Technical notes for people who want the details:
- Reads Claude Code's OAuth token from macOS Keychain; self-heals when Claude rotates it during sleep/wake
- Copilot via `gh` CLI (no PAT required); Cursor and Codex from local session files; Gemini from `~/.gemini/`
- Rings are CoreGraphics, not SwiftUI — menu bar labels need NSImage for template rendering (dark/light mode inversion)
- Activity-aware polling — sleeps after 9 min idle, wakes instantly
- Exponential backoff on 429: 5m → 10m → 20m → 40m → 1h cap
- Desktop widgets (small/medium/large, WidgetKit)
- Signed, notarized, Sparkle auto-update, on Homebrew

Free. Source available on GitHub (source-available license, not MIT — commercial rights reserved for later).

https://trytokenomics.com

**HN posting notes:**
- Post on a weekday morning (Tuesday–Thursday, 8–10 AM Eastern works well for HN visibility)
- Do NOT post the same day as your PH launch — split them by 1–2 days to get independent distribution lifts
- HN tends to engage with technical specifics. The CoreGraphics note and the Keychain truncation workaround (mentioned in the case study) are good topics to have ready for the thread.
- If you get pushback ("just use the dashboard"), respond with the pace dot explanation — it's the most technically interesting thing and the hardest for someone to wave off.

---

### LinkedIn Post

Draft (matching Rob's existing voice from the LinkedIn post file):

---

I built Tokenomics to solve something simple: I kept getting rate-limited mid-task because I had no idea how close I was.

The solution was obvious in hindsight — a menu bar app that shows usage as concentric rings, like Apple Watch Activity Rings. Fill clockwise as you consume quota. Two rings: the nearest limit (inner) and broader context (outer). Any Apple user reads it without a legend.

But the interesting design problem was: a ring at 60% means nothing on its own. Good or bad depends entirely on where you are in the window. So I added the pace dot — a small marker showing where your fill would sit if you'd consumed evenly. Ahead of it, you're burning fast. Behind, you have room. That's the difference between a usage meter and an actual signal.

Three things I'm proud of technically, beyond the pace dot:

The auth is zero-friction. Tokenomics reads credentials from where your AI tools already store them — Keychain, `gh` CLI, local config files. No token pasting. And when Claude Code rotates your OAuth token during sleep/wake (which it does), Tokenomics detects it and re-reads Keychain silently. You never see a logout screen.

The rings are CoreGraphics, not SwiftUI. The menu bar label has to be an NSImage for proper template rendering — so the OS can invert it in dark mode and active states automatically. That meant drawing the rings in CoreGraphics with explicit geometry that maps to the Figma component. Not the intuitive answer, but the right one.

The distribution is production-grade. Signed, notarized, Sparkle auto-updating, on Homebrew. This is a product, not a side project.

Now shipping with five providers: Claude Code, GitHub Copilot, Cursor, Codex CLI, and Gemini CLI. Free. Available at the link below.

https://trytokenomics.com

#BuildInPublic #MacOS #SwiftUI #ClaudeCode

---

**Posting notes:** post this 3–5 days before PH launch. It warms up your network with people who'll genuinely use the tool, not people showing up to support a launch. The technical specifics (CoreGraphics, self-healing auth) serve double duty as portfolio signals for the Anthropic/recruiter audience.

---

### Twitter / X Thread

**Post 1 (hook):**
I've been rate-limited mid-task more times than I can count.

Not because I was careless. I just had no visibility into where I stood.

So I built Tokenomics: all five AI coding tools in one menu bar icon.

[screenshot of menu bar with rings visible + popover open]

---

**Post 2 (the pace dot):**
The thing I care most about isn't the five-provider support.

It's the pace dot.

A ring at 60% means nothing. Good or bad depends on where you are in the window.

The pace dot shows where you'd be at average pace. Ahead of it = burning fast. Behind = room to go.

[diagram or close-up of ring + dot + labels]

---

**Post 3 (auth):**
No token pasting. No cookie extraction.

Tokenomics reads credentials from where your tools already store them:
- Claude Code: macOS Keychain
- Copilot: `gh` CLI
- Cursor, Codex, Gemini: local config files

Sign in to your tools once. That's it.

---

**Post 4 (technical detail — builds credibility):**
The rings are CoreGraphics, not SwiftUI.

Menu bar labels need to be NSImage for template rendering — so macOS can invert the icon in dark mode automatically.

That means drawing the rings explicitly in CoreGraphics with geometry that matches the Figma component.

Not the obvious approach. But it's what the platform requires.

---

**Post 5 (widgets):**
Desktop widgets too.

Small, medium, large — up to 7 providers with usage rings and reset timers on your macOS desktop.

Tap any widget to open the full view.

[screenshot of large widget in desktop context]

---

**Post 6 (launch CTA):**
It's free.

Signed, notarized, and auto-updating via Sparkle. On Homebrew too.

brew install rob-stout/tap/tokenomics

Or download at trytokenomics.com

[link to PH page on launch day]

---

**Post 7 (optional — the builder's note):**
I've been building with Claude Code as my pair programmer.

Building a tool that tracks Claude Code usage, with Claude Code, while burning through Claude Code quota, felt like it should be a paradox.

Turns out it's just recursive.

[no image needed — this one earns engagement on the text alone]

---

**Thread notes:**
- Post the full thread on PH launch day, linking to the PH page at the end
- Posts 1–3 should go out within the first hour. 4–7 can be spread through the day
- Reply to every response in the first 6 hours
- If the thread gets traction, the pace dot post (2) tends to get the most saves/bookmarks — it's the most novel idea and it's visual

---

### Reddit

**Where to post:**

**r/MacApps** — primary. This community exists for exactly this. Frame as: "I built a menu bar app for AI coding tool usage — looking for feedback before the PH launch." Link to trytokenomics.com. Include the pace dot screenshot.

**r/ClaudeAI** — secondary. This is where Claude Code power users live. Frame as: "I got tired of hitting rate limits without warning, so I built this." Don't oversell the multi-provider angle here — this audience cares about Claude specifically. Lead with the OAuth self-healing and pace dot.

**r/webdev or r/programming** — post only if you have something interesting to say technically, like a "I built this using X and here's what I learned" post. Don't post pure promotions there — they'll get buried and you'll get downvoted.

**Avoid:**
- r/SideProject — low engagement, high noise
- r/ProductHunting or similar — these are coordinated launch communities and can trigger PH's vote detection
- r/artificial or r/MachineLearning — wrong audience (researchers, not tool-using developers)

**Timing:** r/MacApps post should go up 1–2 days before PH launch. r/ClaudeAI post can go day-of or day-after PH.

---

## HANDLING THE "WHY NOT FREE/OPEN SOURCE" THREAD

This will happen. On PH, on HN, or on Reddit, someone will post: "claudeusagebar is free and MIT licensed. Why should I use this instead?"

**The response (write this once, use it everywhere):**

"claudeusagebar is a good app and it's genuinely free and MIT licensed. If that's what you need, use it.

Two reasons someone might use Tokenomics instead: it covers five providers (Claude Code, Copilot, Cursor, Codex, Gemini) without requiring token pasting or cookie extraction — auth is automatic from your existing tool credentials. And the pace dot shows whether you're trending toward a limit, not just how much you've used.

Tokenomics source is available on GitHub — you can read every line. The license isn't MIT (it's source-available, commercial rights reserved), but it's free to use. The reason for the license: I want to keep the option open to charge for something later, probably Phase 2 agent approval features. That doesn't affect anyone using the current version."

**What not to do:**
- Don't attack the competitor's quality, uptime, or author
- Don't imply their privacy practices are worse than yours (they're probably fine)
- Don't be defensive — specificity is confidence

The goal of this response isn't to win the argument. It's to be specific enough that the person reading the thread can make their own decision. Developers respect that.

---

## RISK REGISTER

| Risk | Likelihood | Response |
|---|---|---|
| TokenBar already has PH presence + users | High — they launched March 2026 | Position on depth (zero-friction auth, pace dot, widgets) vs breadth. Don't fight the provider count. |
| "Why not MIT license?" thread | High | Response prepared above. Be specific, don't be defensive. |
| PH algorithm de-ranks due to coordinated upvotes | Medium | Don't coordinate. Share the PH link organically. Real engagement only. |
| Low Day 1 vote count | Medium | Have 5–10 genuine users ready to give real feedback. Engagement quality matters more than raw count. |
| "macOS 14 only is too restrictive" | Medium | Acknowledge it honestly. macOS 13 was released in 2022 and macOS 14 is the current release. The widget requirement necessitates 14+. |
| Anthropic changes OAuth token location/format | Low but real | Self-healing retry already in place. If Anthropic breaks it, ship a fix same day — this is the core Claude use case. |
