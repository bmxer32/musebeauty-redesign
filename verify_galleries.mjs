import('puppeteer').then(async ({default: puppeteer}) => {
  const browser = await puppeteer.launch({headless: 'new'});
  const page = await browser.newPage();
  await page.setViewport({width: 1280, height: 800, deviceScaleFactor: 2});

  // Screenshot index.html gallery
  await page.goto('http://localhost:8080/index.html', {waitUntil: 'networkidle0'});
  const galSection = await page.$('.gallery-grid');
  if (galSection) {
    await galSection.screenshot({path: 'c:/autosait/verify_index_gallery.png'});
    console.log('Index gallery screenshot saved');
  }

  // Screenshot nails.html gallery
  await page.goto('http://localhost:8080/nails.html', {waitUntil: 'networkidle0'});
  const nailsGal = await page.$('.gallery-grid');
  if (nailsGal) {
    await nailsGal.screenshot({path: 'c:/autosait/verify_nails_gallery.png'});
    console.log('Nails gallery screenshot saved');
  }

  // Screenshot hair.html gallery
  await page.goto('http://localhost:8080/hair.html', {waitUntil: 'networkidle0'});
  const hairGal = await page.$('.gallery-grid');
  if (hairGal) {
    await hairGal.screenshot({path: 'c:/autosait/verify_hair_gallery.png'});
    console.log('Hair gallery screenshot saved');
  }

  await browser.close();
});
