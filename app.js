const filterButtons = document.querySelectorAll('[data-filter]');
const menuToggle = document.querySelector('#menu-toggle');
const mainNavigation = document.querySelector('#main-navigation');
menuToggle?.addEventListener('click', () => {
  const open = menuToggle.getAttribute('aria-expanded') !== 'true';
  menuToggle.setAttribute('aria-expanded', String(open));
  mainNavigation.classList.toggle('is-open', open);
});
mainNavigation?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
  menuToggle.setAttribute('aria-expanded', 'false');
  mainNavigation.classList.remove('is-open');
}));
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && menuToggle?.getAttribute('aria-expanded') === 'true') {
    menuToggle.setAttribute('aria-expanded', 'false');
    mainNavigation.classList.remove('is-open');
    menuToggle.focus();
  }
});
filterButtons.forEach(button => button.addEventListener('click', () => {
  filterButtons.forEach(b => { b.classList.toggle('active', b === button); b.setAttribute('aria-pressed', String(b === button)); });
  document.querySelectorAll('.project').forEach(project => { project.hidden = button.dataset.filter !== 'all' && project.dataset.category !== button.dataset.filter; });
}));

const projectDialog = document.querySelector('#project-dialog');
const projectContent = document.querySelector('#dialog-content');
const projectDetails = {
  revcore: `<span class="eyebrow">FOUNDER PORTFOLIO / REVCORE AUTOS</span><h2 id="dialog-title">Automotive stories.<br>Made for the screen.</h2><p>RevCore Autos is an automotive channel built around a working garage. Praneel’s work spans content planning, video editing, social media and thumbnail creative.</p><img src="assets/revcore-z4.webp" width="1600" height="900" alt="BMW Z4 exhaust modification thumbnail for RevCore Autos"><div class="detail-grid"><div><h3>The work</h3><p>Content and creative support for technical automotive stories, with attention to clear narratives, visual impact and channel presentation.</p></div><div><h3>About this sample</h3><p>A YouTube thumbnail creative featuring the BMW Z4. Shown as earlier founder portfolio work, rather than a claim that the project was commissioned through Praneel Mohan.</p></div></div><a class="button dark" href="https://www.youtube.com/@revcoreautos" target="_blank" rel="noopener noreferrer">Explore the channel ↗</a>`,
  tlc: `<span class="eyebrow">STUDIO PROJECT / OUR OWN BRAND</span><h2 id="dialog-title">Praneel Mohan.</h2><p>A visual direction developed for Praneel Mohan: bold typography, direct language and a five-colour palette that balances warmth with contrast.</p><div class="detail-palette" aria-label="Orange, black, rust brown, white smoke and lemon lime"><i style="background:#faa613"></i><i style="background:#06070e"></i><i style="background:#9b3d12"></i><i style="background:#f5f5f5"></i><i style="background:#c1df1f"></i></div><div class="detail-grid"><div><h3>The idea</h3><p>Give the work room to speak. Use strong editorial layouts, confident headings and bright accents with a clear purpose.</p></div><div><h3>The application</h3><p>The service sheet and this website bring the direction into use. This is TLC’s own studio project, not an external client commission.</p></div></div><a class="button dark" href="services.html" target="_blank" rel="noopener">Explore our services ↗</a>`
};
document.querySelectorAll('[data-project]').forEach(button => button.addEventListener('click', () => {
  projectContent.innerHTML = projectDetails[button.dataset.project];
  projectDialog.showModal();
}));
document.querySelectorAll('dialog').forEach(dialog => {
  dialog.querySelector('.dialog-close').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => { if (event.target === dialog) { const r = dialog.getBoundingClientRect(); if(event.clientX < r.left || event.clientX > r.right || event.clientY < r.top || event.clientY > r.bottom) dialog.close(); } });
});
document.querySelector('#privacy-open').addEventListener('click', () => document.querySelector('#privacy-dialog').showModal());

const form = document.querySelector('#enquiry-form');
const status = document.querySelector('#form-status');
const copyButton = document.querySelector('#copy-brief');
let enquiryText = '';
if (form) form.addEventListener('submit', event => {
  event.preventDefault();
  if(!form.reportValidity()) return;
  const data = new FormData(form);
  enquiryText = `Hi Praneel,\n\nName: ${data.get('name')}\nEmail: ${data.get('email')}\nCompany / profile: ${data.get('website') || 'Not provided'}\nAbout: ${data.get('service')}\n\nMessage:\n${data.get('brief')}\n`;
  const subject = `Portfolio enquiry: ${data.get('service')}`;
  window.location.href = `mailto:praneelmohan1998@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(enquiryText)}`;
  status.textContent = 'Your email app should open. Send the message there to complete your enquiry. If it does not open, copy the brief and email it to praneelmohan1998@gmail.com.';
  copyButton.hidden = false;
});
if (copyButton) copyButton.addEventListener('click', async () => {
  try { await navigator.clipboard.writeText(enquiryText); status.textContent = 'Enquiry copied. Paste it into an email to praneelmohan1998@gmail.com and send when ready.'; }
  catch { const text = document.createElement('textarea'); text.value = enquiryText; text.setAttribute('aria-label','Your enquiry text — select and copy'); text.style.cssText='width:100%;min-height:180px;margin-top:15px'; form.append(text); text.focus(); text.select(); status.textContent = 'Select and copy the enquiry below, then email it to praneelmohan1998@gmail.com.'; }
});
document.querySelector('#year').textContent = String(new Date().getFullYear());

// Full-size portfolio viewer. Navigation respects the active topic filter.
const galleryDialog = document.querySelector('#gallery-dialog');
let visibleWork = (window.TLC_WORK || []).map((_, i) => i);
let selectedWork = 0;
function showWork(index) {
  const item = window.TLC_WORK[index];
  if (!item) return;
  selectedWork = index;
  const image = document.querySelector('#gallery-image');
  image.src = `assets/${item.file}`;
  image.alt = `RevCore Autos thumbnail: ${item.title}`;
  document.querySelector('#gallery-title').textContent = item.title;
  document.querySelector('#gallery-counter').textContent = `${visibleWork.indexOf(index) + 1} / ${visibleWork.length}`;
  document.querySelector('#gallery-prev').disabled = visibleWork.length < 2;
  document.querySelector('#gallery-next').disabled = visibleWork.length < 2;
}
function stepWork(direction) {
  const position = visibleWork.indexOf(selectedWork);
  showWork(visibleWork[(position + direction + visibleWork.length) % visibleWork.length]);
}
document.querySelectorAll('[data-work-index]').forEach(button => button.addEventListener('click', () => {
  showWork(Number(button.dataset.workIndex));
  galleryDialog.showModal();
}));
document.querySelector('#gallery-prev')?.addEventListener('click', () => stepWork(-1));
document.querySelector('#gallery-next')?.addEventListener('click', () => stepWork(1));
galleryDialog?.addEventListener('keydown', event => {
  if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
    event.preventDefault(); stepWork(event.key === 'ArrowLeft' ? -1 : 1);
  }
});
document.querySelectorAll('[data-gallery-filter]').forEach(button => button.addEventListener('click', () => {
  document.querySelectorAll('[data-gallery-filter]').forEach(b => {
    b.classList.toggle('active', b === button);
    b.setAttribute('aria-pressed', String(b === button));
  });
  visibleWork = [];
  document.querySelectorAll('[data-work-index]').forEach(item => {
    item.hidden = button.dataset.galleryFilter !== 'all' && item.dataset.galleryCategory !== button.dataset.galleryFilter;
    if (!item.hidden) visibleWork.push(Number(item.dataset.workIndex));
  });
}));

// Search the complete service scope, including expanded category descriptions.
const serviceSearch = document.querySelector('#service-search');
serviceSearch?.addEventListener('input', () => {
  const terms = serviceSearch.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
  let count = 0;
  document.querySelectorAll('.directory-card').forEach(card => {
    const matches = terms.every(term => card.dataset.search.includes(term));
    card.hidden = !matches;
    card.open = terms.length > 0 && matches;
    if (matches) count++;
  });
  document.querySelectorAll('.directory-group').forEach(group => {
    group.hidden = ![...group.querySelectorAll('.directory-card')].some(card => !card.hidden);
    const link = document.querySelector(`.directory-jumps a[href="#${group.id}"]`);
    if (link) link.hidden = group.hidden;
  });
  document.querySelector('#service-count').textContent = `${count} ${count === 1 ? 'category' : 'categories'}`;
  document.querySelector('#service-no-results').hidden = count !== 0;
});

// Portfolio media is local, with one player loaded only after the visitor selects a sample.
const videoDialog = document.querySelector('#video-dialog');
const portfolioPlayer = document.querySelector('#portfolio-player');
document.querySelectorAll('[data-video]').forEach(button => button.addEventListener('click', () => {
  const sample = window.TLC_VIDEOS?.[button.dataset.video];
  if (!sample || !videoDialog || !portfolioPlayer) return;
  document.querySelector('#video-title').textContent = sample.title;
  document.querySelector('#video-credit').textContent = sample.credit;
  portfolioPlayer.poster = sample.poster;
  portfolioPlayer.src = sample.file;
  videoDialog.showModal();
  portfolioPlayer.load();
  portfolioPlayer.play().catch(() => {});
}));
videoDialog?.addEventListener('close', () => {
  portfolioPlayer.pause();
  portfolioPlayer.removeAttribute('src');
  portfolioPlayer.load();
});
portfolioPlayer?.addEventListener('error', () => {
  document.querySelector('#video-credit').textContent = 'The video could not load. Please try again or get in touch for the sample.';
});
document.querySelectorAll('[data-collection-filter]').forEach(button => button.addEventListener('click', () => {
  document.querySelectorAll('[data-collection-filter]').forEach(b => {
    b.classList.toggle('active', b === button);
    b.setAttribute('aria-pressed', String(b === button));
  });
  document.querySelectorAll('[data-collection-kind]').forEach(card => {
    card.hidden = button.dataset.collectionFilter !== 'all' && card.dataset.collectionKind !== button.dataset.collectionFilter;
  });
}));

const creativeDialog = document.querySelector('#creative-dialog');
document.querySelectorAll('[data-creative]').forEach(button => button.addEventListener('click', () => {
  const creative = window.TLC_CREATIVES?.[button.dataset.creative];
  if (!creative || !creativeDialog) return;
  const image = document.querySelector('#creative-image');
  image.src = creative.file;
  image.alt = creative.title;
  document.querySelector('#creative-title').textContent = creative.title;
  creativeDialog.showModal();
}));
const selectedRail = document.querySelector('#selected-rail');
const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
for (const [id, direction] of [['rail-prev', -1], ['rail-next', 1]]) {
  document.querySelector(`#${id}`)?.addEventListener('click', () => selectedRail?.scrollBy({left:direction * selectedRail.clientWidth * .8, behavior:reducedMotion ? 'auto' : 'smooth'}));
}
if (serviceSearch) {
  const query = new URLSearchParams(location.search).get('q');
  if (query) { serviceSearch.value = query; serviceSearch.dispatchEvent(new Event('input')); }
}
if ('IntersectionObserver' in window && !reducedMotion) {
  const observer = new IntersectionObserver(entries => entries.forEach(entry => {
    if (entry.isIntersecting) { entry.target.classList.add('reveal-ready'); observer.unobserve(entry.target); }
  }), {threshold:.15});
  document.querySelectorAll('[data-reveal]').forEach(element => observer.observe(element));
}
