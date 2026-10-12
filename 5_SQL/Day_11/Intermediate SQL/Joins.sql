select * from department;
select * from employees;

-- Part 4 — INNER JOIN and LEFT JOIN
-- Display each employee's name and their department's manager.

select emp.name, emp.department, dep.manager
from employees as emp
left join department as dep 
on emp.department = dep.department;

-- Display employee names, salaries, and department managers.
select emp.name, emp.salary, dep.manager 
from employees as emp 
left join department as dep 
on emp.department = dep.department;

-- Display all employees along with their department information.
select emp.*, dep.manager 
from employees as emp 
left join department as dep 
on emp.department = dep.department; 

-- Find employees who belong to departments managed by Vikram.
select emp.*, dep.manager 
from employees as emp 
left join department 
on emp.department = dep.department 
where dep.manager = 'Vikram';

-- Display all departments and their employees, including departments with no employees.
select dep.* , emp.name 
from department as dep 
left join employees as emp
on dep.department = emp.department;

-- Find departments that have no employees using a LEFT JOIN.
select dep.department, emp.name 
from department as dep 
left join employees as emp 
on emp.department = dep.department
where emp.name IS NULL;

-- Count the employees in each department using a LEFT JOIN, including empty departments.
select d.department, count(e.emp_id) as 'Employee Count'
from department as d 
left join employees as e
on d.department = e.department
group by d.department; 


-- Find employees whose department has no matching record in the departments table.


