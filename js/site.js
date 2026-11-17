/* Praneel Mohan — site interactions (no dependencies) */
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const hoverable = matchMedia('(hover: hover)').matches;
  const WORK = window.PM_WORK || [];
  const byId = Object.fromEntries(WORK.map(w => [w.id, w]));
  const ICON = {
    play: '<svg viewBox="0 0 24 24" width="12" height="12" aria-hidden="true"><path d="M7 4l13 8-13 8z" fill="currentColor"/></svg>',
    arrow: '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M4 12h15m-6-6 6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
  };
  const TYPE = { video: 'Video', design: 'Design', thumb: 'Thumbnail' };

  /* ---------- nav: scrolled state, progress bar, mobile menu ---------- */
  const nav = $('.nav');
  if (nav) {
    const onScroll = () => {
      nav.classList.toggle('is-scrolled', scrollY > 8);
      const h = document.documentElement.scrollHeight - innerHeight;
      nav.style.setProperty('--p', h > 0 ? (scrollY / h).toFixed(4) : 0);
    };
    addEventListener('scroll', onScroll, { passive: true }); onScroll();
    const t = $('.nav__toggle');
    t?.addEventListener('click', () => {
      const open = nav.classList.toggle('is-open');
      t.setAttribute('aria-expanded', open); t.textContent = open ? 'Close' : 'Menu';
    });
    $$('.nav__links a').forEach(a => a.addEventListener('click', () => { nav.classList.remove('is-open'); t && (t.textContent = 'Menu', t.setAttribute('aria-expanded', false)); }));
  }

  /* ---------- hero rotating phrase ---------- */
  const rot = $('.rotator');
  if (rot && !reduce) {
    const items = $$('span', rot); let i = 0;
    setInterval(() => {
      const cur = items[i]; i = (i + 1) % items.length; const nxt = items[i];
      cur.classList.remove('is-on'); cur.classList.add('is-out');
      nxt.classList.remove('is-out'); nxt.classList.add('is-on');
      setTimeout(() => cur.classList.remove('is-out'), 600);
    }, 2600);
  }

  /* ---------- hero phone: story-style reel player ---------- */
  const phone = $('.phone');
  if (phone && WORK.length) {
    const ids = phone.dataset.reels.split(',');
    const reels = ids.map(id => byId[id]).filter(Boolean);
    const video = $('video', phone), bars = $('.phone__bars', phone);
    const title = $('.phone__meta strong', phone), role = $('.phone__meta span', phone);
    const sound = $('.phone__sound', phone);
    bars.innerHTML = reels.map(() => '<i></i>').join('');
    const segs = $$('i', bars); let idx = 0;
    const show = n => {
      idx = (n + reels.length) % reels.length; const r = reels[idx];
      segs.forEach((s, k) => s.style.setProperty('--f', k < idx ? 1 : 0));
      video.poster = r.poster; title.textContent = r.title; role.textContent = r.role;
      if (reduce) { video.removeAttribute('src'); return; }
      video.src = r.src; video.play().catch(() => {});
    };
    video.addEventListener('timeupdate', () => {
      const d = Math.min(video.duration || 1, 9);
      segs[idx]?.style.setProperty('--f', Math.min(video.currentTime / d, 1));
      if (video.currentTime >= 9) show(idx + 1);
    });
    video.addEventListener('ended', () => show(idx + 1));
    $('.phone__prev', phone).addEventListener('click', () => show(idx - 1));
    $('.phone__next', phone).addEventListener('click', () => show(idx + 1));
    sound.addEventListener('click', e => {
      e.stopPropagation(); video.muted = !video.muted;
      sound.textContent = video.muted ? 'Sound off' : 'Sound on';
      sound.setAttribute('aria-pressed', !video.muted);
    });
    // only load video once the hero is on screen
    new IntersectionObserver(([e]) => { if (e.isIntersecting) { show(idx); } else video.pause(); }, { threshold: .2 }).observe(phone);
  }

  /* ---------- marquee: duplicate list for a seamless loop ---------- */
  $$('.marquee__track').forEach(t => { const ul = $('ul', t); const c = ul.cloneNode(true); c.setAttribute('aria-hidden', 'true'); t.append(c); });

  /* ---------- in-view: counters, bars, reveals ---------- */
  const fmt = (n, d, loc = 'en-IN') => n.toLocaleString(loc, { minimumFractionDigits: d, maximumFractionDigits: d });
  const count = el => {
    const to = parseFloat(el.dataset.count), dec = (el.dataset.count.split('.')[1] || '').length;
    const pre = el.dataset.pre || '', suf = el.dataset.suf || '';
    const loc = el.dataset.loc || 'en-IN';
    if (reduce) { el.textContent = pre + fmt(to, dec, loc) + suf; return; }
    const t0 = performance.now(), dur = 1400;
    const tick = t => { const p = Math.min((t - t0) / dur, 1), e = 1 - Math.pow(1 - p, 4); el.textContent = pre + fmt(to * e, dec, loc) + suf; if (p < 1) requestAnimationFrame(tick); };
    requestAnimationFrame(tick);
  };
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return;
    const el = e.target; el.classList.add('is-in');
    $$('[data-count]', el).forEach(count);
    if (el.matches('[data-count]')) count(el);
    io.unobserve(el);
  }), { threshold: .25 });
  $$('.reveal, [data-inview]').forEach(el => io.observe(el));

  /* ---------- tiles for work pieces ---------- */
  const pieceHTML = (w, opts = {}) => {
    const vid = w.type === 'video';
    return `<button type="button" class="piece" data-id="${w.id}" data-cat="${w.cat}" data-type="${w.type}" style="--ar:${w.w}/${w.h};${opts.strip ? `aspect-ratio:${w.w}/${w.h}` : ''}" aria-label="Open ${w.title}">
      <img src="${w.poster}" alt="" loading="lazy" decoding="async" width="${w.w}" height="${w.h}">
      ${vid && hoverable ? '<video muted loop playsinline preload="none"></video>' : ''}
      <span class="piece__type">${vid ? ICON.play : ''}${TYPE[w.type]}</span>
      <span class="piece__cap"><strong>${w.title}</strong>${w.role}</span></button>`;
  };
  const wireHoverPlay = root => {
    if (!hoverable || reduce) return;
    $$('.piece[data-type="video"]', root).forEach(p => {
      const v = $('video', p); if (!v) return;
      p.addEventListener('mouseenter', () => { if (!v.src) v.src = byId[p.dataset.id].src; v.play().then(() => p.classList.add('is-playing')).catch(() => {}); });
      p.addEventListener('mouseleave', () => { v.pause(); p.classList.remove('is-playing'); });
    });
  };

  /* ---------- homepage strip ---------- */
  const strip = $('.strip');
  if (strip) {
    const pick = strip.dataset.ids.split(',').map(id => byId[id]).filter(Boolean);
    strip.innerHTML = pick.map(w => pieceHTML(w, { strip: true })).join('');
    wireHoverPlay(strip);
    // drag to scroll (mouse only)
    let down = false, sx = 0, sl = 0, moved = 0;
    strip.addEventListener('pointerdown', e => { if (e.pointerType !== 'mouse') return; down = true; moved = 0; sx = e.clientX; sl = strip.scrollLeft; });
    addEventListener('pointermove', e => { if (!down) return; const dx = e.clientX - sx; moved = Math.max(moved, Math.abs(dx)); if (moved > 6) strip.classList.add('is-drag'); strip.scrollLeft = sl - dx; });
    addEventListener('pointerup', () => { down = false; setTimeout(() => strip.classList.remove('is-drag'), 0); });
    strip.addEventListener('click', e => { if (moved > 6) { e.preventDefault(); e.stopPropagation(); } }, true);
  }

  /* ---------- gallery page ---------- */
  const grid = $('.grid[data-all]');
  if (grid) {
    const order = { realestate: 1, brands: 2, thumbnails: 3, creators: 4, stories: 5, jewellery: 6, ads: 0 };
    const items = [...WORK].sort((a, b) => (order[a.cat] ?? 9) - (order[b.cat] ?? 9));
    grid.innerHTML = items.map(w => pieceHTML(w)).join('');
    wireHoverPlay(grid);
    const chips = $$('.chip'), countEl = $('.filters__count'), empty = $('.empty');
    chips.forEach(c => { const f = c.dataset.filter; const n = f === 'all' ? items.length : items.filter(w => w.cat === f || w.type === f).length; c.insertAdjacentHTML('beforeend', `<sup>${n}</sup>`); if (!n) c.hidden = true; });
    const apply = f => {
      let n = 0;
      $$('.piece', grid).forEach(p => { const on = f === 'all' || p.dataset.cat === f || p.dataset.type === f; p.classList.toggle('is-hidden', !on); n += on; });
      chips.forEach(c => c.setAttribute('aria-pressed', c.dataset.filter === f));
      countEl.textContent = `Showing ${n} ${n === 1 ? 'piece' : 'pieces'}`;
      empty.hidden = n > 0;
      const u = new URL(location); f === 'all' ? u.searchParams.delete('f') : u.searchParams.set('f', f); history.replaceState(null, '', u);
    };
    chips.forEach(c => c.addEventListener('click', () => apply(c.dataset.filter)));
    const start = new URL(location).searchParams.get('f');
    apply(chips.some(c => c.dataset.filter === start) ? start : 'all');
  }

  /* ---------- static galleries on case pages ---------- */
  $$('[data-gallery]').forEach(g => {
    const v = g.dataset.gallery;
    const list = v.startsWith('cat:') ? WORK.filter(w => w.cat === v.slice(4)) : v.split(',').map(id => byId[id]).filter(Boolean);
    g.innerHTML = list.map(w => pieceHTML(w)).join(''); wireHoverPlay(g);
  });

  /* ---------- lightbox ---------- */
  const lb = $('#lightbox');
  if (lb) {
    const stage = $('.lb__stage', lb), t = $('.lb__cap strong', lb), r = $('.lb__cap span', lb), cnt = $('.lb__count', lb);
    let list = [], at = 0;
    const render = () => {
      const w = list[at];
      stage.innerHTML = w.type === 'video'
        ? `<video src="${w.src}" poster="${w.poster}" controls autoplay playsinline></video>`
        : `<img src="${w.src}" alt="${w.title}">`;
      t.textContent = w.title; r.textContent = w.role; cnt.textContent = `${at + 1} of ${list.length}`;
    };
    document.addEventListener('click', e => {
      const p = e.target.closest('.piece'); if (!p) return;
      const scope = p.parentElement;
      list = $$('.piece:not(.is-hidden)', scope).map(x => byId[x.dataset.id]);
      at = list.findIndex(w => w.id === p.dataset.id);
      render(); lb.showModal();
    });
    const go = d => { at = (at + d + list.length) % list.length; render(); };
    $('.lb__prev', lb).addEventListener('click', () => go(-1));
    $('.lb__next', lb).addEventListener('click', () => go(1));
    $('.lb__close', lb).addEventListener('click', () => lb.close());
    lb.addEventListener('close', () => { stage.innerHTML = ''; });
    lb.addEventListener('keydown', e => { if (e.key === 'ArrowRight') go(1); if (e.key === 'ArrowLeft') go(-1); });
    lb.addEventListener('click', e => { if (e.target === lb || e.target.classList.contains('lb__stage')) lb.close(); });
  }

  /* ---------- copy email ---------- */
  $$('.copy').forEach(b => b.addEventListener('click', async () => {
    const v = b.dataset.copy;
    try { await navigator.clipboard.writeText(v); b.classList.add('is-done'); setTimeout(() => b.classList.remove('is-done'), 1800); }
    catch { location.href = 'mailto:' + v; }
  }));

  $$('[data-year]').forEach(y => y.textContent = new Date().getFullYear());
})();
