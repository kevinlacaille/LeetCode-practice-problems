# SQL Schema
Create table If Not Exists Employee (Id int, Name varchar(255), Salary int, ManagerId int)
Truncate table Employee
insert into Employee (Id, Name, Salary, ManagerId) values ('1', 'Joe', '70000', '3')
insert into Employee (Id, Name, Salary, ManagerId) values ('2', 'Henry', '80000', '4')
insert into Employee (Id, Name, Salary, ManagerId) values ('3', 'Sam', '60000', 'None')
insert into Employee (Id, Name, Salary, ManagerId) values ('4', 'Max', '90000', 'None')

# MySQL query statement below
# selected names from Employee table
SELECT E1.Name AS 'Employee'
# make two sets of list, E1 and E2
FROM Employee E1, Employee E2
# where we compare the manager IDs and the IDs AND their respective salaries
WHERE E1.ManagerId = E2.Id AND E1.Salary > E2.Salary
;
