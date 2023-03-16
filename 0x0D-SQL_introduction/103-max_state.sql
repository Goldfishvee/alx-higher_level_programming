-- This script will display max temps of each state in db

-- Results will be ordered by state name

SELECT `state`, MAX(`value`) AS `max_temp` FROM `temperatures`

GROUP BY `state` ORDER BY `state` ASC;
