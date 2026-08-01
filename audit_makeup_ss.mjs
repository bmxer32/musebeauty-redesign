import('puppeteer').then(async ({default: puppeteer}) => {
  const browser = await puppeteer.launch({headless: 'new'});
  const page = await browser.newPage();
  await page.setViewport({width: 1400, height: 600});
  await page.goto('http://localhost:8080/audit_makeup.html', {waitUntil: 'networkidle0'});
  await page.screenshot({path: 'c:/autosait/audit_makeup_screenshot.png', fullPage: true});
  console.log('OK');
  await browser.close();
});
