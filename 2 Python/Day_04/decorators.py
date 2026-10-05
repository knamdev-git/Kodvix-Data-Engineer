# We use decorator to inherit or extend the property of another function inside our function 

def add_cheese(func) : 
    def add_cheese_in_pizza() : 
        print("I'll add cheese")
        func() # <---- this function means it will call that function who is calling it 
        
    return add_cheese_in_pizza

def add_chopsticks(func) : 
    def wrapper(*args, **kwargs) : 
        print("I'll add chopsticks")
        return func(*args, **kwargs)

    return wrapper

def extras_with_ice_cream(func) : 
    def add_extra(*args, **kwargs) :
        print("....I am adding Choco Chips....")
        return func(*args, **kwargs)
    
    return add_extra

@add_cheese # <--- means we are calling that add_cheese decorator / method
def create_pizza() : 
    print("I am creating pizza")


@extras_with_ice_cream
@add_chopsticks
def get_ice_cream(flavor) : 
    print(f"Here's your {flavor} ice cream")

create_pizza()
# get_ice_cream("Chocolate Flavor")