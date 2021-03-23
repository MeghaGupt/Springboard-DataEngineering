#Write a SQL query to find referees and the number of matches they worked in each venue.

SELECT referee_name, venue_name, count(*) AS matches_ct
FROM match_mast m
	INNER JOIN referee_mast r
		ON m.referee_id = r.referee_id
	INNER JOIN soccer_venue s
		on m.venue_id = s.venue_id
GROUP BY referee_name, venue_name