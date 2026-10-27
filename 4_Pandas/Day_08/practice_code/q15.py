'''
Q15
Using employees:
Find the department-wise highest salary.
Requirements:
- Group by department_id
- Find the maximum salary in each department.
- Return department_id and highest salary.
'''

from file import Data 
import pandas as pd

emp = Data.employees
department = Data.departments

dep_with_highest_salary = (emp.groupby("department_id")["salary"]
                           .max()
                           .reset_index(name="Highest Salary"))
# print(dep_with_highest_salary)
# print(department)

dep_wise_highest_salary = department.merge(dep_with_highest_salary, on="department_id")
print(dep_wise_highest_salary)