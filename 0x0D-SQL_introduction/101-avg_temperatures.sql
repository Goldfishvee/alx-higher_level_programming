-- This script will find the avg temp (in deg Fahr) from an imported db

-- sort the avg_temp by city and in descending order

SELECT `city`, AVG(`value`) AS `avg_temp` FROM `temperatures`

GROUP BY `city` ORDER BY `avg_temp` DESC;
