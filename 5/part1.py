import numpy as np
array = np.loadtxt("input.txt")
index = 0
counter = 0
while (index < len(array)):
    value = array[int(index)]
    array[int(index)] = array[int(index)] + 1
    index = index + value
    counter = counter + 1
print("It took {} steps.".format(counter))
    

