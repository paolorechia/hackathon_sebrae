const process = require('process');
const puppeteer = require('puppeteer');
const fs = require('fs');

const TYPE_AWAIT_TIME = 20;
const CLICK_AWAIT_TIME = 100;
const SEARCH_AWAIT_TIME = 2000;


(async () => {
  const search_name = process.argv[2]; 
  const output_filepath = process.argv[3]; 
  if (search_name === undefined) {
    console.log('Missing seach field name');
    return;
  }
  console.log('Starting to scrape ' + search_name);
  width = 800;
  height = 1024;
  const browser = await puppeteer.launch({ 
      headless: false, 
      defaultViewport: { width, height },
  });
  const page = await browser.newPage();
  await page.setViewport( { 'width' : width, 'height' : height } );
  await page.goto('https://google.com');
  await page.waitForSelector('input[title="Pesquisar"]', {visible: true});
  const searchField = await page.$('input[title="Pesquisar"]');
  await searchField.type(search_name);
  await page.waitFor(TYPE_AWAIT_TIME);
  
  await page.waitFor(CLICK_AWAIT_TIME);
  await page.waitForSelector('input[type="submit"]', {visible: true});
  const searchButton = await page.$('input[type="submit"]');
  console.log(searchButton)
  await searchButton.click();
  console.log( 'Clicked search button');
  await page.screenshot({path: search_name + '.png'});
  await page.waitFor(SEARCH_AWAIT_TIME);
  console.log('Searched');
  const hrefs = await page.$$eval('a', as => as.map(a => a.href));
  console.log(hrefs);
  const jsonContent = JSON.stringify(hrefs);

  console.log('Saving at ' + output_filepath)
  fs.writeFile(output_filepath, jsonContent, function (err) {
    console.log(err);
  });

  await browser.close();
})();
