select requester_id as id,sum(num) as num from 
    (select requester_id,count(*) as num from RequestAccepted group by requester_id
    union all
    select accepter_id as requester_id,count(*) as num from RequestAccepted group by accepter_id) x 

group by requester_id order by num desc limit 1;