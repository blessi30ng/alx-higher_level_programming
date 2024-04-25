SELECT g.name, SUM(*) r.rate AS rating
FROM tv_show_rating r
JOIN tv_show s ON  s.id = r.show_id
JOIN tv_shows_genres t ON s.id = t.show_id
JOIN tv_genres g ON g.id = t.genre_id
GROUP BY g.name
ORDER BY rating DESC;
