-- This script will list all shows in `hbtn_0d_tvshows`

-- Results should be sorted by `tv_shows.title` and `tv_show_genres.genre_id` in ascending order

-- If a show doesn't have a genre, NULL will be displaced

-- Only one SELECT statement can be used

-- The db name will passed as an arg of the mysql command

SELECT tv_shows.`title`, tv_show_genres.`genre_id`

FROM `tv_shows` 

LEFT JOIN `tv_show_genres` 

ON tv_shows.`id` = tv_show_genres.`show_id`

ORDER BY tv_shows.`title` ASC, tv_show_genres.`genre_id` ASC;
