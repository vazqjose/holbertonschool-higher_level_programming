-- Lists all shows, and all genres linked to that show:
-- 		If a show doesn’t have a genre, display NULL in the genre column
-- 		Each record should display: tv_shows.title - tv_genres.name
-- 		Results must be sorted in ascending order by the show title and genre name

SELECT
	tv_shows.title, tv_genres.name
FROM
	tv_shows, tv_show_genres, tv_genres
WHERE
	tv_shows.id = tv_show_genres.show_id
AND
	tv_genres.id = tv_show_genres.genre_id
ORDER BY
	tv_shows.title ASC, tv_genres.name ASC;

