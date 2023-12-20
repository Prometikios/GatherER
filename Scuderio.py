import WebScarp1, GatherIngs1, Integrations, Translatior, NeedsCheck, os

def MainFucker():
    NeedsCheck.GoodToGO()
    WebScarp1.THEfunction()
    GatherIngs1.TheFunction()
    AskingForTranslation = input('\nDo u want me to translate them sir?\n [WARNING: it may take 2mins]\n \n Y or N \n')
    if AskingForTranslation == 'Y':
        Translatior.theFunction()
    Integrations.WhatToDo()
    AskingPerPulire = input('\nDo u want me to delete unnecasarry files 4 u shifu? Y or N \n ')
    if AskingPerPulire == 'Y':
        os.remove('cIngredients.json')
        os.remove('Ingredients.json')
MainFucker()

#orginize github
#Goodtogo not sure works like what i want?  