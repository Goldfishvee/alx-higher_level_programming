-- This script will delete specific rows ffrom `second_table`

-- db name will be supplied as an arg of the mysql command

DELETE FROM `second_table` WHERE `score` <= 5;
