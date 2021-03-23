#Write a SQL query to find the number of matches that were won by a single point, but
#do not include matches decided by penalty shootout.

SELECT COUNT(*)
 FROM match_mast
WHERE decided_by = 'N' and results = 'WIN' and ABS(SUBSTRING_INDEX( goal_score, '-', -1 ) - SUBSTRING_INDEX( goal_score, '-', 1 ))
#goal_score IN ('0-1', '1-0')


