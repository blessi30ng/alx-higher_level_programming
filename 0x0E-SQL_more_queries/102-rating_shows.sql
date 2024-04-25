SELECT s.title, COUNT(*) r.rate AS rating
FROM tv_shows s
JOIN tv_shows_ratings r ON s.id = r.show_id
GROUP BY title
ORDER BY rating DESC;
