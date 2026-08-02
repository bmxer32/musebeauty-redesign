import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and not f.startswith(('live_', 'raw_', 'yclients_'))]

nav_template = """      <nav class="main-nav" data-nav aria-label="Главное меню">
        <div class="nav-links-wrapper">
          <a href="./index.html" class="nav-link">Главная</a>
          <a href="./lashes.html" class="nav-link">Ресницы</a>
          <a href="./brows.html" class="nav-link">Брови</a>
          <a href="./nails.html" class="nav-link">Ногтевой сервис</a>
          <a href="./luxhair.html" class="nav-link">Уходы Luxhair</a>
          <a href="./hair.html" class="nav-link">Парикмахерская</a>
          <a href="./makeup.html" class="nav-link">Макияж</a>
          <a href="./contacts.html" class="nav-link">Контакты</a>
        </div>
        <div class="mobile-menu-footer">
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary btn-mobile-cta">Онлайн запись</a>
          <div class="mobile-menu-contacts">
            <a href="tel:+79885088488" class="mobile-contact-link">📞 +7 (988) 508-84-88</a>
            <a href="https://wa.me/79885088488" target="_blank" rel="noopener" class="mobile-contact-link">💬 Написать в WhatsApp</a>
          </div>
        </div>
      </nav>"""

for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace old main-nav with new structured main-nav
    content = re.sub(r'<nav class="main-nav" data-nav.*?</nav>', nav_template, content, flags=re.DOTALL)

    # In index.html, replace blank pattern image A2F7ECE4-6B1B-4A86-8.png with authentic studio photo 294079F4-F2D6-40CD-9.jpeg
    if fname == 'index.html':
        content = content.replace('assets/img/A2F7ECE4-6B1B-4A86-8.png', 'assets/img/294079F4-F2D6-40CD-9.jpeg')

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Successfully updated HTML files ({len(html_files)}) with full burger menu footer and authentic gallery photos!")
