/* BINA HAUS — arah 03. Progressive enhancement only:
   with JS switched off the page is complete, the door is open and every word is readable. */
(function () {
  var root = document.documentElement;
  root.classList.add('js');

  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* --- the door: the CSS animation opens it. This is only a safety net, so the
         panels can never end up parked over the page (background tab, extension
         that strips animations, an old engine). --- */
  var panels = document.querySelector('.door__panels');
  if (panels && !reduce) {
    window.setTimeout(function () {
      var m = window.getComputedStyle(panels.firstElementChild).transform;
      var still = m === 'none' || /matrix\(1,\s*0,\s*0,\s*1,\s*0,\s*0\)/.test(m);
      if (still) {
        panels.querySelectorAll('.door__panel').forEach(function (p, i) {
          p.style.transform = 'translateX(' + (i ? '101%' : '-101%') + ')';
          p.style.transition = 'transform .8s cubic-bezier(.22,.61,.36,1)';
        });
      }
    }, 2600);
  }

  /* --- reveals: the modern path is a scroll-driven CSS animation. This is the
         fallback path only, with a bounded sweep so copy can never stay hidden. --- */
  var revs = Array.prototype.slice.call(document.querySelectorAll('[data-rev]'));
  var supported = window.CSS && CSS.supports && CSS.supports('animation-timeline', 'view()');
  if (!supported && !reduce) {
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
      revs.forEach(function (el) { io.observe(el); });
      window.setTimeout(function () {
        revs.forEach(function (el) {
          if (el.classList.contains('in')) return;
          var r = el.getBoundingClientRect();
          if (r.top < window.innerHeight && r.bottom > 0) el.classList.add('in');
        });
      }, 1500);
      window.setTimeout(function () {
        revs.forEach(function (el) {
          var r = el.getBoundingClientRect();
          if (r.top < window.innerHeight) el.classList.add('in');
        });
      }, 3400);
    } else {
      revs.forEach(function (el) { el.classList.add('in'); });
    }
  }

  /* --- video tiles: poster + play affordance; nothing is fetched until a click --- */
  Array.prototype.forEach.call(document.querySelectorAll('.wk--video'), function (fig) {
    var btn = fig.querySelector('.wk__play');
    var vid = fig.querySelector('video');
    if (!btn || !vid) return;
    btn.addEventListener('click', function () {
      fig.classList.add('playing');
      btn.hidden = true;
      var p = vid.play();
      if (p && typeof p.catch === 'function') p.catch(function () {});
    });
  });

  /* --- the menu: one panel holding every page --- */
  var menu = document.getElementById('menu');
  var burger = document.querySelector('.burger');
  if (menu && burger) {
    var setOpen = function (open) {
      menu.hidden = !open;
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      burger.textContent = open ? 'Tutup' : 'Menu';
      document.body.style.overflow = open ? 'hidden' : '';
      if (open) {
        var first = menu.querySelector('a');
        if (first) first.focus({ preventScroll: true });
      } else {
        burger.focus({ preventScroll: true });
      }
    };
    burger.addEventListener('click', function () { setOpen(menu.hidden); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !menu.hidden) setOpen(false); });
    document.addEventListener('click', function (e) {
      if (menu.hidden) return;
      if (menu.contains(e.target) || burger.contains(e.target)) return;
      setOpen(false);
    });
  }
})();
