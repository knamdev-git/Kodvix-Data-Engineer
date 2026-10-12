-- LEVEL 2 
-- Aggregate functions 
use python_practice;
select * from employees;
select * from department;

-- Ques 1 : Count the total number of employees.
select count(emp_id) as 'Total Employees'
from employees;

-- Ques 2 : Calculate the average salary of all employees.

select AVG(salary) as 'Average Salary' 
from employees;

-- Find the highest salary and lowest salary.
select MAX(salary) as 'Highest Salary', MIN(salary) as 'Lowest Salary'
from employees;

-- Calculate the total salary paid to all employees.
select sum(salary) as 'Total Salary' 
from employees ;

-- Count how many employees work in IT. 
select count(emp_id) as 'Employees Count' 
from employees 
where department = 'IT';

-- Find the average salary of employees living in Indore.
select avg(salary) as 'Average Salary'
from employees 
where city = 'Indore';

-- Count the number of distinct cities in the employees table.
select count(distinct city) from employees;
-- or you can verify by writing : 
select distinct city from employees; 

-- Find the difference between the highest and lowest salaries.
select max(salary) - min(salary) as 'Diff Salary' from employees;

