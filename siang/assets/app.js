/* BINA HAUS — arah 05 "SIANG". Progressive enhancement only.
   With JavaScript switched off the page is complete: the nav links are
   visible, nothing is hidden, and every video is a native player. */
(function () {
  var root = document.documentElement;
  root.classList.add('js');

  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* --- reveals. The hidden state is gated on html.js, so a browser with JS
         blocked never hides a word. Bounded safety sweeps guarantee that copy
         can't stay hidden even if the observer never fires. --- */
  var revs = Array.prototype.slice.call(document.querySelectorAll('[data-rev]'));
  if (!reduce) {
    var reveal = function (el) { el.classList.add('in'); };
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { reveal(e.target); io.unobserve(e.target); }
        });
      }, { rootMargin: '0px 0px -6% 0px', threshold: 0.04 });
      revs.forEach(function (el) { io.observe(el); });
      [1400, 3200].forEach(function (ms) {
        window.setTimeout(function () {
          revs.forEach(function (el) {
            if (el.classList.contains('in')) return;
            var r = el.getBoundingClientRect();
            if (r.top < window.innerHeight) reveal(el);
          });
        }, ms);
      });
      window.setTimeout(function () { revs.forEach(reveal); }, 5200);
    } else {
      revs.forEach(reveal);
    }
  }

  /* --- the menu: one panel holding all seven pages --- */
  var menu = document.getElementById('menu');
  var burger = document.querySelector('.burger');
  if (menu && burger) {
    var setOpen = function (open) {
      menu.hidden = !open;
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      burger.textContent = open ? 'Tutup' : 'Menu';
      if (open) {
        var first = menu.querySelector('a');
        if (first) first.focus({ preventScroll: true });
      } else {
        burger.focus({ preventScroll: true });
      }
    };
    burger.addEventListener('click', function () { setOpen(menu.hidden); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !menu.hidden) setOpen(false);
    });
    document.addEventListener('click', function (e) {
      if (menu.hidden) return;
      if (menu.contains(e.target) || burger.contains(e.target)) return;
      setOpen(false);
    });
  }
})();
