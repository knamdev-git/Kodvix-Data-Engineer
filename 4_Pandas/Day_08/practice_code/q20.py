'''
Q20
Using employees:
Find the employee with the highest salary in each department.
Requirements:
- Find the maximum salary for each department_id.
- Return the complete employee row(s).
- If two employees in the same department have the same highest salary, return both.
'''

from file import Data 
import pandas as pd

emp = Data.employees
department = Data.departments

highest_sal_dep = (emp.groupby("department_id")["salary"]
                   .max()
                   .reset_index(name="max_salary"))

new_emp = emp.merge(highest_sal_dep, on="department_id")
result = new_emp[(new_emp["salary"]) == (new_emp["max_salary"])]

print(result[["name", "department_id", "salary"]])
# now i want to print the emp who has the salary == max_salary 