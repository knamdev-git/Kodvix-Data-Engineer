import numpy as np 

ages = np.array([[21,13,14,18,75],
                [38,22,15,99,18]])


# applying filtering according to our conditions 
teenagers = ages[ages <= 18]

# numpy uses C style arrays so we have to use &&, || of types operator can't use python operator 
adults_below_80 = ages[(ages < 80) & (ages > 18)]
senior_citizen = ages[(ages >= 70)]

evens = ages[(ages % 2 == 0)]
odds = ages[(ages % 2 != 0)]

# also we have .where() function : it will keep our array same but replace the desired value we pass inside the function 
replaced_adults = np.where(ages >= 18, ages, -1)

# we also use where clause if we want to preserve our shape of the array 
# otherwise boolean data will be replace the array with flattened array 
print("Replaced Adults by Array:",replaced_adults)
print("Original Array is not replaced :",ages)

print("Teenagers",teenagers)
print("Adults",adults_below_80)
print("Senior Citizen",senior_citizen)
print("Evens :",evens)
print("Odds :",odds)

list = [1,2,3,4,5,6,7]

count = 0

for l in list : 
    if(l % 2 == 0): 
        count += 1

print("Count of Evens in the list is",count)
print("Count of Odds in the list is",len(list) - count)



