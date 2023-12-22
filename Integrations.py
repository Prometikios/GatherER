def WhatToDo():
    TheCondition = None
    while TheCondition != True:
        UserAnswer = input("\nWhat should I assist you with? \n Email \n Notion \n GoogleKeep\n\n")
        if UserAnswer == 'Email' or UserAnswer == 'email':
            TheCondition = True
            Postman()
        elif UserAnswer == 'Notion' or UserAnswer == 'notion':
            TheCondition = True
            NotionListPageMaker()
        elif UserAnswer == 'GoogleKeep' or UserAnswer=='googlekeep':
            TheCondition = True
            GoogleKeepListMaker()
        else:
            TheCondition = False

def Postman():
    '''Asks for mail to send the files'''
    r_mail = input(f'Would u like me to send the list to your e-mail? \n if yes, log [your mail] \n if no, just log [NO] \n \n')
    bot_mail = 'alfred.mio.bot@gmail.com'
    if str(r_mail) != 'NO':
        print("Great, wait a sec...")
        OnlineListLink = OnlineListMaker()

        body = f"This message is sent from Python. \n And here is your Shop List Link => {OnlineListLink} ."
        yag = yagmail.SMTP(bot_mail, 'xhwj folz okmj xwsg')
        yag.send(
            to=r_mail,
            subject="Your Shop Mail Post shifu",
            contents=body, 
            #attachments=package,
        )
        print('Grande, it should be inside of your inbox.')

def OnlineListMaker():
    '''Makes a list and returns the link of it!'''
    with open('cIngredients.json', "r") as f:
        ImportedDict = json.load(f)
    driver = Driver(uc=True)
    driver.get('https://www.checkli.com')
    firstBUTTON = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a.btn-primary.btn-large.btn-lg.text-decoration-none')))
    firstBUTTON.click()

    for keyDi in ImportedDict:
        place0 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name=add-task]')))
        place0.send_keys(f'{keyDi} : {ImportedDict[keyDi]}')
        place0.send_keys(Keys.ENTER)
    linkOFlist = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea.margintop.ng-binding')))
    Link = linkOFlist.text
    print(Link)
    driver.quit()
    return Link


def GoogleKeepListMaker():
    '''Goes to make a Google-Keep list through user mail and password'''
    user_mail = input('Whats your mail adress? [We need it to make a googleKeep page 4 u] \n ')
    with open('cIngredients.json', "r") as f:
        ImportedDict = json.load(f)
    user_password = input('Whats your e-mail password? [We need it to make a googleKeep page 4 u] \n')
    driver = Driver(uc=True)
    driver.get('https://keep.google.com')
    gmail_mailPlace = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#identifierId')))
    gmail_mailPlace.send_keys(user_mail)
    gmail_mailPlace.send_keys(Keys.ENTER)
    time.sleep(2)
    ActionChains(driver)\
        .send_keys(user_password)\
        .send_keys(Keys.ENTER)\
        .perform()
    print('U have 2mins to skip the verification layer sir! [Just a reminder]')

    TakeNoteButton = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.notes-container.RfDI4d-sKfxWe > div.RfDI4d-Iu19ad > div.RfDI4d-bN97Pc.ogm-kpc > div.h1U9Be-xhiy4.qAWA2 > div.IZ65Hb-n0tgWb.di8rgd-r4nke > div.IZ65Hb-TBnied.zTETae-h1U9Be-hxXJme > div.IZ65Hb-s2gQvd > div.IZ65Hb-qJTHM-haAclf > div.notranslate.IZ65Hb-YPqjbf.fmcmS-x3Eknd.h1U9Be-YPqjbf')))
    TakeNoteButton.click()
    for eachKey in ImportedDict:
        if eachKey == list(ImportedDict.keys())[0]:
            ActionChains(driver)\
                .send_keys(f"{eachKey} : {ImportedDict[eachKey]}")\
                .key_down(Keys.COMMAND)\
                .key_down(Keys.SHIFT)\
                .send_keys('8')\
                .key_up(Keys.COMMAND)\
                .key_up(Keys.SHIFT)\
                .send_keys(Keys.ENTER)\
                .perform()
        else:
            ActionChains(driver)\
                .send_keys(f"{eachKey} : {ImportedDict[eachKey]}")\
                .send_keys(Keys.ENTER)\
                .perform()
    TitlePlace = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.notranslate.IZ65Hb-YPqjbf.fmcmS-x3Eknd.r4nke-YPqjbf')))
    TitlePlace.click()
    TitlePlace.send_keys('Shop list')
    time.sleep(8)
    driver.quit()
    print('It is on your Google Keep page \n check it out =>  https://keep.google.com')
    pc.copy('https://keep.google.com')
    
def NotionListPageMaker():
    '''Goes to make a Notion with just user mail + temp.code => creates a SHOP LIST page'''
    notion_account_mail = str(input("What is your notion account email? \n"))
    #n_a_password = 'AlfredMio2005' #input("What is your notion account password? \n")
    with open('cIngredients.json', "r") as f:
        ImportedDict = json.load(f)
    chrome = Driver()
    chrome.get('https://www.notion.so/login')
    n_MailPlace = WebDriverWait(chrome, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#notion-email-input-2')))
    n_MailPlace.send_keys(notion_account_mail)
    n_MailPlace.send_keys(Keys.ENTER)
    print("Check your inbox and just copy the temp. code? \n")
    pc.waitForNewPaste()
    print(pc.paste())
    n_a_TempCode = pc.paste()
    WebDriverWait(chrome, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#notion-password-input-1')))
    ActionChains(chrome)\
        .send_keys(n_a_TempCode)\
        .send_keys(Keys.ENTER)\
        .perform()

    AddPage = WebDriverWait(chrome, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#notion-app > div > div:nth-child(1) > div > nav > div > div > div > div:nth-child(3) > div > div.notion-scroller.vertical > div.notion-outliner-private > div > div:nth-child(2)')))
    AddPage.click()
    ActionChains(chrome)\
            .send_keys('Your Shop list')\
            .send_keys(Keys.ENTER)\
            .perform()
    for eachKey in ImportedDict:
        if eachKey == list(ImportedDict.keys())[0]:
            ActionChains(chrome)\
                .send_keys("[] ")\
                .send_keys(f"{eachKey} : {ImportedDict[eachKey]}")\
                .send_keys(Keys.ENTER)\
                .perform()
        elif eachKey == list(ImportedDict.keys())[-1]:
            ActionChains(chrome)\
                .send_keys(f"{eachKey} : {ImportedDict[eachKey]}")\
                .perform()
        else:
            ActionChains(chrome)\
                .send_keys(f"{eachKey} : {ImportedDict[eachKey]}")\
                .send_keys(Keys.ENTER)\
                .perform()
    time.sleep(5)
    chrome.save_screenshot("ss.png")
    chrome.quit()
    # =>Notionda inbox pop up
if __name__ == '__main__':
    import undetected_chromedriver as uc
    from seleniumbase import Driver
    from selenium.webdriver import ActionChains
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    import json, yagmail, time
    import pyperclip as pc
    WhatToDo()

#=> inserting mail validation? (its rn in PAPPA.py)