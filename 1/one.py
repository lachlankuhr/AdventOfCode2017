import math

f=open("input.txt", "r")
if f.mode == 'r':
    contents =f.read()

# should replace with numpy read
def convert_to_array(n):
    return [(n//(10**i))%10 for i in range(math.ceil(math.log(n, 10))-1, -1, -1)]
data = convert_to_array(int(contents)) # conver to array 

sum = 0 # initialise 
for i in range(0, len(data)):
    indexWrap = int(i % len(data))
    halfWayWrap = int(i + len(data)/2) % len(data)
    if data[indexWrap] == data[halfWayWrap]:
        sum += data[i]
print(sum)
