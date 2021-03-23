#Write a SQL query to find all the venues where matches with penalty shootouts were
#played.

SELECT DISTINCT venue_name
FROM match_mast m
	INNER JOIN soccer_venue s
			ON m.venue_id = s.venue_id
WHERE decided_by = 'P'