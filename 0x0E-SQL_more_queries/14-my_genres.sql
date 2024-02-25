-- Script that uses the hbtn_0d_tvshow database to lists all genres of the show Dexter
SELECT tv_genres.name FROM tv_shows, tv_genres, tv_show_genres WHERE tv_show_genres.genre_id = tv_genres.id AND tv_show_genres.show_id = tv_shows.id AND tv_shows.title = "Dexter" ORDER BY tv_genres.name;
