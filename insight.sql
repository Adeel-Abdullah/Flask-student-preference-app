SELECT 
    s1.name AS student1_name,
    s2.name AS student2_name,
    c1.name AS favorite_course1,
    c2.name AS favorite_course2
FROM 
    student AS s1
JOIN 
    student AS s2 ON s1.id < s2.id -- to avoid duplicate pairs
JOIN 
    course AS c1 ON s1.course_preference = c1.id
JOIN 
    course AS c2 ON s2.course_preference = c2.id
WHERE 
    s1.partner_1_id = s2.id AND s2.partner_1_id = s1.id
    OR s1.partner_1_id = s2.id AND s2.partner_2_id = s1.id
    OR s1.partner_1_id = s2.id AND s2.partner_3_id = s1.id
    OR s1.partner_2_id = s2.id AND s2.partner_1_id = s1.id
    OR s1.partner_2_id = s2.id AND s2.partner_2_id = s1.id
    OR s1.partner_2_id = s2.id AND s2.partner_3_id = s1.id
    OR s1.partner_3_id = s2.id AND s2.partner_1_id = s1.id
    OR s1.partner_3_id = s2.id AND s2.partner_2_id = s1.id
    OR s1.partner_3_id = s2.id AND s2.partner_3_id = s1.id;
