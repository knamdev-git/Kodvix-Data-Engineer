'''
Question 6
Using employees:
Find the employee(s) who have the highest salary.
Important requirement:
Your solution must return all employees if multiple employees share the highest salary.

Don't assume there is only one highest-paid employee.
'''
from file import Data 
import pandas as pd 

emp = Data.employees

highest_salary_emp  = emp["salary"].max()
print(emp[emp["salary"] == highest_salary_emp])