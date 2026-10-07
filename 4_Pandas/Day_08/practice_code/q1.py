import pandas as pd 
from file import Data

employee_data = Data.employees
projects = Data.projects
departments = Data.departments

# print(employee_data)

# print("Number of rows : \n",employee_data["name"].count())
# print("Number of columns : \n", employee_data.info())
# print(len(employee_data.columns.to_list())) #count column within the employee_data

# print(employee_data.dtypes)
# print(employee_data[employee_data["salary"].isna()])


# print(employee_data[employee_data["salary"].isna() | employee_data["experience"].isna()])

# print(employee_data.isna().sum())
