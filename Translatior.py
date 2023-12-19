from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import json
driver = webdriver.Chrome()


with open('TESTIngredients.json', "r") as f:
    ImportedDictBeforeT = json.load(f)
for eachKey in ImportedDictBeforeT['Dinners'][0]:
    driver.get('https://context.reverso.net/traduzione/turco-italiano/ıspanak')
    Search_Box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input.keyboardInput.ui-autocomplete-input.ltr')))
    Search_Box.send_keys(eachKey)
    Search_Box.send_keys(Keys.ENTER)
    