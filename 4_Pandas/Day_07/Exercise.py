import pandas as pd 

pokemons_data = pd.read_csv("/home/anjali/GitHub/Kodvix-Data-Engineer/4_Pandas/Day_07/pokemon_first_150.csv", index_col="Name")
specific_pokemon = []

pokemon_name = input("Enter the pokemon name : ")
try : 
    print(pokemons_data.loc[pokemon_name])
except : 
    print("This pokemon not listed in Pokedex or not valid")