(Select CITY, LENGTH(CITY) as city_len from STATION
order by city_len, CITY asc limit 1)
UNION
(Select CITY, LENGTH(CITY) as city_len from STATION
order by city_len desc, CITY asc limit 1);