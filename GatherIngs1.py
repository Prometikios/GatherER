
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
      ListDiDicts = ImportedTotalDict["Dinners"]
      return ListCombiner(ListDiDicts)
    except FileNotFoundError:
      print( f"\n \n {bcolors.FAIL}!!!Look again to your file name Because THERE IS NO such file!!!{bcolors.ENDC}\n")

def ListCombiner(ListDiDs):
  d3 = dict(Dinners = None, **ListDiDs[0])
  DinnerNames = ListDiDs[0]["Dinner"]
  for eachDict in ListDiDs[1:]: #Skipping index zero
      for IntersectItem in d3.keys() & eachDict.keys():
        d3[IntersectItem] = d3.get(IntersectItem) + eachDict.get(IntersectItem)
      for eachDifKey in eachDict.keys() - d3.keys():
        d3[eachDifKey] = eachDict[eachDifKey]
      DinnerNames = f"{DinnerNames} & {eachDict["Dinner"]}"
  d3['Dinners'] = DinnerNames
  del d3['Dinner']
  DictPrinter(d3)
  return d3

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
  with open('cIngredients.json', 'w', encoding='utf8') as f: #for Integerations.py
    json.dump(ObjectInput, f, ensure_ascii=False, indent=4)

def TheFunction():
  DictToExport = BreakDownDict()
  DictExporter(DictToExport)

#TheFunction()
