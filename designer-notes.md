# Designer Notes — Tokenomics Landing Page

## Three calls I'm confident about

### 1. The pace dot section earns a full-width branded panel

The competitor gives every feature equal real estate — a grid of six identical cards. That flattens everything. The pace dot is the only idea on this site that requires explanation, and it's also the idea that makes Tokenomics worth paying attention to. So it gets its own branded section (the widget's dark gradient, pulled edge-to-edge), a two-column layout with an annotated live diagram on the left and the narrative on the right.

The psychological mechanism at work: the diagram isn't illustrative decoration, it's demonstrative — bars animate in, the pace dot drifts, callout boxes explain what you're looking at in real time. The user doesn't just read about the pace dot; they experience it. That's a much shorter path to "I get it" than any copywriter's explanation.

### 2. Light mode gets warm cream, not inverted dark

Most developers treating light mode as an afterthought would simply lighten the dark-mode backgrounds and call it done. That produces a pale, washed-out result with no character.

The widget's light theme uses a cream palette (`#F3EFE5` → `#E6E0D4`) that's warm, paper-like, and deliberately differentiated from the cold off-whites of generic SaaS sites. This page honors that fully: the light-mode background is `#EAEAE0`, cards are `#F3EFE5`, and the navy text sits on a warm ground instead of a clinical one. The pace dot is dark navy on cream, not white — which is the correct widget-accurate behavior and reads as a considered detail to anyone who's used the app.

The effect is that both modes feel intentional. Users who prefer light mode get a product that respects them, not a mode that was ticked off a list.

### 3. The nav is a constraint, not an afterthought

The brief asked for a "tiny" nav. The temptation when space-constrained is to stuff things in — dropdowns, megamenus, hamburgers on desktop. I went the other way: four text links, a theme toggle, one button. No hover dropdowns. The visual weight of the nav shouldn't compete with the hero headline, and on a single-page site, every section anchor is only one smooth-scroll away.

The dual-ring logo in the nav is pure inline SVG with `currentColor` — it inherits the correct color in both modes without any image asset dependency, and it communicates the product at 22px with no label required if someone already knows the app. That's a small brand reinforcement that costs zero bytes.

---

## One thing I'm uncertain about

**The widget showcase inside a static HTML file.**

The widgets are the strongest competitive differentiator — the competitor literally has nothing equivalent. But rendering them accurately in HTML/CSS is a fidelity compromise. The bars animate on scroll entry and the pace dots drift, which gets the interactive metaphor across. But the small widget's ring layout is a simplified SVG approximation; the actual SwiftUI ring is rendered at native resolution with `isTemplate` behavior in the menu bar.

The risk: a developer looking at the HTML widgets might find them underwhelming compared to the real app. The mitigation would be replacing the simulated widgets with actual screenshots from the app (rendered at 2x in Xcode previews), dropped in as `<img>` tags inside the `.desktop-frame`. That's a Round 2 task once Rob has clean screenshot exports, but worth flagging now so the decision is deliberate rather than discovered late.

The current implementation is honest — it doesn't fake fidelity it can't deliver, and the bar animation + pace dot drift tell the right story — but real screenshots would elevate this section significantly.
