-- CREATE TABLE employees (
--     emp_id INT PRIMARY KEY,
--     emp_name VARCHAR(50),
--     dept_id INT,
--     salary DECIMAL(10, 2),
--     manager_id INT,
--     FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
-- );
-- CREATE TABLE departments (
--     dept_id INT PRIMARY KEY,
--     dept_name VARCHAR(50),
--     location VARCHAR(50)
-- );
-- show tables;

 INSERT INTO employees VALUES (101, 'Alice Smith', 1, 95000, NULL);
 INSERT INTO employees VALUES (102, 'Bob Jones', 1, 75000, 101);
 INSERT INTO employees VALUES (103, 'Charlie Brown', 2, 60000, 101);
 INSERT INTO employees VALUES (104, 'Diana Prince', 3, 110000, NULL);
 INSERT INTO employees VALUES (105, 'Evan Wright', 3, 80000, 104);
 INSERT INTO employees VALUES (106, 'Fiona Gallagher', 4, 70000, NULL);
 INSERT INTO employees VALUES (107, 'George Clark', 4, 65000, 106);
 INSERT INTO employees VALUES (108, 'Hannah Abbott', 1, 72000, 102);

-- INSERT INTO departments VALUES (1, 'IT', 'New York');
-- INSERT INTO departments VALUES (2, 'HR', 'Chicago');
-- INSERT INTO departments VALUES (3, 'Finance', 'New York');
-- INSERT INTO departments VALUES (4, 'Sales', 'San Francisco');

-- select * from departments;

select * from employees;

-- Practice ques 1 
-- Practice Ques 1 Solution:
WITH avg_salary AS (
    SELECT AVG(salary) AS company_avg FROM employees
)
SELECT emp_name, salary 
FROM employees, avg_salary
WHERE employees.salary > avg_salary.company_avg;

select * from departments;

-- Total Salary for each department 
WITH total_salary_cte AS (
	SELECT e.dept_id, d.dept_name as department_name, sum(e.salary) as total_salary
    from employees as e
    left join departments as d 
    on e.dept_id = d.dept_id
    group by dept_id
),
-- Department whose salary is greater then 150000
filtered_department as (
	SELECT total_salary_cte.department_name, total_salary_cte.total_salary
    from total_salary_cte
    where total_salary_cte.total_salary > 150000
)
-- Department ka naam aur uska total salary expense display karein.
select * from filtered_department;