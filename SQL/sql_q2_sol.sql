#Write a SQL query to find the number of matches that were won by penalty shootout

USE euro_cup_2016;

SELECT COUNT(DISTINCT match_no)
FROM match_mast
WHERE decided_by = 'P' and results  = 'WIN';



