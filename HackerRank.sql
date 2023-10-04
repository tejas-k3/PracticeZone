/*
THIS WHOLE FILE IS BUNCH OF SQL QUERIES WRITTEN WITH MYSQL DB SYNTAX FOR RANDOM QUESTIONS & LEARNINGS!
*/
-- https://www.hackerrank.com/challenges/weather-observation-station-8/
SELECT DISTINCT CITY FROM STATION WHERE lower(substr(CITY,1,1)) in ('a','e','i','o','u') AND lower(substr(CITY,-1,1)) in ('a','e','i','o','u') ;
-- https://www.hackerrank.com/challenges/more-than-75-marks/
SELECT NAME FROM STUDENTS WHERE MARKS > 75 ORDER BY SUBSTR(NAME, -3, 3), ID ASC;