# Write your MySQL query statement below
SELECT employee_id,  team_size FROM Employee E
JOIN (SELECT team_id, COUNT(team_id) as team_size
FROM Employee
GROUP BY team_id) AS M
ON M.team_id = E.team_id


