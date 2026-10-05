import numpy as np

random_numbers = np.random.default_rng()


for i in range(10):
    # numeric_random_generator = random_numbers.integers(low=0, high=9, size=(3,2)) #it
    numeric_random_generator = random_numbers.integers(low=0, high=9)  

    # uniform_random_generator = random_numbers.uniform(low=-1, high=1)
    uniform_random_generator = random_numbers.uniform(low=-1, high=1, size=2) #it 

     
    numeric_random_generator_list = []
    numeric_random_generator_list.append(uniform_random_generator) 
    print(uniform_random_generator)

print(numeric_random_generator_list)
print(random_numbers.shuffle(numeric_random_generator_list))
print(type(numeric_random_generator_list))




# fruits example with string 
fruits = np.array(["apple", "cherry", "banana", "berries", "Strawberry"])
# print(random_numbers.choice(fruits))
print(random_numbers.choice(fruits, size=2))

