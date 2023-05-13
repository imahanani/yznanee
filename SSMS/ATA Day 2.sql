/*ATAD2 - Top, Distinct, Count, As, Min, Avg
*/
Select * 
from [dbo].[EmployeeDemographics] -- return everything

 -- Top | return the most one (top 5,mean the most 5 only)
Select top 5 * 
from [dbo].[EmployeeDemographics]

 -- Distinct | unique value
Select distinct(Gender)
from [dbo].[EmployeeDemographics]

 -- Count | total row
Select COUNT(LastName) 
from [dbo].[EmployeeDemographics]


 -- As | aliases
Select COUNT(LastName) AS LastNameCount
from [dbo].[EmployeeDemographics]


 -- Min, Max, Avg (interchangable query to return the value you want)| minimum column value
Select AVG(Salary)
from [dbo].[EmployeeSalary]


--Note: make sure you are on the right database

/* Where Statement
= , <>, <, >, Anda, Or, Like, Null, Not Null, In
*/
Select * 
from [dbo].[EmployeeDemographics]
Where FirstName = 'Jim'

Select * 
from 
Where


Select * 
from [dbo].[EmployeeDemographics]
Where Age >= 30; 

Select * -- 2 statements has to value TRUE
from [dbo].[EmployeeDemographics]
Where Age <= 32 AND Gender = 'Male';

Select * -- 2 statements has to value TRUE -- 1 of true value TRUE, will be return
from [dbo].[EmployeeDemographics]
Where Age <= 32 or Gender = 'Male';

Select *  -- wildcard %, everything on the column LastName consist S will return
from [dbo].[EmployeeDemographics]
Where LastName like 'S%'

Select *  -- wildcard %, everything on the column LastName consist S and o will return
from [dbo].[EmployeeDemographics]
Where LastName like 'S%o%' 

Select * --return the column FirstName in NULL only 
from [dbo].[EmployeeDemographics]
Where FirstName is null

Select * -- return only FirstName Jim and Michael
from [dbo].[EmployeeDemographics]
Where FirstName IN ('Jim', 'Michael')


