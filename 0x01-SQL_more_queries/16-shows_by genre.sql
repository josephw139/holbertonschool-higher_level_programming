-- Task 16:Lists all shows and their genres
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tc_genres ON tv_shows.id=tv_show_genres.id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;