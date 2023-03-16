-- This script will list all shows in `hbtn_0d_tvshows` w/o the genre Comedy

-- Each record should display 'tv_shows.name'

-- Results must be sorted in ASC order by show_title

-- Maximum of two SELECT statements can be used

-- The db name will passed as an arg of the mysql command

SELECT tv_shows.`title`

FROM `tv_shows`

WHERE tv_shows.`id` NOT IN

	(SELECT tv_show_genres.`show_id`		FROM `tv_show_genres`

		INNER JOIN `tv_genres` 

		ON tv_show_genres.`genre_id` = tv_genres.`id`

		WHERE tv_genres.`name` = "Comedy"

	)

ORDER BY tv_shows.`title` ASC;
