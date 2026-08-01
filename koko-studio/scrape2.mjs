import puppeteer from 'puppeteer';
import fs from 'fs';

const OUT = 'c:/autosait/koko-studio';
const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
const page = await browser.newPage();
await page.setViewport({ width: 1440, height: 1000 });

const api = [];
page.on('response', async (r) => {
  const u = r.url();
  const ct = r.headers()['content-type'] || '';
  if (!ct.includes('json')) return;
  if (/s3\.yandex\.net/.test(u)) return;
  try {
    const body = await r.text();
    if (body.length > 200) api.push({ url: u, body });
  } catch {}
});

await page.goto('https://koko-studio.clients.site/', { waitUntil: 'networkidle2', timeout: 90000 });
await new Promise((r) => setTimeout(r, 3000));

// go to catalog section
await page.evaluate(() => {
  const el = [...document.querySelectorAll('*')].find((e) => e.id && /catalog|goods|product/i.test(e.id));
  (el || document.body).scrollIntoView();
});

const catalog = [];

async function grabCards() {
  return page.evaluate(() => {
    const out = [];
    // find price nodes and walk up to card
    const nodes = [...document.querySelectorAll('*')].filter(
      (e) => e.children.length === 0 && /^\s*[\d\s\u00a0]+₽\s*$/.test(e.textContent || '')
    );
    for (const n of nodes) {
      let card = n;
      for (let i = 0; i < 6 && card.parentElement; i++) {
        card = card.parentElement;
        if (card.querySelector('img')) break;
      }
      const img = card.querySelector('img');
      out.push({
        price: n.textContent.trim(),
        text: card.innerText.trim(),
        img: img ? img.currentSrc || img.src : null,
        alt: img ? img.alt : null,
      });
    }
    return out;
  });
}

async function clickByText(txt) {
  return page.evaluate((t) => {
    const els = [...document.querySelectorAll('button,a,div,span,li')];
    const el = els.reverse().find((e) => (e.textContent || '').trim() === t && e.offsetParent !== null);
    if (el) { el.click(); return true; }
    return false;
  }, txt);
}

// tabs
const tabs = await page.evaluate(() => {
  const t = [
    'Все',
    'LED наращивание ресниц | Ведущий Мастер',
    'LED наращивание ресниц | Топ Мастер',
    'Косметология',
    'LED наращивание ресниц | Дополнительные услуги',
    'АКЦИИ!',
  ];
  return t;
});

for (const tab of tabs) {
  await clickByText(tab);
  await new Promise((r) => setTimeout(r, 2500));
  for (let p = 1; p <= 8; p++) {
    const cards = await grabCards();
    catalog.push({ tab, page: p, cards });
    const ok = await clickByText(String(p + 1));
    if (!ok) break;
    await new Promise((r) => setTimeout(r, 2500));
  }
}

fs.writeFileSync(`${OUT}/catalog.json`, JSON.stringify(catalog, null, 2), 'utf8');
fs.writeFileSync(`${OUT}/api.json`, JSON.stringify(api, null, 2), 'utf8');
console.log('catalog groups:', catalog.length, 'api responses:', api.length);
await browser.close();
