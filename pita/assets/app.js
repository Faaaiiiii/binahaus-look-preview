/* BINA HAUS — arah 06 "PITA". Progressive enhancement only:
   with JS switched off every page is complete, the reel plays (muted autoplay
   needs no script), and the seven-page menu is still reachable as a list. */
(function () {
  var root = document.documentElement;
  root.classList.add('js');

  /* --- the reel: nothing to script; two of the owner's videos crossfade in CSS.
         This only guarantees they are actually playing on load (some engines
         need a nudge after a bfcache restore). Muted autoplay is allowed. --- */
  Array.prototype.forEach.call(document.querySelectorAll('.reel-hero__stage video'), function (v) {
    v.muted = true;
    var p = v.play();
    if (p && typeof p.catch === 'function') p.catch(function () {});
  });

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

  /* --- reveals: the CSS scroll-driven path needs no script. Where the browser has
     no animation-timeline (or the visitor asked for less motion), the same elements
     are revealed once by an observer, so nothing is ever left invisible. */
  var rv = Array.prototype.slice.call(document.querySelectorAll('[data-rv]'));
  var rvSupported = window.CSS && CSS.supports && CSS.supports('animation-timeline', 'view()');
  var rvReduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (rv.length) {
    if (!rvSupported && !rvReduce && 'IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
        });
      }, { rootMargin: '0px 0px -6% 0px', threshold: 0.08 });
      rv.forEach(function (el) { io.observe(el); });
      window.setTimeout(function () {
        rv.forEach(function (el) {
          if (!el.classList.contains('in') && el.getBoundingClientRect().top < window.innerHeight) el.classList.add('in');
        });
      }, 1500);
    } else {
      rv.forEach(function (el) { el.classList.add('in'); });
    }
  }

  /* --- the menu: one panel holding all seven pages plus the one contact line ---
     The panel explains a state change, so it moves: 190ms, exponential ease-out, one
     transition for the whole drawer. `hidden` still carries the accessible state — it is
     set after the close finishes, so the transition is never cut off. */
  var menu = document.getElementById('menu');
  var burger = document.querySelector('.burger');
  if (menu && burger) {
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var openState = false;
    var closeTimer = null;
    var setOpen = function (open) {
      if (closeTimer) { clearTimeout(closeTimer); closeTimer = null; }
      openState = open;
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      burger.textContent = open ? 'Tutup' : 'Menu';
      document.body.style.overflow = open ? 'hidden' : '';
      if (open) {
        menu.hidden = false;
        if (reduce) {
          menu.classList.add('is-open');
        } else {
          /* remove `hidden` first, then move on the next frame so the browser has a
             starting point to animate from */
          requestAnimationFrame(function () {
            requestAnimationFrame(function () { menu.classList.add('is-open'); });
          });
        }
        var first = menu.querySelector('a');
        if (first) first.focus({ preventScroll: true });
      } else {
        menu.classList.remove('is-open');
        var finish = function () { menu.hidden = true; };
        if (reduce) finish(); else closeTimer = setTimeout(finish, 210);
        burger.focus({ preventScroll: true });
      }
    };
    burger.addEventListener('click', function () { setOpen(!openState); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && openState) setOpen(false); });
    document.addEventListener('click', function (e) {
      if (!openState) return;
      if (menu.contains(e.target) || burger.contains(e.target)) return;
      setOpen(false);
    });
  }
})();
