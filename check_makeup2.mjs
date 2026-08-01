import('puppeteer').then(async ({default: puppeteer}) => {
  const browser = await puppeteer.launch({headless: 'new'});
  const page = await browser.newPage();
  await page.setViewport({width: 400, height: 350});
  await page.goto('http://localhost:8080/assets/img/v3_makeup_gal_2.jpg', {waitUntil: 'networkidle0'});
  await page.screenshot({path: 'c:/autosait/check_makeup2.png'});
  console.log('OK');
  await browser.close();
});
