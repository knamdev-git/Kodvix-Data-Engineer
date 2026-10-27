'''
Q17
Using employees:
Find the city with the highest average salary.
Requirements:
- Calculate average salary for each city.
- Find the city with the highest average salary.
- Return city and average salary.
- Don't manually assume the city.
'''

from file import Data 
import pandas as pd

emp = Data.employees
department = Data.departments

average_salaries_by_city = (emp.groupby("city")["salary"]
                            .mean()
)

result = average_salaries_by_city[
    average_salaries_by_city == average_salaries_by_city.max() ]

print(result)