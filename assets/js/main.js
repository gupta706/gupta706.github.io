/* =============================================================================
   Site behavior: theme toggle, mobile nav, BibTeX expand, publication
   filtering, and the client-side search overlay. Vanilla JS, no dependencies.
   ============================================================================= */
(function () {
  "use strict";

  /* ---- Dark / light theme -------------------------------------------------- */
  var toggle = document.getElementById("theme-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var cur = document.documentElement.getAttribute("data-theme") === "dark" ? "dark" : "light";
      var next = cur === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch (e) {}
    });
  }

  /* ---- Mobile navigation --------------------------------------------------- */
  var header = document.getElementById("site-header");
  var menuBtn = document.getElementById("menu-toggle");
  var mobileNav = document.getElementById("mobile-nav");
  if (menuBtn && header && mobileNav) {
    menuBtn.addEventListener("click", function () {
      var open = header.classList.toggle("open");
      menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
      mobileNav.hidden = !open;
    });
  }

  /* ---- BibTeX expand/collapse ---------------------------------------------- */
  document.addEventListener("click", function (e) {
    var btn = e.target.closest(".pill-bib");
    if (!btn) return;
    var pre = document.getElementById(btn.getAttribute("data-bib"));
    if (!pre) return;
    var show = pre.hidden;
    pre.hidden = !show;
    btn.setAttribute("aria-expanded", show ? "true" : "false");
    btn.classList.toggle("active", show);
  });

  /* ---- BibTeX copy-to-clipboard -------------------------------------------- */
  var copyKeys = /Mac|iPhone|iPad/.test(navigator.platform) ? "⌘C" : "Ctrl+C";

  function flashCopy(btn, ok) {
    btn.classList.remove("copied", "failed");
    btn.classList.add(ok ? "copied" : "failed");
    btn.textContent = ok ? "Copied!" : "Press " + copyKeys;
    if (btn._copyTimer) clearTimeout(btn._copyTimer);
    btn._copyTimer = setTimeout(function () {
      btn.classList.remove("copied", "failed");
      btn.textContent = "Copy";
    }, 1800);
  }

  // Fallback for contexts without the async Clipboard API (file://, some
  // sandboxed frames). Returns whether execCommand actually copied.
  function legacyCopy(text) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.setAttribute("readonly", "");
    ta.style.position = "fixed";
    ta.style.top = "0";
    ta.style.left = "0";
    ta.style.width = "1px";
    ta.style.height = "1px";
    ta.style.padding = "0";
    ta.style.border = "0";
    ta.style.opacity = "0";
    document.body.appendChild(ta);
    ta.focus();
    ta.select();
    var ok = false;
    try { ok = document.execCommand("copy"); } catch (err) { ok = false; }
    document.body.removeChild(ta);
    return ok;
  }

  // Last resort when nothing can write programmatically: select the entry so
  // the reader can copy it by hand with the keyboard.
  function selectContents(el) {
    try {
      var range = document.createRange();
      range.selectNodeContents(el);
      var sel = window.getSelection();
      sel.removeAllRanges();
      sel.addRange(range);
    } catch (err) {}
  }

  document.addEventListener("click", function (e) {
    var btn = e.target.closest(".pub-bib-copy");
    if (!btn) return;
    var pre = document.getElementById(btn.getAttribute("data-copy"));
    if (!pre) return;
    var text = pre.textContent;
    var fallback = function () {
      var ok = legacyCopy(text);
      if (!ok) selectContents(pre);
      flashCopy(btn, ok);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () { flashCopy(btn, true); }, fallback);
    } else {
      fallback();
    }
  });

  /* ---- Publication filtering (Publications page) --------------------------- */
  var filterBar = document.getElementById("pub-filters");
  var pubSearch = document.getElementById("pub-search");
  if (filterBar || pubSearch) {
    var groups = Array.prototype.slice.call(document.querySelectorAll(".pub-year-group"));
    var pubs = Array.prototype.slice.call(document.querySelectorAll(".pub"));
    var countEl = document.getElementById("pub-count");
    var curType = "all";

    function apply() {
      var q = (pubSearch && pubSearch.value || "").trim().toLowerCase();
      var shown = 0;
      pubs.forEach(function (el) {
        var okType = curType === "all" || el.getAttribute("data-type") === curType;
        var okText = !q || (el.getAttribute("data-search") || "").indexOf(q) !== -1;
        var vis = okType && okText;
        el.style.display = vis ? "" : "none";
        if (vis) shown++;
      });
      groups.forEach(function (g) {
        var any = g.querySelectorAll('.pub:not([style*="display: none"])').length > 0;
        // recompute robustly:
        var visible = Array.prototype.some.call(g.querySelectorAll(".pub"), function (p) { return p.style.display !== "none"; });
        g.style.display = visible ? "" : "none";
      });
      if (countEl) countEl.textContent = shown + (shown === 1 ? " publication" : " publications");
    }

    if (filterBar) {
      filterBar.addEventListener("click", function (e) {
        var b = e.target.closest(".pub-filter");
        if (!b) return;
        curType = b.getAttribute("data-filter");
        filterBar.querySelectorAll(".pub-filter").forEach(function (x) { x.classList.toggle("active", x === b); });
        apply();
      });
    }
    if (pubSearch) pubSearch.addEventListener("input", apply);
  }

  /* ---- Site search overlay ------------------------------------------------- */
  var overlay = document.getElementById("search-overlay");
  var openBtn = document.getElementById("search-open");
  var closeBtn = document.getElementById("search-close");
  var input = document.getElementById("search-input");
  var results = document.getElementById("search-results");
  var hint = document.getElementById("search-hint");
  var index = null, loading = false, activeIdx = -1;

  function loadIndex() {
    if (index || loading || !window.SEARCH_URL) return;
    loading = true;
    fetch(window.SEARCH_URL).then(function (r) { return r.json(); })
      .then(function (data) { index = data; })
      .catch(function () { index = []; });
  }

  function openSearch() {
    if (!overlay) return;
    loadIndex();
    overlay.hidden = false;
    document.body.style.overflow = "hidden";
    setTimeout(function () { if (input) input.focus(); }, 20);
  }
  function closeSearch() {
    if (!overlay) return;
    overlay.hidden = true;
    document.body.style.overflow = "";
    if (input) input.value = "";
    if (results) results.innerHTML = "";
    if (hint) hint.style.display = "";
    activeIdx = -1;
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  function render(items, q) {
    if (!results) return;
    if (!items.length) {
      results.innerHTML = "";
      if (hint) { hint.style.display = ""; hint.textContent = 'No matches for "' + q + '".'; }
      return;
    }
    if (hint) hint.style.display = "none";
    results.innerHTML = items.map(function (it, i) {
      return '<li><a href="' + it.url + '" class="' + (i === 0 ? "active" : "") + '">' +
        '<span class="sr-type">' + escapeHtml(it.type) + "</span> " +
        '<span class="sr-title">' + escapeHtml(it.title) + "</span>" +
        (it.meta ? '<div class="sr-meta">' + escapeHtml(it.meta) + "</div>" : "") +
        "</a></li>";
    }).join("");
    activeIdx = 0;
  }

  function search(q) {
    if (!index) { if (hint) hint.textContent = "Loading…"; return; }
    q = q.trim().toLowerCase();
    if (!q) { results.innerHTML = ""; if (hint) { hint.style.display = ""; hint.textContent = "Start typing to search across the site."; } return; }
    var terms = q.split(/\s+/);
    var scored = [];
    for (var i = 0; i < index.length; i++) {
      var hay = index[i].search || (index[i].title + " " + (index[i].meta || "")).toLowerCase();
      var ok = true, score = 0;
      for (var t = 0; t < terms.length; t++) {
        var pos = hay.indexOf(terms[t]);
        if (pos === -1) { ok = false; break; }
        score += (index[i].title.toLowerCase().indexOf(terms[t]) !== -1 ? 5 : 1);
      }
      if (ok) scored.push({ it: index[i], score: score });
    }
    scored.sort(function (a, b) { return b.score - a.score; });
    render(scored.slice(0, 12).map(function (s) { return s.it; }), q);
  }

  if (openBtn) openBtn.addEventListener("click", openSearch);
  if (closeBtn) closeBtn.addEventListener("click", closeSearch);
  if (overlay) overlay.addEventListener("click", function (e) { if (e.target === overlay) closeSearch(); });
  if (input) input.addEventListener("input", function () { search(input.value); });

  document.addEventListener("keydown", function (e) {
    if (e.key === "/" && overlay && overlay.hidden && !/input|textarea|select/i.test(document.activeElement.tagName)) {
      e.preventDefault(); openSearch(); return;
    }
    if (!overlay || overlay.hidden) return;
    if (e.key === "Escape") { closeSearch(); return; }
    var links = results ? results.querySelectorAll("a") : [];
    if (!links.length) return;
    if (e.key === "ArrowDown" || e.key === "ArrowUp") {
      e.preventDefault();
      links[activeIdx] && links[activeIdx].classList.remove("active");
      activeIdx = e.key === "ArrowDown"
        ? (activeIdx + 1) % links.length
        : (activeIdx - 1 + links.length) % links.length;
      links[activeIdx].classList.add("active");
      links[activeIdx].scrollIntoView({ block: "nearest" });
    } else if (e.key === "Enter" && links[activeIdx]) {
      window.location = links[activeIdx].getAttribute("href");
    }
  });
})();
