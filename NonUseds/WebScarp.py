from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json


UrlSite1 = 'https://www.nefisyemektarifleri.com/ispanak-yemegi-tarifi/'
UrlSite2 = 'https://www.nefisyemektarifleri.com/yesil-mercimek-yemegi-tarifi/'
URListESEMPIO = [UrlSite1, UrlSite2]

IngType = {
    "SPOON" : 'yemek kaşığı ',
    "C_CUPS" : 'çay bardağı ',
    "PIECE" : 'adet ',
    "KG" : 'kg ',
    "S_CUPS" : 'su bardağı ',
    "CLOATH" : 'diş '
}

def ASKforINPUT():
    URLbase = 'https://www.nefisyemektarifleri.com/'
    WordsStorage = list()
    KeywordEnough = "TAMAM"
    while True:
        ObjectInput = input(f"\n \nWhich dinners' recipies should I look for? AND if these enough write '{KeywordEnough}' \n")
        WordsStorage.append(ObjectInput.lower())
        if KeywordEnough ==ObjectInput:
            break
    print(WordsStorage)
    for i, eachItem in enumerate(WordsStorage):
        if ' ' in eachItem:
            WordsStorage[i] = URLbase + eachItem.replace(' ', '-') + "-tarifi/"
        else:
            WordsStorage[i] = URLbase + eachItem + "-tarifi/"
    print(WordsStorage[:-1])
    return WordsStorage[:-1]

def FuncForFirstTimeOpen(InputURL):
    driver.get(InputURL)
    SkipX = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="İzin ver"]'))
    )
    SkipX.click()

def DinnerDictMaker(InputURL):
    driver.get(InputURL)

    ItemsInUL = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.recipe-materials'))
    )
    EachItem = ItemsInUL.find_elements(By.XPATH, '*')

    DictForExtract = dict()
    for ItemsLI in EachItem:
        ContentLI = ItemsLI.text
        for IngTypeValue in IngType.values():
            if IngTypeValue in ContentLI:
                DictForExtract[ContentLI.split(IngTypeValue)[1]] = ContentLI.split(IngTypeValue)[0] + IngTypeValue
        if all(item not in ContentLI for item in IngType.values()): #OLDU DA KAFALAR SUCUK!?
            DictForExtract[ContentLI] = True
    return DictForExtract

def MainFucker(ListURL):
    ListToStoreInDict = list()
    for eachURL in ListURL:
        if eachURL == ListURL[0]:
            FuncForFirstTimeOpen(ListURL[0]) 
            ListToStoreInDict.append(DinnerDictMaker(ListURL[0]))
        else:
            InstanceDinnerDict = DinnerDictMaker(eachURL)
            ListToStoreInDict.append(InstanceDinnerDict)
    DictToWrite = dict()
    DictToWrite['Dinners'] = ListToStoreInDict
    print(json.dumps(DictToWrite, indent=4, ensure_ascii=False)) #to see in console
    with open('InredientsFROMpy.json', 'w', encoding='utf8') as f: #Not sure how ensure&encoding => solved unicodes?
        json.dump(DictToWrite, f, ensure_ascii=False, indent=4)

URListREAL = ASKforINPUT()
driver = webdriver.Chrome()
MainFucker(URListREAL)
driver.quit()

#PROBLEM => IngTypeValue'u yazinca toplayamiyor!!?
# Yarimi => 0.5 olarak yazmak
# 'Ingredient' + (IngTypeValue) : 'Ne kadarsa'
# string olarak cikacak sayilari num() olarak yazmak!