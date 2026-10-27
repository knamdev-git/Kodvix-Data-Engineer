'''
Q14
Using employees:
Find the employee(s) with the lowest salary.
Requirements:
- Find the minimum salary dynamically.
- Return all employees if multiple employees have the same lowest salary.
- Return the complete employee rows.
'''

from file import Data 
import pandas as pd

emp = Data.employees
department = Data.departments

min_salary = emp["salary"].min()

print(emp[emp["salary"] == min_salary])