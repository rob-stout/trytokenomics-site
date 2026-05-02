#!/usr/bin/env bash
# Design system regression tests.
#
# Verifies that design-system.md and design-system-v3.html stay aligned —
# token values, widget proportions, hover surface unification, etc.
#
# Run from repo root:  bash tests/design-system-regression.sh
# CI-friendly:         exits 0 on pass, non-zero on fail.

set -u

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
MD="$ROOT/design-system.md"
HTML="$ROOT/design-system-v3.html"

# ANSI
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
DIM='\033[2m'
RESET='\033[0m'

PASS=0
FAIL=0
WARN=0
FAILED_TESTS=()

pass() {
  echo -e "${GREEN}✓${RESET} $1"
  PASS=$((PASS + 1))
}

fail() {
  echo -e "${RED}✗${RESET} $1"
  if [ -n "${2:-}" ]; then
    echo -e "  ${DIM}$2${RESET}"
  fi
  FAIL=$((FAIL + 1))
  FAILED_TESTS+=("$1")
}

warn() {
  echo -e "${YELLOW}!${RESET} $1"
  WARN=$((WARN + 1))
}

section() {
  echo ""
  echo -e "${BLUE}━━ $1 ━━${RESET}"
}

# Pre-flight: both files exist
section "Pre-flight"

if [ ! -f "$MD" ]; then
  fail "design-system.md not found at $MD"
  echo ""
  echo -e "${RED}Cannot continue without design-system.md.${RESET}"
  exit 1
else
  pass "design-system.md exists"
fi

if [ ! -f "$HTML" ]; then
  fail "design-system-v3.html not found at $HTML"
  echo ""
  echo -e "${RED}Cannot continue without design-system-v3.html.${RESET}"
  exit 1
else
  pass "design-system-v3.html exists"
fi

# ─────────────────────────────────────────────────────────────────────
# Test group 1: brand color hex values in MD ↔ HTML
# ─────────────────────────────────────────────────────────────────────
section "Brand color parity (MD ↔ HTML)"

# token_name expected_hex — order matters but we look up by name in both files
declare -a brand_tokens=(
  "ink-900:051928"
  "ink-800:0E334D"
  "ink-700:286195"
  "brand-600:2F84BF"
  "brand-500:3389C7"
  "brand-400:4BA6D2"
  "brand-300:56A2D6"
  "brand-200:75CBF5"
  "cream-50:F3EFE5"
  "cream-100:E6E0D4"
  "cream-200:D9D1C0"
)

for entry in "${brand_tokens[@]}"; do
  token="${entry%%:*}"
  expected="${entry##*:}"

  # MD: look for `--token: #expected` or `Hex(token)` style
  md_match=$(grep -ioE "\-\-${token}[: ]+#${expected}" "$MD" | head -1)
  html_match=$(grep -ioE "\-\-${token}:\s*#${expected}" "$HTML" | head -1)

  if [ -n "$md_match" ] && [ -n "$html_match" ]; then
    pass "--${token} = #${expected} in both files"
  elif [ -z "$md_match" ]; then
    fail "--${token} missing or wrong hex in design-system.md (expected #${expected})"
  elif [ -z "$html_match" ]; then
    fail "--${token} missing or wrong hex in design-system-v3.html (expected #${expected})"
  fi
done

# ─────────────────────────────────────────────────────────────────────
# Test group 2: semantic color hex values
# ─────────────────────────────────────────────────────────────────────
section "Semantic color parity (light & dark)"

declare -a semantic_tokens=(
  "success_light:2F8F4F"
  "success_dark:6FD18A"
  "warning_light:C26A1F"
  "warning_dark:E2A765"
  "danger_light:B33A3A"
  "danger_dark:E27777"
)

for entry in "${semantic_tokens[@]}"; do
  hex="${entry##*:}"
  name="${entry%%:*}"
  md_count=$(grep -ic "#${hex}" "$MD" || true)
  html_count=$(grep -ic "#${hex}" "$HTML" || true)

  if [ "$md_count" -ge 1 ] && [ "$html_count" -ge 1 ]; then
    pass "${name} #${hex} present in both"
  elif [ "$md_count" -lt 1 ]; then
    fail "${name} #${hex} missing from design-system.md"
  else
    fail "${name} #${hex} missing from design-system-v3.html"
  fi
done

# ─────────────────────────────────────────────────────────────────────
# Test group 3: critical locked values
# ─────────────────────────────────────────────────────────────────────
section "Critical locked values"

# cream-100 must be #E6E0D4 (long debugging session anchor)
if grep -qE "\-\-cream-100:\s*#E6E0D4" "$HTML"; then
  pass "--cream-100 locked to #E6E0D4 in HTML"
else
  fail "--cream-100 is NOT #E6E0D4 in HTML — check for diagnostic leftovers (e.g. #FF0000)"
fi

# bg-2 must reference cream-100 (not cream-200) in light mode
# Note: this is the FIRST occurrence in :root, before the dark theme override
first_bg2=$(grep -nE "\-\-bg-2:" "$HTML" | head -1)
if echo "$first_bg2" | grep -q "var(--cream-100)"; then
  pass "--bg-2 → var(--cream-100) in light mode (line: ${first_bg2%%:*})"
else
  fail "--bg-2 is not pointing at var(--cream-100) in light mode" "Found: $first_bg2"
fi

# Widget gradient direction must be 135deg
if grep -qE "linear-gradient\(135deg," "$HTML"; then
  pass "Widget gradient uses 135deg"
else
  fail "Widget gradient missing 135deg — was previously 197deg (horizontally backward)"
fi

if ! grep -qE "linear-gradient\(197deg," "$HTML"; then
  pass "No 197deg gradients (horizontally-flipped legacy direction is gone)"
else
  fail "Found a 197deg gradient — should be 135deg"
fi

# Pace dot rule: 0.01 < pace < 0.99
if grep -qE "0\.01.*0\.99|1%.*99%" "$MD"; then
  pass "Pace dot rule (1% < pace < 99%) documented in MD"
else
  warn "Pace dot rule (1% < pace < 99%) — couldn't find clear text in MD"
fi

# ─────────────────────────────────────────────────────────────────────
# Test group 4: widget proportional rule
# ─────────────────────────────────────────────────────────────────────
section "Widget proportional rule"

# Medium width should be 432 (= 2*200 + 32)
if grep -qE "\.w-medium\s*\{[^}]*width:\s*432px" "$HTML"; then
  pass ".w-medium width = 432px"
else
  fail ".w-medium width is not 432px"
fi

# Large should be 432×432
if grep -qE "\.w-large\s*\{[^}]*width:\s*432px[^}]*height:\s*432px" "$HTML"; then
  pass ".w-large = 432×432"
else
  fail ".w-large is not 432×432"
fi

# Small should be 200×200
if grep -qE "\.w-small\s*\{[^}]*width:\s*200px[^}]*height:\s*200px" "$HTML"; then
  pass ".w-small = 200×200"
else
  fail ".w-small is not 200×200"
fi

# Desktop frame grid columns
if grep -qE "grid-template-columns:\s*432px\s+432px\s+200px" "$HTML"; then
  pass "Desktop frame grid: 432px 432px 200px"
else
  fail "Desktop frame grid does not match 432 432 200"
fi

# ─────────────────────────────────────────────────────────────────────
# Test group 5: hover surface unification
# ─────────────────────────────────────────────────────────────────────
section "Hover surface unification"

# All :hover rules with background should use a token, not a literal cream hex
literal_cream_hovers=$(grep -nE ":hover\s*\{[^}]*background:\s*#[Ee]6[Ee]0[Dd]4" "$HTML" || true)

if [ -z "$literal_cream_hovers" ]; then
  pass "No literal #E6E0D4 in :hover background rules"
else
  fail "Found literal #E6E0D4 in :hover rules — use var(--surface-2) or var(--bg-2)" "$literal_cream_hovers"
fi

# .copy-btn-v2:hover and .btn-in-field:hover should use var(--surface-2)
copy_hover=$(grep -nE "\.copy-btn-v2:hover\s*\{[^}]*background:\s*var\(--surface-2\)" "$HTML" || true)
field_hover=$(grep -nE "\.btn-in-field:hover\s*\{[^}]*background:\s*var\(--surface-2\)" "$HTML" || true)

if [ -n "$copy_hover" ]; then
  pass ".copy-btn-v2:hover uses var(--surface-2)"
else
  fail ".copy-btn-v2:hover does not use var(--surface-2)"
fi

if [ -n "$field_hover" ]; then
  pass ".btn-in-field:hover uses var(--surface-2)"
else
  fail ".btn-in-field:hover does not use var(--surface-2)"
fi

# ─────────────────────────────────────────────────────────────────────
# Test group 6: structural integrity
# ─────────────────────────────────────────────────────────────────────
section "HTML structural integrity"

open_sections=$(grep -c "<section" "$HTML" || echo 0)
close_sections=$(grep -c "</section>" "$HTML" || echo 0)

if [ "$open_sections" = "$close_sections" ] && [ "$open_sections" -gt 0 ]; then
  pass "Section tags balanced ($open_sections open / $close_sections close)"
else
  fail "Section tags unbalanced: $open_sections open vs $close_sections close"
fi

# ─────────────────────────────────────────────────────────────────────
# Test group 7: Swift token block sanity (in MD)
# ─────────────────────────────────────────────────────────────────────
section "Swift token block (in MD)"

# Verify Tokens.swift code block exists and contains the key namespaces
if grep -q "enum Tokens" "$MD"; then
  pass "MD contains 'enum Tokens' Swift block"
else
  fail "MD missing 'enum Tokens' Swift block"
fi

declare -a swift_namespaces=(
  "enum Color"
  "enum Spacing"
  "enum Radius"
  "enum Typography"
  "enum Motion"
)

for ns in "${swift_namespaces[@]}"; do
  if grep -q "$ns" "$MD"; then
    pass "Swift block contains '$ns'"
  else
    fail "Swift block missing '$ns'"
  fi
done

# Verify a few critical Swift values match their hex equivalents
declare -a swift_color_checks=(
  "ink800.*14/255.*51/255.*77/255"
  "brand600.*47/255.*132/255.*191/255"
  "cream100.*230/255.*224/255.*212/255"
  "successLight.*47/255.*143/255.*79/255"
  "warningLight.*194/255.*106/255.*31/255"
  "dangerLight.*179/255.*58/255.*58/255"
)

for check in "${swift_color_checks[@]}"; do
  if grep -qE "$check" "$MD"; then
    pass "Swift Color: $check"
  else
    fail "Swift Color RGB mismatch: $check"
  fi
done

# Spacing values
if grep -qE "s4: CGFloat = 16" "$MD" && grep -qE "s5: CGFloat = 24" "$MD"; then
  pass "Spacing tokens (s4=16, s5=24) match"
else
  fail "Spacing token values don't match (expected s4=16, s5=24)"
fi

# Radius values
if grep -qE "xs: CGFloat = 6" "$MD" && grep -qE "md: CGFloat = 14" "$MD" && grep -qE "lg: CGFloat = 20" "$MD"; then
  pass "Radius tokens (xs=6, md=14, lg=20) match"
else
  fail "Radius token values don't match"
fi

# ─────────────────────────────────────────────────────────────────────
# Test group 8: anti-patterns checklist (presence in MD)
# ─────────────────────────────────────────────────────────────────────
section "Anti-patterns documented"

declare -a antipatterns=(
  "Color.accentColor"
  "Color.primary"
  "systemBackground"
  ".body"
  "\.padding\(\)"
)

for pattern in "${antipatterns[@]}"; do
  if grep -qE "$pattern" "$MD"; then
    pass "Anti-pattern documented: $pattern"
  else
    warn "Anti-pattern not explicitly listed: $pattern"
  fi
done

# ─────────────────────────────────────────────────────────────────────
# Summary
# ─────────────────────────────────────────────────────────────────────
echo ""
echo "═══════════════════════════════════════════════════════"
echo -e "  ${GREEN}Passed: $PASS${RESET}    ${RED}Failed: $FAIL${RESET}    ${YELLOW}Warnings: $WARN${RESET}"
echo "═══════════════════════════════════════════════════════"

if [ "$FAIL" -gt 0 ]; then
  echo ""
  echo -e "${RED}Failed tests:${RESET}"
  for t in "${FAILED_TESTS[@]}"; do
    echo "  - $t"
  done
  exit 1
fi

if [ "$WARN" -gt 0 ]; then
  echo ""
  echo -e "${YELLOW}Note: $WARN warning(s) — review above.${RESET}"
fi

exit 0
