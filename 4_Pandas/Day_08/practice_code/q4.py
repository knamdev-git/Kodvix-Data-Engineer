'''
Question 4
Using employees:
Find all employees who live in either Delhi or Indore.
Try to solve it without writing two separate OR conditions
'''

from file import Data 
import pandas as pd 


employees = Data.employees

print(employees[
    (employees["city"] == "Delhi") | (employees["city"] == "Indore")
])

# or we can also write 

print(employees[
    (employees["city"].isin(["Delhi", "Indore"]))
])