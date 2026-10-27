'''
Q9
Using employees:
Find the department that has the highest total salary.
Requirements:
- Calculate total salary for each department.
- Return the department_id and total salary.
- Don't manually assume which department is highest.
'''

from file import Data 
import pandas as pd

emp = Data.employees
department = Data.departments

high_salary_deps = emp.groupby("department_id")["salary"].sum()

merged_data = department.merge(high_salary_deps, on="department_id")
print(merged_data[merged_data["salary"] == merged_data["salary"].max()])



'''
group → aggregate → merge → find maximum → filter row
'''