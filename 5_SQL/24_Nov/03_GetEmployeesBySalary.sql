/*  Q3. Get employees by salary
   Task: Input salary se greater salary wale employees return karo.
 */

CREATE PROCEDURE GetEmployeesBySalary
    @salary DECIMAL(10,2)
AS
BEGIN
    SELECT *
    FROM employees
    WHERE salary > @salary;
END;
GO

EXEC GetEmployeesBySalary @salary = 30000;


