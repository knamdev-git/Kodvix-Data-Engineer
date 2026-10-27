'''
'''

import numpy as np 

salary = np.array([
    25000, 32000, 45000, 28000,
    60000, 52000, 30000
])

'''
1. Average salary
2. Highest salary
3. Lowest salary
4. Salaries above 40000
5. Number of employees earning above 40000
6. Give everyone a 10% increment
7. Find the employee salary index with the highest salary
'''

print("Number of employees earning above 40k ")
print(len(salary[salary>40000]))


# Give everyone a 10% increment
ten_percent_increment = salary * 1.10
print("Give everyone a 10% increment")
print(ten_percent_increment)


# 1. Find the employee salary index with the highest salary
highest_paid_employee = np.argmax(salary)
print(highest_paid_employee)