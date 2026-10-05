import copy

a = [[1, 2, 3], [4, 5, 6]]

# Creating a deep copy of the nested list 'a'
b = copy.deepcopy(a)

# Modifying an element in the deep-copied list
b[0][0] = 99 
print("Deep Copy")
print("b: ", b) 
print("a: ", a)

# but let say we are not doing the deep copy so 
old = [[1, 2, 3], [4, 5, 6]]

new = old.copy()

new[0][0] = 99 

print("Shallow Copy")
print("Old: ",old) 
print("New: ", new)

# but shallow copy is not same in single list 
single_list = [1,2,3,4]

# new_inherited_single_list = single_list
new_inherited_single_list = single_list.copy()

print("Shallow copy in Single List ")
new_inherited_single_list[1] = 11111
print(single_list)
print(new_inherited_single_list)


