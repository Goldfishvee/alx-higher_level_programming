-- This script will calculate the average of all scores in `second_table`

-- The results will be stored in a new column `average`

-- db name will be supplied as an arg of the mysql command

SELECT AVG(`score`) AS `average` FROM `second_table`;
