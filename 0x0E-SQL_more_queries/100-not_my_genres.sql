SELECT g.name
FROM tv_genres g
JOIN tv_shows_genres t ON g.id = t.genre_id
JOIN tv_genres g ON s.id = t.show_id
WHERE g.id NOT IN (
	SELECT genre_id
	FROM t_ shows_genres t
	JOIN tv_shows s ON s.id = t.show_id
	WHERE t.title = "DEXTER"
)
ORDER BY g.name
