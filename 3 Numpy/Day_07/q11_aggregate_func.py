'''
Q20. Sum
'''

import numpy as np 

arr = np.array([10, 20, 30, 40, 50])

two_d_arr = np.array([
    [10, 20, 30],
    [40,50,60]
])

print(np.sum(arr))
print(np.sum(arr, axis=0))

print(np.sum(two_d_arr, axis=0, keepdims=True))
print(np.sum(two_d_arr, axis=1, keepdims=True))


print(np.std(arr))
print(np.var(arr))

# maximum of every row

print("Maximum from each row:",np.max(two_d_arr, axis=1))
