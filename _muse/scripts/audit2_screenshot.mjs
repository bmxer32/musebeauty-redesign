import('puppeteer').then(async ({default: puppeteer}) => {
  const browser = await puppeteer.launch({headless: 'new'});
  const page = await browser.newPage();
  await page.setViewport({width: 1400, height: 2000});
  await page.goto('http://localhost:8080/audit2.html', {waitUntil: 'networkidle0'});
  await page.screenshot({path: 'c:/autosait/audit2_screenshot.png', fullPage: true});
  console.log('audit2_screenshot.png saved');
  await browser.close();
});
