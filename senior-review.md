# Tokenomics Landing Page — Senior Review

Verdict: **needs changes before launch.** The bones are strong. A handful of specific defects will undermine the "this was built by an Apple designer" signal Rob is leaning on, and one copy leak will be the first thing a critic notices.

---

## Must-fix before launch

1. **Hero H1 is Round-1 voice; copy-v2 landed on a different recommendation.** `index.html:64` ships `A menu-bar view of *every* AI tool you pay for.` That line is lifted from the `design-system.html` H1 type specimen (line 717), not from copy-v2. copy-v2.md recommends Option D: `See where you stand *before* the API decides for you.` The design system itself explicitly shows `See it *before* you pay for it.` as the display specimen — the "before [consequence]" pattern is the house grammar. `every` does not italicize meaningfully (it's a plain quantifier, not a tension word). Fix: replace with copy-v2 Option D. The hero `max-width: 14ch` in `styles.css:473` will also need review — Option D wants a 2-line break around `before`.

2. **Pace-dot diagram has a duplicated/misplaced pace dot.** `index.html:278-287` draws TWO outer-ring dots. The first (at `cx=170.9, cy=235.1`, opacity 0.4) is the correct position for 45% of circumference (bottom-right). The second (at `cx=235.1, cy=109.1`, opacity 0.5) is at ~20% of circumference (upper-right) — the math in the comment on line 283 is wrong. The visible "final" dot is in the wrong place, and a ghost dot is rendered behind it at the correct location. This is the single screenshot most likely to end up in Rob's PH gallery and it is visually broken. Fix: delete line 278-280 and line 287's inner-ring dot (which has the same transposition error), redraw both at the true 162° position: outer `cx=170.9, cy=235.1`, inner `cx=159.8, cy=200.9`.

3. **The pace diagram callouts don't connect to what they label.** The `.callout-pace` connector at `styles.css:668-675` sits at 50% vertical on the right edge, but a correctly-placed pace dot at 45% of circumference lives at bottom-right (~80% vertical). The `.callout-behind` connector is bottom-left, but the 60% fill arc ends at the bottom-left — so the "Ahead of dot" label is pointing at the *arc-end*, not at the "ahead" region (which is the arc sector between the dot and the fill endpoint). Once dot #2 is fixed, reposition callouts: `callout-pace` at ~75% top, `callout-behind` at ~40% top. The diagram is the single asset that carries the signature idea — if a first-time visitor can't draw a line from the label to the thing, the concept doesn't land.

4. **Light-mode `--text-subtle` fails WCAG AA on cream background.** `--text-subtle: rgba(14,51,77,0.44)` on `#F3EFE5` computes to ~2.8:1 — below AA 4.5:1 for body text. This token is used for meaningful copy including `.hero-support` (`index.html:91` — the "Signed, notarized, and auto-updating" line, a purchase-decision beat), all `.feature-kicker` eyebrows, `.install-support`, `.provider-coming`, and `.footer-meta` legal disclaimer. Fix: bump alpha from 0.44 → 0.58 (gets to ~4.6:1) or switch to a darker ink base. The footer disclaimer "Not affiliated with Anthropic..." being illegible will catch a lawyer's eye faster than a designer's.

5. **Large widget mockup shows providers that aren't shipped.** `index.html:632-640` renders ElevenLabs and Runway rows in the "7 providers" large widget. The PH audience will install the app and not see those providers. The product_hunt_description says "coming soon — ElevenLabs, Runway, Stability AI," but the hero-level widget *showing them live* is a broken promise. Fix: replace those two rows with a repeat of Claude/Copilot at different usage levels, or a second Claude workspace row. The "up to seven providers" headline is aspirational and currently ships to 5.

6. **FAQ "Is it open source?" answer is not going to survive HN.** `index.html:818-820` — the current answer says "source-available … reserves commercial rights … option to monetize later." HN will read "monetize later" as a BSL-style trap. The launch-plan.md has a better response on line 328-332 that leads with "you can read every line" and names a concrete reason ("probably Phase 2 agent approval features"). Port that language — specificity about *what* will be paid is what makes source-available acceptable to skeptics. Current line will catch exactly the "comment-section fire" the brief flagged.

7. **Nav brand gap: brand-mark is 28×28 but the image inside is sized 24×24 and the container has `width: 28px; height: 28px` plus child `img { width: 24px; height: 24px }` — but the inline HTML overrides to `width="24" height="24"` on a 24px image inside a `width:28px` container with `place-items: center`.** That's fine visually, but the real issue: `brand-mark` in light mode uses `background: var(--widget-dark)` (navy gradient) with a white/dark app icon on it. The icon is `AppIcon.svg` (full-color). On a navy chip that may render with a navy-on-navy clash depending on the icon. Spot-check in browser at light-mode. If the AppIcon is the multicolored version with navy fills, it vanishes. Fix: pre-render a white-foreground monogram variant for the nav chip.

8. **No `<main>` landmark.** Sections sit directly under `<body>` with `<nav>`, `<header class="hero">`, multiple `<section>`s, then `<footer>`. Screen readers expect a `<main>` wrapping the primary content. Wrap the hero through the FAQ in `<main>`. Single-line fix; accessibility-scan blockers will flag it.

9. **Theme toggle button has no visible focus ring.** `styles.css:184-194` — the `.theme-toggle` has no `:focus-visible` style. Keyboard users tabbing through the nav hit nothing they can see. Add `.theme-toggle:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }`. Same applies to `.install-tab` (line 834) and `.copy-btn` (line 872). Three-line fix.

10. **`privacyLink` is `href="#"`.** `index.html:888` — clicking Privacy in the footer scrolls to top. Either point to a real privacy page (`privacy.html`) or remove the link. A broken footer link on a product that markets privacy is a specific, embarrassing miss.

---

## Should-fix, won't block launch

- H2 at `index.html:347` (`Claude Code, Copilot, Cursor, Codex, Gemini — all in *one place*.`) crams five proper nouns before the italic accent. copy-v2 has a cleaner version ("Every tool you run, in *one* place.") — use it.
- The `.reveal` pattern on `index.html:428` uses inline `style="display:flex;…"` which will override the `.reveal` transform. It works because `opacity` isn't overridden, but the translateY doesn't animate. Move inline styles to a class.
- `scroll-behavior: smooth` on html (`styles.css:122`) doesn't respect `prefers-reduced-motion`. Gate it: `@media (prefers-reduced-motion: no-preference) { html { scroll-behavior: smooth; } }`.
- `initNavHighlight` (`app.js:182`) sets `link.style.color` inline, which wins over any `:hover`/`:focus` style and persists after nav leaves intersection (the reset only fires on new intersection). Use a class toggle instead.
- Hero-visual medium widgets show `5-Hour 90%` with pace dot at 74% — "burning fast" state — but the copy next to it (`.lede`) says "see at a glance whether you have headroom." The hero image says "panic" while the copy says "reassurance." Either soften the dark widget to 65% / pace 50% (mild "watch your pace") or lean in with a hero line like the copy-v2 "burning *ahead* of pace" variant.
- `.provider-coming` (`index.html:240`) names three providers; `index.html:632-640` shows two. Pick one list.
- The install-tabs don't support keyboard arrow-key navigation despite `role="tablist"`. ARIA convention is left/right arrow. Not a launch-day blocker but worth 5 minutes.
- Preload the two web-font weights actually used above the fold (serif italic + DM Sans 400) with `<link rel="preload" as="font" crossorigin>` — first-paint on mobile 4G will show FOUT on the H1 otherwise.

## Nice-to-haves

- No `<meta name="robots">`, no canonical URL. Add canonical `https://trytokenomics.com/`.
- OG image is not declared (`og:image`). PH and Twitter previews will render as text-only. Add a 1200×630 image — the widget pair from the hero works.
- `aria-labelledby` is used on most sections; `.feature-section` at `index.html:416` has no `aria-labelledby` referring to the auth-heading.
- `app.js` is not deferred and is loaded at the bottom — harmless but `<script defer src="app.js">` in head is the more conventional pattern, shaves a ms.
- The brand-mark uses `.brand-mark img { width: 24px; height: 24px }` but also `<img width="24" height="24">` — fine, but the light-mode chip with navy gradient background (`--widget-dark`) eats any dark icon. Verify in both themes.
- No 404 page. If `trytokenomics.com/anything-else` hits, default server page surfaces. Cheap GitHub Pages `404.html` would round out the production feel.

---

## The one thing this site does unusually well

The widget showcase section (`desktop-frame`, `index.html:479-647`) is the quiet knockout. It reproduces the real Swift widget gradient (197° with the correct 10.3%/88.1% dark stops and 1.6%/84.5% light stops per `TokenomicsWidgetEntryView.swift`), the correct track opacities (25% dark, 12% light), and the real provider icon assets — so the marketing widgets and the actual widgets are the same object. The dark "desktop frame" with subtle radial-gradient wallpaper and the dock-peek at the bottom gives the mockup a place to live without needing a real macOS screenshot. This is the single thing that will make a competitor's landing page look amateur by comparison. It's the kind of detail a designer notices and a developer doesn't know to ask for — which is exactly the story Rob is selling about himself.

## The one thing that will bite Rob on launch day

The pace-dot diagram is the signature idea of the product, and right now the dot is rendered in the wrong place with a ghost dot behind it at the right place. A first-time visitor trying to parse the concept will trace the fill arc to its end (bottom-left) and see the "Ahead of dot" callout there, then look for the dot itself on the right side where the "Pace dot" callout points — and the dot they see is at 20% of the circumference, not the 45% the arc is supposedly passing. The mental model doesn't assemble. Every subsequent line of copy ("Ahead of the dot, you're burning fast") relies on a diagram that doesn't demonstrate the claim. Fix item #2 and #3 before Rob ships, or the pace dot will look like the one thing the site can't explain — which is devastating because the pace dot is the entire pitch. If Rob fixes nothing else in this review, fix these two.
