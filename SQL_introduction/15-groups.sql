-- Script that lists the number of records with a score under 10
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;