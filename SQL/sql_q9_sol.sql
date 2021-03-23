#Write a SQL query to find the goalkeeper’s name and jersey number, playing for
#Germany, who played in Germany’s group stage matches.

SELECT DISTINCT
       player_name AS goal_keeper_name,
       jersey_no
FROM match_details m
	INNER JOIN player_mast p
		ON p.player_id = m.player_gk
	INNER JOIN soccer_country sc
		ON p.team_id = sc.country_id
WHERE play_stage = 'G' and country_name = 'Germany'