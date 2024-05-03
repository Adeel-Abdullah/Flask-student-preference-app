SELECT student.name, class.name, score
FROM (
    SELECT id AS pk, SUM(score) AS score
    FROM (
        SELECT partner_1_id AS id, 1 AS score FROM student
        UNION ALL
        SELECT partner_2_id AS id, 0.5 AS score FROM student
        UNION ALL
        SELECT partner_3_id AS id, 0.25 AS score FROM student
    ) AS sub
    GROUP BY pk
) AS subquery
JOIN student ON subquery.pk = student.id
JOIN class ON class.id = student.class_id;
