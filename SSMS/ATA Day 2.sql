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

