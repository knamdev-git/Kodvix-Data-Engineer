import numpy as nm 


array = nm.array([1,2,3,4,5])

# these are the arithmetic operations which makes good computing power to our array
# scaler term 
print(array + 1)
print(array - 1)
print(array * 2)
print(array ** 2)
print(array / 2)


# vectorized math function
decimal_array = [1.22, 3.21, 4.3, 1.1]
print("Square root:",nm.sqrt(decimal_array))
print("Floor Values:",nm.floor(decimal_array))
print("Ceil Values:",nm.ceil(decimal_array))
print("Round Values:",nm.round(decimal_array))
print("Pi value :",nm.pi)

# exercise : we have to print the area for each radius 

radii = nm.array([1,2,3])

print("Radius :",radii * nm.pi)