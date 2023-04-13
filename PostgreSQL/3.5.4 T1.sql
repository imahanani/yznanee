      Main Task:
Kamu bekerja sebagai credit data analyst di sebuah perusahaan fintech. Tim-mu  tengah memformulasikan credit score dan kamu harus mengerjakan pekerjaan 
berikut:
1. Berapakah rata-rata persentase outstanding balance dari setiap status pinjaman, dimana persentase outstanding balance didefinisikan sebagai principal balance dibagi amount borrowed?
2. Untuk status pinjaman ‘defaulted’, urutkan grade berdasarkan rata-rata persentase outstanding balance tertinggi ke terendah, serta munculkan juga jumlah pinjaman dan rata-rata suku bunga pinjaman (borrower rate).

      Hints:
- Gunakan AVG diikuti operator “/” untuk menghitung rata-rata outstanding balance percentage dari kolom principal_balance dan amount_borrowed. 
- Gunakan GROUP BY untuk mengelompokkan berdasarkan loan_status_description.
- Gunakan AVG diikuti operator pembagi “/” untuk menghitung rata-rata outstanding balance percentage, COUNT kolom loan_number, AVG kolom amount_borrowed, dan AVG kolom borrower_rate. Kamu perlu menggunakan GROUP BY dan ORDER BY untuk grouping dan mengurutkan.

      Trial and Error
```sql
create table if not exists public.lending_dataset 
(
loan_number int not null,
amount_borrowed	 numeric(11,2), 
term int, 
borrower_rate numeric(8,7),
installment numeric(11,2),	
grade text collate pg_catalog."default",	
origination_date timestamp(0) without time zone,	
listing_title text collate pg_catalog."default", 	
principal_balance numeric(11,2), 	
principal_paid numeric(11,2)),
interest_paid numeric(11,2),	
late_fees_paid	numeric(11,2),
debt_sale_proceeds_received numeric(11,2),
last_payment_date timestamp(0) without time zone, 	
next_payment_due_date	timestamp(0) without time zone, 
days_past_due int, 
loan_status_description	text collate pg_catalog."default",
data_source text collate pg_catalog."default"
)
```
      Data Type of each column
      (
loan_number int ,
amount_borrowed	 numeric(11,2), 
term int, 
borrower_rate numeric(8,7),
installment numeric(11,2),	
grade text ,	
origination_date timestamp,	
listing_title text , 	
principal_balance numeric(11,2), 	
principal_paid numeric(11,2)),
interest_paid numeric(11,2),	
late_fees_paid	numeric(11,2),
debt_sale_proceeds_received numeric(11,2),
last_payment_date timestamp, 	
next_payment_due_date	timestamp, 
days_past_due int, 
loan_status_description	text ,
data_source text
)


```sql
select * from lending_dataset
limit 10;
```
=================q1
Q: menghitung rata-rata outstanding balance percentage?
A: Untuk menghitung rata-rata outstanding balance percentage dari kolom principal_balance dan amount_borrowed pada SQL, Anda dapat menggunakan fungsi AVG dan operator pembagian (/) seperti ini:
```sql
SELECT AVG(principal_balance/amount_borrowed) AS avg_outstanding_balance_percentage 
FROM lending_dataset;
```
----------------penjelasan teknis
1. Perintah SELECT untuk memilih data dari tabel yang ingin dihitung rata-rata outstanding balance percentage-nya.

2. Menggunakan fungsi AVG() untuk menghitung rata-rata  hasil pembagian antara kolom principal_balance dengan kolom amount_borrowed di setiap baris. Lalu memberi nama alias "avg_outstanding_balance_percentage" untuk hasil rata-rata tersebut menggunakan perintah AS.

3. Menentukan tabel yang akan digunakan dengan memasukkan nama tabel di dalam perintah FROM.

Secara keseluruhan, kode SQL tersebut akan mengambil semua baris dari tabel yang ditentukan, menghitung rata-rata outstanding balance percentage dengan membagi nilai principal_balance dengan amount_borrowed di setiap baris, dan menampilkan hasilnya dengan nama alias "avg_outstanding_balance_percentage".

=====================q2
Q: Untuk status pinjaman ‘defaulted’, urutkan grade berdasarkan rata-rata persentase outstanding balance tertinggi ke terendah, serta munculkan juga jumlah pinjaman dan rata-rata suku bunga pinjaman (borrower rate)
A:Assuming you have a table named "loans" with the following columns: Assuming you have a table named "loans" with the following columns:
- loan_number
- outstanding_balance
- amount_borrowed
- borrower_rate
You can use the following SQL query to calculate the requested values:
```sql
SELECT AVG(outstanding_balance/amount_borrowed) AS avg_outstanding_balance_percentage,
       COUNT(loan_number) AS loan_count,
       AVG(amount_borrowed) AS avg_amount_borrowed,
       AVG(borrower_rate) AS avg_borrower_rate
FROM loans
GROUP BY loan_number
ORDER BY avg_outstanding_balance_percentage DESC;
```
----------------------------tecnical explan
Explanation:

- AVG(outstanding_balance/amount_borrowed) calculates the average outstanding balance percentage by dividing the outstanding balance by the amount borrowed, and then taking the average.
- COUNT(loan_number) counts the number of loans in the table.
- AVG(amount_borrowed) calculates the average amount borrowed.
- AVG(borrower_rate) calculates the average borrower rate.
- GROUP BY loan_number groups the results by loan number.
- ORDER BY avg_outstanding_balance_percentage DESC sorts the results in descending order by the average outstanding balance percentage.

================Every inquiry that has been submitted.
select * from lending_dataset limit 10;

--rata-rata outstanding balance percentage
select avg (principal_balance/amount_borrowed) as avg_outstanding_balance_percentage 
from lending_dataset
--limit 10;

--status pinjaman ‘defaulted’ so on....
select (principal_balance/amount_borrowed) as avg_outstanding_balance_percentage,
       count(loan_number) as loan_count,
       avg(amount_borrowed) as avg_amount_borrowed,
       avg(borrower_rate) as avg_borrower_rate
from lending_dataset
group by (principal_balance/amount_borrowed), loan_number
order by avg_outstanding_balance_percentage desc
--limit 100;



