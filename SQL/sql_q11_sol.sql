#Write a SQL query to find the players, their jersey number, and playing club who
#were the goalkeepers for England in EURO Cup 2016.


SELECT DISTINCT
       player_name,
       jersey_no,
       playing_club
FROM match_details m
	INNER JOIN player_mast p
		ON p.player_id = m.player_gk
	INNER JOIN soccer_country sc
		ON p.team_id = sc.country_id
WHERE country_name = 'England'