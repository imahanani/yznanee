-- menambahkan nilai pada [ATA SQL].[dbo].[EmployeeDemographics]
Insert into EmployeeDemographics VALUES
(1011, 'Ryan', 'Howard', 26, 'Male'),  --row 10 
(NULL, 'Holly', 'Flax', NULL, NULL), --row 11
(1013, 'Darryl', 'Philbin', NULL, 'Male') --row 12

Select * --pengecekan apakah penambahan data sudah masuk atau belum
from [dbo].[EmployeeDemographics] 

Insert into EmployeeSalary VALUES
(1010, NULL, 47000),
(NULL, 'Salesman', 43000)


/* Menggabungkan berbagai database
Inner Joins, Full/Left/Right/Outer Joins
*/

Select * 
from [ATA SQL].dbo.EmployeeDemographics

Select * 
From [ATA SQL].dbo.EmployeeSalary

-- menggabugkan 2 table, overlaping keduanya. Berdasarkan kolom EmployeeID
Select * 
From [ATA SQL].dbo.EmployeeDemographics
Join [ATA SQL].dbo.EmployeeSalary
 on EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID

-- return everything from both columns, include NULL . Regardless matched or not. 
Select * 
From [ATA SQL].dbo.EmployeeDemographics
full outer join [ATA SQL].dbo.EmployeeSalary
 on EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID


Select *  --return everything on The Right Table 
From [ATA SQL].dbo.EmployeeDemographics
left join [ATA SQL].dbo.EmployeeSalary
 on EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID

Select * 
From [ATA SQL].dbo.EmployeeDemographics
right join [ATA SQL].dbo.EmployeeSalary
 on EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID

-- select only columns that u need, limit, sort 
Select EmployeeDemographics.EmployeeID, FirstName, Salary
From [ATA SQL].dbo.EmployeeDemographics
inner join [ATA SQL].dbo.EmployeeSalary 
 on EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID
Where FirstName <> 'Michael'
Order by  Salary desc


Select JobTitle , AVG(Salary) as avgSalary
From [ATA SQL].dbo.EmployeeDemographics
inner join [ATA SQL].dbo.EmployeeSalary 
 on EmployeeDemographics.EmployeeID = EmployeeSalary.EmployeeID
Where JobTitle = 'Salesman'
Group by JobTitle
