/* Praneel Mohan portfolio v4 — interactions */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Mobile menu
  var mb = document.querySelector('.menu-btn'), nav = document.querySelector('.nav');
  if (mb && nav) mb.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    mb.setAttribute('aria-expanded', open ? 'true' : 'false');
    mb.textContent = open ? 'Close' : 'Menu';
  });

  // Reveal, chart and count-up when in view
  // Numbers are rendered final in the markup: no count-up, so nothing shifts while reading.
  function countUp() {}
  var targets = document.querySelectorAll('[data-reveal], .chart, .gbars, [data-count]');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        el.classList.add('in');
        if (el.hasAttribute('data-count')) countUp(el);
        io.unobserve(el);
      });
    }, { threshold: 0.2, rootMargin: '0px 0px -40px 0px' });
    targets.forEach(function (el) { io.observe(el); });
  } else {
    targets.forEach(function (el) { el.classList.add('in'); if (el.hasAttribute('data-count')) countUp(el); });
  }

  // Hero services panel: highlights one service at a time
  var sv = document.querySelector('[data-svcx]');
  if (sv && !reduce) {
    var rows = sv.querySelectorAll('.sx'), si = 0, st = null;
    function on(n) {
      rows.forEach(function (r) { r.classList.remove('is-on'); });
      void sv.offsetWidth;
      rows[n].classList.add('is-on'); si = n;
    }
    function run() { stop2(); st = setInterval(function () { on((si + 1) % rows.length); }, 3400); }
    function stop2() { if (st) clearInterval(st); st = null; }
    rows.forEach(function (r, i) { r.addEventListener('mouseenter', function () { stop2(); on(i); }); });
    sv.addEventListener('mouseleave', run);
    document.addEventListener('visibilitychange', function () { document.hidden ? stop2() : run(); });
    if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { es[0].isIntersecting ? run() : stop2(); }).observe(sv);
    else run();
  }

  // Lightbox for videos and images
  var lb = document.createElement('div');
  lb.className = 'lb';
  lb.setAttribute('role', 'dialog');
  lb.setAttribute('aria-modal', 'true');
  lb.setAttribute('aria-label', 'Media viewer');
  lb.innerHTML = '<button class="lb-close" type="button" aria-label="Close"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button><div class="lb-inner"></div>';
  document.body.appendChild(lb);
  var inner = lb.querySelector('.lb-inner'), closeBtn = lb.querySelector('.lb-close'), lastFocus = null;
  function close() {
    lb.classList.remove('open');
    inner.innerHTML = '';
    document.body.style.overflow = '';
    if (lastFocus) lastFocus.focus();
  }
  function open(html) {
    lastFocus = document.activeElement;
    inner.innerHTML = html;
    lb.classList.add('open');
    document.body.style.overflow = 'hidden';
    closeBtn.focus();
  }
  closeBtn.addEventListener('click', close);
  lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && lb.classList.contains('open')) close(); });
  function esc(s) { return String(s || '').replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  document.addEventListener('click', function (e) {
    var v = e.target.closest('[data-video]');
    if (v) {
      e.preventDefault();
      var id = v.getAttribute('data-video'), t = v.getAttribute('data-title') || '';
      open('<video controls autoplay playsinline preload="metadata" poster="assets/posters/' + esc(id) + '.webp" src="assets/videos/' + esc(id) + '.mp4"></video><p class="lb-title">' + esc(t) + '</p>');
      return;
    }
    var im = e.target.closest('[data-img]');
    if (im) {
      e.preventDefault();
      open('<img src="' + esc(im.getAttribute('data-img')) + '" alt="' + esc(im.getAttribute('data-title')) + '"><p class="lb-title">' + esc(im.getAttribute('data-title')) + '</p>');
    }
  });

  // Work page filters
  var chips = document.querySelectorAll('.chip[data-filter]');
  if (chips.length) {
    var secs = document.querySelectorAll('.wsec[data-cat]');
    function apply(f) {
      chips.forEach(function (c) { c.setAttribute('aria-pressed', c.getAttribute('data-filter') === f ? 'true' : 'false'); });
      secs.forEach(function (s) { s.hidden = !(f === 'all' || s.getAttribute('data-cat').split(' ').indexOf(f) > -1); });
      if (history.replaceState) history.replaceState(null, '', f === 'all' ? location.pathname : '#' + f);
    }
    chips.forEach(function (c) { c.addEventListener('click', function () { apply(c.getAttribute('data-filter')); }); });
    var h = location.hash.slice(1);
    if (h && document.querySelector('.chip[data-filter="' + h + '"]')) apply(h);
  }

  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
