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

  // ── Scroll Animations (IntersectionObserver) ─────────────
  // Respects prefers-reduced-motion: skip animation, snap to final state.

  function initScrollAnimations() {
    var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (reducedMotion) {
      // Snap everything to final state immediately
      document.querySelectorAll('.reveal, .craft-card').forEach(function (el) {
        el.classList.add('animated');
      });
      return;
    }

    if (!('IntersectionObserver' in window)) {
      document.querySelectorAll('.reveal, .craft-card').forEach(function (el) {
        el.classList.add('animated');
      });
      return;
    }

    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var delay = parseInt(entry.target.getAttribute('data-delay') || '0', 10);
        setTimeout(function () {
          entry.target.classList.add('animated');
        }, delay);
        revealObserver.unobserve(entry.target);
      });
    }, { threshold: 0.12 });

    document.querySelectorAll('.reveal').forEach(function (el, i) {
      if (!el.hasAttribute('data-delay')) {
        el.setAttribute('data-delay', Math.min(i % 3 * 80, 160));
      }
      revealObserver.observe(el);
    });

    // Craft cards stagger independently
    var craftObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var delay = parseInt(entry.target.getAttribute('data-delay') || '0', 10);
        setTimeout(function () {
          entry.target.classList.add('animated');
        }, delay);
        craftObserver.unobserve(entry.target);
      });
    }, { threshold: 0.1 });

    document.querySelectorAll('.craft-card').forEach(function (el, i) {
      el.setAttribute('data-delay', i * 60);
      craftObserver.observe(el);
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
    initScrollAnimations();
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

  // ── Latest release — version badge + download links ──────
  // Rewrites .js-version pills and .js-download hrefs from the GitHub API.
  // Falls back silently to the hardcoded values if the API call fails.

  (function fetchLatestRelease() {
    var badges    = document.querySelectorAll('.js-version');
    var downloads = document.querySelectorAll('.js-download');
    if (!badges.length && !downloads.length) return;

    fetch('https://api.github.com/repos/rob-stout/Tokenomics/releases/latest', {
      headers: { 'Accept': 'application/vnd.github+json' }
    })
      .then(function (res) { return res.ok ? res.json() : null; })
      .then(function (data) {
        if (!data) return;
        if (data.tag_name) {
          var tag = data.tag_name.replace(/^v?/, 'v');
          badges.forEach(function (el) {
            el.textContent = tag + ' · macOS 14+';
          });
        }
        var dmg = (data.assets || []).find(function (a) {
          return a.name && /\.dmg$/i.test(a.name);
        });
        if (dmg && dmg.browser_download_url) {
          downloads.forEach(function (el) {
            el.setAttribute('href', dmg.browser_download_url);
          });
        }
      })
      .catch(function () { /* keep hardcoded fallback */ });
  })();

})();
