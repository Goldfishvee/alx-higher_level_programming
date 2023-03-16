-- This script will list all Comedy shows in `hbtn_0d_tvshows`

-- Each record should display 'tv_shows.title'

-- Results must be sorted in ASC order by show title

-- Only one SELECT statement can be used

-- The db name will passed as an arg of the mysql command

SELECT tv_shows.`title`

FROM `tv_shows` 

INNER JOIN `tv_show_genres` 

ON tv_shows.`id` = tv_show_genres.`show_id`

INNER JOIN `tv_genres` ON

tv_genres.`id` = tv_show_genres.`genre_id`

WHERE tv_genres.`name` = "Comedy"

ORDER BY tv_shows.`title` ASC;
