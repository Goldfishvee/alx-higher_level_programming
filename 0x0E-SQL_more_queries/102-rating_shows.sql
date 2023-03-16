-- This script will list all shows in `hbtn_0d_tvshows_rate` by their rating 

-- Each record should display 'tv_shows.title' - 'rating sum'

-- Results must be sorted in DESC order by the rating

-- Only one SELECT statement can be used

-- The db name will passed as an arg of the mysql command

SELECT tv_shows.`title`, SUM(`rate`) AS `rating`

FROM `tv_shows`

INNER JOIN `tv_show_ratings` 

ON tv_shows.`id` = tv_show_ratings.`show_id`

GROUP BY tv_shows.`title`

ORDER BY `rating` DESC;
