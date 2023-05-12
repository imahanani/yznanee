/*
SELECT * FROM [ATA SQL].sys.objects WHERE name = 'EmployeeDemographics';
to confirm that you are a) on the right server and b) that the object is getting created.
*/

Create Table EmployeeDemographics  -- create Table1
(EmployeeID int, 
FirstName varchar(50), 
LastName varchar(50), 
Age int, 
Gender varchar(50)
)
Create Table EmployeeSalary --create Table2
(EmployeeID int, 
JobTitle varchar(50), 
Salary int
)
Insert into EmployeeDemographics VALUES --insert data to Table1 that named EmployeeDemographics
(1001, 'Jim', 'Halpert', 30, 'Male'),
(1002, 'Pam', 'Beasley', 30, 'Female'),
(1003, 'Dwight', 'Schrute', 29, 'Male'),
(1004, 'Angela', 'Martin', 31, 'Female'),
(1005, 'Toby', 'Flenderson', 32, 'Male'),
(1006, 'Michael', 'Scott', 35, 'Male'),
(1007, 'Meredith', 'Palmer', 32, 'Female'),
(1008, 'Stanley', 'Hudson', 38, 'Male'),
(1009, 'Kevin', 'Malone', 31, 'Male')

Insert Into EmployeeSalary VALUES --Insert data into Table2 called EmployeeSalary
(1001, 'Salesman', 45000),
(1002, 'Receptionist', 36000),
(1003, 'Salesman', 63000),
(1004, 'Accountant', 47000),
(1005, 'HR', 50000),
(1006, 'Regional Manager', 65000),
(1007, 'Supplier Relations', 41000),
(1008, 'Salesman', 48000),
(1009, 'Accountant', 42000)

Select * from [dbo].[EmployeeDemographics]
Select * from [dbo].[EmployeeSalary]
