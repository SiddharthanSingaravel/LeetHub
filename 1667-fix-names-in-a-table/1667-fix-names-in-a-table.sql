# Write your MySQL query statement below
SELECT user_id, CONCAT(UPPER(LEFT(name, 1)), LOWER(RIGHT(name, length(name) - 1))) as name FROM users
ORDER BY user_id