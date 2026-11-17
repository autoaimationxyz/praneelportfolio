// Sector navigation is progressive enhancement: every sector has its own static page.
(() => {
  const groups = [
    {attribute:'sectorFilter', selector:'[data-sector]', status:'#sector-status', data:'sector', noun:'sectors'},
    {attribute:'caseFilter', selector:'[data-case-sectors]', status:'#case-status', data:'caseSectors', noun:'project stories'}
  ];
  const initial=new URLSearchParams(location.search).get('sector');
  for (const group of groups) {
    const buttons=[...document.querySelectorAll(`[data-${group.attribute.replace(/[A-Z]/g,m=>'-'+m.toLowerCase())}]`)];
    if(!buttons.length)continue;
    const apply=(value,updateUrl=false)=>{
      let count=0;
      for(const item of document.querySelectorAll(group.selector)){
        const visible=value==='all'||item.dataset[group.data].split(' ').includes(value);
        item.hidden=!visible;if(visible)count++;
      }
      for(const item of document.querySelectorAll('[data-case-jump]'))item.hidden=value!=='all'&&!item.dataset.caseJump.split(' ').includes(value);
      buttons.forEach(button=>{const active=button.dataset[group.attribute]===value;button.classList.toggle('active',active);button.setAttribute('aria-pressed',String(active));});
      const status=document.querySelector(group.status);
      if(status)status.textContent=`Showing ${count} ${count===1?(group.noun==='sectors'?'sector':'project story'):group.noun}${value==='all'?' across all sectors':''}`;
      if(updateUrl){const url=new URL(location.href);value==='all'?url.searchParams.delete('sector'):url.searchParams.set('sector',value);url.hash='';history.replaceState(null,'',url);}
    };
    buttons.forEach(button=>button.addEventListener('click',()=>apply(button.dataset[group.attribute],true)));
    const hash=decodeURIComponent(location.hash.slice(1));
    const target=hash?document.getElementById(hash):null;
    // A project deep link takes precedence over a previously selected sector.
    const knownInitial=buttons.some(b=>b.dataset[group.attribute]===initial)?initial:'all';
    const selection=target?.matches('[data-case-sectors]')&&knownInitial!=='all'&&!target.dataset.caseSectors.split(' ').includes(knownInitial)?'all':knownInitial;
    apply(selection);
    window.addEventListener('hashchange',()=>{const article=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(article?.matches('[data-case-sectors]')&&article.hidden){apply('all');article.scrollIntoView();}});
  }
  const page=location.pathname.split('/').pop()||'index.html';
  document.querySelectorAll('#main-navigation a').forEach(link=>{
    const name=link.getAttribute('href').split('#')[0];
    if(name===page||(name==='work.html'&&page.startsWith('sector-')))link.setAttribute('aria-current','page');
  });
})();
