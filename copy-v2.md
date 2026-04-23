# Tokenomics — Landing Page Copy v2
# Revised to editorial voice per design-system.html principles
# Round 1 copy preserved at copy.md

---

## 1. HERO HEADLINE — Four Candidates

Each uses serif sentence case, one italic accent word in accent blue, 6–14 words, reads like a sentence not a slogan.

---

**Option A:**
"Know if you're *ahead* before the window closes."

Voice note: The tension lives in "ahead" — it names the pace dot concept without explaining it, and "before the window closes" is concrete without being threatening. Calm. The user already knows what rate limits are; this doesn't need to explain them.

---

**Option B:**
"Five AI tools. One *honest* look at where you stand."

Voice note: "Honest" carries the emotional payload — it implies every other way you check (browser dashboards, mental models) is somewhat dishonest or incomplete. The sentence is a mild revelation, not a confrontation.

---

**Option C:**
"Your usage, *always* a glance away."

Voice note: Shortest. Most ambient. Closest to the design system's "Quiet polling, loud clarity." The italic on "always" emphasizes the persistent nature — it's there even when you forget to check.

---

**Option D:**
"See where you stand *before* the API decides for you."

Voice note: "Before" is the same anchor word used in the design system specimen ("See it *before* you pay for it") — that's intentional, it matches the established voice register. "The API decides for you" is specific and a little wry without being adversarial.

---

### Recommendation: Option D.

"See where you stand *before* the API decides for you."

The design system explicitly shows "See it *before* you pay for it" as the canonical display-size example. Option D uses the same grammar: subject + *before* + consequence. The italic lands on the adverb that sets up the tension, which is exactly the pattern Rob codified. "The API decides for you" is specific enough to be meaningful to any developer who has been mid-task when a 429 hit — but it isn't adversarial, it's observational. The phrase is complete and natural at display size. It breaks well across two lines: "See where you stand" / "*before* the API decides for you." Options A and B are good but less precisely matched to the voice specimen. Option C is too passive for a hero — calm is not the same as invisible.

---

## 2. HERO SUBHEADLINE — Three Options

One or two sentences. Specific. No stacked value props.

---

**Option A:**
Tokenomics sits in your menu bar and watches Claude Code, Copilot, Cursor, Codex, and Gemini — so you know if you have room for one more run.

---

**Option B:**
A menu-bar app that reads your AI tool credentials automatically and shows usage rings for every provider at once. No tokens to paste. No tabs to open.

---

**Option C:**
Five providers. One icon. The pace dot shows whether you're on track — or burning ahead of schedule.

---

Recommendation: **Option A** for warmth and specificity. Option C if the pace dot diagram is already visible above the fold and the subhead can stay tighter.

---

## 3. ABOVE-THE-FOLD SUPPORTING LINE — Two Alternatives

Replaces: "Signed, notarized, and auto-updating — not a GitHub DMG you'll forget to re-download."

---

**Option A (three-noun, period-stop):**
Signed. Notarized. Auto-updating through Sparkle.

---

**Option B (one-sentence, editorial):**
Developer ID signed, notarized, and kept current through Sparkle — the same distribution standard as any paid Mac app.

---

Note: Option A matches the design system principle exactly ("The product is the proof") — three nouns with period stops, no competitive framing. Option B adds a small context beat ("same standard as any paid Mac app") that addresses the unspoken quality signal without naming anything. Either works. Option A is the stronger choice for above-the-fold brevity.

---

## 4. SECTION TITLES (serif, with italic accent)

### Pace Dot section
Eyebrow: SIGNAL
Title: "The *dot* that tells you if you're on track."

---

### Five Providers section
Eyebrow: BREADTH
Title: "Every tool you run, in *one* place."

---

### Widgets showcase section
Eyebrow: AMBIENT
Title: "Usage on your desktop, *always* in view."

---

### Craft / Built to Last section
Eyebrow: CRAFT
Title: "Built the way a *good* Mac app should be."

---

### Privacy section
Eyebrow: PRIVACY
Title: "Your data stays on *your* Mac."

---

## 5. EYEBROW PILLS

One or two words, uppercase, tracking-wide, above each section title.

| Section | Eyebrow |
|---|---|
| Pace Dot | SIGNAL |
| Five Providers | BREADTH |
| Widgets | AMBIENT |
| Craft / Built to Last | CRAFT |
| Privacy | PRIVACY |
| Zero-Friction Auth | SETUP |

---

## 6. CRAFT GRID — Six Feature Cards

Format per design system example: eyebrow "Feature" + serif H4 (4–7 words) + 1-sentence sans body.

---

**Card 1 — Menu bar rings**
Eyebrow: Feature
Title: One *ring* to rule them all.
Body: Menu-bar rings aggregate every provider into a single glance without opening a tab.

---

**Card 2 — Pace dot**
Eyebrow: Feature
Title: The dot that reads the *room*.
Body: The pace dot marks where even usage would sit — so ahead of it means you're burning fast.

---

**Card 3 — Zero-friction auth**
Eyebrow: Feature
Title: Sign in *once*, then forget it.
Body: Reads credentials from Keychain and your existing CLI sessions. Nothing to paste, nothing to rotate.

---

**Card 4 — Desktop widgets**
Eyebrow: Feature
Title: Usage on your desktop, *no clicks*.
Body: Small, medium, and large widgets sit on your macOS desktop and update without opening the app.

---

**Card 5 — Quiet polling**
Eyebrow: Feature
Title: Quiet by *design*, loud when it matters.
Body: Exponential backoff on rate limits keeps the APIs happy; threshold alerts tell you when to pay attention.

---

**Card 6 — Drag-to-reorder providers**
Eyebrow: Feature
Title: Yours to *arrange* however you work.
Body: Drag providers into the order that matches your day. Hide the ones you're not using. The menu bar stays focused.

---

## 7. PRODUCT HUNT TAGLINE — Three Alternatives

60 characters max. Editorial voice. No overconfident promises.

---

**Option A (45 chars):**
"Track five AI tools from your menu bar."

---

**Option B (58 chars):**
"Five AI providers. One menu bar icon. Free for macOS."

---

**Option C (59 chars):**
"Know your AI usage before the API cuts you off. For macOS."

---

Note: Option A is the cleanest — it's declarative, not a promise. Option B adds the breadth signal. Option C is closest to the pace dot benefit without overpromising; "before the API cuts you off" is observational, not a guarantee. Recommend Option B for PH where breadth and the "free" call matter; Option C for Twitter/X where the benefit reads faster.

---

## 8. HERO CTAs

**Primary CTA:**
"Download for macOS"

Rationale: Matches the button specimen in the design system exactly ("Download for macOS"). Drops the version number from the button label — version is better as a small pill badge adjacent to the button (e.g. "v2.7.7 live") or in the supporting line below. Cleaner tap target.

**Secondary CTA:**
"View on GitHub"

Rationale: "View on GitHub" is the right secondary for developer trust. The Homebrew command belongs in a dedicated install block further down the page (a tabbed install block: "Homebrew" / "Direct download" per the design system component spec). Don't put the Homebrew command inline next to the primary CTA — it competes for attention and makes the hero visually busy. The install block can live just below the hero, where someone who is already sold can act on it immediately.

---

## 9. PACE DOT DIAGRAM — Microcopy

Three callout labels for the annotated ring diagram. Each 2–5 words.

---

**Label 1 — The fill arc (what the user has consumed)**
"Usage so far"

---

**Label 2 — The pace dot (where even consumption would sit)**
"Even-pace mark"

---

**Label 3 — The ahead/behind state (meaning)**
Use two variants, shown conditionally or as a split callout:
- When fill is ahead of the dot: "Burning *ahead* of pace"
- When fill is behind the dot: "Room to run"

If only one static label is needed for the diagram: "Your pace, at a glance"

---

**Diagram caption (one sentence, below the diagram):**
If your fill arc passes the pace mark, you're using faster than average for this window — and a limit is closer than the percentage suggests.

---

Note on this section: these six words carry the entire signature concept. "Even-pace mark" is precise — it names the dot by what it calculates, not by what it looks like. "Burning *ahead* of pace" earns its italic because that's the moment the product creates value. The caption does the one job the visual can't: it explains the implication, not just the mechanism.

---

## 10. VOICE NOTE TO THE DESIGNER

The biggest shift from Round 1: stop framing the product against what's missing and start framing it alongside what the user already does. Round 1 headlines like "Your AI tools don't warn you. Now your menu bar does" are accurate but they read as a brand taking a swing — the site should feel like a calm tool, not a manifesto. The new copy leads with what the user gains, not what they've been missing.

The italic accent word is load-bearing — it does the emotional work that adjectives usually do badly. Don't treat it as decoration; wherever the italic lands, that's the idea the reader should remember from the line. If a headline works without the italic, it's probably the wrong word to italicize.

The pace dot section copy is the most fragile. The diagram labels ("Usage so far," "Even-pace mark," "Burning ahead of pace") have to land without the user having read the body copy — if a visitor lands mid-scroll on that section, those three labels plus the caption are the entire pitch. Review them last, in isolation, with fresh eyes.

FAQ answers are already in the right voice — specific, honest, no hedging. Leave them exactly as written in Round 1.

---

*Round 1 copy is preserved at /Users/jarvis/projects/Tokenomics/site/copy.md for comparison.*
