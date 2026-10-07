'''
Q7
Using employees:
Find the average salary for each department.
Requirements:
- Group employees by department_id
- Calculate the average salary
- Return the result as a DataFrame/Series.
'''

from file import Data 
import pandas as pd

emp = Data.employees
departments = Data.departments

# formula : df.groupby("GROUP_COLUMN")["VALUE_COLUMN"].AGGREGATION()

# print(avg_salary(emp))
grouped_average_salary = emp.groupby("department_id")["salary"].mean()

resultant_department = departments.merge(grouped_average_salary, on=["department_id"])

print(resultant_department)