'''
Q11. Find shape, dimensions, and size
print(arr.shape)print(arr.ndim)print(arr.size)
'''

import numpy as np 

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr.shape)
print(arr.ndim)
print(arr.size)

# print 50 
print(arr[1,1]) #multidimensional indexing

# print second row 
print(arr[1])

# print 3rd column 

print("Third Column",arr[:, 2])

# extract 2x2 matrix
print("2x2 Matrix :\n",arr[:2,:2])