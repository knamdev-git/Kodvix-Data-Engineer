-- Part 5 — Mixed Interview Practice

-- Find the city with the largest number of employees.
select city, max(emp_id)
from employees
group by city order by max(emp_id) desc limit 1; 

-- Find departments where the total salary is greater than the overall average employee 
-- salary multiplied by the number of employees in that department.

select department, sum(salary) as "Total Salary",avg(salary) as "Average Salary", count(emp_id) as "No of Employees"
from employees
group by department
having sum(salary) > (select avg(salary) from employees) * count(emp_id);

-- Display each department's name, manager, employee count, and average salary.
select d.department, d.manager, count(e.emp_id) as "Count" , avg(e.salary) as "Average Salary" 
from department as d
left join employees as e 
on e.department = d.department
group by d.department, d.manager;

