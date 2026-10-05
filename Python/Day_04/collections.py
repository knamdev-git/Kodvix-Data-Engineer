# we have defualt dictionary : that mentations default keys if  
from collections import defaultdict

normal = defaultdict(int)

keys = [1,2,4]

for key in keys : 
    normal[key] += key

print(normal["1"])