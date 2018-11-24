import re
import json

# Find the one that's holding up disks but nothing 
# is holding it up.
# What is the best data structure for this program? JSON

lines = []
with open("input.txt") as file:
    for line in file: 
        firstWord = re.search(r'(?:^|(?:[.!?]\s))(\w+)', line).group(0)
        number = int(re.search(r'\(.*?\)', line).group(0).replace('(','').replace(')',''))
        if len(line.split("-> ",1)) >= 2:
            nameList = line.split("-> ",1)[1].split(', ')
            i = 0
            for name in nameList: 
                nameList[i] = name.rstrip()
                i = i + 1
        else: 
            nameList = []
        json = {'firstWord' : firstWord, 'number' : number, 'names' : nameList}
        lines.append(json)

# Find the one that's holding up disks but nothing 
# is holding it up.
name = ''
for item in lines: 
    isIn = True
    for subitem in lines: 
        if item['firstWord'] in subitem['names']:
            isIn = True
            break
        else: 
            isIn = False
    if isIn == False: 
        print(item['firstWord'])