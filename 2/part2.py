import numpy as np

def find_divisor_division(a):
    # quick and dirty
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            # avoid detecting "even" division with itself
            if i == j: 
                continue
            # make sure modulo doesn't do inverse 
            larger = a[i] if a[i] > a[j] else a[j]
            smaller = a[i] if a[i] <= a[j] else a[j]
            if larger % smaller == 0:
                return  larger / smaller


matrix = np.loadtxt("input.txt")
divisions = np.apply_along_axis(find_divisor_division, axis=1, arr=matrix) 
print(sum(divisions))