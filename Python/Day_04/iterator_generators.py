# we have basic int number which is not iterator 
number = 2133
# print(number)

# trying to iterator in number 
'''
for i in number : 
    print(number)            <--- throw an error 
'''                 

iterable = [number]
for i in iterable : 
    print(i,"-")

# we have to make integer value iterable object first then we can do that 
