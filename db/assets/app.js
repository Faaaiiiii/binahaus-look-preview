/* Bina Haus — look preview 02. Progressive enhancement only:
   without JS the page is complete and fully legible. */
(function () {
  var root = document.documentElement;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var revs = Array.prototype.slice.call(document.querySelectorAll('[data-rev]'));

  root.classList.add('is-ready');

  function showAll() {
    revs.forEach(function (el) { el.classList.add('in'); });
  }

  if (reduce || !('IntersectionObserver' in window)) {
    showAll();
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0.06 });
    revs.forEach(function (el) { io.observe(el); });

    /* bounded, self-clearing sweep: copy can never stay hidden */
    window.setTimeout(function () {
      revs.forEach(function (el) {
        if (el.classList.contains('in')) return;
        var r = el.getBoundingClientRect();
        if (r.top < window.innerHeight && r.bottom > 0) el.classList.add('in');
      });
    }, 1600);
    window.setTimeout(function () {
      revs.forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.top < window.innerHeight) el.classList.add('in');
      });
    }, 3600);
  }

  /* video tiles: poster + play affordance (nothing loads until a click) */
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
})();
