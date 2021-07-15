-- Write a script that lists all cities contained in the database
-- 		Each record should display: cities.id - cities.name - states.name
-- 		Results must be sorted in ascending order by cities.id
-- 		You can use only one SELECT statement

SELECT cities.id, cities.name, states.name 
FROM states
JOIN cities
ON cities.state_id = states.id
ORDER BY cities.id ASC;
