# FAQ + /support page — planning notes

Captured 2026-05-14, after shipping the Chrome extension (Phase 1.5 + 4.5)
which surfaces provider-native units in the popup that some users won't
immediately recognize ("Fast Hours," "Thinking messages," "5-Hour Window").

The popup is intentionally terse — when a user wonders *"wait, what's that
number?"* they need somewhere on the site to land. These notes capture
what to put there and why, not the final copy.

---

## IA decision (still open)

Two options:

1. **`/faq.html`** — a single scannable page with anchored sections.
   Pro: one URL, easy to deep-link from the extension popup (e.g.,
   `?#fast-hours`). Con: gets long.
2. **`/support.html`** with FAQ as one section, "Troubleshooting" as
   another, "Contact" at the bottom.
   Pro: room for a real support flow later. Con: forces a fork in IA
   we don't need yet.

**Recommendation:** ship `/faq.html` first; promote to `/support.html`
when there's enough non-FAQ content (status page link, contact form,
known-issues feed) to justify a section split. Until then, "FAQ" *is*
the support surface.

---

## Provider-native units — explainers

These are the items the extension popup will (eventually) deep-link to.
Each entry below is a draft outline, not finished copy.

### Midjourney "Fast Hours"

Midjourney bills generation time in **credits**. Each Fast minute of GPU
time consumes 60,000 credits. The plans:

| Plan      | Credits / month | Fast Hours |
|-----------|----------------:|-----------:|
| Basic     |     12,000,000  |       3.3h |
| Standard  |     54,000,000  |        15h |
| Pro       |    108,000,000  |        30h |
| Mega      |    216,000,000  |        60h |

Tokenomics shows your current period's usage against this allocation.

**If you see "No plan" / 0%:** your Midjourney account is on trial or has
no active subscription. The bar will populate once you subscribe.

**If you see Fast Hours but the count looks wrong:** Midjourney's billing
cycle and Tokenomics' 30-day fallback may be slightly out of sync. The
extension uses the renewal timestamp from your account when present; when
it's absent, it approximates from your account's last-updated date.

---

### Claude — "5-Hour Window" + "7-Day Window"

These are Anthropic's own quota windows, not Tokenomics' invention:

- **5-Hour Window** — the rolling cap that resets after a 5-hour idle.
  Most users hit this first. If you see 80% with 2h left, you're about
  to be rate-limited; pace your prompts.
- **7-Day Window** — the longer cap. Resets every 7 days from your
  first message in the current cycle.

Pro users also see an **Opus** sub-counter inside the 7-day window —
that's because Opus has its own weekly cap on top of the 7-day total.

---

### ChatGPT — "Thinking messages" + the `estimated` indicator

Two things to explain:

1. **Thinking messages**. On Plus, Pro, and Team plans, "thinking" models
   (o-series, GPT-5 Thinking) have a separate weekly cap on top of the
   3-hour rolling window. Tokenomics shows both bars.
2. **The `estimated` indicator**. OpenAI doesn't expose a usage endpoint
   to the web client — there's no real-time number for the extension to
   read. So Tokenomics counts messages locally as you chat in this
   browser. Messages sent from your phone, another browser, or the
   ChatGPT desktop app don't count.

This is honest framing — every shipping ChatGPT-usage tracker has the
same constraint. The `estimated` indicator makes it explicit.

---

## Likely additional FAQs

Not yet drafted; placeholders so we don't forget:

- **"Is my data sent anywhere?"** — No telemetry, no analytics, no remote
  reporting. All data stays on your machine. Link to `/privacy.html` for
  the full statement.
- **"How does sign-in work?"** — Cookie-based; the extension makes
  authenticated fetches to claude.ai / midjourney.com using your own
  browser session. No tokens are extracted, no API keys are required.
- **"Why doesn't my ChatGPT count include messages from my phone?"** —
  See "estimated" above.
- **"Does Tokenomics work in Safari?"** — Not yet; Chrome only for now.
  Safari is on the roadmap.
- **"Does it support Firefox?"** — Not yet; later phase.
- **"Will it support Gemini?"** — Deferred until Google ships their own
  in-product usage view (per their May 2026 APK teardown signals).
- **"How do I uninstall?"** — Standard Chrome extension removal +
  optional Mac app uninstall (drag from /Applications + Sparkle leftover
  cleanup note).

---

## Copy voice

Match the existing landing pages:
- **Editorial, not breezy.** No "Hey there 👋" headers.
- **Direct.** "If you see X, that means Y" beats "You might be wondering
  why X is happening."
- **Honest about limitations.** The `estimated` framing is the model —
  don't paper over caveats, name them and move on.

---

## Deep-linking from the extension (later)

Once the page exists with anchored sections, the extension popup can link
to specific explainers — e.g., the `estimated` indicator could open
`https://trytokenomics.com/faq.html#chatgpt-estimated` in a new tab.

Until then, the popup carries no such links; we don't want dead anchors
in a shipped UI.
