(function(){
  "use strict";
  const COLORS = { amber:'#E8A33D', teal:'#4FA8A0', ink:'#EDEAE2', dim:'#9BA3AF', faint:'#5B6270', line:'#2A2F38', rust:'#C1594A' };
  const NS = 'http://www.w3.org/2000/svg';
  const REDUCED = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function el(tag, attrs){ const e = document.createElementNS(NS, tag); for (const k in attrs) e.setAttribute(k, attrs[k]); return e; }
  function h(tag, cls, txt){ const e = document.createElement(tag); if (cls) e.className = cls; if (txt != null) e.textContent = txt; return e; }
  function clear(node){ while(node.firstChild) node.removeChild(node.firstChild); }
  function esc(s){ return String(s).replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c])); }
  const ns = s => String(s).replace(/-/g,'−');
  function frame(opts){ const {x0=70,y0=20,w=640,h=250} = opts; return {x0,y0,w,h,x1:x0+w,y1:y0+h}; }
  function ticks(min,max,step){ const a=[]; for(let v=min; v<=max+1e-9; v+=step) a.push({val:Math.round(v*100)/100, frac:(v-min)/(max-min)}); return a; }
  function drawAxes(svg,f,xTicks,yTicks,xLabel,yLabel,xFmt,yFmt){
    xTicks.forEach(t=>{ const gx=f.x0+t.frac*f.w;
      svg.appendChild(el('line',{x1:gx,y1:f.y0,x2:gx,y2:f.y1,class:'gridline'}));
      svg.appendChild(el('text',{x:gx,y:f.y1+18,class:'tick','text-anchor':'middle'})).textContent = xFmt?xFmt(t.val):t.val;
    });
    yTicks.forEach(t=>{ const gy=f.y1-t.frac*f.h;
      svg.appendChild(el('line',{x1:f.x0,y1:gy,x2:f.x1,y2:gy,class:'gridline'}));
      const lbl=el('text',{x:f.x0-10,y:gy+4,class:'tick','text-anchor':'end'}); lbl.textContent=yFmt?yFmt(t.val):t.val; svg.appendChild(lbl);
    });
    svg.appendChild(el('line',{x1:f.x0,y1:f.y1,x2:f.x1,y2:f.y1,class:'axis'}));
    svg.appendChild(el('line',{x1:f.x0,y1:f.y0,x2:f.x0,y2:f.y1,class:'axis'}));
    svg.appendChild(el('text',{x:(f.x0+f.x1)/2,y:f.y1+40,class:'axislabel','text-anchor':'middle'})).textContent = xLabel;
    const yl=el('text',{x:16,y:(f.y0+f.y1)/2,class:'axislabel','text-anchor':'middle'});
    yl.setAttribute('transform',`rotate(-90 16 ${(f.y0+f.y1)/2})`); yl.textContent=yLabel; svg.appendChild(yl);
  }
  window.__ds = {};   // debug hook: each widget exposes its pure step generator for verification

  // Keyed element pool: reuse the same DOM element for the same logical item across
  // steps, so a CSS transition carries it from its old spot to its new one.
  function Pool(parent){
    const map = new Map();
    return {
      get(key, make){
        let e = map.get(key), fresh = false;
        if (!e){ e = make(); parent.appendChild(e); map.set(key, e); fresh = true; }
        e.__seen = true; return [e, fresh];
      },
      begin(){ map.forEach(e => e.__seen = false); },
      end(){ map.forEach((e,k) => { if (!e.__seen){ e.remove(); map.delete(k); } }); },
      clear(){ map.forEach(e => e.remove()); map.clear(); }
    };
  }
  // Place an element; a brand-new element can start from `from` and glide in.
  function place(e, x, y, fresh, from, anim){
    if (fresh && from && anim && !REDUCED){
      e.style.transition = 'none'; e.style.left = from[0]+'px'; e.style.top = from[1]+'px';
      if (from[2] != null) e.style.opacity = from[2];
      void e.offsetWidth; e.style.transition = ''; e.style.opacity = '';
    }
    if (!anim){ e.style.transition = 'none'; }
    e.style.left = x+'px'; e.style.top = y+'px';
    if (!anim){ void e.offsetWidth; e.style.transition = ''; }
  }

  // Fit a stage into its scroller: shrink a wide drawing (never below minK, so text stays
  // legible) and let the rest scroll sideways; follow() keeps the action in view.
  function fit(stage, w, h, minK){
    const sc = stage.parentNode, avail = sc.clientWidth || w;
    w = Math.max(w, avail);
    const k = Math.max(minK || 0.72, Math.min(1, avail / w));
    stage.style.width = w + 'px'; stage.style.height = h + 'px';
    stage.style.transformOrigin = '0 0'; stage.style.transform = k < 1 ? `scale(${k})` : '';
    stage.style.marginRight = (k < 1 ? -(1-k)*w : 0) + 'px'; stage.style.marginBottom = (k < 1 ? -(1-k)*h : 0) + 'px';
    stage.__k = k; return k;
  }
  function follow(stage, x, anim){
    const sc = stage.parentNode, k = stage.__k || 1;
    if (x == null || sc.scrollWidth <= sc.clientWidth + 2) return;
    const left = Math.max(0, x*k - sc.clientWidth/2);
    if (Math.abs(sc.scrollLeft - left) < 30) return;
    try { sc.scrollTo({ left, behavior: anim && !REDUCED ? 'smooth' : 'auto' }); } catch(e){ sc.scrollLeft = left; }
  }

  // ---------- the shared player: precomputed states, render(state i) from scratch ----------
  function Player(panel, render, opts){
    opts = opts || {};
    const q = s => panel.querySelector(s);
    const codeEl = q('pre.pcode'), varsEl = q('.vars'), cap = q('.caption');
    const bReset = q('[data-act=reset]'), bBack = q('[data-act=back]'), bPlay = q('[data-act=play]'), bNext = q('[data-act=next]');
    const ctr = q('.ctr'), bar = q('.bar i');
    let states = [], code = [], i = 0, timer = null, prevVars = {};
    function setCode(lines){
      code = lines; clear(codeEl);
      lines.forEach((l,k) => { const s = h('span','ln'); s.textContent = l || ' '; s.dataset.k = k; codeEl.appendChild(s); });
    }
    function paint(anim){
      const s = states[i];
      codeEl.querySelectorAll('.ln').forEach(ln => {
        const k = +ln.dataset.k, on = [].concat(s.line == null ? [] : s.line);
        ln.classList.toggle('on', on.includes(k) && !(s.bad && s.bad.includes(k)));
        ln.classList.toggle('bad', !!(s.bad && s.bad.includes(k)));
      });
      clear(varsEl);
      (s.vars || []).forEach(([k,v]) => {
        const sp = h('span'); sp.innerHTML = esc(k)+' = <b>'+esc(v)+'</b>';
        if (anim && prevVars[k] !== undefined && prevVars[k] !== String(v)) sp.classList.add('chg');
        varsEl.appendChild(sp);
      });
      prevVars = {}; (s.vars || []).forEach(([k,v]) => prevVars[k] = String(v));
      cap.innerHTML = s.cap || '';
      ctr.textContent = 'step ' + i + ' / ' + (states.length-1);
      bar.style.width = (states.length > 1 ? i/(states.length-1)*100 : 0) + '%';
      bBack.disabled = bReset.disabled = i === 0; bNext.disabled = i === states.length-1;
      render(s, anim, i);
    }
    function go(k, anim){ i = Math.max(0, Math.min(states.length-1, k)); paint(anim); }
    function stop(){ if (timer){ clearInterval(timer); timer = null; } bPlay.textContent = '▶ Play'; }
    function play(){
      if (timer){ stop(); return; }
      if (i >= states.length-1) go(0, false);
      bPlay.textContent = '❚❚ Pause';
      timer = setInterval(() => { if (i >= states.length-1) stop(); else go(i+1, true); }, opts.delay || 1150);
    }
    bNext.addEventListener('click', () => { stop(); go(i+1, true); });
    bBack.addEventListener('click', () => { stop(); go(i-1, true); });
    bReset.addEventListener('click', () => { stop(); go(0, true); });
    bPlay.addEventListener('click', play);
    panel.addEventListener('keydown', e => {
      if (e.target.matches('input,select,textarea')) return;
      if (e.key === 'ArrowRight'){ e.preventDefault(); stop(); go(i+1, true); }
      if (e.key === 'ArrowLeft'){ e.preventDefault(); stop(); go(i-1, true); }
      if (e.key === ' '){ e.preventDefault(); play(); }
    });
    let rz; window.addEventListener('resize', () => { clearTimeout(rz); rz = setTimeout(() => states.length && paint(false), 120); });
    return {
      load(st, lines, at){ stop(); states = st; if (lines) setCode(lines); prevVars = {}; go(at == null ? 0 : at, false); },
      goto(k){ stop(); go(k, true); },
      get index(){ return i; }, get length(){ return states.length; }
    };
  }
  // Wire a preset button row: data-p attributes → callback, with the active one highlighted.
  function presets(row, cb){
    row.querySelectorAll('[data-p]').forEach(b => b.addEventListener('click', () => {
      row.querySelectorAll('[data-p]').forEach(x => x.classList.toggle('on', x === b)); cb(b.dataset.p);
    }));
  }
