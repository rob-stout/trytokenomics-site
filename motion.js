/* Tokenomics homepage motion, driven by scroll position.
 *
 * Each widget and the pace diagram has a progress value (0 → 1) that follows
 * where it sits on screen: it fills as you scroll it up into view and
 * un-fills as you scroll back, so people can rewind and replay.
 *
 * The shape of each animation matches the Mac app (Tokens.Motion):
 *   bars and rings fill on cubic-bezier(.25,.46,.45,.94);
 *   the pace dot runs on the same curve but over a longer stretch, so it
 *   trails the fill and lands last; percentages count with the fill.
 *
 * The hero widgets are already on screen when the page opens, so they play
 * once on load, the way the app animates when you open the popover.
 *
 * Everything else builds in: headings, copy and cards fade up as they enter,
 * staggered when several arrive together, and reset once they drop back below
 * the screen so scrolling up and down again replays them.
 *
 * Without JS, or with Reduce Motion on, everything shows in its final state:
 * this script only sets a starting state when it's about to drive it.
 */
(function () {
  'use strict';
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  // ── Easing: cubic-bezier(.25,.46,.45,.94), the app's bar/pace curve ──
  function bezier(x1, y1, x2, y2) {
    function a(p1, p2) { return 1 - 3 * p2 + 3 * p1; }
    function b(p1, p2) { return 3 * p2 - 6 * p1; }
    function c(p1) { return 3 * p1; }
    function at(t, p1, p2) { return ((a(p1, p2) * t + b(p1, p2)) * t + c(p1)) * t; }
    function slope(t, p1, p2) { return 3 * a(p1, p2) * t * t + 2 * b(p1, p2) * t + c(p1); }
    return function (x) {
      if (x <= 0) return 0;
      if (x >= 1) return 1;
      var t = x;
      for (var i = 0; i < 8; i++) {
        var d = at(t, x1, x2) - x, s = slope(t, x1, x2);
        if (Math.abs(d) < 1e-5 || s === 0) break;
        t -= d / s;
      }
      return at(t, y1, y2);
    };
  }
  var appEase = bezier(0.25, 0.46, 0.45, 0.94);
  // When scroll drives the motion, an ease-out would front-load it (most of the
  // growth in the first third of the scroll), so scrubbed pieces use an even
  // ease-in-out. Time-based playback (the hero) keeps the app's curve.
  var scrollEase = bezier(0.42, 0, 0.58, 1);
  function clamp(x) { return x < 0 ? 0 : x > 1 ? 1 : x; }
  // Progress through a slice [from, to] of the overall 0→1, eased.
  function seg(p, from, to, curve) { return curve(clamp((p - from) / (to - from))); }

  // ── Pieces: each returns render(k) where k is 0 (start) … 1 (final) ──

  function barPiece(fill) {
    var target = parseFloat(fill.style.width) || 0;
    fill.style.transition = 'none';
    return function (k) { fill.style.width = (target * k) + '%'; };
  }
  function pacePiece(dot) {
    var target = parseFloat(dot.style.left) || 0;
    dot.style.transition = 'none';
    return function (k) { dot.style.left = (target * k) + '%'; };
  }
  // "90%" counts up; anything else (like "45 sec ago") is left alone.
  function countPiece(el) {
    var m = /^(\s*)(\d+)(%.*)$/.exec(el.textContent);
    if (!m) return null;
    var target = parseInt(m[2], 10);
    return function (k) { el.textContent = m[1] + Math.round(target * k) + m[3]; };
  }
  function ringPiece(arc) {
    var full = parseFloat(arc.getAttribute('stroke-dasharray'));
    var target = parseFloat(arc.getAttribute('stroke-dashoffset'));
    if (!full || isNaN(target)) return null;
    return function (k) { arc.setAttribute('stroke-dashoffset', (full + (target - full) * k).toFixed(2)); };
  }
  // A dot placed on a ring with transform="rotate(angle [cx cy]) translate(...)".
  function ringDotPiece(dot) {
    var t = dot.getAttribute('transform') || '';
    var m = /rotate\(\s*(-?[\d.]+)/.exec(t);
    if (!m) return null;
    var target = parseFloat(m[1]);
    return function (k) {
      dot.setAttribute('transform', t.replace(/rotate\(\s*-?[\d.]+/, 'rotate(' + (target * k).toFixed(2)));
    };
  }
  function linePiece(line) {
    var len = Math.hypot(line.x2.baseVal.value - line.x1.baseVal.value,
                         line.y2.baseVal.value - line.y1.baseVal.value);
    line.style.strokeDasharray = len;
    return function (k) { line.style.strokeDashoffset = (len * (1 - k)).toFixed(2); };
  }
  function labelPiece(label) {
    var isSvg = label instanceof SVGElement;
    return function (k) {
      label.style.opacity = k;
      if (!isSvg) label.style.transform = 'translateX(' + ((1 - k) * -6).toFixed(2) + 'px)';
    };
  }
  function collect(root, selector, make) {
    var out = [];
    root.querySelectorAll(selector).forEach(function (el) { var r = make(el); if (r) out.push(r); });
    return out;
  }

  // ── Widgets: rows fill one after another, pace dots trail ───────────
  function widgetRenderer(w, curve) {
    function seg2(p, a, b) { return seg(p, a, b, curve); }
    var rows = Array.prototype.slice.call(w.querySelectorAll('.bar-row, .row-compact, .row-large .metrics > *'));
    function rowOf(el) {
      for (var i = 0; i < rows.length; i++) if (rows[i].contains(el)) return Math.min(i, 6);
      return 0;
    }
    var fills = [], paces = [];
    // Fill runs over ~90% of the widget's progress, offset a little per row; the
    // pace dot uses the whole range, so it trails and lands last (500ms vs 800ms in the app).
    function addFill(render, el) { var o = rowOf(el) * 0.05; fills.push(function (p) { render(seg2(p, o, Math.min(1, o + 0.9))); }); }
    function addPace(render, el) { var o = rowOf(el) * 0.05; paces.push(function (p) { render(seg2(p, o, Math.min(1, o + 1))); }); }

    w.querySelectorAll('.pbar .fill').forEach(function (f) { addFill(barPiece(f), f); });
    w.querySelectorAll('.pbar .pace').forEach(function (d) { addPace(pacePiece(d), d); });
    w.querySelectorAll('.pct').forEach(function (el) { var r = countPiece(el); if (r) addFill(r, el); });
    collect(w, 'svg circle[stroke-dasharray]', ringPiece).forEach(function (r) { fills.push(function (p) { r(seg2(p, 0, 0.9)); }); });
    collect(w, 'svg text', countPiece).forEach(function (r) { fills.push(function (p) { r(seg2(p, 0, 0.9)); }); });
    collect(w, 'svg circle[transform*="rotate"]:not([stroke-dasharray])', ringDotPiece).forEach(function (r) { paces.push(function (p) { r(seg2(p, 0, 1)); }); });
    var all = fills.concat(paces);
    if (!all.length) return null;
    return function (p) { all.forEach(function (f) { f(p); }); };
  }

  // ── Menu bar popover: both bars fill, pace dots trail, percentages count ──
  function popoverRenderer(pop, curve) {
    var parts = [];
    pop.querySelectorAll('.pop-section').forEach(function (s, i) {
      var o = i * 0.08;
      var fill = s.querySelector('.pop-bar-fill'), pace = s.querySelector('.pop-bar-pace'), pct = s.querySelector('.pop-section-pct');
      if (fill) { var f = barPiece(fill); parts.push(function (p) { f(seg(p, o, Math.min(1, o + 0.9), curve)); }); }
      var c = pct && countPiece(pct);
      if (c) parts.push(function (p) { c(seg(p, o, Math.min(1, o + 0.9), curve)); });
      if (pace) { var d = pacePiece(pace); parts.push(function (p) { d(seg(p, o, 1, curve)); }); }
    });
    if (!parts.length) return null;
    // Once someone clicks a tab (popover-demo.js), the bars are theirs: stop scrubbing.
    return function (p) { if (!pop.hasAttribute('data-touched')) parts.forEach(function (f) { f(p); }); };
  }

  // ── Pace diagram: rings → dots → each callout line, then its label ───
  function diagramRenderer(d, curve) {
    function seg2(p, a, b) { return seg(p, a, b, curve); }
    var parts = [];
    collect(d, 'circle[stroke-dasharray]', ringPiece).forEach(function (r) { parts.push(function (p) { r(seg2(p, 0, 0.4)); }); });
    collect(d, 'svg text', countPiece).forEach(function (r) { parts.push(function (p) { r(seg2(p, 0, 0.4)); }); });
    collect(d, '.pace-dot', ringDotPiece).forEach(function (r) { parts.push(function (p) { r(seg2(p, 0, 0.5)); }); });

    // Three callouts share the rest of the range. Each line draws from the ring
    // outward (segments in document order), then its label fades in.
    var start = 0.5, slot = 0.16;
    [1, 2, 3].forEach(function (step, i) {
      var s0 = start + i * slot;
      var lines = d.querySelectorAll('.callout-line[data-step="' + step + '"]');
      var n = lines.length || 1, lineSpan = slot * 0.55;
      Array.prototype.forEach.call(lines, function (line, j) {
        var r = linePiece(line), a = s0 + (lineSpan / n) * j, b = a + lineSpan / n;
        parts.push(function (p) { r(clamp((p - a) / (b - a))); });   // lines draw linearly
      });
      collect(d, '.callout-label[data-step="' + step + '"]', labelPiece).forEach(function (r) {
        var a = s0 + lineSpan * 0.9, b = s0 + slot;
        parts.push(function (p) { r(seg2(p, a, b)); });
      });
    });
    return function (p) { parts.forEach(function (f) { f(p); }); };
  }

  // ── Scroll driver ───────────────────────────────────────────────────
  // progress = 0 when the element's top reaches `from` (fraction of the viewport
  // height, measured from the top), 1 when it reaches `to`.
  var scrubbers = [];
  function addScrubber(el, render, from, to) {
    if (render) scrubbers.push({ el: el, render: render, from: from, to: to, last: -1 });
  }
  var ticking = false;
  function update() {
    ticking = false;
    var vh = window.innerHeight || document.documentElement.clientHeight;
    scrubbers.forEach(function (s) {
      var top = s.el.getBoundingClientRect().top;
      var p = clamp((s.from * vh - top) / ((s.from - s.to) * vh));
      if (Math.abs(p - s.last) < 0.001) return;
      s.last = p;
      s.render(p);
    });
  }
  function requestUpdate() {
    if (!ticking) { ticking = true; requestAnimationFrame(update); }
  }

  // Hero widgets: on screen at load, so they play once on a timer (like opening the popover).
  function playOnce(render, ms) {
    var t0 = null;
    render(0);
    function frame(now) {
      if (t0 === null) t0 = now;
      var p = Math.min(1, (now - t0) / ms);
      render(p);
      if (p < 1) requestAnimationFrame(frame);
    }
    setTimeout(function () { requestAnimationFrame(frame); }, 250);
  }

  // ── Build-in: fade up as pieces enter, replay after they leave below ──
  var BUILD = [
    '.reveal',
    '[data-build="children"] > *',
    '.section-wrap > .feature-kicker', '.section-wrap > h2',
    '.widgets-section-inner > .feature-kicker', '.widgets-section-inner > h2', '.widgets-section-inner > p',
    '.provider-strip > *', '.provider-coming',
    '.craft-card',
    '.support-intro > *', '.support-card',
    '.download-card',
    '.faq-item', '.faq-more'
  ].join(',');

  function initBuild() {
    if (!('IntersectionObserver' in window)) return;
    var items = Array.prototype.slice.call(document.querySelectorAll(BUILD));
    if (!items.length) return;
    items.forEach(function (el) { el.classList.add('build'); });

    function show(el, delay) {
      el.style.setProperty('--build-delay', delay + 'ms');
      el.classList.add('in');
    }
    // Enter: once a piece is 12% up from the bottom edge. Pieces that arrive in
    // the same frame stagger in document order, ~90ms apart, capped at 600ms total.
    var enter = new IntersectionObserver(function (entries) {
      var arriving = entries.filter(function (e) { return e.isIntersecting && !e.target.classList.contains('in'); })
        .map(function (e) { return e.target; })
        .sort(function (a, b) { return a.compareDocumentPosition(b) & 4 ? -1 : 1; });
      var step = arriving.length > 1 ? Math.min(90, 600 / (arriving.length - 1)) : 0;
      arriving.forEach(function (el, i) { show(el, Math.round(i * step)); });
    }, { rootMargin: '0px 0px -12% 0px' });
    // Leave: reset only when fully below the screen, so scrolling back down replays.
    // Pieces already above the screen (page opened mid-way) show straight away.
    var leave = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) return;
        if (e.boundingClientRect.top > 0) e.target.classList.remove('in');
        else if (!e.target.classList.contains('in')) show(e.target, 0);
      });
    });
    items.forEach(function (el) { enter.observe(el); leave.observe(el); });
  }

  function init() {
    initBuild();
    document.querySelectorAll('.widget').forEach(function (w) {
      var hero = !!w.closest('.hero');
      var render = widgetRenderer(w, hero ? appEase : scrollEase);
      if (!render) return;
      if (hero) playOnce(render, 900);
      // Widgets start once they're fully up on screen (top 85% down) and finish as
      // they near the top (top 20% down), so the growth plays across the whole screen.
      else addScrubber(w, render, 0.85, 0.2);
    });
    // Pricing: "$19" counts up from $0 as its card rises (skips "$0", nothing to count).
    document.querySelectorAll('.support-price').forEach(function (el) {
      var match = /^(\D*)(\d+)(.*)$/.exec(el.textContent.trim());
      if (!match || match[2] === '0') return;
      var target = parseInt(match[2], 10);
      el.style.fontVariantNumeric = 'tabular-nums';
      addScrubber(el, function (p) {
        el.textContent = match[1] + Math.round(target * scrollEase(p)) + match[3];
      }, 0.85, 0.35);
    });
    // Install arrow: the squiggle draws in, the arrowhead lands, then the
    // "Drag to Install…" caption and the macOS line fade in.
    var flow = document.querySelector('.install-flow');
    var stroke = flow && flow.querySelector('.arrow-stroke');
    if (stroke) {
      var len = stroke.getTotalLength();
      var art = flow.querySelector('.arrow-line'), arrowHead = flow.querySelector('.arrow-head');
      var after = [document.querySelector('.install-flow-caption'), document.getElementById('install-support-line')].filter(Boolean);
      stroke.style.strokeDasharray = len;
      arrowHead.style.transformBox = 'fill-box';
      arrowHead.style.transformOrigin = '80% 50%';
      // The extension card's "Works with" pills build on the same scroll as the arrow,
      // one after another while it draws, so both cards finish together.
      var sitesLabel = document.querySelector('.download-sites-label');
      var pills = Array.prototype.slice.call(document.querySelectorAll('.download-sites li'));
      var pillSpan = 0.68 - 0.1, pillDur = 0.1;
      function popIn(el, k) {
        el.style.opacity = k;
        el.style.transform = 'translateY(' + ((1 - k) * 6).toFixed(1) + 'px) scale(' + (0.94 + 0.06 * k).toFixed(3) + ')';
      }
      function buildPills(p) {
        if (sitesLabel) popIn(sitesLabel, seg(p, 0, 0.08, appEase));
        pills.forEach(function (li, i) {
          var a = 0.04 + (pills.length > 1 ? i * (pillSpan - 0.04) / (pills.length - 1) : 0);
          popIn(li, seg(p, a, a + pillDur, appEase));
        });
      }
      // Side by side, the arrow drives the pills. Stacked (phones), the arrow is far
      // below, so the pills follow their own position instead.
      var grid = document.querySelector('.download-grid');
      function sideBySide() { return !grid || getComputedStyle(grid).gridTemplateColumns.split(' ').length > 1; }
      var sitesList = document.querySelector('.download-sites');
      if (sitesList) addScrubber(sitesList, function (p) { if (!sideBySide()) buildPills(p); }, 0.85, 0.4);
      addScrubber(flow, function (p) {
        if (sideBySide()) buildPills(p);
        stroke.style.strokeDashoffset = (len * (1 - seg(p, 0, 0.68, scrollEase))).toFixed(1);
        // The drawn stroke hands over to the hand-drawn artwork as the arrowhead lands.
        var swap = seg(p, 0.66, 0.76, appEase);
        // Artwork (on top) fades in over the solid stroke; the stroke drops once it's covered.
        stroke.setAttribute('opacity', swap < 1 ? 1 : 0);
        art.style.opacity = swap;
        var h = seg(p, 0.66, 0.8, appEase);
        arrowHead.style.opacity = h;
        arrowHead.style.transform = 'scale(' + (0.6 + 0.4 * h).toFixed(3) + ')';
        var c = seg(p, 0.8, 0.95, appEase);
        after.forEach(function (el) {
          el.style.opacity = c;
          el.style.transform = 'translateY(' + ((1 - c) * 8).toFixed(1) + 'px)';
        });
      }, 0.85, 0.4);   // shorter run: it sits low in its card, so finish while it's mid-screen
    }
    var pop = document.querySelector('.menubar-popover');
    if (pop) addScrubber(pop, popoverRenderer(pop, scrollEase), 0.85, 0.2);
    var diagram = document.querySelector('.pace-diagram');
    // Same idea for the diagram: start once it's up on screen, finish near the top.
    if (diagram) addScrubber(diagram, diagramRenderer(diagram, scrollEase), 0.85, 0.15);

    if (!scrubbers.length) return;
    update();
    window.addEventListener('scroll', requestUpdate, { passive: true });
    window.addEventListener('resize', requestUpdate);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
