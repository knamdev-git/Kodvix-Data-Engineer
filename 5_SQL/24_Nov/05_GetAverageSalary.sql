/*  Q5. Average salary by department
*/

CREATE PROCEDURE GetAverageSalary
    @dept_id INT,
    @avg_salary DECIMAL(10,2) OUTPUT
AS
BEGIN
    SELECT @avg_salary = AVG(salary)
    FROM employees
    WHERE dept_id = @dept_id;
END;
GO

DECLARE @avg DECIMAL(10,2);

EXEC GetAverageSalary
    @dept_id = 10,
    @avg_salary = @avg OUTPUT;

SELECT @avg AS AverageSalary;

