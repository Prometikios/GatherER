import subprocess, os
from pip._internal.operations import freeze

def IsItOkay():
    '''Checks if everything okey and if not Asks for permition to fix'''
    try:
        import pipreqs
    except ImportError:
        subprocess.check_call(['pip3', 'install', 'pipreqs'])

    subprocess.run(["cd", str(os.getcwd)], shell=True, capture_output=True, text=True)
    result = subprocess.run(["pipreqs", '.'], shell=True, capture_output=True, text=True)
    print(result.stdout) #Creates a req file in users device
    ReqSetInProject = set(line.strip().split('=')[0].replace('_', '-') for line in open('requirements.txt'))
    
    ModulesInDevice = set()
    pkgs = freeze.freeze()
    for pkg in pkgs: ModulesInDevice.add(pkg.strip().split('=')[0])
    
    GoSign = False
    if not ReqSetInProject.issubset(ModulesInDevice) : #checks if all modules r not in device
        UserPermission = input('It seems your device missing some modules. Can I install 4 u? \n Y or N \n')
        if UserPermission == 'Y': #If not asks for permition to install
            GoSign = True
        else:
            print('Your choice. Its not gonna work. -_-')
    os.remove('requirements.txt')
    return GoSign, ReqSetInProject, ModulesInDevice

def GoodToGO():
    '''Fixes the dependencies'''
    Signal = IsItOkay()
    if Signal[0] == True:
        for everyModule in Signal[1]:
            if everyModule in Signal[2]:
                print(f'{everyModule} is K.')
            else:
                install(everyModule)
    else:
        print('Everything K. Good 2 go shifu')
def install(module):
    subprocess.check_call(['pip3', 'install', module])
    print(f"The module {module} is installed")

if __name__ == '__main__':
    GoodToGO()
    
#RESULT doesnt print?
