3.5.2 Operasi untuk data angka

1. Create Table Schema
```sql
create table lending_dataset (
loan_number int,
amount_borrowed	 int, 
term int, 
borrower_rate numeric(2,4),
installment numeric(3,2),	
grade text,	
origination_date datetime,	
listing_title text, 	
principal_balance int, 	
principal_paid numeric(5.2),
interest_paid numeric(5,2),	
late_fees_paid	int,
debt_sale_proceeds_received numeric(5,2),
last_payment_date datetime, 	
next_payment_due_date	datetime, 
days_past_due int, 
loan_status_description	text,
data_source text
)
```
-------------------------MASIH ERROR, QUERY DI ATAS
ERROR:  NUMERIC scale 4 must be between 0 and precision 2
LINE 5: borrower_rate numeric(2, 4),
                      ^
SQL state: 22023
Character: 97
================================

NOTE! Our mentor has informed me that the upcoming module, 3.5.4, will include a section on query overflow.
```sql
--membuat table  dan type kolom
drop table if exists public.lending_dataset; 

create table if not exists public.lending_dataset (
loan_number int not null,
amount_borrowed	 numeric(11,2), 
term int, 
borrower_rate numeric(8,7),
installment numeric(11,2),	
grade text collate pg_catalog."default",	
origination_date timestamp(0) without time zone,	
listing_title text collate pg_catalog."default", 	
principal_balance numeric(11,2), 	
principal_paid numeric(11,2),
interest_paid numeric(11,2),	
late_fees_paid	numeric(11,2),
debt_sale_proceeds_received numeric(11,2),
last_payment_date timestamp(0) without time zone, 	
next_payment_due_date	timestamp(0) without time zone, 
days_past_due int, 
loan_status_description	text collate pg_catalog."default",
data_source text collate pg_catalog."default"
)

tablespace pg_default;
alter table if exists public.lending_dataset
owner to postgres; 
``` --succeed


