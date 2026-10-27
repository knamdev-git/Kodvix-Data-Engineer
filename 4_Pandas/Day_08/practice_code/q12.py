'''
Q12
Using employees:
Find the city with the highest number of employees.
Requirements:
- Count employees in each city.
- Return the city and employee count.
- Don't manually assume which city has the highest count.
'''

from file import Data 
import pandas as pd

emp = Data.employees
department = Data.departments

highest_total_emp_in_city = emp.groupby("city").size()
max_count = highest_total_emp_in_city.max()

result = highest_total_emp_in_city[highest_total_emp_in_city == max_count]
print(result)

