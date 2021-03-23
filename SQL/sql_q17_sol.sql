# Write a SQL query to find the country where the most assistant referees come from,
# and the count of the assistant referees.

WITH country_ass_referee_ct AS (
	SELECT country_name, count( distinct ass_ref_id) AS ass_referee_ct
	FROM match_details m
		INNER JOIN asst_referee_mast a
			ON a.ass_ref_id = m.ass_ref
		INNER JOIN soccer_country s
			ON a.country_id = s.country_id
	GROUP BY country_name
)
SELECT country_name, ass_referee_ct
from country_ass_referee_ct
ORDER BY ass_referee_ct DESC
LIMIT 1
