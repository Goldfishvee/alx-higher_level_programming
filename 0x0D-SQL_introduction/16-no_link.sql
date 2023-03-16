-- This script will list all records of `second_table`

-- Don't list rows without a `name` value

-- Records should be listed by descending score

-- db name will be passed as an arg of the mysql command

SELECT `score`, `name` FROM `second_table` 

WHERE `name` is NOT NULL

ORDER BY `score` DESC;
