with open("input.txt") as textFile:
    data = [line.split() for line in textFile]
sum = 0
for item in data:
    if len(item) == len(set(item)):
        sum = sum + 1
    else:
        sum = sum + 0
print("The sum is {}".format(sum))