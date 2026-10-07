'''
Using employees:
Find the department-wise employee count.
Requirements:
- Group by department_id
- Count how many employees belong to each department.
- Return department_id and employee count.
- Include the department name as well.
Try it yourself.
'''

from file import Data 
import pandas as pd

emp = Data.employees
department = Data.departments

emp_count = emp.groupby("department_id")["employee_id"].count()
print(emp_count)

department_with_employee_count = department.merge(emp_count, on="department_id")

print(department_with_employee_count)