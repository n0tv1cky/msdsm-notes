  // ================= Widget 1: bubble sort (S02, 20 Aug) =================
  (function(){
    const panel = document.getElementById('bsPanel'); if (!panel) return;
    const stage = document.getElementById('bsStage'), scroller = stage.parentNode, readout = document.getElementById('bsRead');
    const CODE = [
      'BUBBLE_SORT(A, L, U)',
      '1  I ← U',
      '2  while I > L do',
      '3     J ← L',
      '4     while J < I do',
      '5        if A[J] < A[J+1] is FALSE then',
      '6           swap A[J] and A[J+1]',
      '7        J ← J + 1',
      '8     I ← I − 1',
      '9  stop'];
    // Pure generator (mirrored in Python for verification). 1-based: L = 1, U = n.
    function gen(vals){
      const n = vals.length, A = [null].concat(vals.map((v,k) => ({id:'b'+k, v}))), S = [];
      let comps = 0, swaps = 0, pass = 0;
      const snap = (o) => S.push(Object.assign({ order:A.slice(1).map(x => x.id), vals:A.slice(1).map(x => x.v), comps, swaps, pass }, o));
      const V = (I,J) => [['L',1],['U',n],['I',I],['J',J==null?'–':J],['A[J]',J?A[J].v:'–'],['A[J+1]',J&&J<n?A[J+1].v:'–']];
      let I = n;
      snap({ line:1, I, J:null, mode:'init', vars:V(I,null), cap:`Start: <b>I ← U = ${n}</b>. I marks the right end of the part that is still unsorted (everything, for now).` });
      for(;;){
        if (!(I > 1)){
          snap({ line:[2,9], I, J:null, mode:'done', vars:V(I,null), cap:`I = 1, so <b>I &gt; L is false</b>: a single element is sorted by default. <span class="t">Sorted: ${A.slice(1).map(x=>x.v).join(' ')}</span> — ${comps} comparisons, ${swaps} swaps.` });
          break;
        }
        pass++; let J = 1;
        snap({ line:[2,3], I, J, mode:'start', vars:V(I,J), cap:`Pass ${pass}: I = ${I} &gt; L, so walk the pair window from the left. <b>J ← L = 1</b>.` });
        while (J < I){
          const a = A[J].v, b = A[J+1].v; comps++;
          if (a < b){
            snap({ line:[4,5], I, J, mode:'cmp', vars:V(I,J), cap:`Compare the neighbours A[${J}] = ${a} and A[${J+1}] = ${b}: <b>${a} &lt; ${b}</b> is true → already in order, no swap. Then J ← J + 1.` });
          } else {
            snap({ line:[4,5], I, J, mode:'cmp', vars:V(I,J), cap:`Compare the neighbours A[${J}] = ${a} and A[${J+1}] = ${b}: <b>${a} &lt; ${b}</b> is <span class="a">false</span> → they must swap.` + (a === b ? ' (Equal values fail the <code>&lt;</code> test too, so this rule swaps them.)' : '') });
            const t = A[J]; A[J] = A[J+1]; A[J+1] = t; swaps++;
            snap({ line:6, I, J, mode:'swap', vars:V(I,J), cap:`Swap: ${a} slides right, ${b} slides left. The bigger value keeps <b>bubbling right</b>. Then J ← J + 1.` });
          }
          J++;
        }
        const top = A[I].v; I--;
        snap({ line:[4,8], I, J:null, mode:'pass', settled:I+1, vars:V(I,null), cap:`J = ${J} is no longer &lt; I, so pass ${pass} is over: <span class="t">${top} is now in its final place</span>. <b>I ← I − 1 = ${I}</b> — the unsorted part shrinks by one.` });
      }
      return S;
    }
    window.__ds.bubble = gen;

    const cells = Pool(stage), lbls = Pool(stage);
    const win = h('div','band win mv'), sorted = h('div','band sorted mv');
    stage.appendChild(sorted); stage.appendChild(win);
    const pJ = h('div','ptr a'), pI = h('div','ptr t');
    pJ.innerHTML = '<span class="arw">▲</span>J'; pI.innerHTML = '<span class="arw">▲</span>I';
    stage.appendChild(pJ); stage.appendChild(pI);
    let N = 0;
    function render(s, anim){
      const n = s.order.length;
      if (n !== N){ cells.clear(); lbls.clear(); N = n; }
      const avail = Math.max(scroller.clientWidth, 300);
      const pitch = Math.max(46, Math.min(66, Math.floor((avail - 28) / n)));
      const cw = pitch - 10, x0 = Math.max(14, (avail - n*pitch)/2), yC = 34;
      fit(stage, n*pitch + 28, 176, 0.8);
      const X = k => x0 + (k-1)*pitch;          // k is the 1-based slot
      const settledFrom = s.mode === 'done' ? 1 : s.I + 1;
      cells.begin(); lbls.begin();
      s.order.forEach((id, k) => {
        const slot = k+1;
        const [c] = cells.get(id, () => { const e = h('div','cell mv'); e.style.width = e.style.height = cw+'px'; return e; });
        c.style.width = c.style.height = cw + 'px';
        c.textContent = s.vals[k];
        c.className = 'cell mv';
        if (slot >= settledFrom) c.classList.add('done');
        if ((s.mode === 'cmp' || s.mode === 'swap') && (slot === s.J || slot === s.J+1)) c.classList.add(s.mode === 'swap' ? 'swap' : 'cmp');
        place(c, X(slot), yC, false, null, anim);
        const [l] = lbls.get('l'+slot, () => h('div','slotlbl'));
        l.textContent = slot; l.style.width = cw+'px'; place(l, X(slot), yC + cw + 6, false, null, false);
      });
      cells.end(); lbls.end();
      // pair window around A[J], A[J+1]
      const showWin = s.J != null && (s.mode === 'cmp' || s.mode === 'swap' || s.mode === 'start');
      win.style.opacity = showWin ? 1 : 0;
      if (s.J != null){ win.style.width = (pitch + cw + 10) + 'px'; win.style.height = (cw + 10) + 'px'; place(win, X(s.J) - 5, yC - 5, false, null, anim); }
      // settled (sorted) region
      const sf = Math.min(settledFrom, n+1);
      sorted.style.opacity = sf <= n ? 1 : 0;
      sorted.style.width = Math.max(0, (n - sf + 1) * pitch) + 'px'; sorted.style.height = (cw + 34) + 'px';
      place(sorted, X(sf) - 5, yC - 9, false, null, anim);
      // pointers under the index labels
      const yP = yC + cw + 26;
      pJ.style.opacity = s.J != null ? 1 : 0;
      if (s.J != null){ pJ.style.width = cw + 'px'; place(pJ, X(s.J), yP, false, null, anim); }
      pI.style.opacity = s.mode === 'done' ? 0 : 1;
      pI.style.width = cw + 'px'; place(pI, X(Math.max(1, s.I)), yP + (s.J === s.I ? 30 : 0), false, null, anim);
      follow(stage, s.J != null ? X(s.J) + pitch : X(Math.max(1, s.I)), anim);
      readout.textContent = 'pass ' + s.pass + ' · comparisons ' + s.comps + ' · swaps ' + s.swaps;
    }
    const player = Player(panel, render, { delay:1200 });
    const P = { a:[7,9,5,4,10,8], b:[5,9,7,6] };
    const input = document.getElementById('bsIn'), err = document.getElementById('bsErr');
    function load(v){ player.load(gen(v), CODE); }
    presets(document.getElementById('bsPre'), p => { input.value = P[p].join(' '); err.textContent=''; load(P[p]); });
    document.getElementById('bsGo').addEventListener('click', () => {
      const v = input.value.trim().split(/[\s,]+/).filter(Boolean).map(Number);
      if (v.length < 2 || v.length > 9 || v.some(x => !Number.isFinite(x))){ err.textContent = '2–9 numbers, separated by spaces'; return; }
      err.textContent = ''; document.querySelectorAll('#bsPre [data-p]').forEach(x => x.classList.remove('on')); load(v);
    });
    load(P.b);
  })();

  // ================= Widget 6: Big-O — find c and n0 (S11, 21 Sep) =================
  (function(){
    const svg = document.getElementById('boChart'); if (!svg) return;
    const slider = document.getElementById('boC'), valEl = document.getElementById('boCVal'), readout = document.getElementById('boRead'), verdict = document.getElementById('boVerdict');
    const FN = {
      q:{ f:n => n*n + 3*n + 1, g:n => n*n, fl:'f(n) = n² + 3n + 1', gl:'c·n²', min:0.5, max:8, def:5, yMax:250, thr:1 },
      l:{ f:n => 2*n + 4, g:n => n, fl:'f(n) = 2n + 4', gl:'c·n', min:0.5, max:12, def:10, yMax:60, thr:2 }
    };
    // smallest integer n0 ≥ 1 with f(n) ≤ c·g(n) for every n ≥ n0 (closed form; both gaps are monotone once c > threshold)
    function n0(key, c){
      if (key === 'q'){ if (c <= 1) return null; const r = (3 + Math.sqrt(9 + 4*(c-1))) / (2*(c-1)); return Math.max(1, Math.ceil(r - 1e-9)); }
      if (c <= 2) return null; return Math.max(1, Math.ceil(4/(c-2) - 1e-9));
    }
    window.__ds.bigo = n0;
    let key = 'q';
    const xMax = 10;
    let f = frame({ x0:62, y0:16, w:660, h:250 });
    function render(){
      // phones get a narrower drawing with bigger type instead of a shrunken wide one
      const narrow = (svg.parentNode.clientWidth || 760) < 560;
      svg.setAttribute('viewBox', narrow ? '0 0 420 330' : '0 0 760 320');
      svg.classList.toggle('narrow', narrow);
      f = narrow ? frame({ x0:52, y0:16, w:352, h:252 }) : frame({ x0:62, y0:16, w:660, h:250 });
      const F = FN[key], c = +slider.value, yMax = F.yMax;
      const X = n => f.x0 + n/xMax*f.w, Y = v => f.y1 - v/yMax*f.h;
      clear(svg);
      const defs = el('defs', {}); const cp = el('clipPath', {id:'boClip'}); cp.appendChild(el('rect', {x:f.x0, y:f.y0, width:f.w, height:f.h})); defs.appendChild(cp); svg.appendChild(defs);
      drawAxes(svg, f, ticks(0, xMax, svg.classList.contains('narrow') ? 2 : 1), ticks(0, yMax, yMax/5), 'n (input size)', svg.classList.contains('narrow') ? '' : 'steps', null, v => Math.round(v));
      const k0 = n0(key, c);
      if (k0 != null && k0 <= xMax) svg.appendChild(el('rect', {x:X(k0), y:f.y0, width:f.x1 - X(k0), height:f.h, fill:'rgba(79,168,160,.07)'}));
      const path = fn => { let d = ''; for (let n = 0; n <= xMax + 1e-9; n += 0.05) d += (d ? 'L' : 'M') + X(n).toFixed(1) + ',' + Y(fn(n)).toFixed(1); return d; };
      const g = el('g', {'clip-path':'url(#boClip)'}); svg.appendChild(g);
      g.appendChild(el('path', {d:path(n => c*F.g(n)), fill:'none', stroke:COLORS.teal, 'stroke-width':2.4}));
      g.appendChild(el('path', {d:path(F.f), fill:'none', stroke:COLORS.amber, 'stroke-width':2.4}));
      for (let n = 1; n <= xMax; n++){
        const ok = F.f(n) <= c*F.g(n) + 1e-9, v = F.f(n);
        if (v <= yMax) g.appendChild(el('circle', {cx:X(n), cy:Y(v), r:4.5, fill: ok ? COLORS.teal : COLORS.rust, stroke:'#14171C', 'stroke-width':1.5}));
      }
      if (k0 != null && k0 <= xMax){
        svg.appendChild(el('line', {x1:X(k0), y1:f.y0, x2:X(k0), y2:f.y1, stroke:COLORS.ink, 'stroke-dasharray':'4 4', 'stroke-width':1.2}));
        const t = el('text', {x:X(k0) + 6, y:f.y0 + 14, class:'tick', fill:COLORS.ink}); t.textContent = 'n₀ = ' + k0; t.style.fill = COLORS.ink; svg.appendChild(t);
      }
      // legend
      const lg = [[F.fl, COLORS.amber], [F.gl.replace('c', c.toFixed(1)) + '  (c = ' + c.toFixed(1) + ')', COLORS.teal]];
      lg.forEach(([txt, col], i) => { const y = f.y0 + 16 + i*20, x = f.x0 + 12;
        svg.appendChild(el('line', {x1:x, y1:y-4, x2:x+18, y2:y-4, stroke:col, 'stroke-width':2.4}));
        const t = el('text', {x:x+24, y, class:'tick'}); t.textContent = txt; t.style.fill = COLORS.dim; svg.appendChild(t); });
      valEl.textContent = c.toFixed(1);
      if (k0 == null){
        readout.textContent = `c = ${c.toFixed(1)} · no n₀`;
        verdict.className = 'verdict bad';
        verdict.textContent = `c ≤ ${F.thr}: c·${key === 'q' ? 'n²' : 'n'} never gets above f(n), however large n is. Pick a bigger c. Any c > ${F.thr} works eventually.`;
      } else {
        readout.textContent = `c = ${c.toFixed(1)} · n₀ = ${k0}`;
        verdict.className = 'verdict good';
        verdict.textContent = (k0 > xMax ? `n₀ = ${k0} is off the chart to the right, but it exists. ` : '') + `For every n ≥ ${k0}: f(n) ≤ ${c.toFixed(1)}·g(n), so f(n) = O(${key === 'q' ? 'n²' : 'n'}). Red dots are where the bound fails; only large n matters.`;
      }
    }
    document.querySelectorAll('#boPre [data-p]').forEach(b => b.addEventListener('click', () => {
      key = b.dataset.p; document.querySelectorAll('#boPre [data-p]').forEach(x => x.classList.toggle('on', x === b));
      const F = FN[key]; slider.min = F.min; slider.max = F.max; slider.value = F.def; render();
    }));
    slider.addEventListener('input', render);
    let rz; window.addEventListener('resize', () => { clearTimeout(rz); rz = setTimeout(render, 150); });
    render();
  })();

