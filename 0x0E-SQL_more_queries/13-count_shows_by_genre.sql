-- This script will list all genres in `hbtn_0d_tvshows` and number of shows linked to each

-- Each record should display <TV Show genre> - <Number of shows linked to this genre>

-- First column must be called 'genre'

-- Second column must be called 'number_of_shows'

-- No genre should be displayed if there are no shows linked to it

-- Results must be sorted in DESC order by number of shows linked

-- Only one SELECT statement can be used

-- The db name will passed as an arg of the mysql command

SELECT tv_genres.`name` AS `genre`, COUNT(*) AS `number_of_shows`

FROM `tv_genres` 

INNER JOIN `tv_show_genres` 

ON tv_genres.`id` = tv_show_genres.`genre_id`

GROUP BY tv_genres.`name`

ORDER BY `number_of_shows` DESC;
