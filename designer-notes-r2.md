# Designer Notes — Round 2

## Three design calls I made

### 1. Pace-dot diagram: pure SVG annotation, no screenshots

The brief asked for a "real annotated diagram." I chose a 280px SVG ring rendered
directly in HTML with three positioned CSS callout labels and hairline connector
pseudo-elements, rather than an image export or a canvas draw. The ring values
are set to 60% fill with the pace dot at the 45% position — a scenario where the
user is visibly ahead of even consumption, which makes the concept legible at a
glance without any copy.

Trade-off: the connector lines are CSS `::before` pseudo-elements with fixed
offsets, so they're not mathematically precise to the SVG arc endpoints. They
read as diagram callouts without being technically precise geometry. At the sizes
this renders (280px wide), the visual relationship is unambiguous. If Round 3
raises this as a concern, the fix is SVG `<line>` elements from specific arc
coordinates — possible but adds complexity.

### 2. Desktop frame: dark gradient background, not a realistic screenshot crop

The brief offered two options: (a) faux macOS desktop surface, (b) widget-grid
fallback. I went with (a) but interpreted it as a stylized dark-gradient surface
with a radial glow rather than a literal macOS wallpaper screenshot. Reasons:

- A real macOS wallpaper screenshot would feel dated immediately (Apple changes
  them every major release) and creates a licensing edge case.
- The dark gradient is derived from `--widget-dark` and `--ink-900`, keeping the
  product and marketing surface in the same color language.
- The `::after` dock-peek hairline at the bottom gives enough environmental
  context to read as "this is a desktop" without literal realism.

The large widget inside the frame uses `grid-column: span 2` which keeps the
existing widget system intact — no custom sizing.

### 3. Small widget on narrow screens: hide below 360px

The open question was (a) hide small widget below 360px or (b) use container
queries to adjust. I chose (a): `display: none` at `max-width: 359px`. Rationale:
the small widget is an SVG whose text is rendered at `12.5` font units inside a
100×100 viewBox scaled to ~160px wide in the providers section. Below 360px
that's around 20px rendered, which is readable. But the widget's primary role on
the landing page is to show the dual-ring visual — the medium widgets carry the
full usage story. Hiding on sub-360 keeps the layout clean without a container
query polyfill concern.

Container queries are supported everywhere that matters for this audience, but
the added CSS complexity for a 160px widget on a 320px phone is not worth it when
the content is already represented elsewhere on the same page.

---

## One thing to validate in Round 3

**The install section layout breaks on 800–900px viewport width.**

The install section uses a two-column grid (install block + install art image).
At ~850px the art image gets pushed outside the readable column width and starts
fighting the install panel. Test this width range specifically — the fix is either
hiding the install art at `max-width: 900px` or switching to a single column
earlier. I've left it unresolved because it needs a real browser render to confirm
the exact breakpoint.
