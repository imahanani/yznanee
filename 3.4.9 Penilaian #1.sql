1. Membuat daftar tingkat pendidikan karyawan yang mendapat promosi. Daftar ini harus menunjukkan hanya pendidikan tanpa duplikat.
```sql
Select distinct (education) as unique_edu
from employee_promotion
where education is not null and awards_won is not null
;
---------------------------------------------------------------------------query elaboration
SELECT DISTINCT: This clause selects only unique values in the "education" column from the "employee_promotion" table.

(education) AS unique_edu: This is an alias that renames the "education" column to "unique_edu". The AS keyword is optional, but it helps to make the code more readable.

FROM employee_promotion: This specifies the table to select data from.

WHERE education IS NOT NULL: This is a condition that filters the rows where the "education" column is not null. This means that only rows with a non-null "education" value will be returned.

AND awards_won IS NOT NULL: This is another condition that filters the rows where the "awards_won" column is not null. This means that only rows with a non-null "awards_won" value will be returned.

; : This semicolon at the end of the code signals the end of the SQL statement.

To summarize, this SQL query selects unique values from the "education" column of the "employee_promotion" table where both the "education" and "awards_won" columns are not null. The result set will contain a list of unique education values for employees who have won awards.


|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
2. Karyawan termuda dan tertua yang mendapat promosi dengan tingkat pendidikan “Below Secondary” (di bawah SMP).
```sql
Select min(age), max(age)
from employee_promotion
where education is not null and education = 'Below Secondary' and awards_won is not null--Select distinct (education) from employee_promotion;
;
---------------------------------------------------------------------------------------------
The given SQL code retrieves the minimum and maximum age of employees who meet certain criteria from the "employee_promotion" table. Let's break down the code step by step:

SELECT statement: The SELECT statement is used to retrieve data from the table. In this case, we want to retrieve the minimum and maximum age of employees.

MIN() and MAX() functions: These are aggregate functions used to retrieve the minimum and maximum values of a column. In this case, we want to find the minimum and maximum age.

FROM clause: The FROM clause specifies the table from which we want to retrieve data. In this case, we want to retrieve data from the "employee_promotion" table.

WHERE clause: The WHERE clause is used to filter the rows that meet certain conditions. In this case, we want to retrieve data only for employees who have an education level of "Below Secondary" and have won awards.

education is not null: This condition ensures that we only retrieve data for employees who have a non-null education level.

education = 'Below Secondary': This condition ensures that we only retrieve data for employees who have an education level of "Below Secondary".

awards_won is not null: This condition ensures that we only retrieve data for employees who have won awards.

The entire SQL query ends with a semicolon (;).

In summary, the given SQL code retrieves the minimum and maximum age of employees who have an education level of "Below Secondary" and have won awards from the "employee_promotion" table.


||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
3. Menunjukkan 2 tingkat pendidikan yang paling sedikit menyumbang promosi bagi karyawan wanita. Urutkan tingkat pendidikan berdasarkan jumlah karyawan wanita yang dipromosikan, tempatkan yang paling sedikit di baris paling atas.
```sql
Select distinct(education) as unique_edu, sum(awards_won) as total_awards
from employee_promotion
where gender= 'f' and education is not null
group by unique_edu
order by total_awards asc
limit 2
;
----------------------------------------------------------------
The first line of the code begins with the SELECT statement. It selects two columns, education and awards_won from the employee_promotion table. However, it also includes some modifications to these columns. First, the DISTINCT keyword is used to only select unique values of education. This means that if there are multiple rows with the same value of education, only one of them will be included in the output. Second, the AS keyword is used to give new names to these columns. education is renamed to unique_edu, while awards_won is renamed to total_awards.

The FROM statement specifies that the data will be taken from the employee_promotion table.

The WHERE statement is used to filter the results. It specifies that only rows where the value of gender is 'f' (i.e. female) and education is not null (i.e. has a non-null value) will be included in the output.

The GROUP BY statement is used to group the results by the values in the unique_edu column. This means that all rows with the same value of unique_edu will be grouped together.

The ORDER BY statement is used to sort the results in ascending order by the values in the total_awards column. This means that the rows with the smallest value of total_awards will be listed first.

The LIMIT statement is used to limit the number of rows included in the output. In this case, it specifies that only the first two rows (i.e. the rows with the smallest values of total_awards) will be included.

Finally, the semicolon ; is used to indicate the end of the SQL query.

So, putting it all together, the SQL code selects unique values of education for female employees who have received awards, and returns the total number of awards won for each unique education value. The results are then grouped by education, sorted in ascending order by total awards, and limited to the first two rows of the output.





