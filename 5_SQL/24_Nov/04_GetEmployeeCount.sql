/* Q4. Get employee count using OUTPUT
   Task: Procedure se total employee count return karo.
 */ 
CREATE PROCEDURE GetEmployeeCount
    @total INT OUTPUT
AS
BEGIN
    SELECT @total = COUNT(*)
    FROM employees;
END;
GO

DECLARE @result INT;

EXEC GetEmployeeCount
    @total = @result OUTPUT;

SELECT @result AS TotalEmployees;

