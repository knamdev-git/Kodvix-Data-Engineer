/* Q2. Get employees by department
   Task: Department ID input lo aur us department ke employees return karo.
*/

CREATE PROCEDURE GetEmployeesByDept
    @dept_id INT
AS
BEGIN
    SELECT *
    FROM employees
    WHERE dept_id = @dept_id;
END;
GO

EXEC GetEmployeesByDept @dept_id = 10;

EXEC GetEmployeesByDept @dept_id = 99;

EXEC GetEmployeesByDept @dept_id = NULL;
