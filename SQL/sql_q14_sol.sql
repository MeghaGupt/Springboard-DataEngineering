#Write a SQL query to find referees and the number of bookings they made for the
#entire tournament. Sort your answer by the number of bookings in descending order

SELECT referee_name,  count(*) AS booking_ct
FROM match_mast m
	INNER JOIN referee_mast r
		ON m.referee_id = r.referee_id
	INNER  JOIN player_booked p
		ON p.match_no = p.match_no
GROUP BY referee_name
ORDER BY booking_ct DESC

