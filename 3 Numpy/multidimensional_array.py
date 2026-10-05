import numpy as nm 

one_d_array = nm.array([1,2,3])
print(one_d_array.shape) #(for 1 d it will print the elements count)

two_d_array = nm.array([
    [1,2,3],
    [4,5,6]
])

print(two_d_array.shape) # for 2d it will print (rows, columns)

three_d_array = nm.array([[
    [1,2,3],
    [7,8,9]
], [
    [10, 11, 12],
    [4,5,6],
]])


print(three_d_array.shape)  # for 3d it will print (depth, rows, columns)

# string or word concatination in 3d arrat with multidimensional indexing 
print(three_d_array[0,0,0] + three_d_array[1,0,0])