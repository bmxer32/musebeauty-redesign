import os

def build_header(active_file):
    links = [
        ("index.html", "Главная"),
        ("lashes.html", "Ресницы"),
        ("brows.html", "Брови"),
        ("nails.html", "Ногтевой сервис"),
        ("luxhair.html", "Уходы Luxhair"),
        ("hair.html", "Парикмахерская"),
        ("makeup.html", "Макияж"),
        ("contacts.html", "Контакты"),
    ]
    
    nav_html = []
    for href, title in links:
        active_cls = " is-active" if href == active_file else ""
        nav_html.append(f'        <a href="./{href}" class="nav-link{active_cls}">{title}</a>')
    
    nav_str = "\n".join(nav_html)

    return f"""  <header class="site-header">
    <div class="container header-inner">
      <a href="./index.html" class="brand-logo">
        <img src="./assets/img/5AA1398A-7545-4FC2-B.png" alt="Muse Beauty" class="logo-img">
        <span class="logo-text">MUSE BEAUTY</span>
      </a>

      <nav class="main-nav" data-nav aria-label="Главное меню">
{nav_str}

        <div class="mobile-menu-footer">
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary btn-mobile-cta">Онлайн запись</a>
          <div class="mobile-menu-contacts">
            <a href="tel:+79885088488" class="mobile-contact-link">📞 +7 (988) 508-84-88</a>
            <a href="https://wa.me/79885088488" target="_blank" rel="noopener" class="mobile-contact-link">💬 Написать в WhatsApp</a>
          </div>
        </div>
      </nav>

      <div class="header-actions">
        <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary btn-sm">Онлайн запись</a>
        <button type="button" class="burger-btn" data-burger aria-label="Переключить меню" aria-expanded="false">
          <span class="burger-line"></span>
          <span class="burger-line"></span>
          <span class="burger-line"></span>
        </button>
      </div>
    </div>
  </header>"""

def build_footer():
    return """  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div class="footer-brand-title">MUSE BEAUTY</div>
          <p class="footer-text">Премиальная студия эстетики ресниц, бровей, ногтевого сервиса и здоровых волос в центре Сочи.</p>
        </div>
        <div>
          <h4 class="footer-heading">Навигация</h4>
          <ul class="footer-links">
            <li><a href="./lashes.html" class="footer-link">Ресницы</a></li>
            <li><a href="./brows.html" class="footer-link">Брови</a></li>
            <li><a href="./nails.html" class="footer-link">Ногтевой сервис</a></li>
            <li><a href="./luxhair.html" class="footer-link">Уходы Luxhair</a></li>
            <li><a href="./hair.html" class="footer-link">Парикмахерская</a></li>
            <li><a href="./makeup.html" class="footer-link">Макияж</a></li>
          </ul>
        </div>
        <div>
          <h4 class="footer-heading">Контакты &amp; Запись</h4>
          <ul class="footer-links">
            <li><a href="tel:+79885088488" class="footer-link">📞 +7 (988) 508-84-88</a></li>
            <li><a href="tel:+79663355770" class="footer-link">📞 +7 (966) 335-57-70</a></li>
            <li><a href="https://wa.me/79885088488" target="_blank" rel="noopener" class="footer-link">💬 WhatsApp</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <div>&copy; 2026 Healthy Hair &amp; Muse Beauty. Все права защищены.</div>
        <div>Сочи, ул. Навагинская 15/9 &amp; 5/2</div>
      </div>
    </div>
  </footer>"""

# 1. INDEX.HTML
index_content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Muse Beauty — Студия красоты в Сочи | Навагинская 15/9 и 5/2</title>
  <meta name="description" content="Премиальный салон красоты Muse Beauty и студия уходов Healthy Hair в Сочи на ул. Навагинская. Наращивание ресниц, оформление бровей, маникюр, педикюр, кератин, ботокс, Airtouch и макияж.">
  <link rel="stylesheet" href="./assets/css/style.css">
  <link rel="icon" href="./assets/img/5AA1398A-7545-4FC2-B.png">
</head>
<body>

{build_header("index.html")}

  <!-- HERO SECTION -->
  <section class="hero-section">
    <div class="container hero-grid">
      <div class="hero-content">
        <div class="hero-tag">✨ Студия красоты &amp; Уходов в центре Сочи</div>
        <h1 class="hero-title">Искусство вашей естественной красоты</h1>
        <p class="hero-subtitle">Салон Muse Beauty &amp; Healthy Hair на Навагинской. Премиальный сервис ресниц, бровей, ногтевого сервиса, сложного окрашивания и уходов за волосами.</p>
        <div class="hero-cta-group">
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary">Записаться онлайн</a>
          <a href="#services" class="btn btn-outline">Услуги и цены</a>
        </div>
      </div>
      <div class="hero-image-wrapper">
        <img src="./assets/img/2072743F-D526-49B9-8.jpeg" alt="Интерьер и атмосфера салона Muse Beauty в Сочи" loading="eager">
      </div>
    </div>
  </section>

  <!-- INFO ADVANTAGES BAR -->
  <div class="container">
    <div class="info-bar">
      <div class="info-card">
        <div class="info-icon">📍</div>
        <div>
          <h3 class="info-title">Центр Сочи</h3>
          <p class="info-desc">Ул. Навагинская 15/9 и Навагинская 5/2 (2 этаж)</p>
        </div>
      </div>
      <div class="info-card">
        <div class="info-icon">💎</div>
        <div>
          <h3 class="info-title">Премиум материалы</h3>
          <p class="info-desc">Сертифицированные составы Lebel, Luxhair &amp; гипоаллергенные ресницы</p>
        </div>
      </div>
      <div class="info-card">
        <div class="info-icon">⚡</div>
        <div>
          <h3 class="info-title">Быстрая запись 24/7</h3>
          <p class="info-desc">Мгновенный выбор удобного времени и топ-мастера через YClients</p>
        </div>
      </div>
    </div>
  </div>

  <!-- SERVICES OVERVIEW SECTION -->
  <section class="section section-bg" id="services">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Наши ключевые направления</h2>
        <p class="section-subtitle">Полный спектр эстетических услуг в атмосферных залах студии Muse Beauty</p>
      </div>

      <div class="categories-grid">
        <article class="category-card">
          <div class="category-thumb">
            <img src="./assets/img/v2_lashes.jpg" alt="Наращивание и ламинирование ресниц" loading="lazy">
          </div>
          <div class="category-content">
            <h3 class="category-title">Ресницы</h3>
            <p class="category-desc">Классика, 2D/3D объемы, Голливуд и ламинирование с уходом. Невесомое ношение и идеальная носка.</p>
            <div class="category-footer">
              <span class="price-starting">от 2 200 ₽</span>
              <a href="./lashes.html" class="btn btn-outline btn-sm">Подробнее</a>
            </div>
          </div>
        </article>

        <article class="category-card">
          <div class="category-thumb">
            <img src="./assets/img/v2_brows.jpg" alt="Архитектура и ламинирование бровей" loading="lazy">
          </div>
          <div class="category-content">
            <h3 class="category-title">Брови</h3>
            <p class="category-desc">Коррекция воском/пинцетом, долговременная укладка и комплекс «Счастье для бровей».</p>
            <div class="category-footer">
              <span class="price-starting">от 700 ₽</span>
              <a href="./brows.html" class="btn btn-outline btn-sm">Подробнее</a>
            </div>
          </div>
        </article>

        <article class="category-card">
          <div class="category-thumb">
            <img src="./assets/img/v2_nails.jpg" alt="Маникюр и покрытие гель-лак" loading="lazy">
          </div>
          <div class="category-content">
            <h3 class="category-title">Ногтевой сервис</h3>
            <p class="category-desc">Аппаратный маникюр, гель-лак, укрепление гель/акригель, эстетический педикюр и дизайн.</p>
            <div class="category-footer">
              <span class="price-starting">от 1 200 ₽</span>
              <a href="./nails.html" class="btn btn-outline btn-sm">Подробнее</a>
            </div>
          </div>
        </article>

        <article class="category-card">
          <div class="category-thumb">
            <img src="./assets/img/v2_luxhair.jpg" alt="Спа-уход и восстановление волос" loading="lazy">
          </div>
          <div class="category-content">
            <h3 class="category-title">Уходы Luxhair</h3>
            <p class="category-desc">Ботокс, кератиновое выпрямление, нанопластика и спа-комплекс «Счастье для волос» от Lebel.</p>
            <div class="category-footer">
              <span class="price-starting">от 2 800 ₽</span>
              <a href="./luxhair.html" class="btn btn-outline btn-sm">Подробнее</a>
            </div>
          </div>
        </article>

        <article class="category-card">
          <div class="category-thumb">
            <img src="./assets/img/v2_hair.jpg" alt="Парикмахерский зал и окрашивание Airtouch" loading="lazy">
          </div>
          <div class="category-content">
            <h3 class="category-title">Парикмахерская</h3>
            <p class="category-desc">Сложные техники Airtouch, Шатуш, Балаяж, стильные женские стрижки и тонирование.</p>
            <div class="category-footer">
              <span class="price-starting">от 2 000 ₽</span>
              <a href="./hair.html" class="btn btn-outline btn-sm">Подробнее</a>
            </div>
          </div>
        </article>

        <article class="category-card">
          <div class="category-thumb">
            <img src="./assets/img/v2_makeup.jpg" alt="Профессиональный макияж и визаж" loading="lazy">
          </div>
          <div class="category-content">
            <h3 class="category-title">Макияж &amp; Образы</h3>
            <p class="category-desc">Дневной Nude, вечерний Смоки, свадебный образ и экспресс образ в 4 руки.</p>
            <div class="category-footer">
              <span class="price-starting">от 2 500 ₽</span>
              <a href="./makeup.html" class="btn btn-outline btn-sm">Подробнее</a>
            </div>
          </div>
        </article>
      </div>
    </div>
  </section>

  <!-- AUTHENTIC GALLERY SECTION -->
  <section class="section">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Атмосфера и работы мастеров</h2>
        <p class="section-subtitle">Реальные фотографии наших студий и результатов процедур в Сочи</p>
      </div>

      <div class="gallery-grid">
        <div class="gallery-item">
          <img src="./assets/img/v3_main_interior_1.jpg" alt="Интерьер салона Muse Beauty Сочи" loading="lazy">
          <div class="gallery-caption">Атмосфера студии</div>
        </div>
        <div class="gallery-item">
          <img src="./assets/img/209E1C9C-5C52-4141-9.jpeg" alt="Мастер за работой в студии" loading="lazy">
          <div class="gallery-caption">Мастер за работой</div>
        </div>
        <div class="gallery-item">
          <img src="./assets/img/v3_main_interior_2.jpg" alt="Рабочее место мастера" loading="lazy">
          <div class="gallery-caption">Рабочее пространство</div>
        </div>
        <div class="gallery-item">
          <img src="./assets/img/2558E8CB-F90B-4B83-A.jpeg" alt="Премиальная косметика и уход" loading="lazy">
          <div class="gallery-caption">Премиальная косметика</div>
        </div>
      </div>
    </div>
  </section>

  <!-- ADDRESSES & MAP SECTION -->
  <section class="section section-bg">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Ждём вас на Навагинской</h2>
        <p class="section-subtitle">Две удобные локации в самом центре Сочи</p>
      </div>

      <div class="contacts-grid">
        <div class="contact-card">
          <h3 class="contact-branch-title">📍 Студия Muse Beauty</h3>
          <div class="contact-detail-list">
            <div class="contact-item">
              <strong>Адрес:</strong> г. Сочи, ул. Навагинская, д. 15/9 (напротив ТЦ Атриум)
            </div>
            <div class="contact-item">
              <strong>Телефон:</strong> <a href="tel:+79885088488" class="text-accent">+7 (988) 508-84-88</a>
            </div>
            <div class="contact-item">
              <strong>Часы работы:</strong> Ежедневно с 10:00 до 20:00
            </div>
          </div>
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary">Записаться на Навагинскую 15/9</a>
        </div>

        <div class="contact-card">
          <h3 class="contact-branch-title">🌿 Healthy Hair &amp; Muse</h3>
          <div class="contact-detail-list">
            <div class="contact-item">
              <strong>Адрес:</strong> г. Сочи, ул. Навагинская, д. 5/2 (2 этаж)
            </div>
            <div class="contact-item">
              <strong>Телефон:</strong> <a href="tel:+79663355770" class="text-accent">+7 (966) 335-57-70</a>
            </div>
            <div class="contact-item">
              <strong>Часы работы:</strong> Ежедневно с 10:00 до 20:00
            </div>
          </div>
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-outline">Записаться на Навагинскую 5/2</a>
        </div>
      </div>
    </div>
  </section>

{build_footer()}

  <script src="./assets/js/app.js"></script>
</body>
</html>"""

# 2. LASHES.HTML WITH PRICE DEMO CALCULATOR
lashes_content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Наращивание и Ламинирование Ресниц в Сочи | Muse Beauty</title>
  <meta name="description" content="Услуги профессионального наращивания и ламинирования ресниц в студии Muse Beauty Сочи. Классика, 2D, 3D, Голливуд. Демо прайса, фото работ и онлайн-запись.">
  <link rel="stylesheet" href="./assets/css/style.css">
  <link rel="icon" href="./assets/img/5AA1398A-7545-4FC2-B.png">
</head>
<body>

{build_header("lashes.html")}

  <section class="hero-section">
    <div class="container hero-grid">
      <div>
        <div class="hero-tag">👁️ Эстетика взгляда</div>
        <h1 class="hero-title">Наращивание и Ламинирование Ресниц</h1>
        <p class="hero-subtitle">Легкое, комфортное ношение до 6 недель. Гипоаллергенные премиум-материалы, индивидуальный подбор изгиба и объема под форму ваших глаз.</p>
        <div class="hero-cta-group">
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary">Записаться на ресницы</a>
          <a href="#demo-calculator" class="btn btn-outline">Демо прайса &amp; Калькулятор</a>
        </div>
      </div>
      <div class="hero-image-wrapper">
        <img src="./assets/img/v2_lashes.jpg" alt="Наращивание ресниц Muse Beauty Сочи" loading="eager">
      </div>
    </div>
  </section>

  <div class="container">
    <div class="info-bar">
      <div class="info-card">
        <div class="info-icon">✨</div>
        <div>
          <h3 class="info-title">Носка до 6 недель</h3>
          <p class="info-desc">Надежная фиксация и комфорт без утяжеления века</p>
        </div>
      </div>
      <div class="info-card">
        <div class="info-icon">🌿</div>
        <div>
          <h3 class="info-title">Гипоаллергенный клей</h3>
          <p class="info-desc">Безопасные премиум составы для чувствительных глаз</p>
        </div>
      </div>
      <div class="info-card">
        <div class="info-icon">👑</div>
        <div>
          <h3 class="info-title">Топ-мастера</h3>
          <p class="info-desc">Идеальное разделение и симметрия правого и левого глаза</p>
        </div>
      </div>
    </div>
  </div>

  <!-- INTERACTIVE DEMO PRICE CALCULATOR SECTION -->
  <section class="section" id="demo-calculator">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">⚡ Интерактивное Демо Прайса</h2>
        <p class="section-subtitle">Рассчитайте точную стоимость и длительность процедуры прямо сейчас</p>
      </div>

      <div class="price-demo-card" data-price-demo>
        <div class="price-demo-header">
          <div class="demo-title">Калькулятор ухода за ресницами</div>
          <span class="demo-badge">Онлайн-расчёт YClients</span>
        </div>

        <div class="demo-group">
          <div class="demo-group-label">1. Выберите объем или уход:</div>
          <div class="demo-chips">
            <div class="demo-opt is-selected" data-group="volume" data-price="2200" data-time="90">Классика (2 200 ₽)</div>
            <div class="demo-opt" data-group="volume" data-price="2500" data-time="105">2D Объем (2 500 ₽)</div>
            <div class="demo-opt" data-group="volume" data-price="2800" data-time="120">3D Объем (2 800 ₽)</div>
            <div class="demo-opt" data-group="volume" data-price="3200" data-time="135">Голливуд (3 200 ₽)</div>
            <div class="demo-opt" data-group="volume" data-price="2500" data-time="60">Ламинирование + Уход (2 500 ₽)</div>
          </div>
        </div>

        <div class="demo-group">
          <div class="demo-group-label">2. Дополнительные опции:</div>
          <div class="demo-chips">
            <div class="demo-opt" data-price="400" data-time="20">Снятие чужой работы (+400 ₽)</div>
            <div class="demo-opt" data-price="300" data-time="15">Эффект лучиков / Цветные ресницы (+300 ₽)</div>
          </div>
        </div>

        <div class="demo-result-bar">
          <div>
            <div class="demo-total-label">Итоговая стоимость и время:</div>
            <div class="demo-total-price">2 200 ₽</div>
          </div>
          <div>
            <span class="demo-total-time">⏳ ~90 мин</span>
          </div>
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary">Записаться на этот расчет</a>
        </div>
      </div>

      <!-- DETAILED PRICE LIST TABLE -->
      <div class="price-table-wrapper">
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Классическое наращивание ресниц</span>
            <span class="service-note">Естественный эффект, по 1 искусственной ресничке на натуральную.</span>
          </div>
          <span class="service-price">2 200 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Наращивание 1.5D / 2D</span>
            <span class="service-note">Умеренный объем, придающий взгляду выразительность и бархатистость.</span>
          </div>
          <span class="service-price">2 500 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Наращивание 2.5D / 3D</span>
            <span class="service-note">Пышный, яркий объем для любительниц подкрученного эффекта.</span>
          </div>
          <span class="service-price">2 800 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Голливудское наращивание (4D-6D)</span>
            <span class="service-note">Максимально густой гиперобъем для ярких вечерних образов.</span>
          </div>
          <span class="service-price">3 200 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Ламинирование ресниц + окрашивание + уход</span>
            <span class="service-note">Изгиб, глубокое окрашивание и укрепление своих натуральных ресниц.</span>
          </div>
          <span class="service-price">2 500 ₽</span>
        </div>
      </div>
    </div>
  </section>

  <!-- DEDICATED LASHES GALLERY -->
  <section class="section section-bg">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Примеры работ по ресницам</h2>
        <p class="section-subtitle">Результаты наращивания и ламинирования у мастеров Muse Beauty Сочи</p>
      </div>

      <div class="gallery-grid">
        <div class="gallery-item">
          <img src="./assets/img/v2_lashes_gal_1.jpg" alt="Наращивание 2D объем ресниц" loading="lazy">
          <div class="gallery-caption">Объемное наращивание 2D</div>
        </div>
        <div class="gallery-item">
          <img src="./assets/img/v2_lashes_gal_2.jpg" alt="Ламинирование натуральных ресниц" loading="lazy">
          <div class="gallery-caption">Ламинирование &amp; Изгиб</div>
        </div>
        <div class="gallery-item">
          <img src="./assets/img/F8464A9E-67AB-44E3-B.jpeg" alt="Классическое естественное наращивание" loading="lazy">
          <div class="gallery-caption">Классическое наращивание</div>
        </div>
        <div class="gallery-item">
          <img src="./assets/img/CCB92D88-733F-4D50-9.webp" alt="Ламинирование с окрашиванием" loading="lazy">
          <div class="gallery-caption">Ламинирование + Окрашивание</div>
        </div>
      </div>
    </div>
  </section>

{build_footer()}

  <script src="./assets/js/app.js"></script>
</body>
</html>"""

# 3. BROWS.HTML WITH PRICE DEMO CALCULATOR
brows_content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Оформление и Ламинирование Бровей в Сочи | Muse Beauty</title>
  <meta name="description" content="Коррекция, окрашивание краской и хной, ламинирование и долговременная укладка бровей в Сочи в салоне Muse Beauty на Навагинской. Демо прайса и запись.">
  <link rel="stylesheet" href="./assets/css/style.css">
  <link rel="icon" href="./assets/img/5AA1398A-7545-4FC2-B.png">
</head>
<body>

{build_header("brows.html")}

  <section class="hero-section">
    <div class="container hero-grid">
      <div>
        <div class="hero-tag">✨ Архитектура бровей</div>
        <h1 class="hero-title">Идеальная форма и уход для ваших бровей</h1>
        <p class="hero-subtitle">Архитектура, коррекция воском/пинцетом, профессиональное окрашивание и долговременная укладка с восстанавливающим уходом.</p>
        <div class="hero-cta-group">
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary">Записаться на брови</a>
          <a href="#demo-calculator" class="btn btn-outline">Демо прайса &amp; Калькулятор</a>
        </div>
      </div>
      <div class="hero-image-wrapper">
        <img src="./assets/img/v2_brows.jpg" alt="Коррекция и ламинирование бровей Сочи" loading="eager">
      </div>
    </div>
  </section>

  <div class="container">
    <div class="info-bar">
      <div class="info-card">
        <div class="info-icon">📐</div>
        <div>
          <h3 class="info-title">Индивидуальная геометрия</h3>
          <p class="info-desc">Построение формы с учетом индивидуальной архитектоники лица</p>
        </div>
      </div>
      <div class="info-card">
        <div class="info-icon">🎨</div>
        <div>
          <h3 class="info-title">Стойкие красители</h3>
          <p class="info-desc">Премиум хна и гипоаллергенная краска тон-в-тон</p>
        </div>
      </div>
      <div class="info-card">
        <div class="info-icon">💎</div>
        <div>
          <h3 class="info-title">Уход «Счастье для бровей»</h3>
          <p class="info-desc">Глубокая питательная протеиновая маска для роста волосков</p>
        </div>
      </div>
    </div>
  </div>

  <!-- INTERACTIVE DEMO PRICE CALCULATOR SECTION -->
  <section class="section" id="demo-calculator">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">⚡ Интерактивное Демо Прайса</h2>
        <p class="section-subtitle">Рассчитайте точную стоимость и время процедуры</p>
      </div>

      <div class="price-demo-card" data-price-demo>
        <div class="price-demo-header">
          <div class="demo-title">Калькулятор архитектуры бровей</div>
          <span class="demo-badge">Онлайн-расчёт YClients</span>
        </div>

        <div class="demo-group">
          <div class="demo-group-label">1. Выберите услугу:</div>
          <div class="demo-chips">
            <div class="demo-opt" data-group="brow_service" data-price="700" data-time="30">Коррекция воском/пинцетом (700 ₽)</div>
            <div class="demo-opt" data-group="brow_service" data-price="800" data-time="30">Окрашивание краской/хной (800 ₽)</div>
            <div class="demo-opt is-selected" data-group="brow_service" data-price="1300" data-time="45">Комплекс Коррекция + Окрашивание (1 300 ₽)</div>
            <div class="demo-opt" data-group="brow_service" data-price="2200" data-time="60">Ламинирование (укладка) бровей (2 200 ₽)</div>
            <div class="demo-opt" data-group="brow_service" data-price="2800" data-time="75">Полный комплекс + Счастье для бровей (2 800 ₽)</div>
          </div>
        </div>

        <div class="demo-group">
          <div class="demo-group-label">2. Дополнительные опции:</div>
          <div class="demo-chips">
            <div class="demo-opt" data-price="600" data-time="20">Осветление бровей (+600 ₽)</div>
            <div class="demo-opt" data-price="500" data-time="15">Ботокс-маска для бровей (+500 ₽)</div>
          </div>
        </div>

        <div class="demo-result-bar">
          <div>
            <div class="demo-total-label">Итоговая стоимость и время:</div>
            <div class="demo-total-price">1 300 ₽</div>
          </div>
          <div>
            <span class="demo-total-time">⏳ ~45 мин</span>
          </div>
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary">Записаться на этот расчет</a>
        </div>
      </div>

      <div class="price-table-wrapper">
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Коррекция бровей (пинцет / воск)</span>
            <span class="service-note">Построение чистой формы и удаление лишних волосков.</span>
          </div>
          <span class="service-price">700 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Окрашивание бровей (краска / хна)</span>
            <span class="service-note">Подбор оттенка тон-в-тон к цвету волос и кожи.</span>
          </div>
          <span class="service-price">800 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Комплекс: Коррекция + Окрашивание</span>
            <span class="service-note">Архитектура, построение чистой формы и стойкий цвет.</span>
          </div>
          <span class="service-price">1 300 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Ламинирование (долговременная укладка)</span>
            <span class="service-note">Фиксация послушного направления волосков на 4-6 недель.</span>
          </div>
          <span class="service-price">2 200 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Полный комплекс бровей</span>
            <span class="service-note">Ламинирование + Коррекция + Окрашивание + Счастье для бровей.</span>
          </div>
          <span class="service-price">2 800 ₽</span>
        </div>
      </div>
    </div>
  </section>

  <!-- DEDICATED BROWS GALLERY -->
  <section class="section section-bg">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Примеры оформления бровей</h2>
        <p class="section-subtitle">Чистая коррекция, ламинирование и окрашивание бровей в Сочи</p>
      </div>

      <div class="gallery-grid">
        <div class="gallery-item">
          <img src="./assets/img/v2_brows_gal_1.jpg" alt="Долговременная укладка бровей" loading="lazy">
          <div class="gallery-caption">Долговременная укладка</div>
        </div>
        <div class="gallery-item">
          <img src="./assets/img/v2_brows_gal_2.jpg" alt="Архитектура и окрашивание хной" loading="lazy">
          <div class="gallery-caption">Архитектура &amp; Окрашивание</div>
        </div>
        <div class="gallery-item">
          <img src="./assets/img/v2_brows_gal_3.jpg" alt="Коррекция формы бровей" loading="lazy">
          <div class="gallery-caption">Коррекция воском/пинцетом</div>
        </div>
        <div class="gallery-item">
          <img src="./assets/img/v2_brows_gal_4.jpg" alt="Комплексный уход бровей" loading="lazy">
          <div class="gallery-caption">Комплекс «Счастье для бровей»</div>
        </div>
      </div>
    </div>
  </section>

{build_footer()}

  <script src="./assets/js/app.js"></script>
</body>
</html>"""

# 4. NAILS.HTML WITH PRICE DEMO CALCULATOR
nails_content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Маникюр и Педикюр в Сочи | Muse Beauty</title>
  <meta name="description" content="Аппаратный и комбинированный маникюр, педикюр, покрытие гель-лак, наращивание ногтей гель/акригель и дизайн в Сочи на Навагинской.">
  <link rel="stylesheet" href="./assets/css/style.css">
  <link rel="icon" href="./assets/img/5AA1398A-7545-4FC2-B.png">
</head>
<body>

{build_header("nails.html")}

  <section class="hero-section">
    <div class="container hero-grid">
      <div>
        <div class="hero-tag">💅 Эстетика ногтей</div>
        <h1 class="hero-title">Маникюр &amp; Педикюр премиум класса</h1>
        <p class="hero-subtitle">Стерильный инструментарий в крафт-пакетах, чистый аппаратный маникюр, стойкое покрытие гель-лаком и моделирование ногтей.</p>
        <div class="hero-cta-group">
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary">Записаться на маникюр</a>
          <a href="#demo-calculator" class="btn btn-outline">Демо прайса &amp; Калькулятор</a>
        </div>
      </div>
      <div class="hero-image-wrapper">
        <img src="./assets/img/v2_nails.jpg" alt="Маникюр и покрытия Muse Beauty Сочи" loading="eager">
      </div>
    </div>
  </section>

  <div class="container">
    <div class="info-bar">
      <div class="info-card">
        <div class="info-icon">🛡️</div>
        <div>
          <h3 class="info-title">100% Стерильно</h3>
          <p class="info-desc">Сухожар ГП-10, дезинфекция и вскрытие крафт-пакета при вас</p>
        </div>
      </div>
      <div class="info-card">
        <div class="info-icon">💎</div>
        <div>
          <h3 class="info-title">Гель-лак премиум</h3>
          <p class="info-desc">Стойкость покрытия без сколов и отслоек до 4 недель</p>
        </div>
      </div>
      <div class="info-card">
        <div class="info-icon">✨</div>
        <div>
          <h3 class="info-title">Дизайн любой сложности</h3>
          <p class="info-desc">Френч, втирка, градиент, рисунки и выравнивание формы</p>
        </div>
      </div>
    </div>
  </div>

  <!-- INTERACTIVE DEMO PRICE CALCULATOR SECTION -->
  <section class="section" id="demo-calculator">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">⚡ Интерактивное Демо Прайса</h2>
        <p class="section-subtitle">Выберите вариант покрытия и дизайн для расчета стоимости</p>
      </div>

      <div class="price-demo-card" data-price-demo>
        <div class="price-demo-header">
          <div class="demo-title">Калькулятор ногтевого сервиса</div>
          <span class="demo-badge">Онлайн-расчёт YClients</span>
        </div>

        <div class="demo-group">
          <div class="demo-group-label">1. Основная процедура:</div>
          <div class="demo-chips">
            <div class="demo-opt" data-group="nail_service" data-price="1200" data-time="45">Маникюр гигиена (1 200 ₽)</div>
            <div class="demo-opt is-selected" data-group="nail_service" data-price="2100" data-time="75">Маникюр + Гель-лак (2 100 ₽)</div>
            <div class="demo-opt" data-group="nail_service" data-price="2300" data-time="90">Снятие + Маникюр + Гель-лак (2 300 ₽)</div>
            <div class="demo-opt" data-group="nail_service" data-price="2800" data-time="90">Педикюр полный + Гель-лак (2 800 ₽)</div>
            <div class="demo-opt" data-group="nail_service" data-price="3500" data-time="120">Наращивание ногтей (3 500 ₽)</div>
          </div>
        </div>

        <div class="demo-group">
          <div class="demo-group-label">2. Дизайн и укрепление:</div>
          <div class="demo-chips">
            <div class="demo-opt" data-price="400" data-time="20">Французский маникюр Френч (+400 ₽)</div>
            <div class="demo-opt" data-price="500" data-time="20">Укрепление ногтей гелем/акригелем (+500 ₽)</div>
            <div class="demo-opt" data-price="300" data-time="15">Втирка / Градиент (+300 ₽)</div>
          </div>
        </div>

        <div class="demo-result-bar">
          <div>
            <div class="demo-total-label">Итоговая стоимость и время:</div>
            <div class="demo-total-price">2 100 ₽</div>
          </div>
          <div>
            <span class="demo-total-time">⏳ ~75 мин</span>
          </div>
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary">Записаться на этот расчет</a>
        </div>
      </div>

      <div class="price-table-wrapper">
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Маникюр гигиенический (аппаратный / комбинированный)</span>
            <span class="service-note">Безопасная обработка кутикулы и придание формы ногтям.</span>
          </div>
          <span class="service-price">1 200 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Маникюр + Покрытие гель-лак</span>
            <span class="service-note">Комби-маникюр, выравнивание ногтевой пластины и покрытие.</span>
          </div>
          <span class="service-price">2 100 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Снятие + Маникюр + Покрытие гель-лак</span>
            <span class="service-note">Снятие старого материала, обработка и свежее покрытие.</span>
          </div>
          <span class="service-price">2 300 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Педикюр гигиенический</span>
            <span class="service-note">Аппаратная обработка пальцев и стоп с питанием.</span>
          </div>
          <span class="service-price">2 000 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Педикюр полный + Покрытие гель-лак</span>
            <span class="service-note">Обработка стоп и пальцев с выравниванием и стойким гель-лаком.</span>
          </div>
          <span class="service-price">2 800 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Наращивание ногтей (гель / акригель)</span>
            <span class="service-note">Моделирование любой длины и формы с опилом.</span>
          </div>
          <span class="service-price">3 500 ₽</span>
        </div>
      </div>
    </div>
  </section>

  <!-- DEDICATED NAILS GALLERY -->
  <section class="section section-bg">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Примеры работ по маникюру</h2>
        <p class="section-subtitle">Чистый аппаратный маникюр и дизайн ногтей в студии Muse Beauty</p>
      </div>

      <div class="gallery-grid">
        <div class="gallery-item">
          <img src="./assets/img/v2_nails_gal_1.jpg" alt="Нюдовый маникюр с гель-лаком" loading="lazy">
          <div class="gallery-caption">Nude Маникюр &amp; Выравнивание</div>
        </div>
        <div class="gallery-item">
          <img src="./assets/img/v2_nails_gal_2.jpg" alt="Французский маникюр френч" loading="lazy">
          <div class="gallery-caption">Французский маникюр Френч</div>
        </div>
        <div class="gallery-item">
          <img src="./assets/img/v3_nails_gal_3.jpg" alt="Дизайнерский маникюр" loading="lazy">
          <div class="gallery-caption">Аппаратный маникюр</div>
        </div>
        <div class="gallery-item">
          <img src="./assets/img/v3_nails_gal_4.jpg" alt="Мастер делает маникюр" loading="lazy">
          <div class="gallery-caption">Стойкое покрытие гель-лак</div>
        </div>
      </div>
    </div>
  </section>

{build_footer()}

  <script src="./assets/js/app.js"></script>
</body>
</html>"""

# 5. LUXHAIR.HTML WITH PRICE DEMO CALCULATOR
luxhair_content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Уходы за Волосами Luxhair & Lebel в Сочи | Muse Beauty</title>
  <meta name="description" content="Ботокс для волос, кератин, нанопластика, спа-комплекс «Счастье для волос» Lebel и холодное восстановление в студии Healthy Hair & Muse Beauty Сочи.">
  <link rel="stylesheet" href="./assets/css/style.css">
  <link rel="icon" href="./assets/img/5AA1398A-7545-4FC2-B.png">
</head>
<body>

{build_header("luxhair.html")}

  <section class="hero-section">
    <div class="container hero-grid">
      <div>
        <div class="hero-tag">🌿 Здоровые &amp; Сияющие волосы</div>
        <h1 class="hero-title">Уходы Luxhair &amp; Реконструкция Волос</h1>
        <p class="hero-subtitle">Глубокое спа-восстановление, кератиновое выпрямление, ботокс и профессиональные японские протоколы Lebel для поврежденных волос.</p>
        <div class="hero-cta-group">
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary">Записаться на уход</a>
          <a href="#demo-calculator" class="btn btn-outline">Демо прайса &amp; Калькулятор</a>
        </div>
      </div>
      <div class="hero-image-wrapper">
        <img src="./assets/img/v2_luxhair.jpg" alt="Восстановление волос Luxhair Сочи" loading="eager">
      </div>
    </div>
  </section>

  <div class="container">
    <div class="info-bar">
      <div class="info-card">
        <div class="info-icon">🌸</div>
        <div>
          <h3 class="info-title">Японский уход Lebel</h3>
          <p class="info-desc">Спа-протокол «Счастье для волос» для глубокой гидратации</p>
        </div>
      </div>
      <div class="info-card">
        <div class="info-icon">✨</div>
        <div>
          <h3 class="info-title">Зеркальный блеск</h3>
          <p class="info-desc">Ботокс и кератиновое выпрямление без пушистости до 6 месяцев</p>
        </div>
      </div>
      <div class="info-card">
        <div class="info-icon">🧪</div>
        <div>
          <h3 class="info-title">Молекулярное уплотнение</h3>
          <p class="info-desc">Холодное восстановление кортекса поврежденного блонда</p>
        </div>
      </div>
    </div>
  </div>

  <!-- INTERACTIVE DEMO PRICE CALCULATOR SECTION -->
  <section class="section" id="demo-calculator">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">⚡ Интерактивное Демо Прайса</h2>
        <p class="section-subtitle">Рассчитайте стоимость ухода в зависимости от длины ваших волос</p>
      </div>

      <div class="price-demo-card" data-price-demo>
        <div class="price-demo-header">
          <div class="demo-title">Калькулятор реконструкции волос</div>
          <span class="demo-badge">Онлайн-расчёт YClients</span>
        </div>

        <div class="demo-group">
          <div class="demo-group-label">1. Выберите состав или спа-программу:</div>
          <div class="demo-chips">
            <div class="demo-opt is-selected" data-group="lux_proc" data-price="3500" data-time="90">Ботокс для волос (от 3 500 ₽)</div>
            <div class="demo-opt" data-group="lux_proc" data-price="4000" data-time="120">Кератиновое выпрямление (от 4 000 ₽)</div>
            <div class="demo-opt" data-group="lux_proc" data-price="4500" data-time="120">Нанопластика волос (от 4 500 ₽)</div>
            <div class="demo-opt" data-group="lux_proc" data-price="3000" data-time="60">Спа-уход «Счастье для волос» Lebel (3 000 ₽)</div>
            <div class="demo-opt" data-group="lux_proc" data-price="2800" data-time="60">Холодное восстановление блондок (2 800 ₽)</div>
          </div>
        </div>

        <div class="demo-group">
          <div class="demo-group-label">2. Длина волос:</div>
          <div class="demo-chips">
            <div class="demo-opt is-selected" data-group="lux_len" data-price="0" data-time="0">Короткие / До плеч (+0 ₽)</div>
            <div class="demo-opt" data-group="lux_len" data-price="800" data-time="20">Средняя длина / До лопаток (+800 ₽)</div>
            <div class="demo-opt" data-group="lux_len" data-price="1500" data-time="30">Длинные / Ниже лопаток (+1 500 ₽)</div>
          </div>
        </div>

        <div class="demo-result-bar">
          <div>
            <div class="demo-total-label">Итоговая ориентировочная стоимость и время:</div>
            <div class="demo-total-price">3 500 ₽</div>
          </div>
          <div>
            <span class="demo-total-time">⏳ ~90 мин</span>
          </div>
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary">Записаться на этот расчет</a>
        </div>
      </div>

      <div class="price-table-wrapper">
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Ботокс для волос</span>
            <span class="service-note">Глубокое питание, устранение пушистости и блеск.</span>
          </div>
          <span class="service-price">от 3 500 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Кератиновое выпрямление волос</span>
            <span class="service-note">Идеальная гладкость, термозащита и шелковистость.</span>
          </div>
          <span class="service-price">от 4 000 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Нанопластика волос</span>
            <span class="service-note">Органическое выпрямление жестких и непослушных кудрей.</span>
          </div>
          <span class="service-price">от 4 500 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Спа-уход «Счастье для волос» (Lebel)</span>
            <span class="service-note">Японская многоступенчатая программа восстановления.</span>
          </div>
          <span class="service-price">от 3 000 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Холодное восстановление волос</span>
            <span class="service-note">Бестемпературный молекулярный уход для ломких волос.</span>
          </div>
          <span class="service-price">от 2 800 ₽</span>
        </div>
      </div>
    </div>
  </section>

  <!-- DEDICATED LUXHAIR GALLERY -->
  <section class="section section-bg">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Результаты реконструкции волос</h2>
        <p class="section-subtitle">Здоровые, шелковистые и блестящие волосы у наших клиентов</p>
      </div>

      <div class="gallery-grid">
        <div class="gallery-item">
          <img src="./assets/img/v2_luxhair_gal_1.jpg" alt="Зеркальный блеск ботокс для волос" loading="lazy">
          <div class="gallery-caption">Ботокс &amp; Блеск волос</div>
        </div>
        <div class="gallery-item">
          <img src="./assets/img/v2_luxhair.jpg" alt="Кератиновое выпрямление волос" loading="lazy">
          <div class="gallery-caption">Кератиновое выпрямление</div>
        </div>
        <div class="gallery-item">
          <img src="./assets/img/2558E8CB-F90B-4B83-A.jpeg" alt="Японское Счастье для волос Lebel" loading="lazy">
          <div class="gallery-caption">Спа-уход Lebel «Счастье»</div>
        </div>
        <div class="gallery-item">
          <img src="./assets/img/89C75270-F1FD-4357-8.jpeg" alt="Холодное восстановление блондок" loading="lazy">
          <div class="gallery-caption">Холодное восстановление</div>
        </div>
      </div>
    </div>
  </section>

{build_footer()}

  <script src="./assets/js/app.js"></script>
</body>
</html>"""

# 6. HAIR.HTML WITH PRICE DEMO CALCULATOR
hair_content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Парикмахерский Зал & Окрашивание в Сочи | Muse Beauty</title>
  <meta name="description" content="Стрижки, сложные окрашивания Airtouch, Шатуш, Балаяж, тонирование и укладки в центре Сочи на Навагинской. Демо прайса и запись.">
  <link rel="stylesheet" href="./assets/css/style.css">
  <link rel="icon" href="./assets/img/5AA1398A-7545-4FC2-B.png">
</head>
<body>

{build_header("hair.html")}

  <section class="hero-section">
    <div class="container hero-grid">
      <div>
        <div class="hero-tag">✂️ Колористика &amp; Стрижки</div>
        <h1 class="hero-title">Парикмахерский Зал &amp; Сложные Окрашивания</h1>
        <p class="hero-subtitle">Создание плавно растушеванного блонда Airtouch, женские стрижки любой сложности и идеальное уходовое тонирование.</p>
        <div class="hero-cta-group">
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary">Записаться к стилисту</a>
          <a href="#demo-calculator" class="btn btn-outline">Демо прайса &amp; Калькулятор</a>
        </div>
      </div>
      <div class="hero-image-wrapper">
        <img src="./assets/img/v2_hair.jpg" alt="Окрашивание волос Airtouch Сочи" loading="eager">
      </div>
    </div>
  </section>

  <div class="container">
    <div class="info-bar">
      <div class="info-card">
        <div class="info-icon">🎨</div>
        <div>
          <h3 class="info-title">Airtouch &amp; Балаяж</h3>
          <p class="info-desc">Плавный переход от корней без резких границ и полос</p>
        </div>
      </div>
      <div class="info-card">
        <div class="info-icon">✂️</div>
        <div>
          <h3 class="info-title">Стрижки по форме</h3>
          <p class="info-desc">Текстурированные женские стрижки, не требующие укладки</p>
        </div>
      </div>
      <div class="info-card">
        <div class="info-icon">💎</div>
        <div>
          <h3 class="info-title">Защитные протекторы</h3>
          <p class="info-desc">Окрашивание с добавлением Olaplex / Блеск-тонирования</p>
        </div>
      </div>
    </div>
  </div>

  <!-- INTERACTIVE DEMO PRICE CALCULATOR SECTION -->
  <section class="section" id="demo-calculator">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">⚡ Интерактивное Демо Прайса</h2>
        <p class="section-subtitle">Рассчитайте точную стоимость стрижки или окрашивания</p>
      </div>

      <div class="price-demo-card" data-price-demo>
        <div class="price-demo-header">
          <div class="demo-title">Калькулятор услуг стилиста-колориста</div>
          <span class="demo-badge">Онлайн-расчёт YClients</span>
        </div>

        <div class="demo-group">
          <div class="demo-group-label">1. Выберите услугу парикмахерского зала:</div>
          <div class="demo-chips">
            <div class="demo-opt" data-group="hair_service" data-price="2000" data-time="60">Женская стрижка + Укладка (2 000 ₽)</div>
            <div class="demo-opt" data-group="hair_service" data-price="3500" data-time="90">Окрашивание в 1 тон (3 500 ₽)</div>
            <div class="demo-opt is-selected" data-group="hair_service" data-price="6500" data-time="180">Сложный блонд Airtouch / Шатуш (6 500 ₽)</div>
            <div class="demo-opt" data-group="hair_service" data-price="2500" data-time="60">Тонирование волос (2 500 ₽)</div>
            <div class="demo-opt" data-group="hair_service" data-price="2000" data-time="45">Укладка / Серф-локоны (2 000 ₽)</div>
          </div>
        </div>

        <div class="demo-group">
          <div class="demo-group-label">2. Длина волос:</div>
          <div class="demo-chips">
            <div class="demo-opt is-selected" data-group="hair_len" data-price="0" data-time="0">До плеч (+0 ₽)</div>
            <div class="demo-opt" data-group="hair_len" data-price="1000" data-time="30">До лопаток (+1 000 ₽)</div>
            <div class="demo-opt" data-group="hair_len" data-price="2000" data-time="45">Ниже лопаток / Густые (+2 000 ₽)</div>
          </div>
        </div>

        <div class="demo-result-bar">
          <div>
            <div class="demo-total-label">Итоговая ориентировочная стоимость и время:</div>
            <div class="demo-total-price">6 500 ₽</div>
          </div>
          <div>
            <span class="demo-total-time">⏳ ~180 мин</span>
          </div>
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary">Записаться на этот расчет</a>
        </div>
      </div>

      <div class="price-table-wrapper">
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Женская стрижка (мытье + укладка)</span>
            <span class="service-note">Подбор формы с учетом структуры и овалу лица.</span>
          </div>
          <span class="service-price">2 000 - 2 500 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Стрижка кончиков / Челка</span>
            <span class="service-note">Ровный срез или оформление челки (шторка, прямая).</span>
          </div>
          <span class="service-price">800 - 1 000 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Окрашивание в один тон</span>
            <span class="service-note">Обновление цвета, закрашивание седины и блеск.</span>
          </div>
          <span class="service-price">от 3 500 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Сложное окрашивание (Airtouch, Шатуш, Балаяж)</span>
            <span class="service-note">Плавная растяжка цвета с тонированием.</span>
          </div>
          <span class="service-price">от 6 500 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Тонирование волос</span>
            <span class="service-note">Нейтрализация желтизны и насыщение цвета пигментами.</span>
          </div>
          <span class="service-price">от 2 500 ₽</span>
        </div>
      </div>
    </div>
  </section>

  <!-- DEDICATED HAIR GALLERY -->
  <section class="section section-bg">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Примеры окрашиваний и стрижек</h2>
        <p class="section-subtitle">Работы колористов и стилистов студии Muse Beauty в Сочи</p>
      </div>

      <div class="gallery-grid">
        <div class="gallery-item">
          <img src="./assets/img/v2_hair_gal_1.jpg" alt="Airtouch сложный блонд" loading="lazy">
          <div class="gallery-caption">Сложный блонд Airtouch</div>
        </div>
        <div class="gallery-item">
          <img src="./assets/img/muse_img_24.jpg" alt="Окрашивание и укладка волос" loading="lazy">
          <div class="gallery-caption">Окрашивание &amp; Укладка</div>
        </div>
        <div class="gallery-item">
          <img src="./assets/img/v2_hair_gal_3.jpg" alt="Тонирование и локоны" loading="lazy">
          <div class="gallery-caption">Тонирование &amp; Серф-локоны</div>
        </div>
        <div class="gallery-item">
          <img src="./assets/img/v2_hair_gal_4.jpg" alt="Женская стрижка и укладка" loading="lazy">
          <div class="gallery-caption">Женская стрижка по форме</div>
        </div>
      </div>
    </div>
  </section>

{build_footer()}

  <script src="./assets/js/app.js"></script>
</body>
</html>"""

# 7. MAKEUP.HTML WITH PRICE DEMO CALCULATOR
makeup_content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Макияж и Праздничные Образы в Сочи | Muse Beauty</title>
  <meta name="description" content="Дневной nude макияж, вечерний макияж, свадебные образы и полные сборы в 4 руки в Сочи в салоне Muse Beauty на Навагинской. Демо прайса и запись.">
  <link rel="stylesheet" href="./assets/css/style.css">
  <link rel="icon" href="./assets/img/5AA1398A-7545-4FC2-B.png">
</head>
<body>

{build_header("makeup.html")}

  <section class="hero-section">
    <div class="container hero-grid">
      <div>
        <div class="hero-tag">💄 Профессиональный визаж</div>
        <h1 class="hero-title">Макияж &amp; Создание Образов</h1>
        <p class="hero-subtitle">Стойкий макияж для съемок, вечерних выходов и свадеб. Возможность параллельного сбора в 4 руки (макияж + укладка) за 1.5 часа.</p>
        <div class="hero-cta-group">
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary">Записаться на макияж</a>
          <a href="#demo-calculator" class="btn btn-outline">Демо прайса &amp; Калькулятор</a>
        </div>
      </div>
      <div class="hero-image-wrapper">
        <img src="./assets/img/v2_makeup.jpg" alt="Макияж и праздничный образ Сочи" loading="eager">
      </div>
    </div>
  </section>

  <div class="container">
    <div class="info-bar">
      <div class="info-card">
        <div class="info-icon">👑</div>
        <div>
          <h3 class="info-title">Люкс косметика</h3>
          <p class="info-desc">Dior, Charlotte Tilbury, Tom Ford, Estée Lauder</p>
        </div>
      </div>
      <div class="info-card">
        <div class="info-icon">⚡</div>
        <div>
          <h3 class="info-title">Сборы в 4 руки</h3>
          <p class="info-desc">Макияж + Укладка одновременно всего за 1.5 часа</p>
        </div>
      </div>
      <div class="info-card">
        <div class="info-icon">✨</div>
        <div>
          <h3 class="info-title">Стойкость 24 часа</h3>
          <p class="info-desc">Фиксация тона и пучковые ресницы без тяжести</p>
        </div>
      </div>
    </div>
  </div>

  <!-- INTERACTIVE DEMO PRICE CALCULATOR SECTION -->
  <section class="section" id="demo-calculator">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">⚡ Интерактивное Демо Прайса</h2>
        <p class="section-subtitle">Выберите вариант макияжа или сборов для расчета стоимости</p>
      </div>

      <div class="price-demo-card" data-price-demo>
        <div class="price-demo-header">
          <div class="demo-title">Калькулятор визажа и сборов</div>
          <span class="demo-badge">Онлайн-расчёт YClients</span>
        </div>

        <div class="demo-group">
          <div class="demo-group-label">1. Выберите вариант образа:</div>
          <div class="demo-chips">
            <div class="demo-opt" data-group="mu_service" data-price="2500" data-time="45">Дневной Nude макияж (2 500 ₽)</div>
            <div class="demo-opt is-selected" data-group="mu_service" data-price="3500" data-time="60">Вечерний / Смоки макияж (3 500 ₽)</div>
            <div class="demo-opt" data-group="mu_service" data-price="4500" data-time="75">Свадебный макияж (4 500 ₽)</div>
            <div class="demo-opt" data-group="mu_service" data-price="5500" data-time="90">Образ в 4 руки: Макияж + Укладка (5 500 ₽)</div>
          </div>
        </div>

        <div class="demo-result-bar">
          <div>
            <div class="demo-total-label">Итоговая стоимость и время:</div>
            <div class="demo-total-price">3 500 ₽</div>
          </div>
          <div>
            <span class="demo-total-time">⏳ ~60 мин</span>
          </div>
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary">Записаться на этот расчет</a>
        </div>
      </div>

      <div class="price-table-wrapper">
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Дневной / Nude макияж</span>
            <span class="service-note">Легкий ровный тон, свежий румянец и естественный рельеф.</span>
          </div>
          <span class="service-price">2 500 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Вечерний / Смоки / Интенсивный макияж</span>
            <span class="service-note">Выразительный макияж глаз, контуринг и пучковые ресницы.</span>
          </div>
          <span class="service-price">3 500 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Свадебный макияж</span>
            <span class="service-note">Повышенная стойкость 24ч, проработка декольте и ресницы.</span>
          </div>
          <span class="service-price">4 500 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Полный образ в 4 руки (Макияж + Укладка)</span>
            <span class="service-note">Одновременная работа визажиста и стилиста по волосам.</span>
          </div>
          <span class="service-price">5 000 - 6 500 ₽</span>
        </div>
      </div>
    </div>
  </section>

  <!-- DEDICATED MAKEUP GALLERY -->
  <section class="section section-bg">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Примеры макияжа и образов</h2>
        <p class="section-subtitle">Работы визажистов салона Muse Beauty в Сочи</p>
      </div>

      <div class="gallery-grid">
        <div class="gallery-item">
          <img src="./assets/img/v3_makeup_gal_1.jpg" alt="Палетка и инструменты визажиста" loading="lazy">
          <div class="gallery-caption">Вечерний макияж</div>
        </div>
        <div class="gallery-item">
          <img src="./assets/img/v3_makeup_gal_2.jpg" alt="Кисти для профессионального макияжа" loading="lazy">
          <div class="gallery-caption">Дневной Nude макияж</div>
        </div>
        <div class="gallery-item">
          <img src="./assets/img/v3_makeup_gal_3.jpg" alt="Косметика для создания образа" loading="lazy">
          <div class="gallery-caption">Образ для фотосессии</div>
        </div>
        <div class="gallery-item">
          <img src="./assets/img/v3_makeup_gal_4.jpg" alt="Визажист за работой" loading="lazy">
          <div class="gallery-caption">Свадебный макияж</div>
        </div>
      </div>
    </div>
  </section>

{build_footer()}

  <script src="./assets/js/app.js"></script>
</body>
</html>"""

# 8. CONTACTS.HTML
contacts_content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Контакты и Адреса Филиалов в Сочи | Muse Beauty</title>
  <meta name="description" content="Адреса салонов Muse Beauty и Healthy Hair в центре Сочи: ул. Навагинская 15/9 и Навагинская 5/2. Телефоны, часы работы, онлайн-запись YClients.">
  <link rel="stylesheet" href="./assets/css/style.css">
  <link rel="icon" href="./assets/img/5AA1398A-7545-4FC2-B.png">
</head>
<body>

{build_header("contacts.html")}

  <section class="hero-section">
    <div class="container hero-grid">
      <div>
        <div class="hero-tag">📍 Мы на карте Сочи</div>
        <h1 class="hero-title">Контакты &amp; Запись в Салон</h1>
        <p class="hero-subtitle">Ждем вас ежедневно в наших уютных студиях на пешеходной улице Навагинская в центре Сочи.</p>
        <div class="hero-cta-group">
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary">Выбрать время в YClients</a>
          <a href="https://wa.me/79885088488" target="_blank" rel="noopener" class="btn btn-outline">Написать в WhatsApp</a>
        </div>
      </div>
      <div class="hero-image-wrapper">
        <img src="./assets/img/generated.jpg" alt="Атмосфера студии Muse Beauty Сочи" loading="eager">
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="contacts-grid">
        <div class="contact-card">
          <h2 class="contact-branch-title">📍 Студия Muse Beauty</h2>
          <div class="contact-detail-list">
            <div class="contact-item">
              <strong>Адрес:</strong> г. Сочи, ул. Навагинская, д. 15/9 (напротив ТЦ Атриум)
            </div>
            <div class="contact-item">
              <strong>Телефон:</strong> <a href="tel:+79885088488" class="text-accent">+7 (988) 508-84-88</a>
            </div>
            <div class="contact-item">
              <strong>Email:</strong> musebeauty.mir@mail.ru
            </div>
            <div class="contact-item">
              <strong>Режим работы:</strong> Ежедневно с 10:00 до 20:00
            </div>
          </div>
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary">Записаться онлайн</a>
        </div>

        <div class="contact-card">
          <h2 class="contact-branch-title">🌿 Healthy Hair &amp; Muse</h2>
          <div class="contact-detail-list">
            <div class="contact-item">
              <strong>Адрес:</strong> г. Сочи, ул. Навагинская, д. 5/2 (2 этаж)
            </div>
            <div class="contact-item">
              <strong>Телефон:</strong> <a href="tel:+79663355770" class="text-accent">+7 (966) 335-57-70</a>
            </div>
            <div class="contact-item">
              <strong>Партнерский сайт:</strong> <a href="https://healthyhairfamily.ru/" target="_blank" rel="noopener" class="text-accent">healthyhairfamily.ru</a>
            </div>
            <div class="contact-item">
              <strong>Режим работы:</strong> Ежедневно с 10:00 до 20:00
            </div>
          </div>
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-outline">Записаться онлайн</a>
        </div>
      </div>
    </div>
  </section>

{build_footer()}

  <script src="./assets/js/app.js"></script>
</body>
</html>"""

files_dict = {
    "index.html": index_content,
    "lashes.html": lashes_content,
    "brows.html": brows_content,
    "nails.html": nails_content,
    "luxhair.html": luxhair_content,
    "hair.html": hair_content,
    "makeup.html": makeup_content,
    "contacts.html": contacts_content
}

for fname, content in files_dict.items():
    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Successfully generated all {len(files_dict)} HTML pages with interactive Price Demo Calculators!")
