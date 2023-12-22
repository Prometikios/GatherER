import WebScarp1, GatherIngs1, Integrations, Translatior, NeedsCheck, os



def MainFucker():
    NeedsCheck.GoodToGO()
    WebScarp1.THEfunction()
    GatherIngs1.TheFunction()
    AskingForTranslation = input(f'\nDo u want me to translate them into {GatherIngs1.bcolors.OKGREEN}it{GatherIngs1.bcolors.ENDC}ali{GatherIngs1.bcolors.FAIL}an{GatherIngs1.bcolors.ENDC} sir?\n [WARNING: it may take {GatherIngs1.bcolors.WARNING}2mins{GatherIngs1.bcolors.ENDC}]\n \n Y or N \n')
    if AskingForTranslation == 'Y':
        Translatior.theFunction()
    Integrations.WhatToDo()
    AskingPerPulire = input(f'\nDo u want me to{GatherIngs1.bcolors.WARNING} delete unnecasarry files{GatherIngs1.bcolors.ENDC} [those I created] 4 u shifu? Y or N \n ')
    if AskingPerPulire == 'Y':
        os.remove('cIngredients.json')
        os.remove('Ingredients.json')
MainFucker()



#Eng entegration?
#dont give your infos and user should get in self?