SELECT 
    c.name AS course_name,
    COUNT(s.course_preference) AS popularity
FROM 
    course c
LEFT JOIN 
    student s ON c.id = s.course_preference
GROUP BY 
    c.name
ORDER BY 
    popularity DESC;
