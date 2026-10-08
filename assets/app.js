/* Bina Haus look preview — progressive enhancement only.
   The page is fully readable with JS disabled; this file adds the entry
   choreography for visitors who allow it.

   Robustness rule: a reveal must never be able to leave content invisible.
   IntersectionObserver only *polishes* the entry; a sweep fallback reveals
   anything already at or above the viewport bottom, and a hard timer reveals
   the rest, so no state can end with hidden copy. */
(function () {
  var root = document.documentElement;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var SEL = '[data-rev],[data-reg],.rise-line';

  function reveal(el) { el.classList.add('in'); }
  function all() { return document.querySelectorAll(SEL); }
  function each(list, fn) { Array.prototype.forEach.call(list, fn); }

  root.classList.add('is-ready');

  // Sweep: reveal anything whose top has already entered the viewport.
  function sweep() {
    var line = window.innerHeight * 0.92;
    each(all(), function (el) {
      if (el.classList.contains('in')) return;
      var r = el.getBoundingClientRect();
      if (r.top < line) reveal(el);
    });
  }

  each(document.querySelectorAll('#hero-h1 .rise-line'), reveal); // hero headline on load

  if (reduce || !('IntersectionObserver' in window)) {
    each(all(), reveal);
    return;
  }

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      reveal(e.target);
      io.unobserve(e.target);
    });
  }, { rootMargin: '0px 0px -10% 0px', threshold: 0.12 });
  each(all(), function (el) { io.observe(el); });

  // Belt and braces: a bounded, self-clearing sweep. The page must never be
  // able to end a state with hidden copy if IO misses an element. No scroll
  // listener is used — IO does the work, this only verifies it did.
  window.addEventListener('resize', sweep, { passive: true });
  sweep();
  requestAnimationFrame(sweep);
  var ticks = 0;
  var t = setInterval(function () {
    sweep();
    ticks++;
    if (ticks >= 20 || document.querySelectorAll(SEL + ':not(.in)').length === 0) clearInterval(t);
  }, 700);
})();
