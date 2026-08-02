import puppeteer from 'puppeteer';
import fs from 'fs';
import path from 'path';

const pages = [
  'index.html',
  'lashes.html',
  'brows.html',
  'nails.html',
  'luxhair.html',
  'hair.html',
  'makeup.html',
  'contacts.html'
];

const baseUrl = 'http://localhost:8080/';
const screenshotsDir = path.join(process.cwd(), 'screenshots');

if (!fs.existsSync(screenshotsDir)) {
  fs.mkdirSync(screenshotsDir, { recursive: true });
}

async function runQA() {
  console.log('=== STARTING ENHANCED BROWSER QA VERIFICATION ===\n');

  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const results = {
    scrollOverflow: {},
    burgerMenuButtons: {},
    ctaCountMobile: {},
    ctaCountDesktop: {},
    network404Count: 0,
    consoleErrorsCount: 0
  };

  const page = await browser.newPage();

  page.on('response', response => {
    if (response.status() === 404) {
      results.network404Count++;
      console.error(`  ❌ 404 Error: ${response.url()}`);
    }
  });

  page.on('console', msg => {
    if (msg.type() === 'error') {
      results.consoleErrorsCount++;
      console.error(`  ❌ Console Error: ${msg.text()}`);
    }
  });

  for (const pageName of pages) {
    const targetUrl = `${baseUrl}${pageName}`;
    console.log(`Testing ${pageName}...`);

    // --- MOBILE TESTS (390x844) ---
    await page.setViewport({ width: 390, height: 844, deviceScaleFactor: 2 });
    await page.goto(targetUrl, { waitUntil: 'networkidle0' });

    // Check 1: Overflow
    const scrollDiff = await page.evaluate(() => {
      return Math.max(0, document.documentElement.scrollWidth - document.documentElement.clientWidth);
    });
    results.scrollOverflow[pageName] = scrollDiff;

    // Check 2: Open Burger Menu and test CTA button inside drawer
    await page.click('[data-burger],.burger-btn');
    await new Promise(r => setTimeout(r, 300));

    const hasBurgerFooter = await page.evaluate(() => {
      const btn = document.querySelector('.btn-mobile-cta');
      if (!btn) return false;
      const rect = btn.getBoundingClientRect();
      return rect.width > 0 && rect.height > 0;
    });
    results.burgerMenuButtons[pageName] = hasBurgerFooter;

    const nameWithoutExt = pageName.replace('.html', '');
    await page.screenshot({
      path: path.join(screenshotsDir, `mobile_burger_open_${nameWithoutExt}.png`),
      fullPage: false
    });

    // Close menu
    await page.click('[data-burger],.burger-btn');

    // --- DESKTOP TESTS (1280x800) ---
    await page.setViewport({ width: 1280, height: 800, deviceScaleFactor: 2 });
    await page.goto(targetUrl, { waitUntil: 'networkidle0' });

    await page.screenshot({
      path: path.join(screenshotsDir, `desktop_header_${nameWithoutExt}.png`),
      fullPage: false
    });
  }

  await browser.close();

  console.log('\n================ FINAL QA REPORT ================');
  console.log(`• Horizontal Overflow @ 390px:`, JSON.stringify(results.scrollOverflow, null, 2));
  console.log(`• Burger Menu CTA Button Visible:`, JSON.stringify(results.burgerMenuButtons, null, 2));
  console.log(`• Network 404 Errors: ${results.network404Count}`);
  console.log(`• JS Console Errors: ${results.consoleErrorsCount}`);

  const allPassed = Object.values(results.scrollOverflow).every(v => v === 0) &&
                    Object.values(results.burgerMenuButtons).every(v => v === true) &&
                    results.network404Count === 0 &&
                    results.consoleErrorsCount === 0;

  if (allPassed) {
    console.log('\n🎉 ALL QA CHECKS PASSED WITH 100% PERFECT VERIFICATION!');
  } else {
    console.error('\n⚠️ QA FAILURES DETECTED.');
    process.exit(1);
  }
}

runQA().catch(err => {
  console.error('Fatal error during QA script:', err);
  process.exit(1);
});
