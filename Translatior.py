import undetected_chromedriver as uc
from seleniumbase import Driver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json, time, pyperclip, json

def ToSkipPopup(driver):
    driver.get(f'https://www.reverso.net/traduzione-testo#sl=tur&tl=ita&text=ekmek')
    ActionChains(driver)\
        .send_keys(Keys.TAB *3)\
        .send_keys(Keys.ENTER)\
        .perform()
    driver.get(f'https://www.reverso.net/traduzione-testo#sl=tur&tl=ita&text=ekmek')
    driver.get(f'https://www.reverso.net/traduzione-testo#sl=tur&tl=ita&text=ekmek')
    driver.get(f'https://www.reverso.net/traduzione-testo#sl=tur&tl=ita&text=ekmek')
    driver.get(f'https://www.reverso.net/traduzione-testo#sl=tur&tl=ita&text=ekmek')
    PiuTardiButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#dapp-popup > div.dapp-popup-right > div > div.dapp-button-wrapper > button')))
    PiuTardiButton.click()

def Translatior(driver, ImportedDictBeforeT):
    dNew = dict()
    for eachKeys in ImportedDictBeforeT.keys():
        driver.get(f'https://www.reverso.net/traduzione-testo#sl=tur&tl=ita&text={eachKeys}')
        ReverseButton = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'body > app-root > app-translation > div > app-translation-box > div.translation-box > div.translation-box-wrapper.box-position-wrapper.full-screen > div.translation-languages > app-language-switch > div > button > app-icon > span')))
        ReverseButton.click()
        ActionChains(driver)\
            .key_down(Keys.COMMAND)\
            .send_keys('A')\
            .key_up(Keys.COMMAND)\
            .perform()
        time.sleep(1)
        ActionChains(driver)\
            .key_down(Keys.COMMAND)\
            .send_keys('C')\
            .key_up(Keys.COMMAND)\
            .perform()
        TranslationText = pyperclip.paste()
        print(TranslationText)
        
        dNew[eachKeys] = f'{ImportedDictBeforeT[eachKeys]} [{TranslationText}]'
    return dNew


def theFunction():
    with open('cIngredients.json', "r") as f:
        ImportedDictBeforeT = json.load(f)
    driver = Driver(uc=True)
    ToSkipPopup(driver)
    DictNewWithTranslations = Translatior(driver, ImportedDictBeforeT)
    driver.quit()
    with open('cIngredients.json', 'w', encoding='utf8') as f:
        json.dump(DictNewWithTranslations, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    theFunction()

#pop-up close? MAKES PROCESS TOO LONG!!!
#Asking for which language to translate?