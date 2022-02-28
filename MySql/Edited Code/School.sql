USE school;
CREATE TABLE teacher (
	id INT(11) AUTO_INCREMENT PRIMARY KEY,
    teacher_name VARCHAR(50) NOT NULL, 
    class INT(3) NOT NULL,
    section VARCHAR(2) NOT NULL,
    class_subject VARCHAR(50) NOT NULL
)