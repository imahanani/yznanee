3.3.3 Pekerjaan rumah: Tugas 1

/* 
Gunakan sintaks dasar SELECT [nama kolom] FROM [nama tabel]. Nama 
tabel yang digunakan adalah fitness_tracker. Kamu akan menggunakan 
kolom brand_name, model_name, original_price
Tambah perintah WHERE untuk membatasi data. Kamu akan menggunakan 
kolom brand_name, model_name, dan reviews untuk membatasi data
*/

```sql
select * from fitnes_tracker
--limit 50
--order by reviews asc; 
select distinct brand_name from fitnes_tracker; -- Daftar brand yang ada di dataset fitness tracker
select distinct model_name from fitnes_tracker --Daftar nama model dari brand Huawei
-- select distinct model_name from fitnes_tracker limit 50; 
where brand_name = 'Huawei' ; 
select distinct model_name, original_price --Harga original dari produk Smart Band 5
from fitnes_tracker
where model_name = 'Smart Band 5' ; 
select brand_name, reviews-- Daftar brand yang memiliki review sebanyak 14.
from fitnes_tracker
where reviews = '14' ; --hasilnya 'kosong'karena tidak ada yang memiliki reviews '14'
```sql --contoh
SELECT column1, column2
FROM table1
WHERE column1 = 'value';
