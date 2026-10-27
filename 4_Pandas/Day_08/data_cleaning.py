import pandas as pd 


pokemons_csv_file = pd.read_csv("/home/anjali/GitHub/Kodvix-Data-Engineer/4_Pandas/Day_07/pokemon_first_150.csv")

pokemons_csv_file.drop(columns=["Generation"], inplace=True)
print(pokemons_csv_file)

# dropna : Drop Not Available 
# pokemons_csv_file.dropna(subset=["Type 2"], inplace=True)

# instead of droping we can fill None values with defaults 
pokemons_csv_file.fillna("Not Evolve Yet", inplace=True)
print(pokemons_csv_file.to_string())


# inconsistent value replacement 
pokemons_csv_file["Type 2"].replace({"Not Evolve Yet" : "NaN",
                                    "Poison" : "POISON"}, inplace=True)
print(pokemons_csv_file)

# standardize text
pokemons_csv_file["Type 2"] = pokemons_csv_file["Type 2"].str.capitalize()
print(pokemons_csv_file)

# fix data type
pokemons_csv_file["Type 2"] = pokemons_csv_file["Type 2"].astype(bool)
print(pokemons_csv_file["National ID"])
print(pokemons_csv_file.info())
print(pokemons_csv_file)

# duplicate remove 

print(pokemons_csv_file.drop_duplicates())