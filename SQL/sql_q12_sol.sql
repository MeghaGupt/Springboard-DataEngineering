#Write a SQL query that returns the total number of goals scored by each position on
#each country’s team. Do not include positions which scored no goals.

SELECT pm.team_id, position_desc, count(DISTINCT goal_id) AS goals_scored
FROM player_mast pm
	INNER JOIN playing_position pp
		ON pm.posi_to_play = pp.position_id
	INNER JOIN goal_details g
		ON g.player_id = pm.player_id
GROUP BY pm.team_id, position_desc
ORDER BY team_id