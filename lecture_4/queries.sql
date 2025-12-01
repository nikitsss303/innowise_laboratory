-- 1 query
CREATE TABLE students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT,
    birth_year INT
);

CREATE TABLE grades(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INT,
    subject TEXT,
    grade INT,
    CONSTRAINT FK_grades_students FOREIGN KEY (student_id) REFERENCES students(id)
);

-- 2 query
INSERT INTO students (
  full_name, birth_year
) VALUES 
( "Alice Johnson", 2005),
( "Brian Smith", 2004),
( "Carla Reyes", 2006),
( "Daniel Kim", 2005),
( "Eva Thompson", 2003),
( "Felix Nguyen", 2007),
( "Grace Patel", 2005),
( "Henry Lopez", 2004),
( "Isabel Martinez", 2006);

INSERT INTO grades (
  student_id, subject, grade
) VALUES 
(1,'Math',88),
(1,'English',92),
(1,'Science',85),
(2,'Math',75),
(2,'History',83), 
(2,'English',79), 
(3,'Science',95), 
(3,'Math',91),
(3,'Art',89), 
(4,'Math',84),
(4,'Science',88),
(4,'Physical Education',93), 
(5,'English',90),
(5,'History',85),
(5,'Math',88),
(6,'Science',72), 
(6,'Math',78),
(6,'English',81),
(7,'Art',94),
(7,'Science',87), 
(7,'Math',90),
(8,'History',77), 
(8,'Math',83),
(8,'Science',80), 
(9,'English',96), 
(9,'Math',89),
(9,'Art',92);

-- 3 query
SELECT g.grade, s.full_name  
FROM grades as g
INNER JOIN students as s
  ON g.student_id==s.id
WHERE s.full_name=='Alice Johnson';

-- 4 query
SELECT AVG(grade)
FROM grades;

-- 5 quary
SELECT *
FROM students
WHERE birth_year > 2004;

-- 6 quary
SELECT subject, AVG(grade) as avg_grade
FROM grades
GROUP BY subject;

-- 7 query
SELECT s.full_name, AVG(grade) as avg_grade
FROM grades as g    
INNER JOIN students as s 
  ON g.student_id == s.id 
GROUP BY s.full_name
ORDER BY avg_grade DESC LIMIT 3;

-- 8 quary 
SELECT s.full_name, g.subject, g.grade 
FROM students as s 
LEFT JOIN grades as g 
  ON s.id == g.student_id
WHERE grade < 80;
