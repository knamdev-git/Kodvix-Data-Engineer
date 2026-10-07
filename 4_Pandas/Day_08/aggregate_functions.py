import pandas as pd 


pokemons_csv_file = pd.read_csv("/home/anjali/GitHub/Kodvix-Data-Engineer/4_Pandas/Day_07/pokemon_first_150.csv")

# for all the numeric columns

print(pokemons_csv_file)
print("Mean \n",pokemons_csv_file.mean(numeric_only=True),"\n")
print("Sum \n",pokemons_csv_file.sum(numeric_only=True),"\n")
print("Minimum \n",pokemons_csv_file.min(numeric_only=True),"\n")
print("Maximum \n",pokemons_csv_file.max(numeric_only=True),"\n")
print("Count\n",pokemons_csv_file.count())

# for single column

print(pokemons_csv_file)
print("Single Column Mean \n",pokemons_csv_file["Generation"].mean(),"\n")
print("Single Column Sum \n",pokemons_csv_file["Generation"].sum(),"\n")
# print("Single Column Minimum \n",pokemons_csv_file["Generation"].min(),"\n")
# print("Single Column Maximum \n",pokemons_csv_file["Generation"].max(),"\n")
print("Single Column Count\n",pokemons_csv_file["National ID"].count())


# group elements 
type_grouping = pokemons_csv_file.groupby("Type 2")
print(type_grouping[["Name"]].count())
print(type_grouping[["Generation"]].sum())
# print(type_grouping[["Name"]].mean())
# print(type_grouping[["Name"]].max())
# print(type_grouping[["Name"]].min())

# printing all the fairy type pokemons
print(pokemons_csv_file[pokemons_csv_file["Type 2"]=="Fairy"])
# print(type_grouping["Type 2"].nunique())
