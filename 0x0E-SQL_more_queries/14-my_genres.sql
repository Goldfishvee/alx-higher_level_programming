-- This script will list all genres in `hbtn_0d_tvshows` of the show 'Dexter'

-- Each record should display 'tv_genres.name'

-- Results must be sorted in ASC order by the genre name

-- Only one SELECT statement can be used

-- The db name will passed as an arg of the mysql command

SELECT tv_genres.`name`

FROM `tv_genres` 

INNER JOIN `tv_show_genres` 

ON tv_genres.`id` = tv_show_genres.`genre_id`

INNER JOIN `tv_shows` ON

tv_shows.`id` = tv_show_genres.`show_id`

WHERE tv_shows.`title` = "Dexter"

ORDER BY tv_genres.`name` ASC;
