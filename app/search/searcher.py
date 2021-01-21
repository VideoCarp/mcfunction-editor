from searchlib import *
from os import path, listdir
directory = "infobase"
def do_search(): 
    argument = (input("Search: ")).lower()
    found = []
    def isyes(arg):
        return arg.lower().startswith("y")
    
    
    for file in listdir(directory):
        for word in argument.split(" "):
            matches = 0
            if argument == file or argument == (file.split("."))[0]:
                found.append(file)
                continue
            elif argument in file:
                found.append(file)
                continue
            elif word in file:
                matches += 1
                if matches >= 2:
                    found.append(file)
                    matches -= 2
                continue
            elif argument in read(directory+"/"+file):
                matches += 1
                if matches >= 2:
                    found.append(file)
                    matches -= 2
                continue
            elif word in read(directory+"/"+file):
                matches += 1
                if matches >= 2:
                    found.append(file)
                    matches -= 1
                continue
    
    print(f"Found {len(found)} "+("result" if len(found) == 1 else "results"))
    for info in found:
        if isyes(input(f"Would you like to see '{info}'?")):
            print(cmu_do(read(directory+"/"+info)))
        else:
            continue
