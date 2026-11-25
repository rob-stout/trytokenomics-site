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
  var ease = bezier(0.25, 0.46, 0.45, 0.94);
  function clamp(x) { return x < 0 ? 0 : x > 1 ? 1 : x; }
  // Progress through a slice [from, to] of the overall 0→1, eased.
  function seg(p, from, to) { return ease(clamp((p - from) / (to - from))); }

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
  function widgetRenderer(w) {
    var rows = Array.prototype.slice.call(w.querySelectorAll('.bar-row, .row-compact, .row-large .metrics > *'));
    function rowOf(el) {
      for (var i = 0; i < rows.length; i++) if (rows[i].contains(el)) return Math.min(i, 6);
      return 0;
    }
    var fills = [], paces = [];
    // Fill runs over the first ~60% of the widget's progress, offset a little per row;
    // the pace dot uses the whole range, so it trails and lands last (500ms vs 800ms in the app).
    function addFill(render, el) { var o = rowOf(el) * 0.05; fills.push(function (p) { render(seg(p, o, o + 0.62)); }); }
    function addPace(render, el) { var o = rowOf(el) * 0.05; paces.push(function (p) { render(seg(p, o, Math.min(1, o + 1))); }); }

    w.querySelectorAll('.pbar .fill').forEach(function (f) { addFill(barPiece(f), f); });
    w.querySelectorAll('.pbar .pace').forEach(function (d) { addPace(pacePiece(d), d); });
    w.querySelectorAll('.pct').forEach(function (el) { var r = countPiece(el); if (r) addFill(r, el); });
    collect(w, 'svg circle[stroke-dasharray]', ringPiece).forEach(function (r) { fills.push(function (p) { r(seg(p, 0, 0.62)); }); });
    collect(w, 'svg text', countPiece).forEach(function (r) { fills.push(function (p) { r(seg(p, 0, 0.62)); }); });
    collect(w, 'svg circle[transform*="rotate"]:not([stroke-dasharray])', ringDotPiece).forEach(function (r) { paces.push(function (p) { r(seg(p, 0, 1)); }); });
    var all = fills.concat(paces);
    if (!all.length) return null;
    return function (p) { all.forEach(function (f) { f(p); }); };
  }

  // ── Pace diagram: rings → dots → each callout line, then its label ───
  function diagramRenderer(d) {
    var parts = [];
    collect(d, 'circle[stroke-dasharray]', ringPiece).forEach(function (r) { parts.push(function (p) { r(seg(p, 0, 0.32)); }); });
    collect(d, 'svg text', countPiece).forEach(function (r) { parts.push(function (p) { r(seg(p, 0, 0.32)); }); });
    collect(d, '.pace-dot', ringDotPiece).forEach(function (r) { parts.push(function (p) { r(seg(p, 0, 0.46)); }); });

    // Three callouts share the rest of the range. Each line draws from the ring
    // outward (segments in document order), then its label fades in.
    var start = 0.46, slot = 0.18;
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
        parts.push(function (p) { r(seg(p, a, b)); });
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

  function init() {
    document.querySelectorAll('.widget').forEach(function (w) {
      var render = widgetRenderer(w);
      if (!render) return;
      if (w.closest('.hero')) playOnce(render, 900);
      // Widgets fill as they rise from the bottom edge to about 45% up the screen.
      else addScrubber(w, render, 1.0, 0.45);
    });
    var diagram = document.querySelector('.pace-diagram');
    // The diagram gets a longer stretch of scroll: it starts as it enters and
    // finishes when its top is near the top of the screen.
    if (diagram) addScrubber(diagram, diagramRenderer(diagram), 0.95, 0.12);

    if (!scrubbers.length) return;
    update();
    window.addEventListener('scroll', requestUpdate, { passive: true });
    window.addEventListener('resize', requestUpdate);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
