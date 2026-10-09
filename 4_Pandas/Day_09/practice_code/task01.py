'''
Clean and transform a messy CSV; 
deliver a reproducible notebook and 3 insights.
'''
import pandas as pd 

data = pd.read_csv("/home/anjali/GitHub/Kodvix-Data-Engineer/4_Pandas/Day_09/practice_code/Data.csv")
# print(data)

# Main task is to clean the mess from the csv file 

# EXTRACTING DATA 
print(
    # data.head(),"\n",
# data.tail(2),"\n",
# data.shape,"\n",
# data.columns,"\n",
# data.dtypes,"\n",
# data.info(),"\n",
# data.describe()
)
print(data)

# messy data 
# finding missing values 
# print(data.isna().sum())
# print(data.duplicated().sum())
# print(data.nunique())
# print(data["age"].nunique)

# CLEANING DATA 
data.columns = data.columns.str.title()
# print(data)

    # removing whitespace
# print(data.info())

data["Name"] = data["Name"].str.strip()
data["Salary"] = data["Salary"].str.strip()
data["City"] = data["City"].str.strip()

print(data)

# After striping we are making each structureds
data["City"] = data["City"].str.title()

print("Making Standarize text")
print(data)

# now setup the default values 
data["Salary"] = data["Salary"].str.replace(",", "")

print("Making Standarize text")
print(data)


median = data["Salary"].median()
data["Age"] = pd.to_numeric(data["Age"], errors="coerce")
data["Salary"] = pd.to_numeric(data["Salary"], errors="coerce")

print("Fixing Ages")
print(data)


# fixing bad values now set up the missing values 


data["Name"] = data["Name"].fillna("NA")
data["Age"] = data["Age"].fillna("0.0")
data["Salary"] = data["Salary"].fillna(median)
data["City"] = data["City"].fillna("Unknown")
data["Join_Date"] = data["Join_Date"].fillna("DD/MM/YYYY")

print("Filling improper values")
print(data)

# checking duplicates 

# print("Duplicate Values\n",data.duplicated().sum())
# in this table there should be only 1 customer_id 
print("Duplicate Customer_Ids\n",data["Customer_Id"].duplicated().sum())
data.drop_duplicates(
    subset=["Customer_Id"],
    inplace=True
)
print(data)
# print("Duplicate Customer_Ids\n",data["Customer_Id"].duplicated().sum())

print("==================================")
# transform the data from this file to actaul csv file
#   ---> it  means that to turn the important data into usefull data 
#   ---> Like salary can be converted into Annual Salary 

data["Annual_Salary"] = data["Salary"] * 12
print(data)


# to check the values count
# print(
# data["Join_Date"].value_counts()
# )

print(data['Age'][(data['Annual_Salary'] == data["Annual_Salary"].max())])