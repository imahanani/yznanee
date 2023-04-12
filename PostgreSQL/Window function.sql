Window function atau juga dikenal sebagai analytic function adalah fitur dalam SQL yang memungkinkan pengguna untuk melakukan perhitungan atau agregasi pada subset data dalam sebuah grup, tanpa mengurangi jumlah baris yang ditampilkan dalam hasil query.

Contoh penggunaan window function di SQL:
```sql
SELECT 
   customer_name,
   SUM(total_purchase) OVER (PARTITION BY customer_country ORDER BY order_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM 
   customers_orders;
```

Dalam contoh di atas, kita menggunakan window function "SUM" untuk menghitung total pembelian pelanggan dalam setiap negara secara terurut berdasarkan tanggal pemesanan. Kita menggunakan klausa "PARTITION BY" untuk membagi data ke dalam grup berdasarkan negara pelanggan, dan "ORDER BY" untuk mengurutkan data berdasarkan tanggal pemesanan. Kemudian, dengan menggunakan "ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW", kita dapat menentukan rentang baris yang digunakan untuk menghitung total pembelian secara terakumulasi.

Penggunaan window function sangat berguna dalam menganalisis data dengan tingkat kompleksitas yang tinggi, dan dapat membantu menghasilkan hasil query yang lebih efektif dan efisien. Beberapa jenis window function lainnya yang sering digunakan dalam SQL termasuk "ROW_NUMBER", "RANK", "DENSE_RANK", "LEAD", dan "LAG".
