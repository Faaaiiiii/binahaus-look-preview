/* BINA HAUS — arah 04 "Jurnal Tapak". Progressive enhancement only: with JS blocked
   every page is complete, the navigation is a wrapped list, and the videos use the
   browser's own controls. */
(function () {
  var root = document.documentElement;
  root.classList.add('js');
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* reveals: the modern path is a scroll-driven CSS animation; this is the fallback */
  var revs = Array.prototype.slice.call(document.querySelectorAll('[data-rev]'));
  var supported = window.CSS && CSS.supports && CSS.supports('animation-timeline', 'view()');
  if (!supported && !reduce && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    revs.forEach(function (el) { io.observe(el); });
    window.setTimeout(function () {
      revs.forEach(function (el) {
        if (!el.classList.contains('in') && el.getBoundingClientRect().top < window.innerHeight) el.classList.add('in');
      });
    }, 1600);
  } else {
    revs.forEach(function (el) { el.classList.add('in'); });
  }

  /* video tiles: nothing is fetched until the poster button is pressed */
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

  /* one menu panel holding every page */
  var menu = document.getElementById('menu');
  var burger = document.querySelector('.burger');
  if (menu && burger) {
    var setOpen = function (open) {
      menu.hidden = !open;
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      burger.textContent = open ? 'Tutup' : 'Menu';
      document.body.style.overflow = open ? 'hidden' : '';
      var first = menu.querySelector('a');
      if (open && first) first.focus({ preventScroll: true });
      if (!open) burger.focus({ preventScroll: true });
    };
    burger.addEventListener('click', function () { setOpen(menu.hidden); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !menu.hidden) setOpen(false); });
    document.addEventListener('click', function (e) {
      if (menu.hidden || menu.contains(e.target) || burger.contains(e.target)) return;
      setOpen(false);
    });
  }
})();
