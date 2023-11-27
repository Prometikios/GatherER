
#def fikir():
#    Js.VirtualBrowser = writes a File
#    pyton takes and returns a notepad

import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def BreakDownDict():
  while True: 
    try: 
      ObjectInput = input(f"{bcolors.WARNING} ==> Just NAME of the file to import from?: \n {bcolors.ENDC}")
      ObjectInputAddedJsonName = f"{ObjectInput}.json"
      with open(str(ObjectInputAddedJsonName), "r") as f:
        ImportedTotalDict = json.load(f)
      ImportedDict0 = ImportedTotalDict["Dinners"][0]
      ImportedDict1 = ImportedTotalDict["Dinners"][1]
      return ListCombiner(ImportedDict0, ImportedDict1)
    except FileNotFoundError:
      print( f"\n \n {bcolors.FAIL}!!!Look again to your file name Because THERE IS NO such file!!!{bcolors.ENDC}\n")


def ListCombiner(d1, d2):
  d3 = dict()
  for k1, v1 in d1.items():
    for k2, v2 in d2.items():
      if k1.upper() == k2.upper():
        if v1 == True and v2 == True:
          d3[k1] = v1
        else:
          v3 = v1 + v2
          d3[k1] = v3
  ExistOrNot(d3 ,d1)
  ExistOrNot(d3, d2)
  DictPrinter(d3)
  return d3

def ExistOrNot(Dict3, DictChecking):
  for key1, value1 in DictChecking.items():
    if key1 not in Dict3:
      Dict3[key1] = value1

def DictPrinter(DictToPrint):
  for keyDi in DictToPrint.keys():
    print(keyDi, ":", DictToPrint[keyDi])

def DictExporter(ObjectInput):
  FileToWrite = open("List.txt","w+")
  FileToWrite.write("==> This is your THE LIST <==\n")
  Dot = u'\u2022'
  for keyDi in ObjectInput.keys():
    FileToWrite.write(f"{Dot} {keyDi} : {ObjectInput[keyDi]}\n")
  FileToWrite.close()

def TheFunction():
  DictToExport = BreakDownDict()
  DictExporter(DictToExport)

TheFunction()
#Oneri : Dinnerlari birlestir?
#2) Sira çok saçma oluyor?
#?) Kumeleri birlestirme kafasiyla Ingitsem illa daha kolay yazilir gibi?
#Problem: Web scrapping
#Ilerisi => Multiple dinners