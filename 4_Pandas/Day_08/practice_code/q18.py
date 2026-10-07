'''
Q18
Using employees:
Find the department with the lowest average salary.
Requirements:
- Calculate average salary for each department_id.
- Find the department with the lowest average salary.
- Return department_id and average salary.
- Don't manually assume the department.
'''

from file import Data 
import pandas as pd

emp = Data.employees
department = Data.departments

avg_salary = emp.groupby("department_id")["salary"].mean()
min_avg_salary_department = avg_salary.min()

print(avg_salary)
result = avg_salary[avg_salary == min_avg_salary_department]

ans = department.merge(result, on="department_id")
print(ans)

# print(avg_salary)
# print(min_avg_salary_department)

# department_with_lowest_avg_salary = (department.merge(avg_salary, on="department_id").min())
# print(department_with_lowest_avg_salary)