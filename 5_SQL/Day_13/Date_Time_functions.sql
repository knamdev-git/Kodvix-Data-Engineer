-- Practicing the Order Date and Time fuctions  
use python_practice;

select
CONCAT(FirstName, " ", LastName) as FullName,
RIGHT(FirstName, 2) as last_2_words,
LEFT(FirstName, 2) as First_2_words
from Demo;



CREATE TABLE sample_orders (
    order_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    order_date DATE,
    order_datetime DATETIME
);

INSERT INTO sample_orders (order_id, customer_name, order_date, order_datetime) VALUES
(1, 'Alice Smith', '2026-01-15', '2026-01-15 08:30:00'),
(2, 'Bob Jones', '2026-03-22', '2026-03-22 14:15:00'),
(3, 'Charlie Brown', '2026-06-10', '2026-06-10 19:45:00'),
(4, 'Diana Prince', '2026-10-05', '2026-10-05 11:20:00');

select 
order_date, 
order_datetime,
YEAR(order_datetime) as YEAR,
TIME(order_datetime) as TIME ,
DAY(order_date) as Day,
MONTH(order_date) as OrderMonth,
-- DATEPART(year, order_date) Not available in mysql Instead we can use extract()
EXTRACT(month from order_date) as Extract_months,
EXTRACT(year from order_date) as Extract_years,
EXTRACT(week from order_datetime) as Extract_Week,

EXTRACT(hour from order_datetime) as Extract_HR,
EXTRACT(minute from order_datetime) as Extract_Min,
EXTRACT(second from order_datetime) as Extract_Sec

from sample_orders;


-- Can also Extract the particular part of orderDate 

-- In SQL Server, you would write DATENAME(month, date)
-- In MySQL, use MONTHNAME() or DATE_FORMAT()

select 
order_date,
DAYNAME(order_date) as Day,
MONTHNAME(order_date) as Month
from sample_orders;


-- DateTrunc function : Heirarchy is really Important in sql 

-- reset the hours from date 
select 
order_date
from sample_orders;

select 
order_datetime,
DATE_FORMAT(order_date, '%Y-%M-01') as Date_trunc_sql,
DATE_FORMAT(order_datetime, '%Y-%M-01 %H:%I:%00') as day_min
-- DATE_FORMAT(order_date, '%Y-%M-01') as ,
-- DATE_FORMAT(order_date, '%Y-%M-01') as Date_trunc_sql
from sample_orders;

-- Exercise : How many orders place each year / month
SELECT 
    MONTHNAME(order_date) AS Month,
    COUNT(	*) AS Order_placed
FROM sample_orders
GROUP BY MONTH(order_date), MONTHNAME(order_date)
ORDER BY MONTH(order_date) ASC;

select * from sample_orders;

INSERT INTO sample_orders(order_id, customer_name, order_date, order_datetime) values(10, "Michael", '2026-01-15', '2026-01-15 08:30:00');

-- Have to place the orders which is placed in Feb month 
select 
Month(order_date) as NumMonth, 
MONTHNAME(order_date) as Month,
COUNT(order_id) as OrderPlaced
from sample_orders
WHERE month(order_date) = 1 
GROUP BY MONTH(order_date), MonthName(order_date);


select count(*) from sample_orders
where month(order_date) = 1;

-- EOMONTH() : End of the month in MYSQL Server 
-- LAST_DAY() : Last Day of month in SQL Workbench