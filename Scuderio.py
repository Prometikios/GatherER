import os
from NeedsCheck import GoodToGO
from WebScarp1 import THEfunction
from GatherIngs1 import TheFunction, bcolors
from Translatior import theFunction
from Integrations import WhatToDo


def MainFucker():
    GoodToGO() #NeedsCheck.
    THEfunction() #WebScrap1
    TheFunction() #GatherIngs1
    AskingForTranslation = input(f'\nDo u want me to translate them into {bcolors.OKGREEN}it{bcolors.ENDC}ali{bcolors.FAIL}an{bcolors.ENDC} sir?\n [WARNING: it may take {bcolors.WARNING}2mins{bcolors.ENDC}]\n \n Y or N \n')
    if AskingForTranslation == 'Y':
        theFunction() #Translatior
    WhatToDo() #Integrations
    AskingPerPulire = input(f'\nDo u want me to{bcolors.WARNING} delete unnecasarry files{bcolors.ENDC} [those I created] 4 u shifu? Y or N \n ')
    if AskingPerPulire == 'Y':
        os.remove('cIngredients.json')
        os.remove('Ingredients.json')
MainFucker()


#HOWWWW TO FIND ALL METERS FOR DINNERS
#Eng entegration?
#dont give your infos and user should get in self?