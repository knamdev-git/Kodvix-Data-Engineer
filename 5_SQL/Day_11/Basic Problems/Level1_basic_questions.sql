show databases;
use python_practice;

 
show tables;

select name, salary from employees;



select * from employees;

select * from department;


-- employees with higher salary 

select * from employees
where salary > 50000;


-- Find employees who live in Indore

select * from employees where city ='Indore';

-- Display employees in descending order of salary.

select * from employees order by salary desc;


-- Find employees whose salary is between ₹40,000 and ₹60,000, inclusive.
select * from employees 
where salary between 40000 and 60000;


-- Find employees whose names start with 'A'.
select * from employees where name like 'A%';

-- display unique cities 

select distinct city from employees; 

-- Find the top 3 highest-paid employees
select * from employees 
order by salary desc limit 3;

-- Find employees who work in IT and earn at least ₹50,000.
select * from employees 
where department = 'IT' and salary >= 50000;


-- Count the total number of employees 
select * from employees group by department;

canva