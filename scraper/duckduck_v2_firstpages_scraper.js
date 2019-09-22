const process = require('process');
const puppeteer = require('puppeteer');
const fs = require('fs');

const KNOB_AWAIT_TIME = 100;
const SEARCH_AWAIT_TIME = 2000;


(async () => {
  const search_name = process.argv[2]; 
  const output_filepath = process.argv[3]; 
  if (search_name === undefined) {
    console.log('Missing seach field name');
    return;
  }
  const search_name_filtered = search_name.toLowerCase().replace('calcado', 'calçado');

  console.log('Starting to scrape ' + search_name_filtered);
  width = 800;
  height = 1024;
  const browser = await puppeteer.launch({ 
      headless: false, 
      defaultViewport: { width, height },
  });
  const page = await browser.newPage();
  await page.setViewport( { 'width' : width, 'height' : height } );
  await page.goto('https://duckduckgo.com/');
  const input = await page.$('#search_form_input_homepage');
  await input.type(search_name_filtered);
  const searchButton = await page.$('#search_button_homepage');
  searchButton.click();
  await page.waitFor(SEARCH_AWAIT_TIME);
  console.log('Searched');
  const hrefs = await page.$$eval('a', as => as.map(a => a.href));
  clean_hrefs = hrefs.filter( a => a.indexOf('duckduckgo') === -1)
                     .filter( a => a.indexOf('youtube') === -1)
                     .filter( a => a.indexOf('spreadprivacy') === -1)
                     .filter( a => a.indexOf('donttrack') === -1)
                     .filter( a => a.indexOf('wikipedia') === -1)
                     .filter( a => a.length > 6);
  if (clean_hrefs.length !== 0) {
    console.log(clean_hrefs);
    const jsonContent = JSON.stringify(clean_hrefs);
    console.log('Saving at ' + output_filepath)
    fs.writeFile(output_filepath, jsonContent, function (err) {
      console.log(err);
    });
  } else {
    console.log('Something went wrong, empty links returned')
  }
  await browser.close();
})();
