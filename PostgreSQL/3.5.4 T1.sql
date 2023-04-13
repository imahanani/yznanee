      Main Task:
Kamu bekerja sebagai credit data analyst di sebuah perusahaan fintech. Tim-mu  tengah memformulasikan credit score dan kamu harus mengerjakan pekerjaan 
berikut:
1. Berapakah rata-rata persentase outstanding balance dari setiap status pinjaman, dimana persentase outstanding balance didefinisikan sebagai principal balance dibagi amount borrowed?
2. Untuk status pinjaman ‘defaulted’, urutkan grade berdasarkan rata-rata persentase outstanding balance tertinggi ke terendah, serta munculkan juga jumlah pinjaman dan rata-rata suku bunga pinjaman (borrower rate).

      Hints:
- Gunakan AVG diikuti operator “/” untuk menghitung rata-rata outstanding balance percentage dari kolom principal_balance dan amount_borrowed. 
- Gunakan GROUP BY untuk mengelompokkan berdasarkan loan_status_description.
- Gunakan AVG diikuti operator pembagi “/” untuk menghitung rata-rata outstanding balance percentage, COUNT kolom loan_number, AVG kolom amount_borrowed, dan AVG kolom borrower_rate. Kamu perlu menggunakan GROUP BY dan ORDER BY untuk grouping dan mengurutkan.

================Every inquiry that has been submitted.
select * from lending_dataset limit 10;

--rata-rata outstanding balance percentage
select loan_status_description, avg (principal_balance/amount_borrowed) as avg_outstanding_balance_percentage 
from lending_dataset
GROUP BY loan_status_description
--limit 10;

--status pinjaman ‘defaulted’ so on....
select grade, avg(principal_balance/amount_borrowed) as percentage_outstanding_balance,
       count(loan_number) as loan_count,
       avg(amount_borrowed) as avg_amount_borrowed,
       avg(borrower_rate) as avg_rate
from lending_dataset
WHERE loan_status_description ilike 'defaulted'
group by grade
order by percentage_outstanding_balance desc
--limit 10;
