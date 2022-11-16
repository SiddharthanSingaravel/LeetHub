# Write your MySQL query statement below
select name from salesperson where
name not in (select s.name from orders o
inner join company c on o.com_id = c.com_id
inner join salesperson s on s.sales_id = o.sales_id
where c.name = 'red')