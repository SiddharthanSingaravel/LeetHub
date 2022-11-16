# Write your MySQL query statement below
select employee_id, (salary * case when employee_id%2 <> 0 and name not like 'M%' then 1
                    else 0 end) as bonus 
from employees
order by employee_id asc