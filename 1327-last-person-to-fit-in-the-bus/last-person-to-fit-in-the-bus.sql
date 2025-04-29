# Write your MySQL query statement below
with bus as(
    select person_name, turn,
        sum(weight) over(order by turn) as total_weight
    from queue
)

select person_name 
from bus
where total_weight<=1000
order by total_weight desc
limit 1;