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
  console.log('=== STARTING STAGE D BROWSER QA VERIFICATION ===\n');

  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const results = {
    scrollOverflow: {},
    burgerMenu: {},
    ctaCountMobile: {},
    ctaCountDesktop: {},
    network404Count: 0,
    consoleErrorsCount: 0,
    networkErrors: [],
    consoleErrors: []
  };

  const page = await browser.newPage();

  // Monitor network requests and console errors
  page.on('response', response => {
    if (response.status() === 404) {
      results.network404Count++;
      results.networkErrors.push(`${response.url()} -> 404`);
      console.error(`  ❌ 404 Error: ${response.url()}`);
    }
  });

  page.on('console', msg => {
    if (msg.type() === 'error') {
      results.consoleErrorsCount++;
      results.consoleErrors.push(msg.text());
      console.error(`  ❌ Console Error: ${msg.text()}`);
    }
  });

  for (const pageName of pages) {
    const targetUrl = `${baseUrl}${pageName}`;
    console.log(`Testing ${pageName} (${targetUrl})...`);

    // --- MOBILE TESTS (390x844) ---
    await page.setViewport({ width: 390, height: 844, deviceScaleFactor: 2 });
    await page.goto(targetUrl, { waitUntil: 'networkidle0' });

    // Check 1: Horizontal scroll overflow
    const scrollDiff = await page.evaluate(() => {
      return Math.max(0, document.documentElement.scrollWidth - document.documentElement.clientWidth);
    });
    results.scrollOverflow[pageName] = scrollDiff;
    if (scrollDiff === 0) {
      console.log(`  ✅ Mobile Overflow 390px: ${scrollDiff}px (PASS)`);
    } else {
      console.error(`  ❌ Mobile Overflow 390px: ${scrollDiff}px (FAIL)`);
    }

    // Check 2: Burger menu toggle visibility
    const isBurgerVisible = await page.evaluate(() => {
      const b = document.querySelector('[data-burger],.burger-btn');
      if (!b) return false;
      const rect = b.getBoundingClientRect();
      return rect.width > 0 && rect.height > 0;
    });
    results.burgerMenu[pageName] = isBurgerVisible;
    if (isBurgerVisible) {
      console.log(`  ✅ Mobile Burger Menu visible: PASS`);
    } else {
      console.error(`  ❌ Mobile Burger Menu visible: FAIL`);
    }

    // Check 3: Header CTA button count on mobile (must be exactly 1)
    const mobileCtaCount = await page.evaluate(() => {
      const elements = [...document.querySelectorAll('header a, header button')];
      return elements.filter(e => {
        const rect = e.getBoundingClientRect();
        return rect.width > 0 && rect.height > 0 && /запис|заказ|звон/i.test(e.textContent);
      }).length;
    });
    results.ctaCountMobile[pageName] = mobileCtaCount;
    if (mobileCtaCount === 1) {
      console.log(`  ✅ Header CTA count 390px: ${mobileCtaCount} (PASS)`);
    } else {
      console.error(`  ❌ Header CTA count 390px: ${mobileCtaCount} (FAIL)`);
    }

    // Take mobile screenshot
    const nameWithoutExt = pageName.replace('.html', '');
    await page.screenshot({
      path: path.join(screenshotsDir, `mobile_${nameWithoutExt}.png`),
      fullPage: true
    });

    // Test burger open screenshot
    if (isBurgerVisible) {
      await page.click('[data-burger],.burger-btn');
      await page.waitForTimeout?.(300) || new Promise(r => setTimeout(r, 300));
      await page.screenshot({
        path: path.join(screenshotsDir, `mobile_menu_${nameWithoutExt}.png`),
        fullPage: false
      });
      // Close menu
      await page.click('[data-burger],.burger-btn');
    }

    // --- DESKTOP TESTS (1280x800) ---
    await page.setViewport({ width: 1280, height: 800, deviceScaleFactor: 2 });
    await page.goto(targetUrl, { waitUntil: 'networkidle0' });

    const desktopCtaCount = await page.evaluate(() => {
      const elements = [...document.querySelectorAll('header a, header button')];
      return elements.filter(e => {
        const rect = e.getBoundingClientRect();
        return rect.width > 0 && rect.height > 0 && /запис|заказ|звон/i.test(e.textContent);
      }).length;
    });
    results.ctaCountDesktop[pageName] = desktopCtaCount;

    await page.screenshot({
      path: path.join(screenshotsDir, `desktop_${nameWithoutExt}.png`),
      fullPage: true
    });
  }

  await browser.close();

  console.log('\n================ FINAL STAGE D REPORT ================');
  console.log(`• Horizontal Overflow @ 390px:`, JSON.stringify(results.scrollOverflow, null, 2));
  console.log(`• Mobile Burger Menu Visible:`, JSON.stringify(results.burgerMenu, null, 2));
  console.log(`• Header CTA Count @ 390px:`, JSON.stringify(results.ctaCountMobile, null, 2));
  console.log(`• Header CTA Count @ 1280px:`, JSON.stringify(results.ctaCountDesktop, null, 2));
  console.log(`• Network 404 Errors: ${results.network404Count}`);
  console.log(`• JS Console Errors: ${results.consoleErrorsCount}`);

  const allPassed = Object.values(results.scrollOverflow).every(val => val === 0) &&
                    Object.values(results.burgerMenu).every(val => val === true) &&
                    Object.values(results.ctaCountMobile).every(val => val === 1) &&
                    Object.values(results.ctaCountDesktop).every(val => val === 1) &&
                    results.network404Count === 0 &&
                    results.consoleErrorsCount === 0;

  if (allPassed) {
    console.log('\n🎉 ALL STAGE D QA CHECKS PASSED WITH ZERO ERRORS!');
  } else {
    console.error('\n⚠️ SOME CHECKS FAILED. PLEASE FIX BEFORE DEPLOY.');
  }
}

runQA().catch(err => {
  console.error('Fatal error during QA script:', err);
  process.exit(1);
});
