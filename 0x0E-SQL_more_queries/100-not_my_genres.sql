-- This script will list all shows in `hbtn_0d_tvshows` not linked to 'Dexter'

-- Each record should display 'tv_genres.name'

-- Results must be sorted in ASC order by genre name

-- Maximum of two SELECT statements can be used

-- The db name will passed as an arg of the mysql command

SELECT tv_genres.`name`

FROM `tv_genres`

WHERE tv_genres.`id` NOT IN

	(SELECT tv_show_genres.`genre_id`		FROM `tv_show_genres`

		INNER JOIN `tv_shows` 

		ON tv_show_genres.`show_id` = tv_shows.`id`

		WHERE tv_shows.`title` = "Dexter"

	)

ORDER BY tv_genres.`name` ASC;
