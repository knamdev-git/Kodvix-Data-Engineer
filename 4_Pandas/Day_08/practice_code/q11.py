'''
Q11
Using employees:
Find the number of employees in each city.
Requirements:
- Group by city
- Count employees in each city
- Return city + employee count.
'''

from file import Data 
import pandas as pd

emp = Data.employees
department = Data.departments

number_of_emp_in_each_city = emp.groupby("city")["employee_id"].count()
number_of_emp_in_each_city = emp.groupby("city").size()

print(number_of_emp_in_each_city)