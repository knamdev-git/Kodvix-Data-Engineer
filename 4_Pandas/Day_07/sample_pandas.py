import pandas as pd


data = [101 ,201, 302]
# data = [10,"str",20.0,30] 

print(data, type(data))
series = pd.Series(data)

# if i want to provide the index
list_index = ["*" for val in range(0,len(data))]
print(list_index,type(list_index))

seies_with_index = pd.Series(data, index=[val for val in range(0,len(data))])
 
print(series)

# getting the location of the index
print(series.loc[1])

# Can also work with dictionaries 
food_tracker = {
    "Day 01" : 1200,
    "Day 02" : 1730,
    "Day 03" : 1430,
    "Day 04" : 1500
}

food_tracker_series = pd.Series(food_tracker)

food_tracker_series["Day 03"] += 500

print(food_tracker_series.loc["Day 01"]) #provides the value of Key of that value 
print(food_tracker_series)


# we have to post 1 series 
pokemon = ["Bulbasor", "Charmendar", "Charmelion", "Charizard"]

pokemon_series = pd.Series(pokemon, index=["Pokemon "+str(index) for index in range(1,len(pokemon)+1)])

print(pokemon_series)

