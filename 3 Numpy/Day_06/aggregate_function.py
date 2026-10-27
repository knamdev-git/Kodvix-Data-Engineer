import numpy as np 

arr1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print("Mean value:",np.mean(arr1))
print("Total sum:",np.sum(arr1))
print("Standard Daviation:",np.std(arr1))
print("Variance:",np.var(arr1))
print("Minimum:",np.min(arr1))
print("Maximum:",np.max(arr1))
print("Median :",np.median(arr1))


print("Index of greatest value:",arr1.argmax())
print("Index of Minimum value:",arr1.argmin())
print("Total Sum with axis-row sum ,column sum:",np.sum(arr1, axis=0))
print("Total Sum with axis-row sum ,column sum:",np.sum(arr1, axis=1))
# print("Total Sum with axis-row sum ,column sum:",np.sum(arr1, axis=2))#in this case of our array dimensions it will give us an error

