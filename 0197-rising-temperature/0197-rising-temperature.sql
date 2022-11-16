# Write your MySQL query statement below
SELECT w2.id from weather w1, weather w2
where to_days(w2.recordDate) - to_days(w1.recordDate) = 1
and w2.temperature > w1.temperature