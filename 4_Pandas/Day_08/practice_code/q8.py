'''
Q8
Using employees:
Find the total salary paid by each department.
Requirements:
- Group employees by department_id
- Calculate the total salary for each department.
- Use groupby()
'''

from file import Data 
import pandas as pd

emp = Data.employees
department = Data.departments

total_paid_dep = emp.groupby("department_id")["salary"].sum()

result_department = department.merge(
    total_paid_dep, 
    on="department_id"
)

print(result_department)