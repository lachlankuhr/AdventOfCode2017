import re
import json

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

    
def find_by_name(name, lines):
    for line in lines: 
        if (line['firstWord'] == name):
            return line

def find_total_sum_by_name(name, lines):
    theLine = find_by_name(name, lines)
    theLineNames = theLine['names']
    sum = 0
    for name in theLineNames: 
        lineTwo = find_by_name(name, lines)
        sum = sum + lineTwo['number']
        while len(lineTwo['names'] != 0):
            for 
            sum = sum + find_weight_by_name(name, lines)

def find_weight_by_name(name, lines):
    theLine = find_by_name(name, lines)
    return theLine['number']

for item in lines: 
    for subname in item['names']:
        firstLine = find_by_name(subname, lines)