#  Write a SQL query to find the number of captains who were also goalkeepers.

SELECT count( distinct mc.player_captain)
FROM match_captain mc
	INNER JOIN match_details md
		ON mc.match_no =md.match_no and mc.player_captain = md.player_gk 