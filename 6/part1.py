import numpy as np
array = np.loadtxt("input.txt").tolist()
seens = []
seens.append(array) # we've seen the first array
stepsCounter = 0
oldArray = list(array)
while len(seens) == len(np.unique(seens, axis=0)):
    newArray = list(oldArray)
    maxVal = max(newArray)
    maxValIndex = newArray.index(max(newArray))
    newArray[maxValIndex] = 0
    # my poor little computer is literally screaming
    for i in range(1, int(maxVal) + 1):
        index = (maxValIndex + i) % len(newArray)
        newArray[index] = newArray[index] + 1 
    seens.append(newArray)
    oldArray = list(newArray)
    stepsCounter = stepsCounter + 1
firstTime = seens.index(oldArray)
print("Saw the same in {} steps.".format(stepsCounter - firstTime))