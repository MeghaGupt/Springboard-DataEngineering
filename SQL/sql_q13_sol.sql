#Write a SQL query to find all the defenders who scored a goal for their teams.

SELECT DISTINCT player_name
FROM player_mast pm
	INNER JOIN playing_position pp
		ON pm.posi_to_play = pp.position_id
	INNER JOIN goal_details g
		ON g.player_id = pm.player_id
WHERE position_desc = 'Defenders'