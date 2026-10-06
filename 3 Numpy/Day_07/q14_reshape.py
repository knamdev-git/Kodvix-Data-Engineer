import numpy as np 

arr = np.array([
 [ 1,  2,  3,  4],
 [ 5,  6,  7,  8],
 [ 9, 10, 11, 12]
])

# print(arr.reshape(5,3)) <---- error occurs
'''
Why the Error Occurs
The core rule of numpy.reshape is that the total number of elements must remain exactly the same.
1. Your new target shape is (5, 3), which represents 5 rows and 3 columns.
2. A matrix of size 5 × 3 requires exactly 15 elements (5 × 3 = 15).
3. If your original array (arr) has more or fewer than 15 elements (for example,
 if it has 8, 12, or 16 elements), NumPy cannot evenly fit the data into a 5×3 grid without cutting data out or leaving empty spaces.
 Because reshape() never deletes or fabricates data, it breaks and raises an error
'''

# to prevent this error we can do 

arr = np.arange(15)
arr2 = arr.reshape(5,3)
print(arr2)