LS041223_Bg | M3 | the_look_ecommerce.sql

```sql
count()
sum()
avg()
```
Join a.k.a inner join 

Count: menghitung jumlah data
SUM: total nilai

Count dan sum adalah dua operasi matematika dasar yang sering digunakan dalam analisis data. Perbedaan utama antara kedua operasi ini adalah:

Count: digunakan untuk menghitung jumlah data atau jumlah kemunculan dari suatu nilai dalam kumpulan data. Misalnya, jika Anda memiliki kumpulan data {1, 2, 3, 2, 4}, maka count dari nilai 2 adalah 2, karena nilai 2 muncul sebanyak 2 kali dalam kumpulan data tersebut.

Sum: digunakan untuk menambahkan semua nilai dalam kumpulan data. Misalnya, jika Anda memiliki kumpulan data {1, 2, 3, 2, 4}, maka jumlah dari semua nilai dalam kumpulan data tersebut adalah 12.

Dalam beberapa kasus, kedua operasi ini bisa digunakan bersamaan untuk memberikan informasi yang lebih lengkap. Misalnya, Anda dapat menghitung jumlah total pengeluaran dan jumlah transaksi dalam sebuah toko, yang dapat memberikan informasi yang berguna tentang rata-rata pengeluaran per transaksi.

========================================================

bedanya CAST, SPLIT_PART dan DATE_FORMAT?

CAST, SPLIT_PART, dan DATE_FORMAT adalah fungsi yang berbeda-beda yang digunakan dalam SQL.

CAST digunakan untuk mengonversi tipe data dari satu jenis ke jenis lain. Misalnya, jika Anda memiliki sebuah kolom dengan tipe data string yang berisi angka, Anda dapat menggunakan CAST untuk mengubahnya menjadi tipe data numerik.

Contoh penggunaan CAST:
```sql
SELECT CAST('123' AS INTEGER);
```
Output: 123

SPLIT_PART digunakan untuk memisahkan sebuah string menjadi beberapa bagian berdasarkan pemisah tertentu. Anda dapat mengambil bagian tertentu dari string tersebut menggunakan indeks.

Contoh penggunaan SPLIT_PART:
```sql
SELECT SPLIT_PART('John,Doe,31', ',', 1) AS first_name,
       SPLIT_PART('John,Doe,31', ',', 2) AS last_name,
       SPLIT_PART('John,Doe,31', ',', 3) AS age;
```

DATE_FORMAT digunakan untuk mengubah format tanggal dari satu format ke format lain. Anda dapat menggunakan format yang berbeda-beda, seperti 'YYYY-MM-DD', 'DD/MM/YYYY', atau 'MM/DD/YYYY'.

Contoh penggunaan DATE_FORMAT:
```sql
Output: (berupa dataFrame/tabel)

DATE_FORMAT digunakan untuk mengubah format tanggal dari satu format ke format lain. Anda dapat menggunakan format yang berbeda-beda, seperti 'YYYY-MM-DD', 'DD/MM/YYYY', atau 'MM/DD/YYYY'.

Contoh penggunaan DATE_FORMAT:
```sql
SELECT DATE_FORMAT('2021-09-30', '%d/%m/%Y') AS formatted_date;
```
Output: 30/09/2021

------------------------TO_CHAR
Fungsi TO_CHAR adalah sebuah fungsi dalam SQL yang digunakan untuk mengubah nilai data dalam bentuk tanggal, waktu, atau numerik menjadi sebuah string. Fungsi ini dapat digunakan untuk memformat tampilan data, menambahkan karakter khusus, atau menampilkan data dalam format yang spesifik.

Contoh penggunaan TO_CHAR:

1. Mengubah data numerik menjadi string:
```sql
SELECT TO_CHAR(1234.56, '9999.99') AS formatted_num;
```
Output: '1234.56'

2. Mengubah data tanggal menjadi string dalam format tertentu:
```sql
SELECT TO_CHAR('2021-09-30', 'DD/MM/YYYY') AS formatted_date;
```
Output: '30/09/2021'

3. Menambahkan karakter khusus pada data string:
```sql
SELECT TO_CHAR('John', 'FM99') AS formatted_string;
```
Output: 'John'

Dalam contoh di atas, karakter khusus 'FM' digunakan untuk menghapus karakter spasi yang biasanya muncul di depan string.


Source: https://www.postgresql.org/docs/current/functions-formatting.html

Q
