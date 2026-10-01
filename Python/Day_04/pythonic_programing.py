from itertools import zip_longest
# pythonic programming contains some methods makes our tasks so easy 


# enumerate() methods : 
languages = ["java", "python", "c++"]

# using for loop
for index, items in enumerate(languages, start=1) :
    print(index, items)

print([items for items in enumerate(languages, start=1)]) 

# zip ()  :
player_name = ["Alice", "Bob", "David", "Mikasa"]
scores = [10, 2]

for name, score in zip(player_name, scores):
    print(name,"-",score)

# What happens if one list is longer than the other?
#By default, zip() stops as soon as the shortest iterable runs out of elements. Any extra elements in the longer list are completely ignored.
# zip can igonre the missing places 

# still we can import zip_longest from the pkg 

for name, score in zip_longest(player_name, scores, fillvalue="NA"):
    print(name, score)
