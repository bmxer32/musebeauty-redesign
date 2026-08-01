import puppeteer from 'puppeteer';
import fs from 'fs';

const DIR = 'c:/autosait/koko-studio/assets/img';
const files = fs.readdirSync(DIR).filter((f) => f.endsWith('.jpg')).sort();
const PER = 24;
const browser = await puppeteer.launch({ headless: 'new' });
const page = await browser.newPage();

for (let s = 0; s * PER < files.length; s++) {
  const chunk = files.slice(s * PER, (s + 1) * PER);
  const html = `<style>
  body{margin:0;background:#111;font:12px monospace;color:#fff}
  .g{display:grid;grid-template-columns:repeat(6,1fr);gap:4px;padding:4px}
  .c{position:relative;aspect-ratio:1;overflow:hidden;background:#000}
  .c img{width:100%;height:100%;object-fit:cover}
  .c b{position:absolute;left:0;top:0;background:#000c;padding:2px 4px;font-size:14px;color:#0f0}
  </style><div class="g">${chunk
    .map((f) => `<div class="c"><img src="file:///${DIR}/${f}"><b>${f.replace('.jpg', '')}</b></div>`)
    .join('')}</div>`;
  fs.writeFileSync(`c:/autosait/koko-studio/sheet${s}.html`, html);
  await page.goto(`file:///c:/autosait/koko-studio/sheet${s}.html`, { waitUntil: 'networkidle0' });
  await page.setViewport({ width: 1200, height: 800 });
  await new Promise((r) => setTimeout(r, 800));
  await page.screenshot({ path: `c:/autosait/koko-studio/sheet${s}.png`, fullPage: true });
  console.log('sheet', s, chunk.length);
}
await browser.close();
