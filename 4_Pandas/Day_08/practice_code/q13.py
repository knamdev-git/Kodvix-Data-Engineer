'''
Q13
Using employees:
Find the department with the highest average salary.
Requirements:
- Calculate average salary for each department_id.
- Find the department with the highest average.
- Return department_id and average salary.
'''
from file import Data 
import pandas as pd

emp = Data.employees
department = Data.departments

highest_average_salary = emp.groupby("department_id")["salary"].mean()

# print(highest_average_salary)

department = department.merge(highest_average_salary, on="department_id")
print(department[department["salary"] == highest_average_salary.max()])