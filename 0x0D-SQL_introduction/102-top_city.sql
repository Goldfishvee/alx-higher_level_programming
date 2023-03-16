-- This script willdisplay top 3 cities avg_temp during Jul and Aug

-- Results will be ordered by temp in descending order

SELECT `city`, AVG(`value`) AS `avg_temp` FROM `temperatures`

WHERE `month` IN (7, 8) GROUP BY `city` ORDER BY `avg_temp`

DESC LIMIT 3;
