
/*
Task: Find all customers who have never placed an order.
Requirements:
- Display CustomerID, FirstName, and LastName.
- Use the Customers and Orders tables.
- Use a LEFT JOIN.
- Do not use a subquery.
*/
Select * from Customers;
select * from Orders;

SELECT 
c.CustomerID,
c.FirstName, 
c.LastName
FROM Orders as o  
RIGHT JOIN Customers as c
ON o.CustomerID = c.CustomerID
WHERE o.CustomerID IS NULL;


/*
Find all products that have never been ordered.
Requirements:
- Display ProductID, Product, and Price.
- Use Products and Orders.
- Use an Anti LEFT JOIN.
- Do not use a subquery.
*/
INSERT INTO Products(Product, Category, Price)
VALUES ('Watch','Accessories', 800);

select * from Products ;
select * from Orders;

Select p.ProductID, 
	   p.Product,
	   p.Price
FROM Products as p
LEFT JOIN Orders as o
ON p.ProductID = o.ProductID 
WHERE o.ProductID IS NULL;

/*
Task: Display each employee's full name alongside their manager's full name.
Requirements:
- Use the Employees table.
- Use a SELF JOIN.
- Display Employee_Name and Manager_Name.
- Include employees who don't have a manager.
*/
show tables;
Select CONCAT(e.FirstName," ", e.LastName) as EmployeeName,
CONCAT(e1.FirstName, " ", e1.LastName) as ManagerName
from Employees as e 
LEFT JOIN Employees as e1 
ON e.EmployeeID = e1.ManagerID
WHERE e1.ManagerID IS NULL ;

UPDATE Employees
SET ManagerID = NULL
Where EmployeeID = 4;

select * from person;

select * from Employees;

/*
Question 3 — Set Operations: UNION ALL
Task: Find all customers who belong to India and all customers who belong to the USA. Combine both result sets using UNION ALL.
Requirements:
- Display CustomerID, FirstName, LastName, and Country.
- Use the Customers table twice in separate SELECT statements.
- Combine the results using UNION ALL.
- Do not use OR in the WHERE clause.
*/

CREATE TABLE Demo(
CustomerID INT auto_increment PRIMARY KEY, 
FirstName VARCHAR(50), 
LastName VARCHAR(60),
Country varchar(10),
Score INT
);

INSERT INTO Demo 
select  * 
from Customers
Where Country = 'India'

UNION ALL 

SELECT * 
FROM Customers 
Where Country = "USA";

select * from Demo;

