/*
Union, Uniol All
*/

-- Penambahan Table 3. 
Create Table WareHouseEmployeeDemographics 
(EmployeeID int, 
FirstName varchar(50), 
LastName varchar(50), 
Age int, 
Gender varchar(50)
)

-- Memasukkan value atau data pada table 3
Insert into WareHouseEmployeeDemographics VALUES
(1013, 'Darryl', 'Philbin', NULL, 'Male'),
(1050, 'Roy', 'Anderson', 31, 'Male'),
(1051, 'Hidetoshi', 'Hasagawa', 40, 'Male'),
(1052, 'Val', 'Johnson', 31, 'Female')

-- menggabungkan kolom dengan jumlah dan tipe data yang sama , dengan SYARAT kolomya sama. Union= Distinct
Select *
From [dbo].[WareHouseEmployeeDemographics]
UNION
Select *
from [dbo].[EmployeeDemographics];

Select * -- Union + Null values
From [dbo].[WareHouseEmployeeDemographics]
UNION ALL
Select *
from [dbo].[EmployeeDemographics];


-- menggabungkan kedua kolom dengan atau tidak sama value/kolom
Select *
from [dbo].[EmployeeDemographics]
full outer join [dbo].[WareHouseEmployeeDemographics]
 on [dbo].[EmployeeDemographics].EmployeeID = [dbo].[WareHouseEmployeeDemographics].EmployeeID



Select EmployeeID, FirstName, Age
From [dbo].[EmployeeDemographics]
Union
Select EmployeeID, JobTitle, Salary
from [dbo].[EmployeeSalary]
order by EmployeeID


/*
AS |  Aliasing - readibility to user end
*/

Select FirstName + ' ' + LastName AS FullName
From EmployeeDemographics

-- Aliasing Table Name,instead of Column
Select ED.EmployeeID
From EmployeeDemographics as ED

-- You'll find aliasing table much hellful when came to JOIN 2 tables or more
Select ED.EmployeeID, ED.FirstName, ED.LastName, ES.JobTitle, WED.age
from EmployeeDemographics as ED
left join EmployeeSalary as ES
 on ED.EmployeeID = ES.EmployeeID
left join WareHouseEmployeeDemographics as WED
on ED.EmployeeID = WED.EmployeeID;


Complete desc: https://medium.com/@imahanani_/atad-4-full-outer-join-unions-f145081db996
