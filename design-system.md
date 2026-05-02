# Tokenomics Design System

> **Source of truth for both the macOS app (SwiftUI) and the website (HTML/CSS).**
>
> This document mirrors `design-system-v3.html` 1:1. Every value here ships in
> production. Visual demos live in `design-system-v3.html` — open it in a
> browser when you need to see a component rendered.
>
> **For Swift implementers:** This system is opinionated. Don't fall back to
> Apple's defaults — the app and the website must feel like the same product,
> and that requires explicit values. See [Anti-patterns](#anti-patterns-swift)
> below for what to avoid.

---

## Table of contents

1. [Anti-patterns (Swift)](#anti-patterns-swift)
2. [Quick start: Tokens.swift](#quick-start-tokensswift)
3. [Quick start: CSS variables](#quick-start-css-variables)
4. [Foundations](#01-foundations)
5. [Color](#02-color)
6. [Typography](#03-typography)
7. [Space & Radius](#04-space--radius)
8. [Shadow & Motion](#05-shadow--motion)
9. [Components](#06-components)
10. [Widgets (canonical)](#07-widgets-canonical)
11. [App-only components](#08-app-only-components)
12. [Web-only components](#09-web-only-components)
13. [Token reference](#10-token-reference)
14. [Regression tests](#11-regression-tests)

---

## Anti-patterns (Swift)

The single biggest failure mode for the Swift app is silently inheriting Apple's
defaults. **Do not** use these:

| Don't use | Why | Use instead |
|---|---|---|
| `Color.accentColor` | Pulls macOS system blue | `Tokens.Color.brand600` (light) / `.brand200` (dark) |
| `Color.primary` / `.secondary` | macOS dynamic gray | `Tokens.Color.text` / `.textMuted` |
| `Color(.systemBackground)` | macOS off-white | `Tokens.Color.bg` (cream-50) |
| `Color(.controlBackgroundColor)` | macOS gray | `Tokens.Color.surface` (white) |
| `.font(.body)` / `.title` / `.headline` | macOS dynamic type | `.system(size: 16, weight: .regular)` etc. |
| `.padding()` (no argument) | 16pt default — wrong for design system | `.padding(Tokens.Spacing.s4)` (16pt explicit) |
| `Toggle` (default style) | Apple chrome | Custom toggle (see [iOS toggle](#ios-toggle)) |
| `Button` (default style) | Apple gray rounded button | Custom button modifier (see [Buttons](#buttons)) |
| `RoundedRectangle(cornerRadius: 8)` | Magic number | `Tokens.Radius.sm` (10pt) |
| `Color.green` / `.red` / `.yellow` | Apple system | `Tokens.Color.success/danger/warning` |

**Rule of thumb:** if you're typing a system color, system font, or naked
number, stop and replace it with a token.

---

## Quick start: Tokens.swift

Drop this file into the app target. Every other file in the app should
reference these tokens — never hex literals or magic numbers.

**Two ways to consume theme-aware colors** (pick one per view, both are valid):

1. **`Tokens.Color.text(scheme)`** — explicit `ColorScheme` argument. Safer, type-checked at compile time. Requires `@Environment(\.colorScheme) var scheme` in the view.
2. **`Tokens.DynamicColor.text`** — auto-flips via dynamic `NSColor`. Cleaner view code. Resolves at draw time. macOS-only (uses AppKit).

For raw brand colors that should *never* flip with theme (widget icons, ring fills tied to a specific WidgetTheme), use the constants directly: `Tokens.Color.brand600`, `Tokens.Color.cream100`, etc.

```swift
import SwiftUI

enum Tokens {
    // MARK: - Color

    enum Color {
        // Ink (navy ramp)
        static let ink900 = SwiftUI.Color(red: 5/255,   green: 25/255,  blue: 40/255)   // #051928
        static let ink800 = SwiftUI.Color(red: 14/255,  green: 51/255,  blue: 77/255)   // #0E334D
        static let ink700 = SwiftUI.Color(red: 40/255,  green: 97/255,  blue: 149/255)  // #286195

        // Brand (blue ramp — short bar / ring fills, accents)
        static let brand600 = SwiftUI.Color(red: 47/255,  green: 132/255, blue: 191/255) // #2F84BF
        static let brand500 = SwiftUI.Color(red: 51/255,  green: 137/255, blue: 199/255) // #3389C7
        static let brand400 = SwiftUI.Color(red: 75/255,  green: 166/255, blue: 210/255) // #4BA6D2
        static let brand300 = SwiftUI.Color(red: 86/255,  green: 162/255, blue: 214/255) // #56A2D6
        static let brand200 = SwiftUI.Color(red: 117/255, green: 203/255, blue: 245/255) // #75CBF5

        // Cream (paper ramp)
        static let cream50  = SwiftUI.Color(red: 243/255, green: 239/255, blue: 229/255) // #F3EFE5
        static let cream100 = SwiftUI.Color(red: 230/255, green: 224/255, blue: 212/255) // #E6E0D4
        static let cream200 = SwiftUI.Color(red: 217/255, green: 209/255, blue: 192/255) // #D9D1C0

        static let white = SwiftUI.Color.white

        // Semantic — light theme
        static let successLight = SwiftUI.Color(red: 47/255,  green: 143/255, blue: 79/255)  // #2F8F4F
        static let warningLight = SwiftUI.Color(red: 194/255, green: 106/255, blue: 31/255)  // #C26A1F  (burnt amber, not yellow)
        static let dangerLight  = SwiftUI.Color(red: 179/255, green: 58/255,  blue: 58/255)  // #B33A3A

        // Semantic — dark theme
        static let successDark  = SwiftUI.Color(red: 111/255, green: 209/255, blue: 138/255) // #6FD18A
        static let warningDark  = SwiftUI.Color(red: 226/255, green: 167/255, blue: 101/255) // #E2A765
        static let dangerDark   = SwiftUI.Color(red: 226/255, green: 119/255, blue: 119/255) // #E27777

        // Light-theme raw values — used as the input to the theme-resolved
        // accessors below. View code should NOT reference these directly.
        fileprivate static let _textLight         = ink800                                                              // #0E334D
        fileprivate static let _textMutedLight    = ink800.opacity(0.64)
        fileprivate static let _textSubtleLight   = ink800.opacity(0.44)
        fileprivate static let _bgLight           = cream50                                                             // #F3EFE5
        fileprivate static let _bg2Light          = cream100                                                            // #E6E0D4
        fileprivate static let _surfaceLight      = SwiftUI.Color.white                                                 // #FFFFFF
        fileprivate static let _surface2Light     = SwiftUI.Color(red: 251/255, green: 248/255, blue: 241/255)          // #FBF8F1
        fileprivate static let _borderLight       = ink800.opacity(0.12)
        fileprivate static let _borderStrongLight = ink800.opacity(0.22)
        fileprivate static let _accentLight       = brand600                                                            // #2F84BF
        fileprivate static let _accentInkLight    = ink800                                                              // #0E334D

        // Dark-theme raw values
        fileprivate static let _textDark          = SwiftUI.Color(red: 230/255, green: 238/255, blue: 246/255)          // #E6EEF6
        fileprivate static let _textMutedDark     = SwiftUI.Color(red: 230/255, green: 238/255, blue: 246/255).opacity(0.68)
        fileprivate static let _textSubtleDark    = SwiftUI.Color(red: 230/255, green: 238/255, blue: 246/255).opacity(0.44)
        fileprivate static let _bgDark            = SwiftUI.Color(red: 7/255,   green: 16/255,  blue: 26/255)           // #07101a
        fileprivate static let _bg2Dark           = SwiftUI.Color(red: 11/255,  green: 26/255,  blue: 41/255)           // #0b1a29
        fileprivate static let _surfaceDark       = ink800                                                              // #0E334D
        fileprivate static let _surface2Dark      = SwiftUI.Color(red: 10/255,  green: 36/255,  blue: 57/255)           // #0a2439
        fileprivate static let _borderDark        = SwiftUI.Color.white.opacity(0.10)
        fileprivate static let _borderStrongDark  = SwiftUI.Color.white.opacity(0.22)
        fileprivate static let _accentDark        = brand200                                                            // #75CBF5
        fileprivate static let _accentInkDark     = _textDark                                                           // mirrors --text in dark

        // ─────────────────────────────────────────────────────────────────
        // PUBLIC THEME-RESOLVED ACCESSORS
        // Always pass `colorScheme` from the view's environment.
        //
        // Usage:
        //   @Environment(\.colorScheme) var scheme
        //   .foregroundStyle(Tokens.Color.text(scheme))
        //
        // For static surfaces that should never flip (e.g. widget icons that
        // are always white on the dark widget gradient), use the raw `cream*`
        // / `brand*` / `ink*` constants directly.
        // ─────────────────────────────────────────────────────────────────

        // Surfaces
        static func bg(_ scheme: ColorScheme) -> SwiftUI.Color {
            scheme == .dark ? _bgDark : _bgLight
        }
        static func bg2(_ scheme: ColorScheme) -> SwiftUI.Color {
            scheme == .dark ? _bg2Dark : _bg2Light
        }
        static func surface(_ scheme: ColorScheme) -> SwiftUI.Color {
            scheme == .dark ? _surfaceDark : _surfaceLight
        }
        /// Hover surface — unified across all hovers (button-secondary, copy, in-field, etc.)
        static func surface2(_ scheme: ColorScheme) -> SwiftUI.Color {
            scheme == .dark ? _surface2Dark : _surface2Light
        }

        // Text
        static func text(_ scheme: ColorScheme) -> SwiftUI.Color {
            scheme == .dark ? _textDark : _textLight
        }
        static func textMuted(_ scheme: ColorScheme) -> SwiftUI.Color {
            scheme == .dark ? _textMutedDark : _textMutedLight
        }
        static func textSubtle(_ scheme: ColorScheme) -> SwiftUI.Color {
            scheme == .dark ? _textSubtleDark : _textSubtleLight
        }

        // Borders
        static func border(_ scheme: ColorScheme) -> SwiftUI.Color {
            scheme == .dark ? _borderDark : _borderLight
        }
        static func borderStrong(_ scheme: ColorScheme) -> SwiftUI.Color {
            scheme == .dark ? _borderStrongDark : _borderStrongLight
        }

        // Accent — flips brand-600 (light) ↔ brand-200 (dark)
        static func accent(_ scheme: ColorScheme) -> SwiftUI.Color {
            scheme == .dark ? _accentDark : _accentLight
        }
        /// Used for the Primary button's *fill*. Light mode = ink-800 (navy on cream).
        /// Dark mode = brand-200 (cyan on navy).
        static func accentInk(_ scheme: ColorScheme) -> SwiftUI.Color {
            scheme == .dark ? _accentInkDark : _accentInkLight
        }

        // Semantic
        static func success(_ scheme: ColorScheme) -> SwiftUI.Color {
            scheme == .dark ? successDark : successLight
        }
        static func warning(_ scheme: ColorScheme) -> SwiftUI.Color {
            scheme == .dark ? warningDark : warningLight
        }
        static func danger(_ scheme: ColorScheme) -> SwiftUI.Color {
            scheme == .dark ? dangerDark : dangerLight
        }
    }

    // MARK: - Dynamic NSColor convenience (optional)
    //
    // The accessor pattern above (`Tokens.Color.text(scheme)`) is explicit and
    // type-safe but means every view body needs `@Environment(\.colorScheme)`.
    //
    // If you'd rather have tokens that auto-flip without threading scheme
    // through, use these dynamic NSColors. They resolve at draw time based on
    // the effective appearance of the host view. Safe for any AppKit-backed
    // SwiftUI hierarchy on macOS.

    enum DynamicColor {
        static let text         = dynamic(light: Tokens.Color._textLight,         dark: Tokens.Color._textDark)
        static let textMuted    = dynamic(light: Tokens.Color._textMutedLight,    dark: Tokens.Color._textMutedDark)
        static let textSubtle   = dynamic(light: Tokens.Color._textSubtleLight,   dark: Tokens.Color._textSubtleDark)
        static let bg           = dynamic(light: Tokens.Color._bgLight,           dark: Tokens.Color._bgDark)
        static let bg2          = dynamic(light: Tokens.Color._bg2Light,          dark: Tokens.Color._bg2Dark)
        static let surface      = dynamic(light: Tokens.Color._surfaceLight,      dark: Tokens.Color._surfaceDark)
        static let surface2     = dynamic(light: Tokens.Color._surface2Light,     dark: Tokens.Color._surface2Dark)
        static let border       = dynamic(light: Tokens.Color._borderLight,       dark: Tokens.Color._borderDark)
        static let borderStrong = dynamic(light: Tokens.Color._borderStrongLight, dark: Tokens.Color._borderStrongDark)
        static let accent       = dynamic(light: Tokens.Color._accentLight,       dark: Tokens.Color._accentDark)
        static let accentInk    = dynamic(light: Tokens.Color._accentInkLight,    dark: Tokens.Color._accentInkDark)
        static let success      = dynamic(light: Tokens.Color.successLight,       dark: Tokens.Color.successDark)
        static let warning      = dynamic(light: Tokens.Color.warningLight,       dark: Tokens.Color.warningDark)
        static let danger       = dynamic(light: Tokens.Color.dangerLight,        dark: Tokens.Color.dangerDark)

        private static func dynamic(light: SwiftUI.Color, dark: SwiftUI.Color) -> SwiftUI.Color {
            #if canImport(AppKit)
            return SwiftUI.Color(nsColor: NSColor(name: nil) { appearance in
                let isDark = appearance.bestMatch(from: [.darkAqua, .vibrantDark]) != nil
                return NSColor(isDark ? dark : light)
            })
            #else
            return light
            #endif
        }
    }

    // MARK: - Spacing (8pt grid)

    enum Spacing {
        static let s1: CGFloat = 4
        static let s2: CGFloat = 8
        static let s3: CGFloat = 12
        static let s4: CGFloat = 16
        static let s5: CGFloat = 24
        static let s6: CGFloat = 32
        static let s7: CGFloat = 48
        static let s8: CGFloat = 64
        static let s9: CGFloat = 96
    }

    // MARK: - Radius

    enum Radius {
        static let xs: CGFloat = 6     // buttons-in-field
        static let sm: CGFloat = 10    // small chips, inputs
        static let md: CGFloat = 14    // cards, install-block, FAQ items
        static let lg: CGFloat = 20    // section cards, principle blocks
        static let xl: CGFloat = 28    // hero / featured surfaces
        static let pill: CGFloat = 999 // pills, capsule progress bars
    }

    // MARK: - Typography

    /// SF Pro is the system font on macOS. Use `.system(...)` always — never
    /// `.body`, `.title`, etc. (those pull dynamic type and break design intent).
    enum Typography {
        // Display & headers (rarely used in the app — these are website territory.
        // Included only for parity with website style guide.)
        static let h1 = SwiftUI.Font.system(size: 28, weight: .semibold).leading(.tight)
        static let h2 = SwiftUI.Font.system(size: 22, weight: .semibold).leading(.tight)
        static let h3 = SwiftUI.Font.system(size: 18, weight: .semibold).leading(.tight)

        // Body & UI
        static let bodyLg = SwiftUI.Font.system(size: 17, weight: .regular)
        static let body   = SwiftUI.Font.system(size: 15, weight: .regular)
        static let small  = SwiftUI.Font.system(size: 13, weight: .regular)
        static let micro  = SwiftUI.Font.system(size: 11, weight: .medium)

        // Widget-specific (matches WidgetKit caption sizes)
        static let widgetCaption  = SwiftUI.Font.caption.weight(.semibold)   // 12pt semibold
        static let widgetCaption2 = SwiftUI.Font.caption2                    // 11pt regular
        static let widgetTiny     = SwiftUI.Font.system(size: 9)             // labels in compact rows

        // Numeric formatter — apply via `.monospacedDigit()` or
        // `.fontDesign(.default).monospacedDigit()` on any percentage display.
    }

    // MARK: - Motion

    enum Motion {
        static let fast: Double = 0.12     // hover states
        static let standard: Double = 0.22 // default
        static let slow: Double = 0.42     // scroll-enter, card reveals

        // Default ease — matches CSS cubic-bezier(.2,.7,.2,1)
        static let ease = Animation.timingCurve(0.2, 0.7, 0.2, 1, duration: standard)
    }
}
```

---

## Quick start: CSS variables

Drop this into `:root` of your stylesheet. Mirrors `Tokens.swift` exactly.

```css
:root {
  /* Brand */
  --ink-900: #051928;
  --ink-800: #0E334D;
  --ink-700: #286195;
  --brand-600: #2F84BF;
  --brand-500: #3389C7;
  --brand-400: #4BA6D2;
  --brand-300: #56A2D6;
  --brand-200: #75CBF5;
  --cream-50:  #F3EFE5;
  --cream-100: #E6E0D4;
  --cream-200: #D9D1C0;
  --white: #FFFFFF;

  /* Semantic — light theme */
  --bg:        var(--cream-50);
  --bg-2:      var(--cream-100);
  --surface:   #FFFFFF;
  --surface-2: #FBF8F1;
  --border:    rgba(14,51,77,0.12);
  --border-strong: rgba(14,51,77,0.22);
  --text:      #0E334D;
  --text-muted: rgba(14,51,77,0.64);
  --text-subtle: rgba(14,51,77,0.44);
  --accent:    #2F84BF;
  --accent-ink: #0E334D;
  --success:   #2F8F4F;
  --warning:   #C26A1F;
  --danger:    #B33A3A;

  /* Type */
  --font-serif: 'Hedvig Letters Serif', 'Iowan Old Style', Georgia, serif;
  --font-sans:  'DM Sans', system-ui, -apple-system, 'Helvetica Neue', sans-serif;
  --font-mono:  ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace;

  --fs-display: clamp(48px, 6.4vw, 88px);
  --fs-h1: clamp(36px, 4.4vw, 56px);
  --fs-h2: clamp(28px, 3.2vw, 40px);
  --fs-h3: clamp(22px, 2.2vw, 28px);
  --fs-h4: 20px;
  --fs-body-lg: 18px;
  --fs-body: 16px;
  --fs-small: 14px;
  --fs-micro: 12px;

  /* Spacing (8pt) */
  --s-1: 4px;  --s-2: 8px;  --s-3: 12px; --s-4: 16px;
  --s-5: 24px; --s-6: 32px; --s-7: 48px; --s-8: 64px; --s-9: 96px;

  /* Radius */
  --r-xs: 6px;  --r-sm: 10px; --r-md: 14px;
  --r-lg: 20px; --r-xl: 28px; --r-pill: 999px;

  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(14,51,77,0.06), 0 1px 1px rgba(14,51,77,0.04);
  --shadow-md: 0 8px 24px rgba(14,51,77,0.10), 0 2px 6px rgba(14,51,77,0.06);
  --shadow-lg: 0 28px 60px rgba(14,51,77,0.10), 0 8px 18px rgba(14,51,77,0.05);
  --shadow-ring: 0 0 0 4px rgba(47,132,191,0.18);

  /* Motion */
  --ease: cubic-bezier(.2,.7,.2,1);
  --dur-fast: 120ms;
  --dur: 220ms;
  --dur-slow: 420ms;

  /* Widget gradients */
  --widget-light: linear-gradient(135deg, #F3EFE5 1.6%, #E6E0D4 84.5%);
  --widget-dark:  linear-gradient(135deg, #0E334D 10.3%, #051928 88.1%);
}

[data-theme="dark"] {
  --bg:        #07101a;
  --bg-2:      #0b1a29;
  --surface:   #0E334D;
  --surface-2: #0a2439;
  --border:    rgba(255,255,255,0.10);
  --border-strong: rgba(255,255,255,0.22);
  --text:      #E6EEF6;
  --text-muted: rgba(230,238,246,0.68);
  --text-subtle: rgba(230,238,246,0.44);
  --accent:    #75CBF5;
  --accent-ink: #E6EEF6;
  --success:   #6FD18A;
  --warning:   #E2A765;
  --danger:    #E27777;
}
```

---

## 01. Foundations

Three principles drive everything below.

1. **Calm, not clever.** Voice and motion should never compete with the data.
2. **The product is the proof.** Lead with screenshots, not slogans.
3. **Serif for soul, sans for signal.** Hedvig serif for headlines and pull-quotes. DM Sans for UI/body. SF Pro for the app itself and widgets.

---

## 02. Color

### Brand palette

| Name | Hex | Swift token | CSS variable | Usage |
|---|---|---|---|---|
| Ink 900 | `#051928` | `Tokens.Color.ink900` | `--ink-900` | Deepest navy · widget gradient end |
| Ink 800 | `#0E334D` | `Tokens.Color.ink800` | `--ink-800` | Primary ink · widget gradient start · `--text` (light) |
| Ink 700 | `#286195` | `Tokens.Color.ink700` | `--ink-700` | Bar track base (light dial) |
| Brand 600 | `#2F84BF` | `Tokens.Color.brand600` | `--brand-600` | Short bar / labels (light) · `--accent` (light) |
| Brand 500 | `#3389C7` | `Tokens.Color.brand500` | `--brand-500` | Long bar (dark) |
| Brand 400 | `#4BA6D2` | `Tokens.Color.brand400` | `--brand-400` | Bar track base (dark) |
| Brand 300 | `#56A2D6` | `Tokens.Color.brand300` | `--brand-300` | Long bar (light) |
| Brand 200 | `#75CBF5` | `Tokens.Color.brand200` | `--brand-200` | Short bar / labels (dark) · `--accent` (dark) |
| Cream 50 | `#F3EFE5` | `Tokens.Color.cream50` | `--cream-50` | Page bg (light) · widget gradient start |
| Cream 100 | `#E6E0D4` | `Tokens.Color.cream100` | `--cream-100` | Secondary surface · widget gradient end |
| Cream 200 | `#D9D1C0` | `Tokens.Color.cream200` | `--cream-200` | Reserved (deep cream) — not used in current UI |
| White | `#FFFFFF` | `Tokens.Color.white` | `--white` | Surface (light) · widget icons (dark) |

### Semantic colors

| Name | Light | Dark | Usage |
|---|---|---|---|
| Success | `#2F8F4F` | `#6FD18A` | "Connected" badges · done-check · OK icons |
| Warning | `#C26A1F` | `#E2A765` | Soft alerts (burnt amber, **not yellow**) |
| Danger | `#B33A3A` | `#E27777` | Errors · failed steps · destructive actions |

**On warning (the not-yellow):** True yellow on cream washes out and breaks the editorial calm. The amber preserves the universal "caution" semantic while harmonizing with navy/cream. If you need a more saturated yellow some day, test `#A87B14` (deep mustard, light) and `#D9B463` (warm gold, dark).

### Theme tokens (light)

| Token | Hex | Swift | Notes |
|---|---|---|---|
| `--bg` | `#F3EFE5` | `Tokens.Color.bg` (= cream50) | Page background |
| `--bg-2` | `#E6E0D4` | `Tokens.Color.bg2` (= cream100) | Secondary background |
| `--surface` | `#FFFFFF` | `Tokens.Color.surface` | Card / panel fills |
| `--surface-2` | `#FBF8F1` | `Tokens.Color.surface2` | **Hover surface** (off-white tint) |
| `--text` | `#0E334D` | `Tokens.Color.text` | Body / headline text |
| `--text-muted` | `rgba(14,51,77,0.64)` | `.text.opacity(0.64)` or `Tokens.Color.textMuted` | Secondary text |
| `--text-subtle` | `rgba(14,51,77,0.44)` | `Tokens.Color.textSubtle` | Captions / placeholders |
| `--border` | `rgba(14,51,77,0.12)` | `Tokens.Color.border` | Card borders, dividers |
| `--border-strong` | `rgba(14,51,77,0.22)` | `Tokens.Color.borderStrong` | Inputs, button outlines |

### Theme tokens (dark) — `[data-theme="dark"]`

| Token | Hex | Notes |
|---|---|---|
| `--bg` | `#07101a` | Dark mode page bg |
| `--bg-2` | `#0b1a29` | Dark mode secondary bg |
| `--surface` | `#0E334D` | Dark mode cards (uses ink-800) |
| `--surface-2` | `#0a2439` | Dark mode hover surface |
| `--text` | `#E6EEF6` | Dark mode text |
| `--text-muted` | `rgba(230,238,246,0.68)` | |
| `--text-subtle` | `rgba(230,238,246,0.44)` | |
| `--border` | `rgba(255,255,255,0.10)` | |
| `--border-strong` | `rgba(255,255,255,0.22)` | |

### Widget palette (per `WidgetTheme`)

The widget theme structure in Swift is the source of truth for widget colors. Mirrors `TokenomicsWidgetEntryView.swift`:

```swift
struct WidgetTheme {
    let labelColor: Color       // labels, secondary text
    let shortColor: Color       // short-window bars / outer ring fill
    let longColor: Color        // long-window bars / inner ring fill
    let barTrack: Color         // bar / ring track
    let backgroundStops: [Gradient.Stop]
    let paceDotColor: Color
}

extension WidgetTheme {
    static let dark = WidgetTheme(
        labelColor: Color(red: 117/255, green: 203/255, blue: 245/255).opacity(0.5),  // brand200 @ 50%
        shortColor: Color(red: 117/255, green: 203/255, blue: 245/255),                // brand200
        longColor:  Color(red: 51/255,  green: 137/255, blue: 199/255),                // brand500
        barTrack:   Color(red: 75/255,  green: 166/255, blue: 210/255).opacity(0.25),  // brand400 @ 25%
        backgroundStops: [
            .init(color: Color(red: 14/255, green: 51/255, blue: 77/255), location: 0.103), // ink800
            .init(color: Color(red: 5/255,  green: 25/255, blue: 40/255), location: 0.881)  // ink900
        ],
        paceDotColor: .white
    )

    static let light = WidgetTheme(
        labelColor: Color(red: 47/255, green: 132/255, blue: 191/255).opacity(0.67),   // brand600 @ 67%
        shortColor: Color(red: 47/255, green: 132/255, blue: 191/255),                 // brand600
        longColor:  Color(red: 86/255, green: 162/255, blue: 214/255),                 // brand300
        barTrack:   Color(red: 40/255, green: 97/255,  blue: 149/255).opacity(0.12),   // ink700 @ 12%
        backgroundStops: [
            .init(color: Color(red: 243/255, green: 239/255, blue: 229/255), location: 0.016), // cream50
            .init(color: Color(red: 230/255, green: 224/255, blue: 212/255), location: 0.845)  // cream100
        ],
        paceDotColor: Color(red: 14/255, green: 51/255, blue: 77/255)                  // ink800
    )
}
```

### Widget gradient direction

- **Swift**: `LinearGradient(stops: theme.backgroundStops, startPoint: UnitPoint(x: 0.35, y: 0), endPoint: UnitPoint(x: 0.65, y: 1))`
- **CSS**: `linear-gradient(135deg, [stops])` — light at top-left → dark at bottom-right

---

## 03. Typography

### Font stacks per surface

The app has **two type systems** depending on the surface. This is intentional — the onboarding flow is meant to feel like the website (editorial, warm, on-brand), while the steady-state app surfaces (popover, settings, widgets) feel like the OS (calm, native, predictable).

| Surface | Fonts | Notes |
|---|---|---|
| **Website** (`trytokenomics.com`) | Hedvig Letters Serif (display/H1–H4) + DM Sans (UI/body) | Bundled fonts |
| **App · Onboarding wizard** | Hedvig Letters Serif (H1) + DM Sans (UI/body) | **Bundle these in the app target.** Match website voice. Mirrors `docs/guided-onboarding-mockup.html`. |
| **App · Popover** (menu-bar dropdown) | SF Pro (system) | Use `.system(...)` — never `.body`/`.title`/etc. |
| **App · Settings** | SF Pro (system) | Same as popover |
| **App · Widgets** | SF Pro Text (system) | `.font(.caption)`, `.font(.caption2)`, `.system(size: 9)` |

**Quick decision rule:** if the user is in *guided onboarding flow* (window with stepper, "OpenAI is connected." headline, etc.), use Hedvig + DM Sans. If they're in the menu-bar popover, settings panel, or looking at a widget, use SF Pro.

**Why the split?** Onboarding is a curated, voice-bearing experience — the serif headline is what makes it feel un-system. Steady-state app UI shouldn't compete with macOS chrome and shouldn't pay the bundling cost on every screen. SF Pro reads as quiet, native, trustworthy.

> **For the Swift session:** Yes, keep DM Sans bundled — it's needed for the onboarding wizard. Drop it from any non-onboarding view.

### Type scale (web)

| Token | Size | Weight | Line height | Letter spacing | Usage |
|---|---|---|---|---|---|
| `--fs-display` | `clamp(48px, 6.4vw, 88px)` | 400 (Hedvig) | 0.98 | -0.022em | Hero |
| `--fs-h1` | `clamp(36px, 4.4vw, 56px)` | 400 (Hedvig) | 1.08 | -0.018em | Section heads |
| `--fs-h2` | `clamp(28px, 3.2vw, 40px)` | 400 (Hedvig) | 1.1 | -0.01em | Subsection |
| `--fs-h3` | `clamp(22px, 2.2vw, 28px)` | 400 (Hedvig) | 1.2 | 0 | Card titles |
| `--fs-h4` | 20px | 600 (DM Sans) | 1.2 | 0 | Component titles |
| `--fs-body-lg` | 18px | 400 (DM Sans) | 1.55 | 0 | Lede |
| `--fs-body` | 16px | 400 (DM Sans) | 1.55 | 0 | Body |
| `--fs-small` | 14px | 400 (DM Sans) | 1.5 | 0 | Supporting |
| `--fs-micro` | 12px | 500 (DM Sans) | 1.4 | 0.02em | Eyebrow / labels |

### Type scale (app · onboarding wizard) — Hedvig + DM Sans

These styles only apply inside the onboarding flow (window with stepper). Headlines are **serif (Hedvig)**, all body and UI is **sans (DM Sans)**.

| Style | Font | Swift | Usage |
|---|---|---|---|
| Onboarding H1 | Hedvig 400 | `.custom("HedvigLettersSerif-Regular", size: 30)` | "OpenAI is connected." |
| Onboarding H2 | DM Sans 600 | `.custom("DMSans-SemiBold", size: 22)` | "Couldn't install the Codex CLI" |
| Onboarding H3 | DM Sans 600 | `.custom("DMSans-SemiBold", size: 17)` | Inline section heads |
| Lede | DM Sans 400 | `.custom("DMSans-Regular", size: 15)` | Subheadline body |
| Body | DM Sans 400 | `.custom("DMSans-Regular", size: 14)` | Default body |
| Small | DM Sans 400 | `.custom("DMSans-Regular", size: 13)` | Captions |
| Micro | DM Sans 500 | `.custom("DMSans-Medium", size: 11)` | Step labels, eyebrow |
| Stepper number | DM Sans 600 | `.custom("DMSans-SemiBold", size: 11)` | Inside `.step-mark` |
| Window title (titlebar) | DM Sans 500 | `.custom("DMSans-Medium", size: 13)` | Centered titlebar text |

If a custom font fails to load (e.g. the bundle didn't ship correctly), SwiftUI falls back to the system font — which is acceptable degradation, not a crash.

### Type scale (app · popover, settings, native UI) — SF Pro

Steady-state app surfaces use the system font. **Never use `.body` / `.title` / `.headline`** — those pull macOS dynamic type and break design intent.

| Style | Swift | Usage |
|---|---|---|
| Section title | `.system(size: 14, weight: .semibold)` | Popover section headers |
| Body | `.system(size: 13, weight: .regular)` | Most popover/settings text |
| Caption | `.system(size: 12, weight: .medium)` | Status text, labels |
| Tiny | `.system(size: 11, weight: .regular)` | Provider scopes, "Updated just now" |
| Micro | `.system(size: 10.5, weight: .semibold)` | UPPERCASE section labels (popover) |

### Type scale (widget)

Pulled directly from `TokenomicsWidgetEntryView.swift`:

| Element | SwiftUI |
|---|---|
| "Tokenomics" header | `.font(.caption).fontWeight(.semibold)` (12pt semibold) |
| Relative time ("30 sec ago") | `.font(.caption2)` (11pt) |
| Provider name (large row) | `.font(.caption).fontWeight(.medium)` (12pt medium @ 0.85 opacity) |
| Plan label (large row) | `.font(.caption2)` (11pt @ labelColor) |
| Bar-row label | `.font(.system(size: 9))` |
| Bar-row percentage | `.font(.caption2).fontWeight(.medium)` (11pt medium) |
| Compact label | `.font(.system(size: 9))` |
| Compact percentage | `.font(.caption2).fontWeight(.medium)` |
| ShareCTA arrow icon | `.font(.system(size: 9))` |
| ShareCTA "Tokenomics" | `.font(.caption2)` |
| Footer "+N in app" | `.font(.caption2)` |
| Small widget center % | `.system(size: size * 0.125, weight: .bold)` (where `size` is widget side) |
| Small widget "Resets in 2h 45m" | `.system(size: size * 0.052)` |
| Compact row spacing | 2pt VStack gap; 16pt between rows (medium), 20pt (large) |

### Typography rules

- **Tabular numerics on every percentage / counter.**
  - Swift: `.font(...).monospacedDigit()` or `.fontDesign(.default).monospacedDigit()`
  - CSS: `font-variant-numeric: tabular-nums`
- **Serif discipline (web only).** Hedvig only for H1–H4 and pull-quotes. Never CTAs, labels, numerics.
- **Headline italics use the accent.** `<em>` inside `.display` / `h1` / `h2` is set in serif italic at `var(--accent)`.

---

## 04. Space & Radius

### Spacing scale (8pt base)

| Token | Px | Swift | Use case |
|---|---|---|---|
| `--s-1` | 4 | `Tokens.Spacing.s1` | Hairline gaps |
| `--s-2` | 8 | `Tokens.Spacing.s2` | Tight chrome (badge padding) |
| `--s-3` | 12 | `Tokens.Spacing.s3` | Default gap |
| `--s-4` | 16 | `Tokens.Spacing.s4` | Card padding (small), input padding |
| `--s-5` | 24 | `Tokens.Spacing.s5` | Card padding (default), section gap |
| `--s-6` | 32 | `Tokens.Spacing.s6` | Subsection rhythm |
| `--s-7` | 48 | `Tokens.Spacing.s7` | Section vertical |
| `--s-8` | 64 | `Tokens.Spacing.s8` | Hero rhythm |
| `--s-9` | 96 | `Tokens.Spacing.s9` | Top-level section padding |

### Radius scale

| Token | Px | Swift | Use case |
|---|---|---|---|
| `--r-xs` | 6 | `Tokens.Radius.xs` | Buttons-in-field, copy chips |
| `--r-sm` | 10 | `Tokens.Radius.sm` | Inputs, install-block, FAQ items |
| `--r-md` | 14 | `Tokens.Radius.md` | Cards, install-block outer, error block |
| `--r-lg` | 20 | `Tokens.Radius.lg` | Section cards, principle blocks |
| `--r-xl` | 28 | `Tokens.Radius.xl` | Hero / featured surfaces |
| `--r-pill` | 999 | `Tokens.Radius.pill` | Pills, capsule progress bars, primary buttons |

### Nesting rule

**Children always have a smaller radius than their parent: 20 → 14 → 10.**
Concentric corners stay parallel rather than gapping. Same rule for widgets:
22 (widget chrome) → 14 (row content) → 999 (pill).

---

## 05. Shadow & Motion

### Shadow tiers

| Token | Spec | Swift equivalent | Use case |
|---|---|---|---|
| `--shadow-sm` | `0 1px 2px rgba(14,51,77,0.06), 0 1px 1px rgba(14,51,77,0.04)` | `.shadow(color: .ink800.opacity(0.06), radius: 1, y: 1)` | Cards at rest |
| `--shadow-md` | `0 8px 24px rgba(14,51,77,0.10), 0 2px 6px rgba(14,51,77,0.06)` | `.shadow(color: .ink800.opacity(0.10), radius: 12, y: 8)` | Hover / popover |
| `--shadow-lg` | `0 28px 60px rgba(14,51,77,0.10), 0 8px 18px rgba(14,51,77,0.05)` | `.shadow(color: .ink800.opacity(0.10), radius: 30, y: 28)` | Hero widgets, featured art |
| `--shadow-ring` | `0 0 0 4px rgba(47,132,191,0.18)` | (use SwiftUI `.focused` modifier) | Focus rings |

### Motion table

Honor `prefers-reduced-motion` — collapse all transitions to 0ms when set.

| Element | Property | Duration | Easing |
|---|---|---|---|
| Buttons (hover / active) | transform, filter, shadow | 120ms · `--dur-fast` | `cubic-bezier(.2,.7,.2,1)` |
| Cards (scroll-enter) | opacity 0→1, translateY 16→0 | 420ms · `--dur-slow` | ease-out, 80ms stagger |
| Bars (scroll-enter) | width 0→final | 500ms | `cubic-bezier(.25,.46,.45,.94)` |
| Rings (scroll-enter) | stroke-dashoffset 0→filled | 600ms | `cubic-bezier(.25,.46,.45,.94)` |
| Pace dot (after bar fills) | ±4px sinusoidal drift | 2.5s loop, 400ms delay | ease-in-out, infinite |
| FAQ expand | max-height (only) | 300ms | `cubic-bezier(.25,.46,.45,.94)` |
| Theme toggle | background, color, border, shadow | 220ms · `--dur` | `cubic-bezier(.2,.7,.2,1)` |

---

## 06. Components

For each component below: HTML class + CSS sketch on top, SwiftUI sketch below.

### Buttons

Five variants. Hover surface is **always `--surface-2`** (off-white tint) for unified hover language.

#### Primary

- HTML: `.btn.btn-primary`
- CSS:
  ```css
  .btn-primary {
    padding: 12px 20px;
    border-radius: var(--r-pill);
    background: var(--accent-ink);  /* #0E334D light, #75CBF5 dark */
    color: #fff;                    /* dark mode flips to ink-900 */
    font: 500 16px var(--font-sans);
  }
  .btn-primary:hover { transform: translateY(-1px); box-shadow: var(--shadow-md); }
  ```
- SwiftUI:
  ```swift
  Button("Download for macOS") { ... }
      .buttonStyle(PrimaryButtonStyle())

  struct PrimaryButtonStyle: ButtonStyle {
      @Environment(\.colorScheme) var scheme
      func makeBody(configuration: Configuration) -> some View {
          configuration.label
              .font(.system(size: 16, weight: .medium))
              .padding(.horizontal, 20).padding(.vertical, 12)
              .foregroundStyle(scheme == .dark ? Tokens.Color.ink900 : Color.white)
              .background(scheme == .dark ? Tokens.Color.brand200 : Tokens.Color.ink800)
              .clipShape(Capsule())
              .scaleEffect(configuration.isPressed ? 0.98 : 1)
              .animation(.easeOut(duration: 0.12), value: configuration.isPressed)
      }
  }
  ```

#### Secondary

- HTML: `.btn.btn-secondary` — transparent fill, `--border-strong` 1px, hovers to `--surface-2`
- SwiftUI: similar to Primary but `.background(Tokens.Color.surface2.opacity(isHover ? 1 : 0))` and `.overlay(Capsule().strokeBorder(Tokens.Color.borderStrong, lineWidth: 1))`

#### Ghost

- HTML: `.btn.btn-ghost` — transparent, `--text-muted`, smaller padding (10px 14px), hovers to `--surface-2`
- SwiftUI: ghost + tertiary action button styling

#### Text (naked link)

- HTML: `.btn-text` — no background, no border, accent color, optional inline arrow
- Variants: `.is-back` (text-muted), `.is-danger` (red text)
- Hover: text-decoration underline at 3px offset; arrow nudges 2px
- SwiftUI:
  ```swift
  Button {
      // action
  } label: {
      HStack(spacing: 4) {
          Text("Open the guided setup")
          Image(systemName: "arrow.right")
              .font(.system(size: 10))
      }
      .font(.system(size: 13, weight: .medium))
      .foregroundStyle(Tokens.Color.brand600)
  }
  .buttonStyle(.plain)
  ```

#### Button-in-field

- HTML: `.btn-in-field` — sits inside `.field-row` (input or code field)
- CSS: small padding (5px 10px), `--r-xs`, `--text-muted` default, `--surface-2` hover
- Variants: `.is-icon` (icon-only square), `.is-success` (green text/border for "Copied" state)
- SwiftUI:
  ```swift
  Button("Copy") { ... }
      .buttonStyle(InFieldButtonStyle())

  struct InFieldButtonStyle: ButtonStyle {
      func makeBody(configuration: Configuration) -> some View {
          configuration.label
              .font(.system(size: 12, weight: .medium))
              .padding(.horizontal, 10).padding(.vertical, 5)
              .foregroundStyle(Tokens.Color.textMuted)
              .background(
                  RoundedRectangle(cornerRadius: Tokens.Radius.xs)
                      .stroke(Tokens.Color.borderStrong, lineWidth: 1)
              )
      }
  }
  ```

#### Sizes

Three size variants apply to **any** of the variants above (`.btn-primary`, `.btn-secondary`, `.btn-ghost`). Stack with the variant class: e.g. `.btn.btn-primary.btn-lg`.

| Size | Padding (vert × horiz) | Font | HTML class | Swift |
|---|---|---|---|---|
| `.regular` (default) | 10 × 22 | 14pt / 500 | `.btn` (no modifier) | `.tokenPrimary` / `.tokenSecondary` |
| `.lg` | 14 × 36 | 16pt / 500 | `.btn.btn-lg` | `.tokenPrimaryLg` / `.tokenSecondaryLg` |
| `.sm` | 6 × 14 | 12.5pt / 500 | `.btn.btn-sm` | `.tokenPrimary(size: .sm)` / `.tokenGhost(size: .sm)` |

`.btn-lg` is reserved for hero CTAs (Welcome's "Get started"). `.btn-sm` is for compact inline contexts (helper "Skip" links, "← Back" in tight footers). The default `.btn` covers everything else.

### Pills & badges

- HTML: `.pill` — accent fill at 14% opacity + 30% border + accent text color
- HTML: `.badge.success` / `.warn` / `.danger` — same recipe with semantic color
- Sizing: 22px height (small), `--r-pill` radius, 11px text, font-weight 500
- SwiftUI:
  ```swift
  Text("Connected")
      .font(.system(size: 11, weight: .medium))
      .padding(.horizontal, 10).padding(.vertical, 3)
      .foregroundStyle(Tokens.Color.success(scheme))
      .background(Tokens.Color.success(scheme).opacity(0.12))
      .overlay(Capsule().strokeBorder(Tokens.Color.success(scheme).opacity(0.25), lineWidth: 1))
      .clipShape(Capsule())
  ```

### Inputs

- Height: 12px vertical padding × 14px horizontal
- `--r-sm` radius, `--border-strong` 1px border
- Focus: `--accent` border + `--shadow-ring` (4px accent @ 18%)
- SwiftUI: `TextField(...)` styled with custom modifier (avoid `.textFieldStyle(.roundedBorder)` — that's macOS default chrome)

### Cards

- Background `--surface`, `--border` 1px, `--r-lg` (20px) radius, `--space-5` (24px) padding, `--shadow-sm`
- Hover (interactive cards): bump to `--shadow-md`

### Progress bars (with pace dot)

- Track: 4px height, `--r-pill` radius, `--track-bg` (rgba 40/97/149/0.12 light)
- Fill: capsule, `--brand-600` (short) or `--brand-300` (long) light variants
- **Pace dot rule (canonical, from `WidgetProgressBar.swift:646`):**
  ```swift
  if pace > 0.01 && pace < 0.99 {
      let paceX = geometry.size.width * pace
      Circle().fill(theme.paceDotColor).frame(width: 4, height: 4).offset(x: paceX - 2)
  }
  ```
  CSS equivalent: only render `.pace` element when `1% < paceX% < 99%`. At extremes the dot merges with the cap.

### Provider chips

- 48px tall, `--r-md` radius, `--surface` bg, `--border` 1px, 20px icon
- Used in marketing copy ("supports Claude, Codex, Gemini…") and compact lists

### Segmented control

Two rounding variants:

- `.seg.seg-rounded` — `--r-sm` corners, used by **Install Download/Homebrew**
- `.seg.seg-pill` — full-pill, tighter padding, used by **plan tabs Free/Standard/Enterprise**

Both share: tinted track (`--bg-2` background), padded cradle (3px), active option elevated on white pill with `--shadow-sm`.

SwiftUI:
```swift
struct Segmented<T: Hashable>: View {
    @Binding var selection: T
    let options: [(value: T, label: String)]
    var rounded: Bool = false  // false = pill, true = sm rounded

    var body: some View {
        HStack(spacing: rounded ? 2 : 0) {
            ForEach(options, id: \.value) { option in
                Button {
                    selection = option.value
                } label: {
                    Text(option.label)
                        .font(.system(size: 12, weight: .medium))
                        .foregroundStyle(selection == option.value ? Tokens.Color.text : Tokens.Color.textMuted)
                        .padding(.vertical, rounded ? 8 : 6)
                        .padding(.horizontal, rounded ? 16 : 18)
                        .background(
                            selection == option.value
                                ? Tokens.Color.surface
                                : Color.clear
                        )
                        .clipShape(rounded
                            ? AnyShape(RoundedRectangle(cornerRadius: Tokens.Radius.xs))
                            : AnyShape(Capsule()))
                }
                .buttonStyle(.plain)
            }
        }
        .padding(3)
        .background(Tokens.Color.bg2)
        .overlay(
            Group {
                if rounded {
                    RoundedRectangle(cornerRadius: Tokens.Radius.sm).strokeBorder(Tokens.Color.border, lineWidth: 1)
                } else {
                    Capsule().strokeBorder(Tokens.Color.border, lineWidth: 1)
                }
            }
        )
        .clipShape(rounded ? AnyShape(RoundedRectangle(cornerRadius: Tokens.Radius.sm)) : AnyShape(Capsule()))
    }
}
```

### FAQ

- HTML: `<details class="faq">` with `<summary>` containing question + chevron
- Dividers between siblings only (`.faq + .faq { border-top }`), no top/bottom border
- Chevron rotates 180deg on `[open]`, max-height transition 300ms

---

## 07. Widgets (canonical)

The widget code in `TokenomicsWidgetEntryView.swift` is the single source of truth. The HTML in `design-system-v3.html` mirrors it.

### Sizes (rendered at canonical pixel dimensions in design system)

| Widget | Width × Height | Aspect | Notes |
|---|---|---|---|
| Small | 200 × 200 | 1:1 | Square |
| Medium | 432 × 200 | 2.16:1 | = 2 × small + 32 gap |
| Large | 432 × 432 | 1:1 | Width = medium width; height = 2 × medium height + 32 gap |

**Proportional rule (don't break this):**
- 2 × small + gap = medium width
- 2 × medium height + gap = large height
- medium width = large width

### Small widget — dual ring

From `SmallWidgetView.swift`. Rendered as a single SVG that fills the widget so text/icon scale with the rings.

| Property | Value |
|---|---|
| Outer diameter | `size * 0.61` (r ≈ 30.5 in 100×100 viewBox) |
| Inner diameter | `size * 0.46` (r ≈ 23) |
| Stroke width | `size * 0.07` (≈ 7) |
| Center percentage font | `size * 0.125` bold (≈ 12.5pt) |
| Corner provider icon | 11.2 × 11.2 at (8.2, 8.2) |
| Ring offset (y) | `size * 0.024` (sits slightly below center, leaves room for "Resets in" text) |
| "Resets in" font | `size * 0.052` |
| Pace dot radius | 3.5 (when fill > 1% and < 99%) |

### Medium widget

From `MediumWidgetView.swift`:

| Provider count | Layout | Footer |
|---|---|---|
| 1 | `LargeProviderRow`, spacious-center, 20pt gap below header | ShareCTA "↑ Tokenomics" |
| 2 | `CompactProviderRow` × 2, 8pt gap below header, 16pt between rows | ShareCTA |
| 3 | `CompactProviderRow` × 3 | ShareCTA |
| 4+ | Compact ×3 + "+N in app" footer | "+N in app" |

`maxVisible = 3`. Padding: top 14, sides 16, bottom 16.

### Large widget

From `LargeWidgetView.swift`:

| Provider count | Layout | Footer |
|---|---|---|
| 1–3 | `LargeProviderRow` ×N, spacious, 20pt gap below header, 16pt min between rows | ShareCTA |
| 4–7 | `CompactProviderRow` ×N, 14pt below header (overflow gap), 20pt min between rows | ShareCTA |
| 8+ | Compact ×7 + "+N in app" | "+N in app" |

`maxVisible = 7`. Padding: top 14, sides 16, bottom 14.

### CompactProviderRow

```
HStack(spacing: 10) {
    Icon (17×17)
    VStack(spacing: 2) {
        HStack(spacing: 0) { Label .system(size:9) | Spacer | Pct .caption2 .medium }
        Bar (4pt)
    }
    VStack(spacing: 2) { ... long window ... }
}
```

### LargeProviderRow

```
VStack(alignment: .leading, spacing: 12) {
    HStack(spacing: 10) {
        Icon (17×17)
        Name .caption .medium @ 0.85 opacity
        Spacer
        Plan .caption2 @ labelColor
    }
    VStack(spacing: 8) {
        BarRow(label: "5-Hour", utilization: ...)
        BarRow(label: "7-Day", utilization: ..., isLong: true)
    }
}
```

`BarRow` is HStack(spacing: 8) with label width 48, bar (flex), pct width 30.

### Footer rules

- `if overflowCount > 0` → `Text("+\(N) in app")`
- `else` → `ShareCTA` (square.and.arrow.up icon at 9pt + "Tokenomics" at .caption2)
- ShareCTA padding-top: 10pt (medium), 12pt (large)

### Widget gradient

```swift
LinearGradient(
    stops: theme.backgroundStops,
    startPoint: UnitPoint(x: 0.35, y: 0),
    endPoint: UnitPoint(x: 0.65, y: 1)
)
```

CSS equivalent: `linear-gradient(135deg, ...stops)`. Both produce light-top-left / dark-bottom-right.

---

## 08. App-only components

Components that live in the macOS app and have no website equivalent. These are most prone to drift back to Apple defaults — implement carefully.

### Window chrome (macOS)

- 12px corner radius, `--shadow-window` (subtle)
- 38px titlebar with traffic lights (12px circles, 8px gap, real macOS traffic-light colors)
- Centered title, 13px medium, `--text-muted`
- Window body: 32px top, 40px sides, 28px bottom padding

> Don't use the macOS native title bar — these onboarding windows have custom chrome so they read as a curated experience, not a system dialog.

### Stepper

```swift
struct Stepper: View {
    let steps: [String]            // labels
    let current: Int               // 0-indexed
    let errorAt: Int?              // step that failed, if any

    var body: some View {
        HStack(spacing: 0) {
            ForEach(0..<steps.count, id: \.self) { i in
                VStack(spacing: 8) {
                    StepMark(index: i, current: current, errorAt: errorAt)
                    Text(steps[i])
                        .font(.system(size: 11, weight: state(i) == .active || state(i) == .error ? .semibold : .medium))
                        .foregroundStyle(stepColor(i))
                }
                .frame(width: 110)         // FIXED slot — labels never push neighbors
                if i < steps.count - 1 {
                    Capsule()
                        .fill(i < current ? Tokens.Color.brand600 : Tokens.Color.borderStrong)
                        .frame(width: 36, height: 2)   // FIXED line length
                        .padding(.top, 11)
                }
            }
        }
    }
}
```

- Step mark: 22×22 circle, 11pt font, semibold
- Done: accent fill, white text
- Active: accent fill + 4px accent ring (22% alpha)
- Error: danger fill + 4px danger ring (22% alpha)
- Pending: surface-2 fill, `--text-subtle` text, `--border-strong` 1.5px ring

### Done-check

64×64 circle, success-tinted disc (16% alpha), success-colored 32pt SF Symbol checkmark inside.

```swift
ZStack {
    Circle().fill(Tokens.Color.success(scheme).opacity(0.16))
    Image(systemName: "checkmark")
        .font(.system(size: 32, weight: .semibold))
        .foregroundStyle(Tokens.Color.success(scheme))
}
.frame(width: 64, height: 64)
```

### Error block

Inline failure surface with a single concrete next-step button below.

```swift
VStack(alignment: .leading, spacing: 4) {
    Text("EACCES: permission denied")
        .font(.system(size: 14, weight: .semibold))
        .foregroundStyle(Tokens.Color.danger(scheme))
    Text("/opt/homebrew/lib/node_modules/@openai")
        .font(.system(size: 13).monospaced())
        .foregroundStyle(Tokens.Color.textMuted)
}
.padding(.horizontal, 16).padding(.vertical, 14)
.background(Tokens.Color.danger(scheme).opacity(0.08))
.overlay(
    RoundedRectangle(cornerRadius: Tokens.Radius.sm)
        .strokeBorder(Tokens.Color.danger(scheme).opacity(0.30), lineWidth: 1)
)
.clipShape(RoundedRectangle(cornerRadius: Tokens.Radius.sm))
```

**Rule:** every error block ends with one concrete next-step CTA (e.g. "Use per-user install instead"). Never two CTAs of equal weight.

### Provider chooser row

List item used in the provider chooser screen. Grid:
- Column 1: 32×32 squircle icon (`--r-sm` corner) with provider letter or SVG
- Column 2: name (14px semibold) + scope (12px subtle)
- Column 3: action — `Connected` badge OR `Quick setup` pill button

### Check row (detect list)

22px status icon | label + sublabel (14/12) | optional right meta. Used in "Checking tools" step.

### iOS toggle

40 × 24 capsule, 20px white thumb with 1px shadow, transitions in 220ms.

```swift
struct AppToggle: View {
    @Binding var isOn: Bool
    var body: some View {
        Button { isOn.toggle() } label: {
            ZStack(alignment: isOn ? .trailing : .leading) {
                Capsule()
                    .fill(isOn ? Tokens.Color.brand600 : Tokens.Color.borderStrong)
                    .frame(width: 40, height: 24)
                Circle()
                    .fill(Color.white)
                    .frame(width: 20, height: 20)
                    .shadow(color: .black.opacity(0.15), radius: 1, y: 1)
                    .padding(.horizontal, 2)
            }
        }
        .buttonStyle(.plain)
        .animation(.easeOut(duration: 0.22), value: isOn)
    }
}
```

> Don't use SwiftUI's default `Toggle` — that pulls macOS native chrome which doesn't match the design.

### Plan segment

See `Segmented` component in section 06 — use `rounded: false` (pill variant) for plan tiers.

### Help banner

Surfaces at the top of the Providers popover with 8% accent tint background.

```swift
HStack {
    Text("Need help connecting a provider?")
        .font(.system(size: 12.5))
        .foregroundStyle(Tokens.Color.textMuted)
    Spacer()
    Button("Open the guided setup →") { ... }
        .font(.system(size: 12.5, weight: .medium))
        .foregroundStyle(Tokens.Color.brand600)
        .buttonStyle(.plain)
}
.padding(.horizontal, 16).padding(.vertical, 11)
.background(Tokens.Color.brand600.opacity(0.08))
.overlay(
    RoundedRectangle(cornerRadius: Tokens.Radius.md).strokeBorder(Tokens.Color.border, lineWidth: 1)
)
```

### Quick-setup pill button

For provider rows that aren't connected yet — small pill with subtle accent fill.

```swift
HStack(spacing: 4) {
    Text("Quick setup")
    Text("›").opacity(0.6)
}
.font(.system(size: 12, weight: .medium))
.foregroundStyle(Tokens.Color.brand600)
.padding(.horizontal, 14).padding(.vertical, 6)
.background(Tokens.Color.brand600.opacity(0.12))
.clipShape(Capsule())
```

---

## 09. Web-only components

Brief reference. See `design-system-v3.html` sections 08–11 for full demos.

- **Pace-dot diagram** (`#pace-diagram`) — Annotated dual-ring SVG (460×440) used on marketing pages to teach the pace concept. Same ring math as small widget, scaled ~3× with annotation callouts.
- **Widget showcase / desktop frame** (`#showcase`) — Dark gradient platter with radial glow holding all 5 widgets in a fixed 3-column mosaic.
- **Menu-bar popover** (`#popover`) — Translucent glass popover (24px backdrop-blur, 16px radius). Tab strip with active provider expanded as pill.
- **Install block** (`#install`) — Two-column layout: segmented Download/Homebrew tabs left, drag-to-install flow OR `$ brew install` row right. Uses real brand SVGs (`assets/brand/`).

---

## 10. Token reference

Master flat list of every token in the system. Use this for find/replace audits.

```
# Color · brand
--ink-900   #051928
--ink-800   #0E334D
--ink-700   #286195
--brand-600 #2F84BF
--brand-500 #3389C7
--brand-400 #4BA6D2
--brand-300 #56A2D6
--brand-200 #75CBF5
--cream-50  #F3EFE5
--cream-100 #E6E0D4
--cream-200 #D9D1C0
--white     #FFFFFF

# Color · semantic (light · dark)
--success   #2F8F4F · #6FD18A
--warning   #C26A1F · #E2A765
--danger    #B33A3A · #E27777

# Color · theme tokens (light · dark)
--bg            #F3EFE5 · #07101a
--bg-2          #E6E0D4 · #0b1a29
--surface       #FFFFFF · #0E334D
--surface-2     #FBF8F1 · #0a2439
--text          #0E334D · #E6EEF6
--text-muted    rgba(...,.64) · rgba(...,.68)
--text-subtle   rgba(...,.44) · rgba(...,.44)
--border        rgba(...,.12) · rgba(...,.10)
--border-strong rgba(...,.22) · rgba(...,.22)
--accent        #2F84BF · #75CBF5
--accent-ink    #0E334D · #E6EEF6

# Spacing (px)
--s-1=4  --s-2=8  --s-3=12  --s-4=16  --s-5=24
--s-6=32 --s-7=48 --s-8=64  --s-9=96

# Radius (px)
--r-xs=6  --r-sm=10  --r-md=14  --r-lg=20  --r-xl=28  --r-pill=999

# Shadow (light theme)
--shadow-sm    0 1px 2px rgba(14,51,77,.06), 0 1px 1px rgba(14,51,77,.04)
--shadow-md    0 8px 24px rgba(14,51,77,.10), 0 2px 6px rgba(14,51,77,.06)
--shadow-lg    0 28px 60px rgba(14,51,77,.10), 0 8px 18px rgba(14,51,77,.05)
--shadow-ring  0 0 0 4px rgba(47,132,191,.18)

# Motion
--dur-fast  120ms
--dur       220ms
--dur-slow  420ms
--ease      cubic-bezier(.2,.7,.2,1)

# Widget gradient
--widget-light  linear-gradient(135deg, #F3EFE5 1.6%, #E6E0D4 84.5%)
--widget-dark   linear-gradient(135deg, #0E334D 10.3%, #051928 88.1%)
```

---

## 11. Regression tests

A test script lives at `tests/design-system-regression.sh`. Run it whenever the design system changes:

```bash
bash tests/design-system-regression.sh
```

The script verifies:

1. **Token parity** — every token defined in `design-system.md` exists in `design-system-v3.html` with the same hex value.
2. **No drift** — color hex values match across MD and HTML (catches typos like `#E6E0D4` vs `#E6E0D5`).
3. **Critical values locked**:
   - `--cream-100` = `#E6E0D4` (was at the center of a long debugging session)
   - `--bg-2` resolves to `var(--cream-100)` in light mode
   - Widget gradient direction is `135deg` (not `197deg`)
   - Pace dot rule: bar height 4px, dot rendered when 1% < pace < 99%
4. **Widget proportional rule**: medium width = 2 × small + gap, large height = 2 × medium height + gap.
5. **Hover surface unification**: every `:hover` rule that changes background uses `var(--surface-2)` or `var(--bg-2)` — not literal hex.

Failure modes the test catches:
- Someone adds a new token to MD but forgets to add it to HTML (or vice versa).
- A hex value drifts in one file but not the other.
- A widget size gets changed without updating the proportional math.
- A hover rule is hardcoded to a literal cream value instead of a token.

When adding a new token to the system, update **both** `design-system.md` and `design-system-v3.html`, then run the regression test.
