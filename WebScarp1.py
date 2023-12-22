

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
    KeywordEnough = "K"
    while True:
        ObjectInput = input(f"\n \nWhich dinners' recipies should I look for? [write w/ english letters] AND if these enough write '{KeywordEnough} to stop' \n")
        WordsStorage.append(ObjectInput.lower())
        if KeywordEnough ==ObjectInput:
            break
    print(WordsStorage)
    for i, eachItem in enumerate(WordsStorage):
        if ' ' in eachItem:
            WordsStorage[i] = eachItem, URLbase + eachItem.replace(' ', '-') + "-tarifi/"
        else:
            WordsStorage[i] = eachItem, URLbase + eachItem + "-tarifi/"
    print(WordsStorage[:-1])
    return WordsStorage[:-1]

def FuncForFirstTimeOpen(driver, InputURL):
    driver.get(InputURL)
    SkipX = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="İzin ver"]'))
    )
    SkipX.click()

def DinnerDictMaker(driver, nameOFdinner, InputURL):
    driver.get(InputURL)

    ItemsInUL = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.recipe-materials'))
    )
    EachItem = ItemsInUL.find_elements(By.XPATH, '*')

    DictForExtract = dict()
    DictForExtract['Dinner'] = nameOFdinner
    for ItemsLI in EachItem:
        ContentLI = ItemsLI.text
        for IngTypeValue in IngType.values():
            if IngTypeValue in ContentLI:
                if ContentLI.split(IngTypeValue)[0].strip().lower() == 'yarım':
                    DictForExtract[f"{ContentLI.split(IngTypeValue)[1]} ({IngTypeValue.strip()})"] = 0.5
                elif ',' in ContentLI.split(IngTypeValue)[0].strip():
                    Value = float(ContentLI.split(IngTypeValue)[0].strip().split(',')[0]) + float(f"0.{ContentLI.split(IngTypeValue)[0].strip().split(',')[1]}")
                    DictForExtract[f"{ContentLI.split(IngTypeValue)[1]} ({IngTypeValue.strip()})"] = Value
                elif '-' in ContentLI.split(IngTypeValue)[0].strip():
                    DictForExtract[f"{ContentLI.split(IngTypeValue)[1]} ({IngTypeValue.strip()})"] = float(ContentLI.split(IngTypeValue)[0].strip().split('-')[0])
                else:
                    DictForExtract[f"{ContentLI.split(IngTypeValue)[1]} ({IngTypeValue.strip()})"] = float(ContentLI.split(IngTypeValue)[0].strip())
        if all(item not in ContentLI for item in IngType.values()): #OLDU DA KAFALAR SUCUK!?
            DictForExtract[ContentLI] = True
    return DictForExtract

def MainFucker(driver, ListURL):
    ListToStoreInDict = list()
    for DinnerName, eachURL in ListURL:
        if eachURL == ListURL[0][1]:
            FuncForFirstTimeOpen(driver, ListURL[0][1]) 
            ListToStoreInDict.append(DinnerDictMaker(driver, DinnerName, eachURL))
        else:
            InstanceDinnerDict = DinnerDictMaker(driver, DinnerName, eachURL)
            ListToStoreInDict.append(InstanceDinnerDict)
    DictToWrite = dict()
    DictToWrite['Dinners'] = ListToStoreInDict
    print(json.dumps(DictToWrite, indent=4, ensure_ascii=False)) #to see in console
    with open('Ingredients.json', 'w', encoding='utf8') as f: #Not sure how ensure&encoding => solved unicodes?
        json.dump(DictToWrite, f, ensure_ascii=False, indent=4)

def THEfunction():
    URListREAL = ASKforINPUT()
    driver = webdriver.Chrome()
    MainFucker(driver, URListREAL)
    driver.quit()

if __name__ == '__main__':
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import subprocess
    import json
    THEfunction()
#HOŞAF!!! elifler can sikici degismeli?!
#Fixs => Farkli sekilde cikabiliyor ayni malzeme
