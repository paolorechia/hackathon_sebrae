const process = require('process');
const puppeteer = require('puppeteer');

const TYPE_AWAIT_TIME = 200;
const SEARCH_AWAIT_TIME = 2000;


(async () => {
  const search_name = process.argv[2]; 
  if (search_name === undefined) {
    console.log('Missing seach field name');
    return;
  }
  console.log('Starting to scrape' + search_name);
  width = 800;
  height = 1024;
  const browser = await puppeteer.launch({ 
      headless: false, 
      defaultViewport: { width, height } 
  });
  const page = await browser.newPage();
  await page.setViewport( { 'width' : width, 'height' : height } );
  await page.goto('https://google.com');
  const searchField = await page.$('input[title="Pesquisar"]');
  await searchField.type(search_name);
  const searchButton = await page.$('input[type="submit"]');
  await page.waitFor(TYPE_AWAIT_TIME);
  await searchButton.click();
  await page.screenshot({path: search_name + '.png'});
  await page.waitFor(SEARCH_AWAIT_TIME);
  const hrefs = await page.$$eval('a', as => as.map(a => a.href));
  console.log(hrefs);
  await browser.close();
})();
