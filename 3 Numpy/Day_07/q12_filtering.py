'''
Print Values greater than 40
'''

import numpy as np

arr = np.array([10, 25, 30, 45, 50, 65, 70])

# Print Values greater than 40
print("Values greater than 40")
print(arr[arr > 40])

# Even numbers
print("Even Numbers")
print(arr[arr % 2 == 0])

# Values between 30 and 60
print("Values between 30 and 60")
print(arr[(arr >= 30) & (arr <= 60)])

# Replace values > 40 with 100 
print("Replace values > 40 with 100")
new_arr = arr.copy() #it will change the referene from the memory do not allow to change the value for the same reference

arr[arr > 40] = 100
print(arr)

# ============== we can also use where ============
print(new_arr)