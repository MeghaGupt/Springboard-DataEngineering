#Write a SQL query to find all available information about the players under contract to
#Liverpool F.C. playing for England in EURO Cup 2016

SELECT p.*, country_name
FROM player_mast p
	INNER JOIN soccer_country sc
		ON p.team_id = sc.country_id
WHERE country_name = 'England' and playing_club = 'Liverpool'
