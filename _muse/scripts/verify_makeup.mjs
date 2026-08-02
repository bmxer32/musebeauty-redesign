import('puppeteer').then(async ({default: puppeteer}) => {
  const browser = await puppeteer.launch({headless: 'new'});
  const page = await browser.newPage();
  await page.setViewport({width: 1280, height: 800, deviceScaleFactor: 2});
  await page.goto('http://localhost:8080/makeup.html', {waitUntil: 'networkidle0'});
  const gal = await page.$('.gallery-grid');
  if (gal) {
    await gal.screenshot({path: 'c:/autosait/verify_makeup_gallery.png'});
    console.log('Makeup gallery screenshot saved');
  }
  await browser.close();
});
