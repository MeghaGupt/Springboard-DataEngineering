# Write a SQL query to find the substitute players who came into the field in the first
# half of play, within a normal play schedule.

SELECT player_name
FROM player_in_out po
	INNER JOIN player_mast pm
		ON po.player_id  = pm.player_id
WHERE in_out = 'I' and play_schedule = 'NT' and play_half  = 1