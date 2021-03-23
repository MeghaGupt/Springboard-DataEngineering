#Write a SQL query to find the match number for the game with the highest number of
#penalty shots, and which countries played that match.

WITH pen_shots_ct AS (
	SELECT m.match_no, 
		COUNT(kick_id) AS count
	FROM match_mast  m
		INNER JOIN penalty_shootout p
			ON m.match_no = p.match_no
	GROUP BY m.match_no
)    
SELECT country_name
FROM match_details m
	INNER JOIN soccer_country sc
		ON m.team_id = sc.country_id
WHERE match_no = (
	SELECT match_no 
    FROM pen_shots_ct
    ORDER BY count DESC
	LIMIT 1
)



