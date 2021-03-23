#Write a SQL query to find the highest number of foul cards given in one match

WITH foul_card_ct AS (
	SELECT match_no, count(*) AS ct
	FROM player_booked
	GROUP BY match_no
)
SELECT *
FROM foul_card_ct
ORDER BY ct DESC
LIMIT 1