select id, sum(score) as score
from
(
select partner_1_id as id, 1 as score from student
union all
select partner_2_id as id, 0.5 as score from student
union all
select partner_3_id as id, 0.25 as score from student
)
group by id; 