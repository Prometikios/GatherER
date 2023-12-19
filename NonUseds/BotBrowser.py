import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://www.nefisyemektarifleri.com/ispanak-yemegi-tarifi/')
    await page.waitForSelector('button[aria-label="İzin ver"]')
    await page.click('button[aria-label="İzin ver"]')
    await page.waitForSelector("ul.recipe-materials li")

    element = await page.querySelectorAll('ul.recipe-materials li')
    title = await page.evaluate('(element) => element.textContent', element)

    print(title)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())