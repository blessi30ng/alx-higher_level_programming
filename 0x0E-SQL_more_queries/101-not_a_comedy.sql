SELECT DISTINCT s.title
FROM tv_shows s
LEFT JOIN tv_shows_genres t ON s.id = t.show_id
LEFT JOIN tv_genres g ON  g.id = t.genre_id
WHERE s.title NOT IN (
	SELECT s.title
	FROM tv_shows s
        JOIN tv_shows_genres t ON s.id = t.show_id
	JOIN tv_genres g ON g.id = t.genre_id
	WHERE g.name = COMEDY
)
ORDER BY  s.title
