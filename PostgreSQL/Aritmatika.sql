------------------------Apa itu aritmatika?
Aritmatika adalah cabang matematika yang berkaitan dengan operasi matematika dasar seperti penjumlahan, pengurangan, perkalian, dan pembagian. Aritmatika biasanya dipelajari pada tingkat pendidikan dasar dan menengah sebagai dasar untuk pemahaman matematika lebih lanjut.
Dalam aritmatika, kita menggunakan bilangan untuk melakukan operasi matematika dasar tersebut. Bilangan dapat berupa bilangan bulat, pecahan, atau desimal. Operasi aritmatika yang paling dasar adalah penjumlahan dan pengurangan, di mana dua bilangan atau lebih digabungkan atau dikurangi untuk mendapatkan jumlah atau selisihnya.

Selain itu, aritmatika juga melibatkan konsep seperti bilangan prima, faktorisasi, dan sifat-sifat bilangan. Aritmatika sangat penting dalam kehidupan sehari-hari karena digunakan dalam berbagai situasi, seperti pengukuran, perhitungan biaya, dan keuangan.

--------------------------Penerapan di SQL
Aritmatika juga dapat diterapkan dalam SQL (Structured Query Language) yang digunakan untuk mengelola database. SQL memiliki fungsi-fungsi matematika yang dapat digunakan untuk melakukan operasi aritmatika pada nilai-nilai numerik dalam tabel.

Berikut adalah beberapa contoh fungsi matematika dalam SQL dan cara menggunakannya:

- Fungsi SUM()
Fungsi SUM() digunakan untuk menjumlahkan nilai-nilai numerik dalam kolom. Contohnya:
```sql
SELECT SUM(harga) AS total_harga
FROM tabel_produk
```
-Fungsi AVG()
Fungsi AVG() digunakan untuk menghitung rata-rata nilai numerik dalam kolom. Contohnya:
```sql
SELECT AVG(harga) AS rata_harga
FROM tabel_produk
```
- Fungsi MIN() dan MAX()
Fungsi MIN() dan MAX() digunakan untuk menemukan nilai terkecil dan terbesar dalam kolom. Contohnya:
```sql
SELECT MIN(harga) AS harga_terendah, MAX(harga) AS harga_tertinggi
FROM tabel_produk
```
- Operasi aritmatika dasar
SQL juga mendukung operasi aritmatika dasar seperti penjumlahan (+), pengurangan (-), perkalian (*), dan pembagian (/). Contohnya:
```sql
SELECT harga * jumlah AS total_bayar
FROM tabel_penjualan
```

Dalam SQL, operasi aritmatika juga dapat dikombinasikan dengan fungsi-fungsi matematika untuk melakukan perhitungan yang lebih kompleks.
