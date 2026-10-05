import numpy as np

print(np.__version__)

arr = np.array([10, 20, 30, 40])
arr *= 2 

# but in simple list 
ls = [10,20,30,40]
ls = [ele*2 for ele in ls]
print(ls, type(ls))
print(arr,"", type(arr))