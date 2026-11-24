/*Q1. Get all employees
   Task: Aisa procedure banao jo employees table ke saare records return kare.
*/

CREATE PROCEDURE GetAllEmployees
AS
BEGIN
    SELECT *
    FROM employees;
END;
GO

EXEC GetAllEmployees;

