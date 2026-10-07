'''
Q19
Using employees:
Find all employees whose salary is above their department's average salary.
Requirements:
- Calculate the average salary for each department_id.
- Compare each employee's salary with their own department's average.
- Return the complete employee rows.
💡 Hint: You'll need groupby() + merge() + filtering.
'''
from file import Data 
import pandas as pd

emp = Data.employees
department = Data.departments

dep_avg_salary =(
    emp.groupby("department_id")["salary"]
    .mean()
    .reset_index(name="average_salary")
) 
new_emp_dep_sal = emp.merge(dep_avg_salary, on="department_id")

# print(new_emp_dep_sal)
print(new_emp_dep_sal[["name", "department_id", "salary", "average_salary" ]][new_emp_dep_sal["salary"] > new_emp_dep_sal["average_salary"]])
# print(emp)

#  print(emp_salary_high_then_avg)
