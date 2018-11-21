import numpy as np

def find_difference_between_max_min(a):
    maxValue = np.max(a)
    minValue = np.min(a)
    difference = maxValue - minValue
    return difference


matrix = np.loadtxt("input.txt")
differences = np.apply_along_axis(find_difference_between_max_min, axis=1, arr=matrix)
print(sum(differences))