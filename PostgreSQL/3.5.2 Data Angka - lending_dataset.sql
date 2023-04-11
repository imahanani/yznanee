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


