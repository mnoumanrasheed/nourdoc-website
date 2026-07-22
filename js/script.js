/* NourDoc — Shared behavior & interactions */

/* ---- Prevent browser scroll-restore jumping on page refresh ---- */
if ('scrollRestoration' in history) {
  history.scrollRestoration = 'manual';
}
/* Scroll to the very top instantly on every fresh load */
window.scrollTo(0, 0);

/* ---- Smooth-scroll only for internal anchor (#) links ---- */
document.addEventListener('click', function (e) {
  var a = e.target.closest('a[href^="#"]');
  if (!a) return;
  var target = document.querySelector(a.getAttribute('href'));
  if (!target) return;
  e.preventDefault();
  var navEl = document.querySelector('.nav');
  var offset = navEl ? navEl.offsetHeight : 0;
  var top = target.getBoundingClientRect().top + window.scrollY - offset - 12;
  window.scrollTo({ top: top, behavior: 'smooth' });
});

document.addEventListener('DOMContentLoaded', function () {

  /* ---------- Nav scroll state + mobile toggle & accessibility ---------- */
  var nav = document.querySelector('.nav');
  if (nav) {
    var onScroll = function () {
      nav.classList.toggle('scrolled', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  var toggle = document.querySelector('.nav-toggle');
  var links = document.querySelector('.nav-links');
  if (toggle && links) {

    /* Align the slide-in panel exactly to the bottom of the nav bar */
    var setNavTop = function () {
      if (nav) {
        links.style.top = nav.offsetHeight + 'px';
      }
    };
    setNavTop();
    window.addEventListener('resize', setNavTop, { passive: true });

    var closeMenu = function () {
      links.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
      document.body.classList.remove('menu-open');
    };

    var openMenu = function () {
      setNavTop(); /* recalc in case viewport changed */
      links.classList.add('open');
      toggle.setAttribute('aria-expanded', 'true');
      document.body.classList.add('menu-open');
    };

    toggle.addEventListener('click', function () {
      var isOpen = links.classList.contains('open');
      if (isOpen) { closeMenu(); } else { openMenu(); }
    });

    /* Close when any nav link is clicked */
    links.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', closeMenu);
    });

    /* Close on Escape key */
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && links.classList.contains('open')) {
        closeMenu();
        toggle.focus();
      }
    });

    /* Close when clicking outside the nav */
    document.addEventListener('click', function (e) {
      if (links.classList.contains('open') &&
          !nav.contains(e.target)) {
        closeMenu();
      }
    });
  }

  /* ---------- Lightweight scroll-reveal (AOS-style, no dependency) ---------- */
  var revealables = document.querySelectorAll('[data-aos]');
  if ('IntersectionObserver' in window && revealables.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var delay = entry.target.getAttribute('data-aos-delay') || 0;
          setTimeout(function () { entry.target.classList.add('aos-in'); }, parseInt(delay, 10));
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealables.forEach(function (el) { io.observe(el); });
  } else {
    revealables.forEach(function (el) { el.classList.add('aos-in'); });
  }

  /* ---------- Animated counters ---------- */
  var counters = document.querySelectorAll('.counter[data-count]');
  if ('IntersectionObserver' in window && counters.length) {
    var cIo = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        var target = parseFloat(el.getAttribute('data-count'));
        var decimals = (el.getAttribute('data-count').split('.')[1] || '').length;
        var suffix = el.getAttribute('data-suffix') || '';
        var duration = 1400;
        var start = null;
        function step(ts) {
          if (!start) start = ts;
          var progress = Math.min((ts - start) / duration, 1);
          var eased = 1 - Math.pow(1 - progress, 3);
          el.textContent = (target * eased).toFixed(decimals) + suffix;
          if (progress < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
        cIo.unobserve(el);
      });
    }, { threshold: 0.5 });
    counters.forEach(function (el) { cIo.observe(el); });
  }

  /* ---------- FAQ accordion ---------- */
  document.querySelectorAll('.acc-item').forEach(function (item) {
    var head = item.querySelector('.acc-head');
    var body = item.querySelector('.acc-body');
    if (!head || !body) return;
    head.addEventListener('click', function () {
      var isOpen = item.classList.contains('open');
      item.parentElement.querySelectorAll('.acc-item.open').forEach(function (o) {
        if (o !== item) { o.classList.remove('open'); o.querySelector('.acc-body').style.maxHeight = null; }
      });
      if (isOpen) {
        item.classList.remove('open');
        body.style.maxHeight = null;
      } else {
        item.classList.add('open');
        body.style.maxHeight = body.scrollHeight + 'px';
      }
    });
  });

  /* ---------- Hero waveform (canvas) ---------- */
  var canvas = document.getElementById('heroWave');
  if (canvas && canvas.getContext) {
    var ctx = canvas.getContext('2d');
    var dpr = window.devicePixelRatio || 1;
    function size() {
      var rect = canvas.getBoundingClientRect();
      canvas.width = rect.width * dpr;
      canvas.height = rect.height * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }
    size();
    window.addEventListener('resize', size);
    var bars = 46;
    var phases = Array.from({ length: bars }, function () { return Math.random() * Math.PI * 2; });
    var reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    function draw(t) {
      var rect = canvas.getBoundingClientRect();
      var w = rect.width, h = rect.height;
      ctx.clearRect(0, 0, w, h);
      var gap = w / bars;
      for (var i = 0; i < bars; i++) {
        var phase = phases[i];
        var amp = reduced ? 0.35 : (0.25 + 0.55 * Math.abs(Math.sin(t * 0.0016 + phase)));
        var bh = Math.max(4, amp * h * 0.82);
        var x = i * gap + gap * 0.28;
        var y = (h - bh) / 2;
        var mid = i / bars;
        var colorMix = Math.sin(mid * Math.PI);
        ctx.fillStyle = i % 7 === 0
          ? 'rgba(14,166,114,' + (0.55 + colorMix * 0.3) + ')'
          : 'rgba(255,255,255,' + (0.18 + colorMix * 0.32) + ')';
        var bw = gap * 0.44;
        var r = Math.min(3, bw / 2);
        roundRect(ctx, x, y, bw, bh, r);
      }
      if (!reduced) requestAnimationFrame(draw);
    }
    function roundRect(context, x, y, w, h, r) {
      context.beginPath();
      context.moveTo(x + r, y);
      context.arcTo(x + w, y, x + w, y + h, r);
      context.arcTo(x + w, y + h, x, y + h, r);
      context.arcTo(x, y + h, x, y, r);
      context.arcTo(x, y, x + w, y, r);
      context.closePath();
      context.fill();
    }
    requestAnimationFrame(draw);
  }

  /* ---------- Contact / demo form validation ---------- */
  document.querySelectorAll('form[data-validate]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var valid = true;
      form.querySelectorAll('[required]').forEach(function (input) {
        var field = input.closest('.field');
        var ok = input.value.trim().length > 0;
        if (input.type === 'email' && ok) {
          ok = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value.trim());
        }
        if (field) field.classList.toggle('invalid', !ok);
        if (!ok) valid = false;
      });
      var successEl = form.querySelector('.form-success');
      if (valid) {
        form.reset();
        form.style.display = 'none';
        if (successEl) successEl.style.display = 'block';
      }
    });
    form.querySelectorAll('[required]').forEach(function (input) {
      input.addEventListener('input', function () {
        var field = input.closest('.field');
        if (field) field.classList.remove('invalid');
      });
    });
  });

  /* ---------- Pricing / ROI calculator ---------- */
  var calc = document.getElementById('roiCalculator');
  if (calc) {
    var doctors = calc.querySelector('#c-doctors');
    var consults = calc.querySelector('#c-consults');
    var duration = calc.querySelector('#c-duration');
    var rate = calc.querySelector('#c-rate');
    var inputs = [doctors, consults, duration, rate];

    function fmt(n) { return Math.round(n).toLocaleString('en-US'); }

    function recalc() {
      var d = parseFloat(doctors.value);
      var c = parseFloat(consults.value);
      var dur = parseFloat(duration.value);
      var r = parseFloat(rate.value);

      calc.querySelector('#v-doctors').textContent = d;
      calc.querySelector('#v-consults').textContent = c;
      calc.querySelector('#v-duration').textContent = dur + ' min';
      calc.querySelector('#v-rate').textContent = '$' + r + '/hr';

      var workingDays = 22;
      var monthlyMinutes = d * c * dur * workingDays;
      var costPerMinute = 0.28; // blended platform rate used for estimate
      var monthlyCost = monthlyMinutes * costPerMinute;

      // Physician hours saved: assumes ~9 minutes of documentation removed per 15-minute consult
      var minutesSavedPerConsult = Math.min(dur * 0.6, 9);
      var hoursSaved = (d * c * minutesSavedPerConsult * workingDays) / 60;
      var valueOfTimeSaved = hoursSaved * r;
      var roi = monthlyCost > 0 ? ((valueOfTimeSaved - monthlyCost) / monthlyCost) * 100 : 0;

      calc.querySelector('#r-minutes').textContent = fmt(monthlyMinutes) + ' min';
      calc.querySelector('#r-cost').textContent = '$' + fmt(monthlyCost);
      calc.querySelector('#r-hours').textContent = fmt(hoursSaved) + ' hrs';
      calc.querySelector('#r-roi').textContent = (roi > 0 ? '+' : '') + fmt(roi) + '%';
    }
    inputs.forEach(function (input) { input.addEventListener('input', recalc); });
    recalc();
  }

});
