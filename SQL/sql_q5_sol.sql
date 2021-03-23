#Write a SQL query to find the number of bookings that happened in stoppage time

USE euro_cup_2016;

SELECT count(*)
FROM player_booked
WHERE play_schedule  = 'ST'
