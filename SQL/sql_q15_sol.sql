#Write a SQL query to find the referees who booked the most number of players.

WITH referee_booking AS (
SELECT referee_name,  count(*) AS booking_ct
FROM match_mast m
	INNER JOIN referee_mast r
		ON m.referee_id = r.referee_id
	INNER  JOIN player_booked p
		ON p.match_no = p.match_no
GROUP BY referee_name
),
referee_max AS (
	SELECT *,
		RANK() OVER (ORDER by booking_ct DESC) AS rank_
	FROM referee_booking
 )
 SELECT * FROM referee_max
 WHERE rank_ = 1
