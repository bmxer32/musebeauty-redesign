import('puppeteer').then(async ({default: puppeteer}) => {
  const browser = await puppeteer.launch({headless: 'new'});
  const page = await browser.newPage();
  await page.setViewport({width: 1400, height: 600});
  await page.goto('http://localhost:8080/audit3.html', {waitUntil: 'networkidle0'});
  await page.screenshot({path: 'c:/autosait/audit3_screenshot.png', fullPage: true});
  console.log('OK');
  await browser.close();
});
