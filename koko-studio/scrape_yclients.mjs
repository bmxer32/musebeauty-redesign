import puppeteer from 'puppeteer';
import fs from 'fs';
const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
const page = await browser.newPage();
await page.setViewport({ width: 420, height: 900, isMobile: true });

const api = [];
page.on('response', async (r) => {
  const u = r.url();
  if (!/api\.yclients|\/api\//.test(u)) return;
  try {
    const t = await r.text();
    if (t.length > 100) api.push({ url: u, body: t.slice(0, 200000) });
  } catch {}
});

await page.goto('https://n596014.yclients.com/company/563183/personal/select-services?o=', {
  waitUntil: 'networkidle2',
  timeout: 90000,
});
await new Promise((x) => setTimeout(x, 6000));
// expand all "ещё"
for (let i = 0; i < 3; i++) {
  await page.evaluate(() => {
    document.querySelectorAll('*').forEach((e) => {
      if (e.children.length === 0 && (e.textContent || '').trim() === 'ещё') e.click();
    });
  });
  await new Promise((x) => setTimeout(x, 1200));
}
const txt = await page.evaluate(() => document.body.innerText);
fs.writeFileSync('c:/autosait/koko-studio/yclients_services.txt', txt, 'utf8');

// master selection page
await page.goto('https://n596014.yclients.com/company/563183/personal/select-master?o=', {
  waitUntil: 'networkidle2',
  timeout: 90000,
});
await new Promise((x) => setTimeout(x, 6000));
const mtxt = await page.evaluate(() => document.body.innerText);
fs.writeFileSync('c:/autosait/koko-studio/yclients_masters.txt', mtxt, 'utf8');
const mimgs = await page.evaluate(() =>
  [...document.querySelectorAll('img')].map((i) => ({ src: i.currentSrc || i.src, alt: i.alt }))
);
fs.writeFileSync('c:/autosait/koko-studio/yclients_master_imgs.json', JSON.stringify(mimgs, null, 2), 'utf8');
fs.writeFileSync('c:/autosait/koko-studio/yclients_api.json', JSON.stringify(api, null, 2), 'utf8');
console.log('done. api responses:', api.length);
console.log(mtxt.slice(0, 800));
await browser.close();
