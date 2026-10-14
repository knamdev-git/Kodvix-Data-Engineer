CREATE DATABASE IF NOT EXISTS sql_practice;
USE sql_practice;

-- Remove existing versions of these tables.
-- WARNING: This deletes their existing data.
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Products;

-- 1. Products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,
    Product VARCHAR(100) NOT NULL,
    Category VARCHAR(50),
    Price DECIMAL(10, 2) NOT NULL
);

-- 2. Customers
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Country VARCHAR(50),
    Score INT
);

-- 3. Employees
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Department VARCHAR(50),
    BirthDate DATE,
    Gender VARCHAR(20),
    Salary DECIMAL(12, 2),
    ManagerID INT,
    CONSTRAINT fk_employee_manager
        FOREIGN KEY (ManagerID)
        REFERENCES Employees(EmployeeID)
);

-- 4. Orders
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    ProductID INT NOT NULL,
    CustomerID INT NOT NULL,
    SalesPersonID INT NOT NULL,
    OrderDate DATE,
    ShipDate DATE,
    OrderStatus VARCHAR(30),
    ShipAddress VARCHAR(255),
    BillAddress VARCHAR(255),
    Quantity INT NOT NULL,
    Sales DECIMAL(12, 2),
    CreationTime DATETIME DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_order_product
        FOREIGN KEY (ProductID)
        REFERENCES Products(ProductID),

    CONSTRAINT fk_order_customer
        FOREIGN KEY (CustomerID)
        REFERENCES Customers(CustomerID),

    CONSTRAINT fk_order_employee
        FOREIGN KEY (SalesPersonID)
        REFERENCES Employees(EmployeeID)
);


INSERT INTO Products (Product, Category, Price)
VALUES
('Laptop', 'Electronics', 65000.00),
('Smartphone', 'Electronics', 25000.00),
('Office Chair', 'Furniture', 8500.00),
('Desk', 'Furniture', 12000.00),
('Headphones', 'Accessories', 2500.00),
('Keyboard', 'Accessories', 1500.00),
('Monitor', 'Electronics', 18000.00),
('Mouse', 'Accessories', 800.00),
('Printer', 'Electronics', 14000.00),
('Bookshelf', 'Furniture', 6500.00);



INSERT INTO Customers
    (FirstName, LastName, Country, Score)
VALUES
('Aarav', 'Sharma', 'India', 85),
('Priya', 'Verma', 'India', 92),
('Rahul', 'Patel', 'India', 70),
('Emma', 'Wilson', 'USA', 88),
('Oliver', 'Brown', 'UK', 65),
('Sophia', 'Miller', 'USA', 95),
('Rohan', 'Gupta', 'India', 78),
('Olivia', 'Davis', 'Canada', 82),
('Liam', 'Taylor', 'UK', 55),
('Ananya', 'Joshi', 'India', 90);


INSERT INTO Employees
    (FirstName, LastName, Department, BirthDate,
     Gender, Salary, ManagerID)
VALUES
('Vikram', 'Mehta', 'Management', '1980-04-12',
 'Male', 120000.00, NULL),

('Neha', 'Kapoor', 'Sales', '1990-08-22',
 'Female', 75000.00, 1),

('Arjun', 'Singh', 'Sales', '1992-02-15',
 'Male', 68000.00, 1),

('Isha', 'Malhotra', 'IT', '1995-11-05',
 'Female', 82000.00, 1),

('Karan', 'Desai', 'Sales', '1988-06-18',
 'Male', 72000.00, 2),

('Meera', 'Reddy', 'IT', '1993-09-27',
 'Female', 78000.00, 4);


INSERT INTO Orders
    (ProductID, CustomerID, SalesPersonID,
     OrderDate, ShipDate, OrderStatus,
     ShipAddress, BillAddress, Quantity, Sales)
VALUES
(1, 1, 2, '2026-01-05', '2026-01-08', 'Delivered',
 'Indore, India', 'Indore, India', 1, 65000.00),

(2, 2, 3, '2026-01-10', '2026-01-13', 'Delivered',
 'Bhopal, India', 'Bhopal, India', 2, 50000.00),

(3, 3, 5, '2026-01-15', '2026-01-18', 'Delivered',
 'Ahmedabad, India', 'Ahmedabad, India', 2, 17000.00),

(4, 4, 2, '2026-02-01', '2026-02-04', 'Delivered',
 'New York, USA', 'New York, USA', 1, 12000.00),

(5, 5, 3, '2026-02-06', '2026-02-09', 'Delivered',
 'London, UK', 'London, UK', 3, 7500.00),

(6, 6, 5, '2026-02-12', NULL, 'Processing',
 'Chicago, USA', 'Chicago, USA', 2, 3000.00),

(7, 7, 2, '2026-03-01', '2026-03-05', 'Delivered',
 'Pune, India', 'Pune, India', 2, 36000.00),

(8, 8, 3, '2026-03-07', NULL, 'Shipped',
 'Toronto, Canada', 'Toronto, Canada', 5, 4000.00),

(9, 9, 5, '2026-03-15', '2026-03-20', 'Delivered',
 'Manchester, UK', 'Manchester, UK', 1, 14000.00),

(10, 10, 2, '2026-04-02', NULL, 'Processing',
 'Jaipur, India', 'Jaipur, India', 2, 13000.00),

(1, 2, 3, '2026-04-10', '2026-04-14', 'Delivered',
 'Bhopal, India', 'Bhopal, India', 1, 65000.00),

(5, 1, 5, '2026-04-15', NULL, 'Pending',
 'Indore, India', 'Indore, India', 4, 10000.00),

(7, 4, 2, '2026-05-03', '2026-05-07', 'Delivered',
 'New York, USA', 'New York, USA', 3, 54000.00),

(2, 7, 3, '2026-05-10', NULL, 'Processing',
 'Pune, India', 'Pune, India', 1, 25000.00),

(3, 10, 5, '2026-05-20', '2026-05-24', 'Delivered',
 'Jaipur, India', 'Jaipur, India', 1, 8500.00);



-- Check the number of records
SELECT 'Products' AS TableName, COUNT(*) AS TotalRows
FROM Products
UNION ALL
SELECT 'Customers', COUNT(*) FROM Customers
UNION ALL
SELECT 'Employees', COUNT(*) FROM Employees
UNION ALL
SELECT 'Orders', COUNT(*) FROM Orders;

-- View all orders
SELECT * FROM Orders;


/*============================================================================== 
   MULTIPLE TABLE JOINS (4 Tables)
=============================================================================== */
   SHOW TABLES;
   select * from Customers;
   select * from Employees;
   select * from Orders;
   select * from Products;

/* Task: Using SalesDB, Retrieve a list of all orders, along with the related customer, product, 
   and employee details. For each order, display:
   - Order ID
   - Customer's name
   - Product name
   - Sales amount
   - Product price
   - Salesperson's name */
describe Orders;

select o.OrderID, 
	   c.FirstName,
       c.LastName,
	   p.Product as Product_Name,
       o.Sales as Sales_Amount,
       p.Price as Product_Price,
       CONCAT(s.FirstName, " ", s.LastName) as SalesPerson_Name
FROM Orders as o 
LEFT JOIN Customers as c
ON c.CustomerID = o.CustomerID
LEFT JOIN Products as p 
ON o.ProductID = p.ProductID
LEFT JOIN Employees as s 
ON s.EmployeeID = o.SalesPersonID;