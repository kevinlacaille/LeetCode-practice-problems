# SQL Schema
Create table If Not Exists Person (Id int, Email varchar(255))
Truncate table Person
insert into Person (Id, Email) values ('1', 'a@b.com')
insert into Person (Id, Email) values ('2', 'c@d.com')
insert into Person (Id, Email) values ('3', 'a@b.com')

# MySQL query statement below
# selects all emails from Person table
SELECT Email from Person
# group emails together, gets rid of douplicates, but remembers how many there are of each
GROUP BY Email
# return all that have more than 1 count (e.g., all that are douplicates)
HAVING COUNT(Email)>1;
