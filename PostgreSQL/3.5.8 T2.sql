Main Point: menggunakan query yang dapat memanipulasi data teks dan tanggal

Scenario:
Kamu bekerja sebagai credit data analyst di sebuah perusahaan fintech. Tim-mu tengah memformulasikan credit score dan kamu harus mengerjakan pekerjaan berikut:

1. Tampilkan total pinjaman yang telah diberikan ke setiap nasabah berdasarkan tahun di kolom origination_date.
2. Tampilkan total pinjaman yang telah diberikan pada nasabah dengan  peruntukan kebutuhan yang berkaitan dengan rumah, yang dapat kamu  temukan dari listing_title yang mengandung kata “home”

Yang perlu kamu lakukan:
1. Gunakan SUM pada kolom amount_borrowed dan EXTRACT tahun  dari kolom origination_date untuk mendapatkan tahun pinjaman. GROUP BY data berdasarkan tahun pinjaman.
2. Gunakan SUM pada kolom amount_borrowed, gunakan WHERE dan ILIKE untuk menyaring data hanya listing_title yang mengandung kata “home”

```All sql code
select sum(amount_borrowed)as total_borrowed, extract(year from origination_date) as year_borrowed
from lending_dataset
group by year_borrowed
--limit 10;

select sum(amount_borrowed)as total_borrowed --, listing_title
from lending_dataset
where listing_title ilike '%home%'
--group by listing_title
--limit 10;
/*select distinct listing_title
from lending_dataset;*/
```

----------------------technical explain
Q1
1. select sum(amount_borrowed)as total_borrowed, extract(year from origination_date) as year_borrowed: Perintah ini memilih dua kolom dari tabel lending_dataset, yaitu amount_borrowed dan origination_date. Kolom amount_borrowed akan dijumlahkan untuk setiap tahun pada kolom origination_date. Hasil penjumlahan tersebut akan ditampilkan sebagai kolom baru dengan nama total_borrowed. Selain itu, tahun pada kolom origination_date akan diekstrak dan ditampilkan sebagai kolom baru dengan nama year_borrowed.
2. from lending_dataset: Perintah ini menentukan bahwa sumber data yang digunakan adalah tabel lending_dataset.
3. group by year_borrowed: Perintah ini membagi hasil query ke dalam kelompok-kelompok berdasarkan nilai pada kolom year_borrowed.
4. --limit 10;: Tanda "--" menandakan bahwa ini adalah komentar dalam kode dan tidak akan dijalankan. Namun, jika tanda "--" dihapus maka query akan membatasi jumlah baris hasil query hanya sebanyak 10 baris.


Q2
1.select sum(amount_borrowed)as total_borrowed : Memilih kolom amount_borrowed dari tabel dan menjumlahkannya dengan menggunakan fungsi sum(), lalu memberikan alias total_borrowed untuk hasil penjumlahan tersebut.
2. from lending_dataset : Mengambil data dari tabel lending_dataset.
3. where listing_title ilike '%home%' : Memfilter data di mana kolom listing_title mengandung kata "home" dengan menggunakan operator ilike yang artinya pencarian kata "home" bersifat case-insensitive (tidak memperdulikan huruf besar atau kecil) dan % digunakan sebagai wildcard atau pengganti karakter apapun yang ada sebelum atau sesudah kata "home".
4. --group by listing_title : Komentar dalam kode yang menunjukkan bahwa seharusnya dilakukan pengelompokan data berdasarkan kolom listing_title, namun komentar ini di-ignore oleh server karena diawali dengan --.
5. --limit 10; : Komentar dalam kode yang menunjukkan bahwa seharusnya diambil hanya 10 baris data dari hasil query, namun komentar ini di-ignore oleh server karena diawali dengan --.

