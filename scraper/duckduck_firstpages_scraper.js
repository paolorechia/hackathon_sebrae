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
  const search_name_filtered = encodeURI(search_name.toLowerCase().replace('calcado', 'calçado'));

  console.log('Starting to scrape ' + search_name_filtered);
  width = 800;
  height = 1024;
  const browser = await puppeteer.launch({ 
      headless: false, 
      defaultViewport: { width, height },
  });
  const page = await browser.newPage();
  await page.setViewport( { 'width' : width, 'height' : height } );
  const useKnob = false;
  if (useKnob) {
    await page.goto(`https://duckduckgo.com/t`);
    await page.waitFor(KNOB_AWAIT_TIME);
    const switch_knob = await page.$('.switch__knob')
    await switch_knob.click();
    await page.waitFor(2000);
  }
  await page.goto(`https://duckduckgo.com/${search_name_filtered}`);
  console.log('Searched');
  await page.waitFor(SEARCH_AWAIT_TIME);
  const hrefs = await page.$$eval('a', as => as.map(a => a.href));
  clean_hrefs = hrefs.filter( a => a.indexOf('duckduckgo') === -1)
                     .filter( a => a.indexOf('youtube') === -1)
                     .filter( a => a.indexOf('spreadprivacy') === -1)
                     .filter( a => a.indexOf('donttrack') === -1);

  console.log(hrefs);
  const jsonContent = JSON.stringify(clean_hrefs);

  console.log('Saving at ' + output_filepath)
  fs.writeFile(output_filepath, jsonContent, function (err) {
    console.log(err);
  });
//  await browser.close();
})();
