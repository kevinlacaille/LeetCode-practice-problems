# SQL Schema
Create table If Not Exists courses (student varchar(255), class varchar(255))
Truncate table courses
insert into courses (student, class) values ('A', 'Math')
insert into courses (student, class) values ('B', 'English')
insert into courses (student, class) values ('C', 'Math')
insert into courses (student, class) values ('D', 'Biology')
insert into courses (student, class) values ('E', 'Math')
insert into courses (student, class) values ('F', 'Computer')
insert into courses (student, class) values ('G', 'Math')
insert into courses (student, class) values ('H', 'Math')
insert into courses (student, class) values ('I', 'Math')

# MySQL query statement below
# selects all classes from the courses table
SELECT class from courses
# group classes together, gets rid of douplicates, but remembers how many there are of each
GROUP BY class
# return all classes that have more than or equal to 5 distinct students
HAVING COUNT(distinct student)>=5;
