// Browser sweep for a recap page: paste into the page (or run via a JS tool).
// Drives every slider min->max, every preset button, every Player to the end and back,
// every select option and every "go"-style button, and reports thrown errors, widgets
// whose verdict/readout stayed empty, SVG marks outside their viewBox, KaTeX errors and
// horizontal page overflow.
(async () => {
  const errs = [];
  const onErr = e => errs.push(String(e.message || e.reason || e));
  window.addEventListener('error', onErr); window.addEventListener('unhandledrejection', onErr);
  const tick = () => Promise.resolve();  // no setTimeout: hidden panes throttle timers
  const fire = (el, t) => { try { el.dispatchEvent(new Event(t, { bubbles: true })); } catch (e) { errs.push(t + ': ' + e.message); } };
  const report = { panels: 0, sliders: 0, presets: 0, steps: 0, empty: [], offChart: [] };
  for (const p of document.querySelectorAll('.panel')) {
    report.panels++;
    const id = p.id || (p.closest('section') || {}).id;
    for (const b of p.querySelectorAll('[data-p]')) { b.click(); report.presets++; await tick();
      for (const s of p.querySelectorAll('input[type=range]')) {
        const lo = +s.min, hi = +s.max, st = +(s.step) || (hi - lo) / 50, n = Math.min(60, Math.round((hi - lo) / st));
        for (let i = 0; i <= n; i++) { s.value = lo + (hi - lo) * i / n; fire(s, 'input'); fire(s, 'change'); }
        report.sliders++;
      }
      for (const sel of p.querySelectorAll('select')) for (const o of sel.options) { sel.value = o.value; fire(sel, 'change'); }
      const next = p.querySelector('[data-act=next]'), back = p.querySelector('[data-act=back]');
      if (next) { let k = 0; while (!next.disabled && k++ < 400) { next.click(); report.steps++; } k = 0; while (back && !back.disabled && k++ < 400) back.click(); if (next && !next.disabled) next.click(); }
      for (const svg of p.querySelectorAll('svg')) {
        const vb = (svg.getAttribute('viewBox') || '').split(/\s+/).map(Number);
        if (vb.length !== 4) continue;
        for (const m of svg.querySelectorAll('circle,text')) {
          let x, y; try { const bb = m.getBBox(); x = bb.x + bb.width / 2; y = bb.y + bb.height / 2; } catch (e) { continue; }
          if (x < vb[0] - 2 || y < vb[1] - 2 || x > vb[0] + vb[2] + 2 || y > vb[1] + vb[3] + 2) { report.offChart.push(id + ':' + m.tagName + ':' + (m.textContent || '').slice(0, 20)); }
        }
      }
    }
    for (const r of p.querySelectorAll('.verdict,.readout,.caption')) if (!r.textContent.trim() && !r.hidden) report.empty.push(id + ' ' + r.className);
  }
  report.offChart = [...new Set(report.offChart)].slice(0, 15);
  report.empty = [...new Set(report.empty)];
  report.katexErrors = document.querySelectorAll('.katex-error').length;
  report.overflow = document.documentElement.scrollWidth - document.documentElement.clientWidth;
  report.errors = [...new Set(errs)].slice(0, 15);
  window.removeEventListener('error', onErr); window.removeEventListener('unhandledrejection', onErr);
  window.__sweep = report;
  return report;
})();
