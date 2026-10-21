/*
Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.

Input Format

The STATION table is described as follows:
*/

SELECT distinct city 
from station 
where city not in(
    select distinct city from station where city regexp '^[AEIOUaeiou]'
);

-- or there is multiple approaches 

SELECT distinct city 
from station 
where city not like '[AEIOU]%';

-- with regex 
SELECT distinct city 
from station 
where city not regex '^[AEIOUaeiou]';

-- with left function 
select distinct city 
from STATION 
where left(city,1) NOT IN('a','e','i','o','u','A','E','I','O','U');

