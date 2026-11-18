  // ---------- page chrome ----------
  const progress = document.getElementById('progress');
  window.addEventListener('scroll', () => {
    const d = document.documentElement;
    progress.style.width = (d.scrollTop/(d.scrollHeight-d.clientHeight)*100) + '%';
  });
  // Jump-nav via JS, not native #anchors: the preview pane loads pages as data: URIs where anchor jumps fail
  document.querySelectorAll('nav.jumpnav a[href^="#"]').forEach(a => {
    a.addEventListener('click', (e) => {
      e.preventDefault();
      const target = document.getElementById(a.getAttribute('href').slice(1));
      if (!target) return;
      const navH = document.querySelector('nav.jumpnav').offsetHeight + 12;
      window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - navH, behavior:'smooth' });
    });
  });
  let closedForPrint = [];
  window.addEventListener('beforeprint', () => {
    closedForPrint = [...document.querySelectorAll('details:not([open])')];
    closedForPrint.forEach(d => d.open = true);
  });
  window.addEventListener('afterprint', () => closedForPrint.forEach(d => d.open = false));
})();
