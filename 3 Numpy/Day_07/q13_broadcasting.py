'''
Broadcasting 
'''

import numpy as np 

a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

b = np.array([1, 2, 3])

print(np.shape(a))
print(np.shape(b))
print(a+b)


# now have to calculate the same for another dimension array
arr2 = np.array([
    [10],
    [20],
    [30]
])

brr2 = np.array([1, 2, 3, 4])

print(np.shape(arr2))
print(np.shape(brr2))

print(arr2+brr2)

# creating new array 
a1 = np.ones((3,4))
b1 = np.ones(4)

print()
print("A1",a1)
print("B1",b1)

print("A + B",a1+b1)