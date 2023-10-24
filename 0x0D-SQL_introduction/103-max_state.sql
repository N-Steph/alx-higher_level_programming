-- Script that displays the top 3 of cities temperature during July and August
-- selecting each state and determining the max temperature for each
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
