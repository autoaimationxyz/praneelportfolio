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

  // Hero stage: cycles through three real examples
  var stage = document.querySelector('[data-stage]');
  if (stage) {
    var scenes = stage.querySelectorAll('[data-scene]'), tabs = stage.querySelectorAll('.st'), cur = 0, timer = null, DUR = 5600, loaded = false;
    function loadRest() {
      if (loaded) return; loaded = true;
      stage.querySelectorAll('img[data-src]').forEach(function (im) { im.src = im.getAttribute('data-src'); });
    }
    function count(el) {
      var a = +el.getAttribute('data-from'), b = +el.getAttribute('data-to'), t0 = null;
      if (reduce) { el.textContent = b + 'K'; return; }
      el.textContent = a + 'K';
      function step(t) {
        if (!t0) t0 = t;
        var p = Math.min(1, (t - t0) / 1400), v = Math.round(a + (b - a) * (1 - Math.pow(1 - p, 3)));
        el.textContent = v + 'K';
        if (p < 1) requestAnimationFrame(step);
      }
      setTimeout(function () { requestAnimationFrame(step); }, 350);
    }
    function show(n) {
      cur = n;
      scenes.forEach(function (el) {
        var on = +el.getAttribute('data-scene') === n;
        el.classList.toggle('is-on', false);
        if (on) { void el.offsetWidth; el.classList.add('is-on'); }
      });
      tabs.forEach(function (b, i) {
        var on = i === n, bar = b.querySelector('i i');
        b.classList.toggle('is-on', on); b.setAttribute('aria-pressed', on ? 'true' : 'false');
        if (bar) { bar.style.animation = 'none'; void bar.offsetWidth; bar.style.animation = ''; }
      });
      var c = stage.querySelector('.is-on [data-to]');
      if (c) count(c);
      if (n > 0) loadRest();
    }
    function play() { if (reduce) return; stop(); timer = setInterval(function () { show((cur + 1) % 3); }, DUR); stage.classList.remove('paused'); }
    function stop() { if (timer) clearInterval(timer); timer = null; }
    tabs.forEach(function (b) {
      b.addEventListener('click', function () { show(+b.getAttribute('data-go')); play(); });
    });
    stage.addEventListener('mouseenter', function () { stop(); stage.classList.add('paused'); });
    stage.addEventListener('mouseleave', function () {
      var bar = stage.querySelector('.st.is-on i i');
      if (bar) { bar.style.animation = 'none'; void bar.offsetWidth; bar.style.animation = ''; }
      play();
    });
    document.addEventListener('visibilitychange', function () { document.hidden ? stop() : play(); });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) { es[0].isIntersecting ? play() : stop(); }).observe(stage);
    } else play();
    window.addEventListener('load', function () { setTimeout(loadRest, 1200); });
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
