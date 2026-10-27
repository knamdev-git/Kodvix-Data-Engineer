'''
Question 2
Using employee_data:
Find all employees whose salary is greater than 50,000 AND whose experience is greater than or equal to 3 years.
'''

from file import Data 
import pandas as pd 


employees = Data.employees

print(employees[
    (employees["salary"] > 50000) & (employees["experience"] >= 3)
])