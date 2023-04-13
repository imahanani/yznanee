3.5.10 Penilaian #1

Scenario:
Kamu bekerja sebagai associate data analyst di suatu perusahaan produsen mainan. Manajer penjualan ingin:
1. Membuat inisiatif diskon hanya untuk unit produk yang terjual lebih dari 7; harganya akan dikurangi sebanyak $2 per unit. Hitung berapa total penjualan dengan diskon (hanya untuk produk dengan diskon) per toko.
2. Agar dataset lebih mudah terbaca, harap gabungkan nama toko dengan nama produk yang terpisah dengan spasi.
3. Manajer ingin mengetahui tahun data penjualan ini.

Yang perlu kamu lakukan:
1. Gunakan SUM di bidang units dikali dengan (product_price dikurangi diskon). Filter data hanya untuk unit yang terjual lebih dari 7, dan kelompokkan berdasarkan nama toko.
2. Gabungkan nama toko dengan nama produk.
3. Ambil tahun dari bidang date

```sql trial&error
SELECT SUM((jumlah_produk - 7) * 2) AS total_penjualan_diskon
FROM nama_tabel
WHERE jumlah_produk > 7;
SELECT CONCAT(nama_toko, ' ', nama_produk) AS nama_toko_produk
FROM nama_tabel;
```


----------------all queries
```sql
/*
1. Membuat inisiatif diskon hanya untuk unit produk yang terjual lebih dari 
7; harganya akan dikurangi sebanyak $2 per unit. Hitung berapa total 
penjualan dengan diskon (hanya untuk produk dengan diskon) per toko.
2. Agar dataset lebih mudah terbaca, harap gabungkan nama toko dengan 
nama produk yang terpisah dengan spasi.
3. Manajer ingin mengetahui tahun data penjualan ini*/

select * from sales limit 1;

SELECT sum(units * (product_price - 2)) AS total_discount, 
		concat(store_name, ' ', product_name) AS concat_store_product
FROM sales
WHERE units > 7
group by store_name, product_name
;

select distinct (extract(year from date))as extract_year
from sales 
;
```
