'''
Question 5
Using employees:
Find all employees whose salary is greater than the overall average salary.
Requirements:
- Don't manually calculate the average.
- Don't hard-code any value.
- Return the complete employee rows, not just their names.
'''

from file import Data 
import pandas as pd 

emp = Data.employees

def avg_salary(emp) : 
    return emp["salary"].mean(numeric_only=True)

print("Average salary is :",avg_salary(emp))
print(emp[
    (emp["salary"] > (avg_salary(emp)))
])
