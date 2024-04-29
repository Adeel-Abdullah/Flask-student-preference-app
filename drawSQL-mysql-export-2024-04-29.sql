CREATE TABLE `course`(
    `id` INT NOT NULL,
    `name` VARCHAR(100) NOT NULL,
    PRIMARY KEY(`id`)
);
CREATE TABLE `student`(
    `id` INT NOT NULL,
    `name` VARCHAR(100) NOT NULL,
    `class_id` INT NOT NULL,
    `course_preference` INT NOT NULL,
    `partner_1_id` INT NOT NULL,
    `partner_2_id` INT NOT NULL,
    `partner_3_id` INT NOT NULL,
    PRIMARY KEY(`id`)
);
CREATE TABLE `teacher`(
    `id` INT NOT NULL,
    `name` VARCHAR(100) NOT NULL,
    PRIMARY KEY(`id`)
);
CREATE TABLE `class`(
    `id` INT NOT NULL,
    `name` VARCHAR(2) NOT NULL,
    `teacher_id` INT NOT NULL,
    PRIMARY KEY(`id`)
);
ALTER TABLE
    `student` ADD CONSTRAINT `student_partner_1_id_foreign` FOREIGN KEY(`partner_1_id`) REFERENCES `student`(`id`);
ALTER TABLE
    `student` ADD CONSTRAINT `student_partner_2_id_foreign` FOREIGN KEY(`partner_2_id`) REFERENCES `student`(`id`);
ALTER TABLE
    `student` ADD CONSTRAINT `student_course_preference_foreign` FOREIGN KEY(`course_preference`) REFERENCES `course`(`id`);
ALTER TABLE
    `student` ADD CONSTRAINT `student_class_id_foreign` FOREIGN KEY(`class_id`) REFERENCES `class`(`id`);
ALTER TABLE
    `class` ADD CONSTRAINT `class_teacher_id_foreign` FOREIGN KEY(`teacher_id`) REFERENCES `teacher`(`id`);
ALTER TABLE
    `student` ADD CONSTRAINT `student_partner_3_id_foreign` FOREIGN KEY(`partner_3_id`) REFERENCES `student`(`id`);