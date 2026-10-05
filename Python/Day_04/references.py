spam = 100 

trust = spam

spam = 2000

print(trust)


# but in case of python data structure it will work differently

num = [1,2,3,4]
digit = num

digit.append(5)

print(num) # <--- o/p : 1,2,3,4,5 here the reference works diff 

def update_funtion(list): 
    list.append(3)

# data structure
org = [1,2]
update_funtion(org)
print(org) # <--- here data structure got updated

# 
