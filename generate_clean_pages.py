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
        <img src="./assets/img/5AA1398A-7545-4FC2-B.png" alt="Muse Beauty Logo" width="32" height="32">
        <span>Muse Beauty</span>
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
          <div class="footer-brand-title">Muse Beauty</div>
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

# 2. LASHES.HTML
lashes_content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Наращивание и Ламинирование Ресниц в Сочи | Muse Beauty</title>
  <meta name="description" content="Услуги профессионального наращивания и ламинирования ресниц в студии Muse Beauty Сочи. Классика, 2D, 3D, Голливуд. Прайс-лист, фото работ и онлайн-запись.">
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
        <p class="hero-subtitle">Легкое, комфортное ношение до 6 недель. Гипоаллергенные премиум-материалы, подбор изгиба и объема под форму ваших глаз.</p>
        <div class="hero-cta-group">
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary">Онлайн запись на ресницы</a>
        </div>
      </div>
      <div class="hero-image-wrapper">
        <img src="./assets/img/CCB92D88-733F-4D50-9.webp" alt="Наращивание ресниц Muse Beauty Сочи" loading="eager">
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Прайс-лист на Услуги Ресниц</h2>
        <p class="section-subtitle">Точные цены без скрытых доплат. Все процедуры включают очищение и подготовку</p>
      </div>

      <div class="price-table-wrapper">
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Классическое наращивание ресниц</span>
            <span class="service-note">Естественный эффект, по 1 искусственной ресничке на каждую натуральную.</span>
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
            <span class="service-note">Максимально густой гиперобъем для особых случаев и ярких образов.</span>
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
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Снятие ресниц (чужая работа / без последующего)</span>
            <span class="service-note">Бережная обработка ремувером без повреждения собственных ресниц.</span>
          </div>
          <span class="service-price">400 - 500 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Снятие ресниц с последующим наращиванием</span>
            <span class="service-note">При проведении процедуры наращивания в нашей студии.</span>
          </div>
          <span class="service-price">Бесплатно</span>
        </div>
      </div>
    </div>
  </section>

{build_footer()}

  <script src="./assets/js/app.js"></script>
</body>
</html>"""

# 3. BROWS.HTML
brows_content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Оформление и Ламинирование Бровей в Сочи | Muse Beauty</title>
  <meta name="description" content="Коррекция, окрашивание краской и хной, ламинирование и долговременная укладка бровей в Сочи в салоне Muse Beauty на Навагинской. Точные цены и запись.">
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
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary">Онлайн запись на брови</a>
        </div>
      </div>
      <div class="hero-image-wrapper">
        <img src="./assets/img/CF9B0EE0-51FE-4E0A-A.webp" alt="Коррекция и ламинирование бровей Сочи" loading="eager">
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Прайс-лист на Брови</h2>
        <p class="section-subtitle">Профессиональный подход с учётом архитектоники вашего лица</p>
      </div>

      <div class="price-table-wrapper">
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Коррекция бровей (пинцет/воск)</span>
            <span class="service-note">Построение чистой формы и удаление нежелательных волосков.</span>
          </div>
          <span class="service-price">700 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Окрашивание бровей (краска/хна)</span>
            <span class="service-note">Подбор оттенка тон-в-тон к тону кожи и цвету волос.</span>
          </div>
          <span class="service-price">800 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Комплекс: Коррекция + Окрашивание бровей</span>
            <span class="service-note">Полная архитектура, коррекция формы и стойкое окрашивание.</span>
          </div>
          <span class="service-price">1 300 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Ламинирование (долговременная укладка) бровей</span>
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
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Осветление бровей</span>
            <span class="service-note">Мягкое осветление волосков для гармоничного образа блондинок.</span>
          </div>
          <span class="service-price">600 ₽</span>
        </div>
      </div>
    </div>
  </section>

{build_footer()}

  <script src="./assets/js/app.js"></script>
</body>
</html>"""

# 4. NAILS.HTML
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
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary">Онлайн запись на маникюр</a>
        </div>
      </div>
      <div class="hero-image-wrapper">
        <img src="./assets/img/3B52DDCC-3A98-424D-B.webp" alt="Маникюр и покрытия Muse Beauty Сочи" loading="eager">
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Прайс-лист Ногтевого Сервиса</h2>
        <p class="section-subtitle">Качественные материалы, безопасность и безупречное покрытие</p>
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
            <span class="service-name">Маникюр + Покрытие гель-лак (в один тон)</span>
            <span class="service-note">Маникюр, выравнивание ногтевой пластины и покрытие премиум гель-лаком.</span>
          </div>
          <span class="service-price">2 100 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Снятие + Маникюр + Покрытие гель-лак</span>
            <span class="service-note">Снятие предыдущего материала, комби-маникюр и новое однотонное покрытие.</span>
          </div>
          <span class="service-price">2 300 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Педикюр гигиенический</span>
            <span class="service-note">Обработка пальчиков и стопы с использованием питательного крема.</span>
          </div>
          <span class="service-price">2 000 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Педикюр полный + Покрытие гель-лак</span>
            <span class="service-note">Полный педикюр стоп и пальцев с выравниванием и стойким гель-лаком.</span>
          </div>
          <span class="service-price">2 800 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Наращивание ногтей (гель / акригель)</span>
            <span class="service-note">Моделирование любой длины и формы с опилом и укреплением.</span>
          </div>
          <span class="service-price">3 500 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Дизайн ногтей (1 ноготь / френч / втирка)</span>
            <span class="service-note">Французский маникюр, втирка, геометрия, градиент или слайдеры.</span>
          </div>
          <span class="service-price">от 100 до 500 ₽</span>
        </div>
      </div>
    </div>
  </section>

{build_footer()}

  <script src="./assets/js/app.js"></script>
</body>
</html>"""

# 5. LUXHAIR.HTML
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
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary">Онлайн запись на уход</a>
        </div>
      </div>
      <div class="hero-image-wrapper">
        <img src="./assets/img/89C75270-F1FD-4357-8.jpeg" alt="Восстановление волос Luxhair Сочи" loading="eager">
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Прайс-лист на Процедуры Luxhair</h2>
        <p class="section-subtitle">Оздоровление и плотность волос с длительным накопительным эффектом</p>
      </div>

      <div class="price-table-wrapper">
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Ботокс для волос</span>
            <span class="service-note">Глубокое питание, устранение пушистости и зеркальный блеск.</span>
          </div>
          <span class="service-price">от 3 500 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Кератиновое выпрямление волос</span>
            <span class="service-note">Идеальная гладкость, термозащита и шелковистость до 6 месяцев.</span>
          </div>
          <span class="service-price">от 4 000 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Нанопластика волос</span>
            <span class="service-note">Органическое выпрямление и оздоровление структуры даже самых жестких кудрей.</span>
          </div>
          <span class="service-price">от 4 500 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Спа-уход «Счастье для волос» (Lebel)</span>
            <span class="service-note">Японская многоступенчатая программа восстановления кортекса и кутикулы.</span>
          </div>
          <span class="service-price">от 3 000 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Холодное восстановление волос</span>
            <span class="service-note">Бестемпературный молекулярный уход для осветленных и ломких волос.</span>
          </div>
          <span class="service-price">от 2 800 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Пилинг кожи головы + стимулирующий уход</span>
            <span class="service-note">Глубокое очищение пор, нормализация себума и активация роста новых волос.</span>
          </div>
          <span class="service-price">2 000 ₽</span>
        </div>
      </div>
    </div>
  </section>

{build_footer()}

  <script src="./assets/js/app.js"></script>
</body>
</html>"""

# 6. HAIR.HTML
hair_content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Парикмахерский Зал & Окрашивание в Сочи | Muse Beauty</title>
  <meta name="description" content="Стрижки, сложные окрашивания Airtouch, Шатуш, Балаяж, тонирование и укладки в центре Сочи на Навагинской. Точные цены и запись к тонировщикам и стилистам.">
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
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary">Онлайн запись к стилисту</a>
        </div>
      </div>
      <div class="hero-image-wrapper">
        <img src="./assets/img/A0C70495-F617-43CF-B.jpeg" alt="Окрашивание волос Airtouch Сочи" loading="eager">
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Прайс-лист Парикмахерского Зала</h2>
        <p class="section-subtitle">Работа на премиальных красителях с максимальным сохранением качества волос</p>
      </div>

      <div class="price-table-wrapper">
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Женская стрижка (включает мытье и укладку по форме)</span>
            <span class="service-note">Подбор формы с учетом структуры волос, овалу лица и росту волос.</span>
          </div>
          <span class="service-price">2 000 - 2 500 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Стрижка кончиков / Челка</span>
            <span class="service-note">Ровный срез или оформление челки (шторка, прямая, текстурированная).</span>
          </div>
          <span class="service-price">800 - 1 000 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Окрашивание в один тон</span>
            <span class="service-note">Обновление цвета, закрашивание седины и глубокий блеск.</span>
          </div>
          <span class="service-price">от 3 500 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Сложное окрашивание (Airtouch, Шатуш, Балаяж, Мелирование)</span>
            <span class="service-note">Многочасовая работа с плавной растяжкой цвета и тонированием.</span>
          </div>
          <span class="service-price">от 6 500 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Тонирование волос</span>
            <span class="service-note">Нейтрализация желтизны и насыщение цвета питательными пигментами.</span>
          </div>
          <span class="service-price">от 2 500 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Укладка дневная / Серф-локоны</span>
            <span class="service-note">Создание красивой текстуры и объема на брашинг или плойку.</span>
          </div>
          <span class="service-price">2 000 - 3 000 ₽</span>
        </div>
      </div>
    </div>
  </section>

{build_footer()}

  <script src="./assets/js/app.js"></script>
</body>
</html>"""

# 7. MAKEUP.HTML
makeup_content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Макияж и Праздничные Образы в Сочи | Muse Beauty</title>
  <meta name="description" content="Дневной nude макияж, вечерний макияж, свадебные образы и полные сборы в 4 руки в Сочи в салоне Muse Beauty на Навагинской.">
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
          <a href="https://n581246.yclients.com/company/549326/personal/menu" target="_blank" rel="noopener" class="btn btn-primary">Онлайн запись на макияж</a>
        </div>
      </div>
      <div class="hero-image-wrapper">
        <img src="./assets/img/F09AB9EC-4715-4CE5-8.jpeg" alt="Макияж и праздничный образ Сочи" loading="eager">
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Прайс-лист на Визаж</h2>
        <p class="section-subtitle">Работа на люксовой косметике Dior, Charlotte Tilbury, Tom Ford, Estée Lauder</p>
      </div>

      <div class="price-table-wrapper">
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Дневной / Nude макияж</span>
            <span class="service-note">Легкий ровный тон, свежий румянец и подчеркнутый естественный рельеф.</span>
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
            <span class="service-name">Свадебный макияж (с проработкой декольте)</span>
            <span class="service-note">Повышенная стойкость 24ч, фиксация и пучковые ресницы.</span>
          </div>
          <span class="service-price">4 500 ₽</span>
        </div>
        <div class="price-row">
          <div class="price-info">
            <span class="service-name">Полный образ в 4 руки (Макияж + Укладка/Локоны)</span>
            <span class="service-note">Одновременная работа визажиста и стилиста по волосам. Экономит ваше время.</span>
          </div>
          <span class="service-price">5 000 - 6 500 ₽</span>
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

print(f"Successfully generated all {len(files_dict)} subpages with unique photos and clean non-nested header markup!")
