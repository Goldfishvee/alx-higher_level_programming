-- This script will list all records with a score >= 10 in `second_table`

-- Results will be ordered by top score first

-- db name will be supplied as an arg of the mysql command

SELECT `score`, `name` 

FROM `second_table` 

WHERE `score` >= 10

ORDER BY `score` DESC;
