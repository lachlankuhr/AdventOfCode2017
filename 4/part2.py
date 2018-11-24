with open("input.txt") as textFile:
    data = [line.split() for line in textFile]
sum = 0
for item in data:
    # just sort it by alphabet now 
    sortedByAlphabet = []
    for chars in item: 
        sortedByAlphabet.append(''.join(sorted(chars)))
    if len(sortedByAlphabet) == len(set(sortedByAlphabet)):
        sum = sum + 1
    else:
        sum = sum + 0
print("The sum is {}".format(sum)) 