show databases;


use python_practice;
show tables;

select * from sample_orders;

select 
order_date,
DATE_FORMAT(order_date, '%W-%d-%M-%Y') dd,
DATE_FORMAT(order_date, '%a-%d-%b-%y') Abbreviated_Names
from sample_orders;


-- We use format for numeric values 
-- Day wed Jan Q1 2025 12:34:56 PM 
select 
CONCAT('Day ',
DATE_FORMAT(order_date, '%a %b'),
' Q1 ',
Year(order_date),
' ',
TIME(order_datetime)
,' PM') ans
from sample_orders; 

