/* Tokenomics homepage: the menu bar popover is clickable.
 *
 * Each tab shows that tool's real meters (labels match the app). Codex has just
 * reset, so opening its tab plays the app's reset celebration: the 🎉 pop and
 * the confetti burst from ResetCelebrationView / ConfettiView, ported to canvas
 * with the same numbers (Tokens.Motion.Confetti). "Let's go" dismisses it and
 * shows the fresh meters. Opening Codex again replays it.
 *
 * With Reduce Motion on, tabs still switch and the celebration still shows,
 * just without movement or confetti.
 */
(function () {
  'use strict';
  var pop = document.querySelector('.menubar-popover');
  if (!pop) return;
  var body = pop.querySelector('.pop-body');
  var tabs = Array.prototype.slice.call(pop.querySelectorAll('.pop-tab[data-provider]'));
  var plan = pop.querySelector('[data-pop-plan]');
  if (!body || !tabs.length) return;
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // pct = used %, pace = where even use would sit (%), as in the app's bars.
  var PROVIDERS = {
    claude: { plan: 'Max', windows: [
      { title: '5-Hour Window', pct: 46, pace: 60, resets: 'Resets in 1h 36m' },
      { title: '7-Day Window', pct: 32, pace: 78, resets: 'Resets tomorrow' }
    ] },
    codex: { plan: 'Plus', celebrate: {
        title: 'Codex CLI is ready again',
        subtitle: 'Your 5-hour window reset. Ready to build!'
      }, windows: [
      { title: '5-Hour Window', pct: 0, pace: 0, resets: 'Resets in 5h' },
      { title: 'Weekly', pct: 41, pace: 52, resets: 'Resets in 3 days' }
    ] },
    gemini: { plan: 'Free', windows: [
      { title: 'Requests Today', pct: 28, pace: 40, resets: 'Estimated · Resets at midnight' }
    ] },
    copilot: { plan: 'Pro', windows: [
      { title: 'Premium Requests', pct: 64, pace: 55, resets: 'Resets Dec 1' }
    ] },
    cursor: { plan: 'Pro', windows: [
      { title: 'Premium Requests', pct: 22, pace: 48, resets: 'Resets in 12 days' }
    ] }
  };

  // The popover keeps its size as tabs change (one-meter tools would otherwise shrink it).
  // Measured while a two-meter tab is showing.
  function lockHeight() {
    if (body.querySelectorAll('.pop-section').length < 2) return;
    body.style.minHeight = ''; body.style.minHeight = body.offsetHeight + 'px';
  }

  function sectionHTML(w) {
    return '<div class="pop-section">' +
      '<div class="pop-section-head"><div class="pop-section-title">' + w.title + '</div>' +
      '<div class="pop-section-pct">0%</div></div>' +
      '<div class="pop-bar"><div class="pop-bar-fill" style="width:0%"></div>' +
      (w.pace > 0 ? '<div class="pop-bar-pace" style="left:0%"></div>' : '') + '</div>' +
      '<div class="pop-section-resets">' + w.resets + '</div></div>';
  }

  // Bars fill on the app's curve (500ms), pace dots trail (800ms), numbers count with the fill.
  function fillIn(windows) {
    var sections = body.querySelectorAll('.pop-section');
    windows.forEach(function (w, i) {
      var s = sections[i]; if (!s) return;
      var fill = s.querySelector('.pop-bar-fill'), dot = s.querySelector('.pop-bar-pace'), pct = s.querySelector('.pop-section-pct');
      if (reduceMotion) {
        fill.style.width = w.pct + '%'; if (dot) dot.style.left = w.pace + '%'; pct.textContent = w.pct + '%';
        return;
      }
      fill.style.transition = 'width 500ms cubic-bezier(.25,.46,.45,.94)';
      if (dot) dot.style.transition = 'left 800ms cubic-bezier(.25,.46,.45,.94)';
      requestAnimationFrame(function () { requestAnimationFrame(function () {
        fill.style.width = w.pct + '%';
        if (dot) dot.style.left = w.pace + '%';
      }); });
      var t0 = null;
      (function count(now) {
        if (t0 === null) t0 = now;
        var k = Math.min(1, (now - t0) / 500);
        pct.textContent = Math.round(w.pct * (1 - Math.pow(1 - k, 3))) + '%';
        if (k < 1) requestAnimationFrame(count);
      })(performance.now());
    });
  }

  function showMeters(id) {
    var p = PROVIDERS[id];
    body.innerHTML = p.windows.map(sectionHTML).join('<div class="pop-divider"></div>');
    fillIn(p.windows);
  }

  // ── Reset celebration ─────────────────────────────────────────────
  var overlay = null;
  function endCelebration() {
    if (!overlay) return;
    overlay.remove(); overlay = null;
    pop.classList.remove('celebrating');
  }
  function celebrate(id) {
    var c = PROVIDERS[id].celebrate;
    endCelebration();
    pop.classList.add('celebrating');
    overlay = document.createElement('div');
    overlay.className = 'pop-celebrate';
    overlay.innerHTML =
      '<canvas class="pop-confetti" aria-hidden="true"></canvas>' +
      '<div class="pop-celebrate-mark" aria-hidden="true">🎉</div>' +
      '<div class="pop-celebrate-title"></div>' +
      '<div class="pop-celebrate-sub"></div>' +
      '<button type="button" class="pop-celebrate-btn">Let’s go</button>';
    overlay.querySelector('.pop-celebrate-title').textContent = c.title;
    overlay.querySelector('.pop-celebrate-sub').textContent = c.subtitle;
    overlay.querySelector('.pop-celebrate-btn').addEventListener('click', function () {
      endCelebration();
      showMeters(id);
    });
    pop.appendChild(overlay);
    if (!reduceMotion) confetti(overlay.querySelector('canvas'));
  }

  // ── Confetti: ConfettiView's simulation, one canvas ───────────────
  // Spec mirrors Tokens.Motion.Confetti: burst from the top center, full 360° fan.
  var SPEC = { originX: 0.5, originY: 0, depth: 0.2, aim: 0, spread: 360, pop: 800,
               gravity: 1100, drag: 0.4, emit: 0.14, density: 1680 };
  function confetti(canvas) {
    var dark = document.documentElement.getAttribute('data-theme') === 'dark';
    var colors = dark
      ? ['#75CBF5', '#56A2D6', '#3389C7', '#F3EFE5', '#D9D1C0', '#6FD18A']
      : ['#75CBF5', '#56A2D6', '#2F84BF', '#286195', '#D9D1C0', '#2F8F4F'];
    var dpr = window.devicePixelRatio || 1;
    var w = canvas.clientWidth, h = canvas.clientHeight;
    canvas.width = w * dpr; canvas.height = h * dpr;
    var ctx = canvas.getContext('2d');
    ctx.scale(dpr, dpr);

    var col = 6, piles = new Array(Math.ceil(w / col) + 1).fill(0);
    var count = Math.round(SPEC.emit * SPEC.density), fan = SPEC.spread * Math.PI / 180;
    var ox = w * SPEC.originX, oy = h * SPEC.originY - 4;
    function rnd(a, b) { return a + Math.random() * (b - a); }
    var pieces = [];
    for (var n = 0; n < count; n++) {
      var angle = (SPEC.aim - 90) * Math.PI / 180 + (Math.random() - 0.5) * fan;
      var speed = SPEC.pop * Math.sqrt(Math.random());
      pieces.push({ born: n / count * SPEC.emit, x: ox, y: oy,
        vx: Math.cos(angle) * speed, vy: Math.sin(angle) * speed, z: 0, vz: SPEC.depth * rnd(2, 5),
        sway: rnd(0, 6.283), swayRate: rnd(3, 6), rot: rnd(0, 6.283), spin: rnd(-6, 6),
        flip: rnd(0, 6.283), flipRate: rnd(6, 14), size: rnd(5, 10), round: Math.random() < 0.25,
        color: colors[Math.floor(Math.random() * colors.length)], launched: false, landed: false, gone: false });
    }
    var start = null, last = null;
    function colIndex(x) { return Math.max(0, Math.min(piles.length - 1, Math.floor(x / col))); }
    function frame(now) {
      if (!canvas.isConnected) return;               // dismissed or replaced
      if (start === null) { start = last = now; }
      var dt = Math.min(0.05, (now - last) / 1000), t = (now - start) / 1000;
      last = now;
      var active = 0;
      ctx.clearRect(0, 0, w, h);
      pieces.forEach(function (p) {
        if (t < p.born) { active++; return; }
        p.launched = true;
        if (!p.gone && !p.landed) {
          active++;
          var k = Math.exp(-SPEC.drag * dt);
          p.vx *= k; p.vy = p.vy * k + SPEC.gravity * dt;
          p.sway += p.swayRate * dt;
          var flutter = Math.sin(p.sway) * 30 * Math.min(1, Math.max(0, p.vy) / 300);
          p.x += (p.vx + flutter) * dt; p.y += p.vy * dt;
          p.rot += p.spin * dt; p.flip += p.flipRate * dt;
          p.vz = (p.vz - p.z * 7 * dt) * Math.exp(-2.5 * dt);
          p.z = Math.max(0, p.z + p.vz * dt);
          if (p.x < -p.size || p.x > w + p.size) { p.gone = true; return; }
          var i = colIndex(p.x);
          if (p.y >= h - piles[i] - p.size * 0.2) {
            // Roll toward a lower neighbor so the pile spreads like sand.
            var step = p.size * 0.3;
            for (var s = 0; s < 6; s++) {
              var l = i > 0 ? piles[i - 1] : Infinity, r = i < piles.length - 1 ? piles[i + 1] : Infinity;
              if (piles[i] - Math.min(l, r) <= step) break;
              i = l < r ? i - 1 : i + 1;
              p.x = (i + 0.5) * col;
            }
            p.y = h - piles[i] - p.size * 0.2;
            piles[i] += step;
            p.landed = true; p.z = 0; p.flip = 0;
          }
        }
        if (p.gone) return;
        var zoom = 1 + p.z;
        ctx.save();
        ctx.translate(w / 2 + (p.x - w / 2) * zoom, h / 2 + (p.y - h / 2) * zoom);
        ctx.rotate(p.rot);
        ctx.scale(zoom, zoom * (Math.abs(Math.cos(p.flip)) * 0.8 + 0.2));
        ctx.fillStyle = p.color;
        if (p.round) { ctx.beginPath(); ctx.arc(0, 0, p.size / 2.4, 0, 6.283); ctx.fill(); }
        else ctx.fillRect(-p.size / 2, -p.size / 4, p.size, p.size / 2);
        ctx.restore();
      });
      if (active > 0 && t < 20) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }

  // ── Tabs ──────────────────────────────────────────────────────────
  function select(tab) {
    var id = tab.getAttribute('data-provider');
    pop.setAttribute('data-touched', '');            // motion.js stops scrubbing the bars
    tabs.forEach(function (t) {
      var on = t === tab;
      t.classList.toggle('active', on);
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      t.tabIndex = on ? 0 : -1;
    });
    if (plan) plan.textContent = PROVIDERS[id].plan;
    endCelebration();
    showMeters(id);
    if (PROVIDERS[id].celebrate) celebrate(id);
  }
  lockHeight();
  window.addEventListener('resize', lockHeight);
  tabs.forEach(function (t, i) {
    t.tabIndex = i === 0 ? 0 : -1;
    t.addEventListener('click', function () { if (!t.classList.contains('active') || PROVIDERS[t.getAttribute('data-provider')].celebrate) select(t); });
    // Arrow keys move between tabs, as in a standard tab list.
    t.addEventListener('keydown', function (e) {
      var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (!d) return;
      e.preventDefault();
      var next = tabs[(i + d + tabs.length) % tabs.length];
      next.focus(); select(next);
    });
  });
})();
