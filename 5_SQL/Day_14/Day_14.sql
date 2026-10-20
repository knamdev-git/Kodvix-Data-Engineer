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
DATE_FORMAT(order_datetime, '%Y %h:%i:%s %p')) ans
from sample_orders; 

-- Convert the data type format into another by using some inbuild functions in sql 
show tables ;

select * from person;

select 
cast('121' as SIGNED) as ans,
cast('20-02-22' as DATE) as Date,
cast('20-02-22' as DATETIME) as DateTime,
format(12.33333, 0) as format_numeric_float,
format(12, 2) as format_numeric_Integers;	


