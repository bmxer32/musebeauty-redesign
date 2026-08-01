/* ==========================================================================
   MUSE BEAUTY SOCHI — INTERACTIVE JS & BURGER MENU LOGIC
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Burger Menu Controller
  const burgerBtn = document.querySelector('[data-burger]');
  const mainNav = document.querySelector('[data-nav]');
  const body = document.body;

  if (burgerBtn && mainNav) {
    burgerBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      const isOpen = mainNav.classList.contains('is-open');
      if (isOpen) {
        closeMenu();
      } else {
        openMenu();
      }
    });

    function openMenu() {
      mainNav.classList.add('is-open');
      burgerBtn.classList.add('is-active');
      burgerBtn.setAttribute('aria-expanded', 'true');
      body.style.overflow = 'hidden';
    }

    function closeMenu() {
      mainNav.classList.remove('is-open');
      burgerBtn.classList.remove('is-active');
      burgerBtn.setAttribute('aria-expanded', 'false');
      body.style.overflow = '';
    }

    // Close when clicking nav links
    const closeTargets = mainNav.querySelectorAll('.nav-link, .btn-mobile-cta, .mobile-contact-link');
    closeTargets.forEach(link => {
      link.addEventListener('click', () => {
        closeMenu();
      });
    });

    // Close when clicking outside
    document.addEventListener('click', (e) => {
      if (mainNav.classList.contains('is-open') && !mainNav.contains(e.target) && !burgerBtn.contains(e.target)) {
        closeMenu();
      }
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mainNav.classList.contains('is-open')) {
        closeMenu();
      }
    });
  }

  // 2. Interactive Price Demo Calculator Controller
  initPriceDemo();
});

function initPriceDemo() {
  const calculators = document.querySelectorAll('[data-price-demo]');
  
  calculators.forEach(calc => {
    const options = calc.querySelectorAll('.demo-opt');
    const totalEl = calc.querySelector('.demo-total-price');
    const timeEl = calc.querySelector('.demo-total-time');

    function updatePrice() {
      let total = 0;
      let time = 0;

      options.forEach(opt => {
        if (opt.classList.contains('is-selected') || (opt.tagName === 'INPUT' && opt.checked)) {
          total += parseInt(opt.dataset.price || 0, 10);
          time += parseInt(opt.dataset.time || 0, 10);
        }
      });

      if (totalEl) totalEl.textContent = total.toLocaleString('ru-RU') + ' ₽';
      if (timeEl) timeEl.textContent = time + ' мин';
    }

    options.forEach(opt => {
      opt.addEventListener('click', () => {
        const group = opt.dataset.group;
        if (group) {
          // Radio behavior in same group
          calc.querySelectorAll(`.demo-opt[data-group="${group}"]`).forEach(o => o.classList.remove('is-selected'));
          opt.classList.add('is-selected');
        } else {
          // Toggle behavior
          opt.classList.toggle('is-selected');
        }
        updatePrice();
      });
    });

    updatePrice();
  });
}
