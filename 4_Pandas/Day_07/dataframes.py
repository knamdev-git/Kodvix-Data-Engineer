import pandas as pd 

data = {
    "Name" : ["Kanha","Micke", "David", "Lucy"],
    "Age" : [18,21,33,22],
    "Address" : ["Indore","Austria", "UK", "USA"]
}

dataframe = pd.DataFrame(data, index=["Employee "+str(val) for val in range(1, len(data)+2)])

print(dataframe)
print(dataframe.loc["Employee 1"])
print(dataframe.iloc[1])
print(len(data))

# creating new key to the dataframe 
dataframe["Hobby"] = ["Anime", "Painting", "Singing", "Vibe Coding"]
print(dataframe)

# adding new row inside the data frame 
row = pd.DataFrame([{
    "Name" : "Traver",
    "Age" : 22,
    "Address" : "South America",
    "Hobby" : "Workout"
}])

dataframe = pd.concat([dataframe, row])
print("Concatinated Dataframe")
print(dataframe)

# Now adding more rows simultaneously 
rows = pd.DataFrame([{"Name" : "Traver", "Age" : 22, "Address" : "South America", "Hobby" : "Workout"},
                     {"Name" : "Hustler", "Age" : 32, "Address" : "Polland", "Hobby" : "Singing"},
                     {"Name" : "Newby", "Age" : 21, "Address" : "Iceland", "Hobby" : "Dancing"},
                    ], index=["Employee 5", "Employee 6", "Employee 7"])

dataframe = pd.concat([dataframe, rows])

print("=========================================")
print(dataframe)

print(dataframe.columns) # list out all the columns inside the dataframe

print(dataframe.head(2)) #from top 2 rows
print(dataframe.tail(3)) # from bottom of the table
print(dataframe.index) #list all the indexes 
print(dataframe.dtypes) # list the datatypes of all the keys 


print("=================== Information of Dataframe Students ================")
print(dataframe.info())

print("================== Statistical Information  =================")
print(dataframe.describe()) #Provides statistical information about <<<< numerical columns >>>>.


print("======Accessing Single Column =============")
print(dataframe["Name"])


print("========== Multiple columns =============")
print(dataframe[["Name", "Age", "Hobby"]])

print("============ Conditional Usecases ========")
print(dataframe[(dataframe["Age"] < 25) & (dataframe["Hobby"] == "Workout")])


print("=========== Printing Multiple Rows ===========")
print(dataframe.iloc[0:2]) # or i think we can use head 
print(dataframe.head(2)) # o/p wil same 

# for specific cell we can write dataframe.iloc[1,2]
print("============ Setting random Value ===========")
dataframe.loc["Employee 5", "Name"] = "Twilight"
dataframe.loc["Employee 5", "Address"] = "NewYork"

print(dataframe[dataframe["Hobby"] == "Workout"]) #conditon where the user's hobby is Workout

# Rename columns
dataframe.rename(
    columns={"Name" : "First Name", "Hobby" : "Hobbies"}, #Can pass multiple column name to be replace
    inplace=True
)

print("================= After Renaming ==============\n",dataframe)

# If we want to remove a column we can do 
'''
column_name = "Age"
dataframe.drop(columns=[column_name], inplace=True) # If you do not write inplace=True then it will not delete the column 


# instead we can do 
dataframe = dataframe.drop(columns=["Hobbies"])
print(f"=================== Removing {column_name} Column =====
========")
print(dataframe)
'''
# If we want to delete the rows only 
dataframe = dataframe.drop(index=["Employee 1", "Employee 2"]) #inside index we'll pass the << label name >>> only
print("======== Deleting the row 1 & 2 ===============")
print(dataframe)

# We can perform sorting too
print("========== Sorted Table ========")
# print(dataframe.sort_values(["First Name", "Age"], ascending=[False,True]))
print(dataframe.sort_values(["Age"], ascending=[False]))