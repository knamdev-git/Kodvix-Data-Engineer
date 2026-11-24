CREATE TABLE customers (
    customer_id INT IDENTITY(1,1) PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    city VARCHAR(50) NOT NULL,
    total_spent DECIMAL(10, 2) DEFAULT 0.00,
    joined_date DATE
);


INSERT INTO customers (full_name, email, city, total_spent, joined_date) VALUES
('Aarav Sharma', 'aarav.sharma@example.com', 'Indore', 12500.50, '2025-01-15'),
('Priya Verma', 'priya.v@example.com', 'Mumbai', 34200.00, '2024-11-20'),
('Rohan Joshi', 'rohan.j@example.com', 'Indore', 8400.00, '2025-03-10'),
('Ananya Singh', 'ananya.s@example.com', 'Bengaluru', 45000.75, '2024-08-05'),
('Vikram Patel', 'vikram.p@example.com', 'Delhi', 19800.00, '2025-02-18'),
('Sneha Nair', 'sneha.n@example.com', 'Mumbai', 27500.25, '2025-04-02');



-- store procedure 
create procedure customers_city_data
    @city_name VARCHAR(50)
as
begin
    select * 
    from customers
    where city = @city_name
end;



exec customers_city_data @city_name = 'Indore';
