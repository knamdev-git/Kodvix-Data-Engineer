import pandas as pd
import numpy as np

df = pd.read_csv("/home/anjali/GitHub/Kodvix-Data-Engineer/4_Pandas/Day_07/pokemon_first_150.csv")

poisonous_pokemon = df[(df["Type 2"] == "Poison")]
print(poisonous_pokemon)

# adding one more column : based on condition
poisonous_pokemon["Dangerous"] = np.where((poisonous_pokemon["Type 1"] == "Ghost"), "Yes", "No")
print(poisonous_pokemon)
print()

# finding only water type pokemon
water_type_pokemon = df[df["Type 1"] == "Water"]
water_ice_type_pokemon = df[(df["Type 1"] == "Water") & (df["Type 2"] == "Ice")]

print("================ Water Type Pokemons ======================")
print(water_ice_type_pokemon)