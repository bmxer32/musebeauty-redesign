document.addEventListener('DOMContentLoaded', () => {
  // Mobile Burger Menu Toggle
  const burger = document.querySelector('[data-burger]');
  const nav = document.querySelector('[data-nav]');

  if (burger && nav) {
    burger.addEventListener('click', () => {
      const isOpen = nav.classList.toggle('is-open');
      burger.classList.toggle('is-active');
      burger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    // Close menu when clicking link inside mobile nav
    nav.querySelectorAll('.nav-link, .btn').forEach(link => {
      link.addEventListener('click', () => {
        nav.classList.remove('is-open');
        burger.classList.remove('is-active');
        burger.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // Filter Chips for Price Tables
  const filterBar = document.querySelector('[data-filter-bar]');
  if (filterBar) {
    const chips = filterBar.querySelectorAll('[data-filter]');
    const blocks = document.querySelectorAll('[data-cat]');

    chips.forEach(chip => {
      chip.addEventListener('click', () => {
        const filter = chip.getAttribute('data-filter');

        chips.forEach(c => c.classList.remove('is-active'));
        chip.classList.add('is-active');

        blocks.forEach(block => {
          const category = block.getAttribute('data-cat');
          if (filter === 'all' || category === filter) {
            block.style.display = 'block';
          } else {
            block.style.display = 'none';
          }
        });
      });
    });
  }
});
