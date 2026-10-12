-- Part 3 — HAVING
-- Find departments with more than 2 employees.

select department, count(emp_id) as 'No. of Employees'
from employees
group by department 
having count(emp_id) > 2;

-- 18. Find departments whose average salary is greater than ₹50,000.
select department, avg(salary) as 'Salary'
from employees
group by department
having avg(salary) > 50000;

-- Find cities with at least 2 employees 
select city, count(emp_id) as "Employees Count"
from employees 
group by city 
having count(emp_id) >= 2;

--  Find departments whose total salary expense exceeds ₹100,000.
select department, sum(salary) as 'Expenses'
from employees
group by department
having sum(salary) > 100000;

-- Find departments where the maximum salary exceeds ₹60,000.
select department, max(salary) as 'Maximum Salary' 
from employees 
group by department
having max(salary) > 60000;

-- 22. Find cities whose average salary is below ₹50,000. 
select city, avg(salary) as 'Average Salary' 
from employees
group by city 
having avg(salary) < 50000;


-- 	Find salary values earned by more than one employee.
select salary, count(emp_id) as 'Total Employee' 
from employees 
group by salary 
having count(emp_id) > 1 ; 

-- Find departments with at least 3 employees and an average salary above ₹45,000.
select department, count(emp_id) as 'Employee Count' , avg(salary) as 'Average Salary' 
from employees
group by department
having avg(salary) > 45000;