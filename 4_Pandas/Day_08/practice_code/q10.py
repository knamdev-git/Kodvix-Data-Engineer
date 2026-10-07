'''
Q10
Using employees:

Find the average salary of employees in each city.

Requirements:

Group by city
Calculate average salary
Return city + average salary.
'''

from file import Data 
import pandas as pd

emp = Data.employees
department = Data.departments

average_salary_city = emp.groupby("city")["salary"].mean()
print(average_salary_city)