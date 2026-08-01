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

# INDEX.HTML
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

  <!-- SERVICES OVERVIEW SECTION (100% CACHE-BUSTED ACCURATE V2 IMAGES) -->
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
          <img src="./assets/img/noroot.png" alt="Уютная лаундж зона салона Muse Beauty Сочи" loading="lazy">
          <div class="gallery-caption">Атмосфера лаунджа</div>
        </div>
        <div class="gallery-item">
          <img src="./assets/img/294079F4-F2D6-40CD-9.jpeg" alt="Рабочее пространство студии" loading="lazy">
          <div class="gallery-caption">Пространство студии</div>
        </div>
        <div class="gallery-item">
          <img src="./assets/img/4BA72AEE-E5E5-41B0-A.jpeg" alt="Рабочие места мастеров" loading="lazy">
          <div class="gallery-caption">Комфортный сервис</div>
        </div>
        <div class="gallery-item">
          <img src="./assets/img/image_-1.png" alt="Зона встречи гостей и ресепшн" loading="lazy">
          <div class="gallery-caption">Зона ресепшн</div>
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

# SUBPAGES
subpages_data = {
    "lashes.html": ("v2_lashes.jpg", "Наращивание и Ламинирование Ресниц в Сочи | Muse Beauty", "Услуги профессионального наращивания и ламинирования ресниц в студии Muse Beauty Сочи. Классика, 2D, 3D, Голливуд. Прайс-лист, фото работ и онлайн-запись.", "👁️ Эстетика взгляда", "Наращивание и Ламинирование Ресниц", "Легкое, комфортное ношение до 6 недель. Гипоаллергенные премиум-материалы, подбор изгиба и объема под форму ваших глаз.", "Онлайн запись на ресницы"),
    "brows.html": ("v2_brows.jpg", "Оформление и Ламинирование Бровей в Сочи | Muse Beauty", "Коррекция, окрашивание краской и хной, ламинирование и долговременная укладка бровей в Сочи в салоне Muse Beauty на Навагинской. Точные цены и запись.", "✨ Архитектура бровей", "Идеальная форма и уход для ваших бровей", "Архитектура, коррекция воском/пинцетом, профессиональное окрашивание и долговременная укладка с восстанавливающим уходом.", "Онлайн запись на брови"),
    "nails.html": ("v2_nails.jpg", "Маникюр и Педикюр в Сочи | Muse Beauty", "Аппаратный и комбинированный маникюр, педикюр, покрытие гель-лак, наращивание ногтей гель/акригель и дизайн в Сочи на Навагинской.", "💅 Эстетика ногтей", "Маникюр & Педикюр премиум класса", "Стерильный инструментарий в крафт-пакетах, чистый аппаратный маникюр, стойкое покрытие гель-лаком и моделирование ногтей.", "Онлайн запись на маникюр"),
    "luxhair.html": ("v2_luxhair.jpg", "Уходы за Волосами Luxhair & Lebel в Сочи | Muse Beauty", "Ботокс для волос, кератин, нанопластика, спа-комплекс «Счастье для волос» Lebel и холодное восстановление в студии Healthy Hair & Muse Beauty Сочи.", "🌿 Здоровые & Сияющие волосы", "Уходы Luxhair & Реконструкция Волос", "Глубокое спа-восстановление, кератиновое выпрямление, ботокс и профессиональные японские протоколы Lebel для поврежденных волос.", "Онлайн запись на уход"),
    "hair.html": ("v2_hair.jpg", "Парикмахерский Зал & Окрашивание в Сочи | Muse Beauty", "Стрижки, сложные окрашивания Airtouch, Шатуш, Балаяж, тонирование и укладки в центре Сочи на Навагинской. Точные цены и запись к тонировщикам и стилистам.", "✂️ Колористика & Стрижки", "Парикмахерский Зал & Сложные Окрашивания", "Создание плавно растушеванного блонда Airtouch, женские стрижки любой сложности и идеальное уходовое тонирование.", "Онлайн запись к стилисту"),
    "makeup.html": ("v2_makeup.jpg", "Макияж и Праздничные Образы в Сочи | Muse Beauty", "Дневной nude макияж, вечерний макияж, свадебные образы и полные сборы в 4 руки в Сочи в салоне Muse Beauty на Навагинской.", "💄 Профессиональный визаж", "Макияж & Создание Образов", "Стойкий макияж для съемок, вечерних выходов и свадеб. Возможность параллельного сбора в 4 руки (макияж + укладка) за 1.5 часа.", "Онлайн запись на макияж"),
    "contacts.html": ("generated.jpg", "Контакты и Адреса Филиалов в Сочи | Muse Beauty", "Адреса салонов Muse Beauty и Healthy Hair в центре Сочи: ул. Навагинская 15/9 и Навагинская 5/2. Телефоны, часы работы, онлайн-запись YClients.", "📍 Мы на карте Сочи", "Контакты & Запись в Салон", "Ждем вас ежедневно в наших уютных студиях на пешеходной улице Навагинская в центре Сочи.", "Выбрать время в YClients")
}

files_dict = {"index.html": index_content}

for fname, (img, title, desc, tag, h1, sub, btn_txt) in subpages_data.items():
    content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="stylesheet" href="./assets/css/style.css">
  <link rel="icon" href="./assets/img/5AA1398A-7545-4FC2-B.png">
</head>
<body>

{build_header(fname)}

  <section class="hero-section">
    <div class="container hero-grid">
      <div>
        <div class="hero-tag">{tag}</div>
        <h1 class="hero-title">{h1}</h1>
        <p class="hero-subtitle">{sub}</p>
        <div class="hero-cta-group">
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary">{btn_txt}</a>
        </div>
      </div>
      <div class="hero-image-wrapper">
        <img src="./assets/img/{img}" alt="{h1}" loading="eager">
      </div>
    </div>
  </section>

{build_footer()}

  <script src="./assets/js/app.js"></script>
</body>
</html>"""
    files_dict[fname] = content

for fname, content in files_dict.items():
    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Successfully generated all {len(files_dict)} HTML pages with v2 cache-busted image filenames!")
