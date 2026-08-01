import puppeteer from 'puppeteer';
import fs from 'fs';

const OUT = 'c:/autosait/koko-studio';

const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
const page = await browser.newPage();
await page.setViewport({ width: 1440, height: 1000 });
const imgUrls = new Set();
page.on('response', (r) => {
  const u = r.url();
  if (/avatars\.mds\.yandex\.net|\.(jpg|jpeg|png|webp)(\?|$)/i.test(u)) imgUrls.add(u);
});

await page.goto('https://koko-studio.clients.site/', { waitUntil: 'networkidle2', timeout: 90000 });
await new Promise((r) => setTimeout(r, 4000));

// click every "Показать ещё" / expand button we can find, repeatedly
for (let pass = 0; pass < 8; pass++) {
  const clicked = await page.evaluate(() => {
    const btns = [...document.querySelectorAll('button, a, div[role="button"]')];
    let n = 0;
    for (const b of btns) {
      const t = (b.textContent || '').trim().toLowerCase();
      if (t.includes('показать ещё') || t.includes('показать еще') || t === 'показать') {
        b.click();
        n++;
      }
    }
    return n;
  });
  await page.evaluate(() => window.scrollBy(0, 2000));
  await new Promise((r) => setTimeout(r, 2500));
  if (!clicked) break;
}
// full scroll to trigger lazy loads
await page.evaluate(async () => {
  for (let y = 0; y < document.body.scrollHeight; y += 600) {
    window.scrollTo(0, y);
    await new Promise((r) => setTimeout(r, 120));
  }
});
await new Promise((r) => setTimeout(r, 4000));

const html = await page.content();
fs.writeFileSync(`${OUT}/rendered.html`, html, 'utf8');

const domImgs = await page.evaluate(() =>
  [...document.querySelectorAll('img')].map((i) => ({ src: i.currentSrc || i.src, alt: i.alt, w: i.naturalWidth, h: i.naturalHeight }))
);

const text = await page.evaluate(() => document.body.innerText);
fs.writeFileSync(`${OUT}/rendered.txt`, text, 'utf8');

fs.writeFileSync(
  `${OUT}/images.json`,
  JSON.stringify({ network: [...imgUrls], dom: domImgs }, null, 2),
  'utf8'
);

console.log('network imgs:', imgUrls.size, 'dom imgs:', domImgs.length);
await browser.close();
