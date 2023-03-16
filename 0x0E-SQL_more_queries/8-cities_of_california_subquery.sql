-- This script will perform a subquery of cities of California

-- From the db `htbn_0d_usa`

-- Results must be sorted in ascending order by cities.id

-- db name will be provided as an arg of the mysql command

-- You are not allowed to use JOIN

SELECT `id`, `name` FROM `cities` 

WHERE `state_id` IN (SELECT `id` FROM `states` WHERE `name` = "California")

ORDER BY `id` ASC; 
