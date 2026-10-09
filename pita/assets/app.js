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

  /* --- the menu: one panel holding all seven pages plus the one contact line --- */
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
