-- Script that lists all cities of California found in database
SELECT id, name
FROM cities
WHERE state_id = 1
ORDER BY cities.id ASC;