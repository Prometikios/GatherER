const puppeteer = require('puppeteer');

(async () => {
    // Launch the browser and open a new blank page
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();
  
    
    await page.goto('https://www.nefisyemektarifleri.com/ispanak-yemegi-tarifi/');
    //await page.waitForTimeout(2000)
    await page.waitForSelector('button[aria-label="İzin ver"]')
    await page.click('button[aria-label="İzin ver"]')
    await page.waitForSelector("ul.recipe-materials li")

    
    await page.$eval(
        "#recipe-inner-body > article.recipe-inner.content-articles > div.row > div.recipe-materials-div.col-md-6.col-sm-12.col-xs-12 > ul",
        (ul) => {
            const AllItems = [];
    
            for (let i = 0; i < ul.children.length; i++) {
                if (ul.children[i].textContent.includes("yemek kaşığı")){
                    KeyWord_kasik = "yemek kaşığı"
                    var IndexToSliceStart = ul.children[i].textContent.lastIndexOf(KeyWord_kasik)
                    var result = ul.children[i].textContent.slice(IndexToSliceStart)

                    AllItems.push(result)
                }
                else{
                    AllItems.push(ul.children[i].textContent);
                }
                
            }
            
            return AllItems;
        }
    ).then((AllItems) => { console.log(AllItems) });


    await browser.close();

  })();