import math
print(len(data)/2)

f=open("input.txt", "r")
if f.mode == 'r':
    contents =f.read()

def convert(n):
    return [(n//(10**i))%10 for i in range(math.ceil(math.log(n, 10))-1, -1, -1)]

data = convert(int(contents))

sumInt = 0
for i in range(0, len(data)):
    index1 = int(i % len(data))
    index2 = int(i + len(data)/2) % len(data)
    if data[index1] == data[index2]:
        sumInt += data[i]
print(sumInt)
