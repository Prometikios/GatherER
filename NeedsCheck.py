import subprocess, sys, os

def IsItOkay():
    '''Checks if everything okey and Ask for permition to fix'''
    try:
        import pipreqs
    except ImportError:
        subprocess.check_call(['pip3', 'install', 'pipreqs'])

    subprocess.run(["cd", str(os.getcwd)], shell=True, capture_output=True, text=True)
    result = subprocess.run(["pipreqs", '.'], shell=True, capture_output=True, text=True)
    print(result.stdout) #Creates a req file in users device

    ReqSetInDevice = set(line.strip().split('=')[0] for line in open('requirements.txt'))
    ListsOfModuleNames = ['pyperclip', 'selenium', 'seleniumbase', 'undetected_chromedriver', 'yagmail']
    GoSign = False
    if set(ListsOfModuleNames) <= ReqSetInDevice:
        GoSign = False
    else:
        UserPermission = input('It seems your device needs some modules. Can I install 4 u? \n Y or N \n')
        if UserPermission == 'Y':
            GoSign = True
        else:
            print('Your choice Its not gonna work. -_-')
    os.remove('requirements.txt')
    return GoSign, ListsOfModuleNames

def GoodToGO():
    '''Fixes the dependencies'''
    Sign = IsItOkay() 
    if Sign[0] == True:
        for everyModule in Sign[1]:
            if str(everyModule) in sys.modules:
                print('K 2 go.')
            else:
                install(str(everyModule))
    else:
        print('Everything K. Good to go shifu')
def install(module):
    subprocess.check_call(['pip3', 'install', module])
    print(f"The module {module} is installed")
#GoodToGO()
    
#RESULT doesnt print?