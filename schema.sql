CREATE TABLE course (
    id INTEGER NOT NULL,
    name VARCHAR(100) NOT NULL,
    CONSTRAINT pk_course PRIMARY KEY (id)
);

CREATE TABLE teacher (
    id INTEGER NOT NULL,
    name VARCHAR(100) NOT NULL,
    CONSTRAINT pk_teacher PRIMARY KEY (id)
);

CREATE TABLE class (
    id INTEGER NOT NULL,
    name VARCHAR(2) NOT NULL,
    teacher_id INTEGER NOT NULL,
    CONSTRAINT pk_class PRIMARY KEY (id),
    CONSTRAINT fk_class_teacher_id_teacher FOREIGN KEY(teacher_id) REFERENCES teacher (id)
);

CREATE TABLE student (
    id INTEGER NOT NULL,
    name VARCHAR(100) NOT NULL,
    class_id INTEGER NOT NULL,
    course_preference INTEGER NOT NULL,
    partner_1_id INTEGER,
    partner_2_id INTEGER,
    partner_3_id INTEGER,
    CONSTRAINT pk_student PRIMARY KEY (id),
    CONSTRAINT fk_student_class_id_class FOREIGN KEY(class_id) REFERENCES class (id),
    CONSTRAINT fk_student_course_preference_course FOREIGN KEY(course_preference) REFERENCES course (id),
    CONSTRAINT fk_student_partner_1_id_student FOREIGN KEY(partner_1_id) REFERENCES student (id),
    CONSTRAINT fk_student_partner_2_id_student FOREIGN KEY(partner_2_id) REFERENCES student (id),
    CONSTRAINT fk_student_partner_3_id_student FOREIGN KEY(partner_3_id) REFERENCES student (id)
);
