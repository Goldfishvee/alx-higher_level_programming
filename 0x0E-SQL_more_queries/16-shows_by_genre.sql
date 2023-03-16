-- This script will list all shows in `hbtn_0d_tvshows` and all genres linked to that show

-- If show doesn't have genre, display NULL in genre coln

-- Each record should display 'tv_shows.title' - 'tv_genres.name'

-- Results must be sorted in ASC order by show title and genre name

-- Only one SELECT statement can be used

-- The db name will passed as an arg of the mysql command

SELECT tv_shows.`title`, tv_genres.`name`

FROM `tv_shows` 

LEFT JOIN `tv_show_genres` 

ON tv_shows.`id` = tv_show_genres.`show_id`

LEFT JOIN `tv_genres` 

ON tv_show_genres.`genre_id` = tv_genres.`id`

ORDER BY tv_shows.`title` ASC, tv_genres.`name` ASC;
