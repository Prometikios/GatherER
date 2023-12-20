const puppeteer = require('puppeteer');

(async () => {
    // Launch the browser and open a new blank page
    const browser = await puppeteer.launch({ headless: true });
    const page = await browser.newPage();
  
    
    await page.goto('https://www.nefisyemektarifleri.com/ispanak-yemegi-tarifi/');
    await page.waitForSelector("img")
    await page.waitForTimeout(2000)
    await page.click('button.fc-button,.fc-cta-consent,.fc-primary-button')
    /*const Imgs = await page.evaluate(() =>{
        const ImgLinks = Array.from(document.querySelectorAll(".giphy-grid a"))
        const ImgLink1 = ImgLinks[0].getAttribute("href")
        return ImgLink1
    })*/
    const ulPath = '/html/body/div[1]/section/div/div/div[1]/article[1]/div[1]/div[1]/ul'
    let ul = await page.$x(ulPath)
    let ul_value = await page.evaluate(el => el.textContent, ul[0])
    for (const liItems of ul.children) {
        console.log(liItems)
    }

    await browser.close();

  })();
