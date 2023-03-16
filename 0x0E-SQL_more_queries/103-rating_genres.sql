-- This script will list all genres in `hbtn_0d_tvshows_rate` by their rating 

-- Each record should display 'tv_genres.name' - 'rating sum'

-- Results must be sorted in DESC order by the rating

-- Only one SELECT statement can be used

-- The db name will passed as an arg of the mysql command

SELECT tv_genres.`name`, SUM(`rate`) AS `rating`

FROM `tv_genres`

INNER JOIN `tv_show_genres` 

ON tv_show_genres.`genre_id` = tv_genres.`id`

INNER JOIN `tv_show_ratings` 

ON tv_show_ratings.`show_id` = tv_show_genres.`show_id`

GROUP BY tv_genres.`name`

ORDER BY `rating` DESC;
