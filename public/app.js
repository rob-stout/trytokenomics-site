/* ============================================================
   Tokenomics — Landing Page Script
   No frameworks. Pure vanilla JS.
   ============================================================ */

(function () {
  'use strict';

  // ── Theme Toggle ─────────────────────────────────────────
  // Persists in localStorage. On first visit, honors prefers-color-scheme.
  // Toggle button label reflects current opposite state ("Dark" = click to go dark).

  var html     = document.documentElement;
  var themeKey = 'tokenomics-theme';

  function applyTheme(theme) {
    if (theme === 'dark') {
      html.setAttribute('data-theme', 'dark');
    } else {
      html.removeAttribute('data-theme');
    }
    localStorage.setItem(themeKey, theme);
    updateToggleLabel(theme);
  }

  function updateToggleLabel(theme) {
    var btn = document.getElementById('themeToggle');
    if (!btn) return;
    btn.textContent = theme === 'dark' ? 'Light' : 'Dark';
    btn.setAttribute('aria-label', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
  }

  function initTheme() {
    var saved = localStorage.getItem(themeKey);
    if (saved) {
      applyTheme(saved);
    } else {
      // Honor system preference on first visit
      var prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      applyTheme(prefersDark ? 'dark' : 'light');
    }
  }

  function toggleTheme() {
    var current = html.getAttribute('data-theme');
    applyTheme(current === 'dark' ? 'light' : 'dark');
  }

  // ── Copy to Clipboard ────────────────────────────────────
  // Wires any button with [data-copy] attribute.
  // Expects .copy-icon and .copy-check children inside the button.

  function initCopyButtons() {
    document.querySelectorAll('[data-copy]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var text = btn.getAttribute('data-copy');
        if (!navigator.clipboard) {
          // Fallback for file:// protocol
          var el = document.createElement('textarea');
          el.value = text;
          el.style.position = 'fixed';
          el.style.opacity = '0';
          document.body.appendChild(el);
          el.focus();
          el.select();
          try { document.execCommand('copy'); } catch (e) {}
          document.body.removeChild(el);
          showCopyConfirm(btn);
          return;
        }
        navigator.clipboard.writeText(text).then(function () {
          showCopyConfirm(btn);
        }).catch(function () {
          // Silently fail — the text is visible to copy manually
        });
      });
    });
  }

  function showCopyConfirm(btn) {
    var icon  = btn.querySelector('.copy-icon');
    var check = btn.querySelector('.copy-check');
    var label = btn.lastChild;
    if (icon)  icon.style.display  = 'none';
    if (check) check.style.display = 'block';
    if (label && label.nodeType === Node.TEXT_NODE) {
      label.textContent = 'Copied';
    }
    setTimeout(function () {
      if (icon)  icon.style.display  = '';
      if (check) check.style.display = 'none';
      if (label && label.nodeType === Node.TEXT_NODE) {
        label.textContent = 'Copy';
      }
    }, 1800);
  }

  // ── Install Tabs ─────────────────────────────────────────

  function initInstallTabs() {
    var tabs   = document.querySelectorAll('.install-tab');
    var panels = document.querySelectorAll('.install-panel');

    tabs.forEach(function (tab) {
      tab.addEventListener('click', function () {
        var target = tab.getAttribute('data-tab');

        tabs.forEach(function (t) {
          var isActive = t === tab;
          t.classList.toggle('active', isActive);
          t.setAttribute('aria-selected', isActive ? 'true' : 'false');
        });

        panels.forEach(function (p) {
          var isActive = p.id === 'panel-' + target;
          p.classList.toggle('active', isActive);
        });
      });
    });
  }

  // ── Nav active link highlighting ─────────────────────────
  // Highlights nav links as sections scroll into view.

  function initNavHighlight() {
    var navLinks = document.querySelectorAll('.nav-links a[href^="#"]');
    if (!navLinks.length || !('IntersectionObserver' in window)) return;

    var sectionMap = {};
    navLinks.forEach(function (link) {
      var id = link.getAttribute('href').slice(1);
      var section = document.getElementById(id);
      if (section) sectionMap[id] = link;
    });

    var sectionObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var link = sectionMap[entry.target.id];
        if (!link) return;
        if (entry.isIntersecting) {
          navLinks.forEach(function (l) { l.style.color = ''; });
          link.style.color = 'var(--text)';
        }
      });
    }, { rootMargin: '-20% 0px -70% 0px' });

    Object.keys(sectionMap).forEach(function (id) {
      var section = document.getElementById(id);
      if (section) sectionObserver.observe(section);
    });
  }

  // ── Init ─────────────────────────────────────────────────

  // Theme runs synchronously before paint to avoid flash
  initTheme();

  document.addEventListener('DOMContentLoaded', function () {
    var toggleBtn = document.getElementById('themeToggle');
    if (toggleBtn) {
      toggleBtn.addEventListener('click', toggleTheme);
      // Sync label with current state
      var currentTheme = html.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
      updateToggleLabel(currentTheme);
    }

    initCopyButtons();
    initInstallTabs();

    initNavHighlight();
    initProviderFlip();
    initHashDetails();
  });

  // ── Auto-open <details> when linked by URL hash ──────────
  function initHashDetails() {
    function openFromHash() {
      var hash = window.location.hash;
      if (!hash) return;
      var target = document.querySelector(hash);
      if (target && target.tagName === 'DETAILS') {
        target.open = true;
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }
    openFromHash();
    window.addEventListener('hashchange', openFromHash);
  }

  // ---------- Rotating provider in hero — box rolling backwards ----------
  function initProviderFlip() {
    var el = document.getElementById('flipWord');
    if (!el) return;
    var words = [
      'Claude.', 'GitHub Copilot.', 'Cursor.',
      'OpenAI.', 'Gemini.',
      'Stability AI.', 'Runway.', 'ElevenLabs.'
    ];
    var i = 0;
    var PHASE = 300;    // must match animation duration
    var HOLD = 2400;    // time each provider is fully visible

    setInterval(function () {
      // Phase 1: current word rolls away from viewer (top tilts back).
      el.classList.add('rolling-out');
      setTimeout(function () {
        // Swap text while invisible, then roll the new word in from the front.
        i = (i + 1) % words.length;
        el.textContent = words[i];
        el.classList.remove('rolling-out');
        el.classList.add('rolling-in');
        setTimeout(function () {
          el.classList.remove('rolling-in');
        }, PHASE);
      }, PHASE);
    }, HOLD);
  }

  // ── Latest release — version badge ───────────────────────
  // Updates .js-version pills from /api/latest-version (a same-site function
  // that asks GitHub, so visitors' browsers never contact GitHub). Download links go through
  // /download/dmg/latest so the Cloudflare Pages Function can count them and
  // redirect to the right release — no client-side href rewrite needed.

  (function fetchLatestRelease() {
    var badges = document.querySelectorAll('.js-version');
    if (!badges.length) return;

    fetch('/api/latest-version')
      .then(function (res) { return res.ok ? res.json() : null; })
      .then(function (data) {
        if (!data || !data.tag) return;
        var tag = data.tag;
        badges.forEach(function (el) {
          el.textContent = tag + ' · macOS 14+';
        });
      })
      .catch(function () { /* keep hardcoded fallback */ });
  })();

})();
