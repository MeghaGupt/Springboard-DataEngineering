#Write a SQL query to compute a list showing the number of substitutions that
#happened in various stages of play for the entire tournament.

USE euro_cup_2016;

SELECT match_no, COUNT(*)
FROM player_in_out
WHERE  in_out = 'O'
GROUP BY match_no