-- Part 2 — GROUP BY
-- Count the employees in each department.
use python_practice;

select * from department;
select * from employees;

select department, count(*) as 'Employee Count' 
from employees group by department;

-- Calculate the average salary for each department
select department, avg(salary) as 'Average Salary'
from employees 
group by department;

-- Find the total salary expense for each city.
select city, sum(salary) as 'Salary Expense'
from employees 
group by city;

-- Find the maximum salary in each department.
select department, max(salary)
from employees 
group by department;

-- Count employees in each city.
select city, count(emp_id) as 'No. of Employee'
from employees
group by city;

-- Calculate the average salary for each city and department combination.
select department, city, avg(salary) as 'Average Salary' 
from employees 
group by city, department;


-- Find the minimum salary for each department.
select department, min(salary) as "Minimum Salary"
from employees 
group by department;

-- Count how many employees earn each distinct salary.

select salary , count(emp_id)
from employees 
group by salary;