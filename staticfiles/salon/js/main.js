// =====================================================
// GROOM STUDIO — MAIN JS
// =====================================================

$(document).ready(function () {

  // ── 1. NAVBAR scroll shadow ──────────────────────
  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', function () {
    if (window.scrollY > 40) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });

  // ── 2. HAMBURGER MENU ───────────────────────────
  const hamburger = document.getElementById('hamburger');
  const navLinks = document.getElementById('navLinks');

  if (hamburger && navLinks) {
    hamburger.addEventListener('click', function () {
      hamburger.classList.toggle('open');
      navLinks.classList.toggle('open');
    });

    // close menu when link is clicked
    navLinks.querySelectorAll('.nav-link').forEach(function (link) {
      link.addEventListener('click', function () {
        hamburger.classList.remove('open');
        navLinks.classList.remove('open');
      });
    });
  }

  // ── 3. SCROLL TO TOP ────────────────────────────
  const scrollTopBtn = document.getElementById('scrollTop');
  if (scrollTopBtn) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 400) {
        scrollTopBtn.classList.add('visible');
      } else {
        scrollTopBtn.classList.remove('visible');
      }
    });
    scrollTopBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // ── 4. INTERSECTION OBSERVER (fade-in animations) ──
  const animatedEls = document.querySelectorAll('.fade-in, .fade-in-left, .fade-in-right');
  if (animatedEls.length > 0) {
    const observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });

    animatedEls.forEach(function (el) {
      observer.observe(el);
    });
  }

  // ── 5. HERO CAROUSEL (Owl Carousel) ─────────────
  if ($('.hero-carousel').length) {
    $('.hero-carousel').owlCarousel({
      items: 1,
      loop: true,
      autoplay: true,
      autoplayTimeout: 3000,
      autoplayHoverPause: true,
      animateOut: 'fadeOut',
      animateIn: 'fadeIn',
      dots: true,
      nav: false,
      smartSpeed: 1000,
    });
  }

  // ── 6. TESTIMONIALS CAROUSEL ────────────────────
  if ($('.testimonial-carousel').length) {
    $('.testimonial-carousel').owlCarousel({
      loop: true,
      autoplay: true,
      autoplayTimeout: 1000,
      autoplayHoverPause: true,
      dots: true,
      nav: false,
      smartSpeed: 800,
      margin: 0,
      responsive: {
        0: { items: 1 },
        640: { items: 2 },
        1024: { items: 3 },
      },
    });
  }

  // ── 7. GALLERY FILTER ───────────────────────────
  document.querySelectorAll('.filter-pill').forEach(function (pill) {
    pill.addEventListener('click', function () {
      const url = new URL(window.location.href);
      const cat = pill.dataset.category || '';
      if (cat) {
        url.searchParams.set('category', cat);
      } else {
        url.searchParams.delete('category');
      }
      window.location.href = url.toString();
    });
  });

  // ── 8. AUTO-DISMISS ALERTS ──────────────────────
  setTimeout(function () {
    document.querySelectorAll('.gs-alert').forEach(function (alert) {
      alert.style.opacity = '0';
      alert.style.transform = 'translateX(30px)';
      alert.style.transition = 'all .5s ease';
      setTimeout(function () { alert.remove(); }, 500);
    });
  }, 4500);

  // ── 9. FORM LABEL ANIMATE (float on focus) ──────
  document.querySelectorAll('.form-control').forEach(function (input) {
    input.addEventListener('focus', function () {
      this.parentElement.classList.add('focused');
    });
    input.addEventListener('blur', function () {
      this.parentElement.classList.remove('focused');
    });
  });

});
