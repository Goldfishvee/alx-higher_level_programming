-- This script will list all cities in `hbtn_0d_usa`

-- Each record should display: `cities.id`-`cities.name`-`states.name`

-- Results should be ordered in ascending order by `cities.id`

-- You can only use one `SELECT` STATEMENT

SELECT cities.`id`, cities.`name`, states.`name`

FROM `cities` INNER JOIN `states` ON cities.`state_id` = states.`id`

ORDER BY cities.`id` ASC;
