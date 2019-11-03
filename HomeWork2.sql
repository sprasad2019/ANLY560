use sakila

SELECT f.title, f.description, a.first_name, a.last_name
FROM film as f 
  JOIN film_actor as fa	on f.film_id = fa.film_id
  JOIN actor as a on fa.actor_id = a.actor_id
WHERE f.title LIKE 'zo%'
GROUP BY f.title
ORDER BY f.title