#Write a SQL query to find the date EURO Cup 2016 started on.
USE euro_cup_2016;

SELECT MIN(play_date) FROM match_mast;
