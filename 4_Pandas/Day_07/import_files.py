import pandas as pd 

# importing file and read the data 
csv_data = pd.read_csv("/home/anjali/GitHub/Kodvix-Data-Engineer/4_Pandas/Day_07/pokemon_first_150.csv", index_col="Name")

print(csv_data)
# print(csv_data.to_string())

json_data = pd.read_json("/home/anjali/GitHub/Kodvix-Data-Engineer/4_Pandas/Day_07/pokemon_first_150.json")

print(json_data)

# let say if we want to write something inside the csv 
data = pd.DataFrame([{
    "National ID" : 190,
    "Name" : "Kanha",
    "Type 1" : "NA",
    "Type 2 ": "NA",
    "Generation" : 1
}])

# print(csv_data.info())
csv_data = pd.concat([csv_data, data])
# print(csv_data)

# print(csv_data.tail(1))


csv_data.drop(index=[0], inplace=True) # if we do not apply inplace then it will not remove that row untill we apply assignment to the same variable
print(csv_data.to_string())


print(csv_data["Name"])

# prnt the pokemons where type is poison 
# print("Type 2=============\n",csv_data["Type 2"] == "Poison")

poison_type_pokemons = csv_data.loc[csv_data["Type 2"] == ("Poison")]

# print(poison_type_pokemons)
print("+++++++++++++++++++++++++++++++++++++++++++++++")
print(csv_data.loc["Charizard" : "Ditto"])
print(csv_data.loc[csv_data["Type 1"] == "Water"])