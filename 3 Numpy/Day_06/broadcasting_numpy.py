import numpy as nm 


# broadcasting has some operations that allows us to make multiplication b/w two matrices 
# Rule : Two dimensions are compatible when they are equal or one of them is 1; compare dimensions from right to left.

arr1 = nm.array([[1,2,3,4,5]])
arr2 = nm.array([[1],[2],[3],[4],[5]])


print(arr1.shape)
print(arr2.shape)

print(arr1 * arr2)



a = nm.array([
    [1],
    [2],
    [3]
])

b = nm.array([[10, 20, 30, 40]])


print(a.shape)
print(b.shape)

print(a + b)