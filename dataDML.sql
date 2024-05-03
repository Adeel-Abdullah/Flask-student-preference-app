-- Insert data into the course table
INSERT INTO course (id, name) VALUES
(1, 'Math'),
(2, 'Language'),
(3, 'Science'),
(4, 'Art'),
(5, 'Gym');

-- Insert data into the teacher table
INSERT INTO teacher (id, name) VALUES
(1, 'Mr. Smith'),
(2, 'Ms. Johnson'),
(3, 'Ms. Taylor');

-- Insert data into the class table
INSERT INTO class (id, name, teacher_id) VALUES
(1, '1A', 1),
(2, '1B', 2),
(3, '1C', 3);

-- Insert data into the student table
INSERT INTO student (name, class_id, course_preference, partner_1_id, partner_2_id, partner_3_id) VALUES
('John Doe', 1, 1, 2, 3, 4),
('Jane Smith', 1, 2, 1, 3, 4),
('Alice Johnson', 2, 1, 1, 2, 4),
('Bob Brown', 2, 3, 1, 2, 3),
('Emily Davis', 3, 4, 3, 4, 6),
('Michael Wilson', 3, 5, 2, 3, 4);

