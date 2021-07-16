-- Write a script that lists all genres from hbtn_0d_tvshows and displays the
-- number of shows linked to each.
-- 		Each record should display:
-- 			<TV Show genre> - <Number of shows linked to this genre>
-- 		First column must be called genre
-- 		Second column must be called number_of_shows
-- 		Don’t display a genre that doesn’t have any shows linked
-- 		Results must be sorted in descending order by the number of shows linked

SELECT
	tv_genres.name AS 'genre', count(tv_shows.title) AS 'number_of_shows'
FROM
	tv_genres, tv_shows, tv_show_genres
WHERE
	tv_genres.id = tv_show_genres.genre_id
AND
	tv_shows.id = tv_show_genres.show_id
GROUP BY
	tv_genres.name
ORDER BY
	count(tv_shows.title) DESC;
