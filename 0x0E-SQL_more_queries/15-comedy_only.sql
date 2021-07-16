-- Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.
-- 		The tv_genres table contains only one record where name = Comedy
-- 			(but the id can be different)
-- 		Each record should display: tv_shows.title
-- 		Results must be sorted in ascending order by the show title

SELECT
	tv_shows.title
FROM
	tv_shows, tv_show_genres, tv_genres
WHERE
	tv_genres.name = 'Comedy'
AND
	tv_shows.id = tv_show_genres.show_id
AND
	tv_genres.id = tv_show_genres.genre_id
ORDER BY
	tv_shows.title ASC;

