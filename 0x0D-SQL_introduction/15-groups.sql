-- This script will list the number of records with the same score

-- The table is `second_table`

-- Result will be displayed as:

-- `score` and stored in `number`

-- Grouped by descending order

SELECT `score`, COUNT(*) AS `number` FROM `second_table`

GROUP BY `score` ORDER BY `number` DESC;
