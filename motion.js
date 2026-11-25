/* Tokenomics homepage motion: the app's own usage animations, played once
 * as each widget or the pace diagram scrolls into view.
 *
 * Timing matches the Mac app (Tokens.Motion in Tokens.swift):
 *   bars / rings fill 0 → value in 500ms, cubic-bezier(.25,.46,.45,.94)
 *   the pace dot rides in on the same curve over 800ms, so it lands last
 *   percentages count up with the fill
 *
 * Without JS, or with Reduce Motion on, everything shows in its final state:
 * this script only sets the starting state right before it animates.
 */
(function () {
  'use strict';
  if (!('IntersectionObserver' in window)) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  var FILL_MS = 500;
  var PACE_MS = 800;
  var EASE_CSS = 'cubic-bezier(.25,.46,.45,.94)';

  // cubic-bezier(.25,.46,.45,.94) solved numerically, for the JS-driven parts
  // (counting numbers, dots moving along a ring) so they stay in step with CSS.
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
        var d = at(t, x1, x2) - x;
        var s = slope(t, x1, x2);
        if (Math.abs(d) < 1e-5 || s === 0) break;
        t -= d / s;
      }
      return at(t, y1, y2);
    };
  }
  var ease = bezier(0.25, 0.46, 0.45, 0.94);

  function tween(ms, delay, step) {
    var start = null;
    function frame(now) {
      if (start === null) start = now;
      var p = Math.min(1, (now - start) / ms);
      step(ease(p));
      if (p < 1) requestAnimationFrame(frame);
    }
    setTimeout(function () { requestAnimationFrame(frame); }, delay || 0);
  }

  // ── Pieces ────────────────────────────────────────────────────────
  // Each "prepare" puts an element at its start state and returns a
  // function that plays it to the final state.

  function prepareBar(fill) {
    var target = fill.style.width;
    fill.style.transition = 'none';
    fill.style.width = '0%';
    return function (delay) {
      setTimeout(function () {
        fill.style.transition = 'width ' + FILL_MS + 'ms ' + EASE_CSS;
        fill.style.width = target;
      }, delay);
    };
  }

  function preparePace(dot) {
    var target = dot.style.left;
    dot.style.transition = 'none';
    dot.style.left = '0%';
    return function (delay) {
      setTimeout(function () {
        dot.style.transition = 'left ' + PACE_MS + 'ms ' + EASE_CSS;
        dot.style.left = target;
      }, delay);
    };
  }

  // Text like "90%" or "45 sec ago" — only a leading number followed by % counts up.
  function prepareCount(el, ms) {
    var m = /^(\s*)(\d+)(%.*)$/.exec(el.textContent);
    if (!m) return null;
    var target = parseInt(m[2], 10);
    el.textContent = m[1] + '0' + m[3];
    return function (delay) {
      tween(ms || FILL_MS, delay, function (k) {
        el.textContent = m[1] + Math.round(target * k) + m[3];
      });
    };
  }

  // A ring arc drawn with stroke-dasharray / stroke-dashoffset.
  function prepareRing(arc, ms) {
    var full = parseFloat(arc.getAttribute('stroke-dasharray'));
    var target = parseFloat(arc.getAttribute('stroke-dashoffset'));
    if (!full || isNaN(target)) return null;
    arc.setAttribute('stroke-dashoffset', full);
    return function (delay) {
      tween(ms || FILL_MS, delay, function (k) {
        arc.setAttribute('stroke-dashoffset', full + (target - full) * k);
      });
    };
  }

  // A pace dot placed on a ring with transform="rotate(angle [cx cy]) translate(...)".
  function prepareRingDot(dot, ms) {
    var t = dot.getAttribute('transform') || '';
    var m = /rotate\(\s*(-?[\d.]+)/.exec(t);
    if (!m) return null;
    var target = parseFloat(m[1]);
    function set(angle) {
      dot.setAttribute('transform', t.replace(/rotate\(\s*-?[\d.]+/, 'rotate(' + angle.toFixed(2)));
    }
    set(0);
    return function (delay) {
      tween(ms || PACE_MS, delay, function (k) { set(target * k); });
    };
  }

  function onEnter(el, play, threshold) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        io.unobserve(e.target);
        play();
      });
    }, { threshold: threshold || 0.4 });
    io.observe(el);
  }

  // ── Widgets: bars, rings, pace dots, percentages ──────────────────
  function initWidget(w) {
    var plays = [];
    // Rows fill one after another, like the app's rows settling in.
    var rows = w.querySelectorAll('.bar-row, .row-compact .col, .row-large, .w-rows > *');
    var rowIndex = new Map();
    Array.prototype.forEach.call(rows, function (r, i) { rowIndex.set(r, i); });
    function stagger(el) {
      var p = el.parentElement;
      while (p && p !== w) {
        if (rowIndex.has(p)) return Math.min(rowIndex.get(p), 6) * 70;
        p = p.parentElement;
      }
      return 0;
    }

    w.querySelectorAll('.pbar .fill').forEach(function (f) {
      var play = prepareBar(f); plays.push(function () { play(stagger(f)); });
    });
    w.querySelectorAll('.pbar .pace').forEach(function (d) {
      var play = preparePace(d); plays.push(function () { play(stagger(d)); });
    });
    w.querySelectorAll('.pct').forEach(function (p) {
      var play = prepareCount(p); if (play) plays.push(function () { play(stagger(p)); });
    });
    w.querySelectorAll('svg circle[stroke-dasharray]').forEach(function (arc) {
      var play = prepareRing(arc); if (play) plays.push(function () { play(0); });
    });
    w.querySelectorAll('svg circle[transform*="rotate"]').forEach(function (dot) {
      var play = prepareRingDot(dot); if (play) plays.push(function () { play(0); });
    });
    w.querySelectorAll('svg text').forEach(function (t) {
      var play = prepareCount(t); if (play) plays.push(function () { play(0); });
    });
    if (!plays.length) return;
    onEnter(w, function () { plays.forEach(function (p) { p(); }); }, 0.45);
  }

  // ── Pace diagram: rings fill, dots ride in, then each callout's line
  //    draws toward the thing it explains and its label fades in. ─────
  function initPaceDiagram(d) {
    var RING_MS = 900, DOT_MS = 1300;   // larger than a widget, so a touch slower
    var plays = [];
    d.querySelectorAll('circle[stroke-dasharray]').forEach(function (arc) {
      var play = prepareRing(arc, RING_MS); if (play) plays.push(function () { play(0); });
    });
    d.querySelectorAll('.pace-dot').forEach(function (dot) {
      var play = prepareRingDot(dot, DOT_MS); if (play) plays.push(function () { play(0); });
    });
    d.querySelectorAll('svg text').forEach(function (t) {
      var play = prepareCount(t, RING_MS); if (play) plays.push(function () { play(0); });
    });

    // Callouts: lines draw from the ring outward (the order they're written in),
    // then the label appears. Steps follow one another.
    var LINE_MS = 320, LABEL_MS = 280, GAP = 120;
    var t0 = DOT_MS - 150;
    [1, 2, 3].forEach(function (step) {
      var lines = d.querySelectorAll('.callout-line[data-step="' + step + '"]');
      var labels = d.querySelectorAll('.callout-label[data-step="' + step + '"]');
      var delay = t0;
      Array.prototype.forEach.call(lines, function (line) {
        var len = Math.hypot(line.x2.baseVal.value - line.x1.baseVal.value,
                             line.y2.baseVal.value - line.y1.baseVal.value);
        var segMs = LINE_MS * 0.5;
        var start = delay;
        line.style.strokeDasharray = len;
        line.style.strokeDashoffset = len;
        plays.push(function () {
          setTimeout(function () {
            line.style.transition = 'stroke-dashoffset ' + segMs + 'ms linear';
            line.style.strokeDashoffset = '0';
          }, start);
        });
        delay += segMs;
      });
      Array.prototype.forEach.call(labels, function (label) {
        var at = delay;
        label.style.opacity = '0';
        label.style.transform = label.tagName.toLowerCase() === 'text' ? '' : 'translateX(-6px)';
        plays.push(function () {
          setTimeout(function () {
            label.style.transition = 'opacity ' + LABEL_MS + 'ms ' + EASE_CSS + ', transform ' + LABEL_MS + 'ms ' + EASE_CSS;
            label.style.opacity = '';
            label.style.transform = '';
          }, at);
        });
      });
      t0 = delay + LABEL_MS * 0.6 + GAP;
    });
    if (!plays.length) return;
    onEnter(d, function () { plays.forEach(function (p) { p(); }); }, 0.5);
  }

  function init() {
    document.querySelectorAll('.widget').forEach(initWidget);
    var diagram = document.querySelector('.pace-diagram');
    if (diagram) initPaceDiagram(diagram);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
