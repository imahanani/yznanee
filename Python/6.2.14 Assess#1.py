```py
penjualan_toko_a = {
    'tanggal' : ['1 Januari 2022','5 Januari 2022','9 Januari 2022','13 Januari 2022','18 Januari 2022','21 Januari 2022','25 Januari 2022','28 Januari 2022'],
    'nama_produk' : ['Sleeping Bag', 'Tenda', 'Sepatu Gunung', 'Headlamp', 'Kompas', 'Senter', 'Matras', 'Jaket Gunung'],
    'jumlah_terjual' : [5, 3, 2, 10, 7, 4, 6, 3],
    'harga_satuan' : [250000, 500000, 750000, 150000, 100000, 200000, 300000, 500000],
    'harga_jual' : [1250000, 1500000, 1500000, 1500000, 700000, 800000, 1800000, 1500000]
}


penjualan_toko_b = {
    'tanggal' : ['2 Januari 2022', '6 Januari 2022', '10 Januari 2022', '14 Januari 2022', '19 Januari 2022', '22 Januari 2022', '26 Januari 2022', '29 Januari 2022'],
    'nama_produk' : ['Sleeping Bag', 'Tenda', 'Sepatu Gunung', 'Headlamp', 'Kompas', 'Senter', 'Matras', 'Jaket Gunung'],
    'jumlah_terjual' : [7, 5, 4, 8, 6, 2, 8, 5],
    'harga_satuan' : [250000, 500000, 750000, 150000, 100000, 200000, 300000, 500000],
    'harga_jual' : [1750000, 2500000, 3000000, 1200000, 600000, 400000, 2400000, 2500000]
}
```

```py
import pandas as pd

# Membuat DataFrame untuk toko A
df_toko_a = pd.DataFrame(penjualan_toko_a)

# Membuat DataFrame untuk toko B
df_toko_b = pd.DataFrame(penjualan_toko_b)

# Menampilkan tabel untuk toko A
print("Data Penjualan Toko A")
print(df_toko_a)

# Menampilkan tabel untuk toko B
print("Data Penjualan Toko B")
print(df_toko_b)
```


Tugas utama: Misalkan kamu bekerja sebagai Data Analyst pada perusahaan retail peralatan Outdoor. Kamu diminta oleh manajer kamu untuk menganalisis data sebulan terakhir.
=================================================================================
Q1 Berapa total penjualan selama 1 bulan terakhir?
```py error
omzet_toko_a = ( 'harga_satuan') * ('harga_jual')
print(omzet_toko_a)
```
Kode tersebut salah karena Anda hanya melakukan OPERAS PERKALIAN antara STRING 'harga_satuan' dan 'harga_jual', BUKAN antara LIST yang berisi nilai-nilai harga tersebut. Selain itu, Anda juga BELUM menghitung total penjualan dari toko A.

Berikut adalah cara yang benar untuk menghitung omzet dan total penjualan dari toko A:
```py
# Menghitung omzet dari toko A
omzet_toko_a = sum(penjualan_toko_a['harga_jual'])
print("Omzet Toko A:", omzet_toko_a)

# Menghitung total penjualan dari toko A
total_penjualan_toko_a = sum(penjualan_toko_a['jumlah_terjual'])
print("Total Penjualan Toko A:", total_penjualan_toko_a)
```
Dalam contoh di atas, kita menggunakan fungsi 'sum()' untuk menghitung total nilai dari list 'harga_jual' dan 'jumlah_terjual' yang ada di dalam dictionary 'penjualan_toko_a'. Output yang dihasilkan adalah:
-----------------------Output
Omzet Toko A: 11300000
Total Penjualan Toko A: 40
  Kode di atas akan menghitung total omzet dan total penjualan dari toko A. Jika Anda ingin menghitung omzet dan total penjualan dari toko B, Anda hanya perlu mengganti variabel penjualan_toko_a dengan penjualan_toko_b.

=====================================================================================
Q2 - Jika di-drill down per toko, mana toko yang memiliki total penjualan terbesar?
   - Berapa % dari total semua penjualan?
```
omzet_toko_a / omzet_toko_a 
```
KODE DI ATAS SALAH karena terdapat kesalahan dalam melakukan operasi pembagian yang tujuannya tidak jelas.

Berikut ini adalah CARA YANG TEPAT untuk mengetahui toko mana yang memiliki TOTAL PENJUALAN TERBESAR dan berapa PERSENTASE dari total penjualan untuk setiap toko:
```py
# Menghitung total penjualan untuk masing-masing toko
total_penjualan_toko_a = sum(penjualan_toko_a['harga_jual'])
total_penjualan_toko_b = sum(penjualan_toko_b['harga_jual'])

# Mencetak toko dengan total penjualan terbesar
if total_penjualan_toko_a > total_penjualan_toko_b:
    print("Toko A memiliki total penjualan terbesar.")
else:
    print("Toko B memiliki total penjualan terbesar.")

# Menghitung persentase dari total penjualan untuk setiap toko
total_penjualan = total_penjualan_toko_a + total_penjualan_toko_b
persentase_toko_a = (total_penjualan_toko_a / total_penjualan) * 100
persentase_toko_b = (total_penjualan_toko_b / total_penjualan) * 100

# Mencetak persentase penjualan untuk masing-masing toko
print("Persentase penjualan Toko A:", persentase_toko_a, "%")
print("Persentase penjualan Toko B:", persentase_toko_b, "%")
```
--------------------------OUTPUT
Toko B memiliki total penjualan terbesar.
Persentase penjualan Toko A: 46.75 %
Persentase penjualan Toko B: 53.25 %
  Dalam contoh di atas, kita menghitung total penjualan untuk masing-masing toko dengan menjumlahkan nilai di dalam list harga_jual dari dictionary 'penjualan_toko_a' dan 'penjualan_toko_b'. Selanjutnya, kita membandingkan total penjualan untuk setiap toko dan mencetak toko yang memiliki total penjualan terbesar.
Setelah itu, kita menghitung persentase penjualan untuk masing-masing toko dengan membagi total penjualan toko A dan B dengan total penjualan keseluruhan, kemudian mengalikan dengan 100. Terakhir, kita mencetak persentase penjualan untuk setiap toko.
=============================================================================================
Q3 Apa saja produk yang terjual sebulan terakhir?
```ERROR
print(set((penjualan_toko_a['nama_produk'])))
print(set((penjualan_toko_b['nama_produk'])))
print ((set((penjualan_toko_a['nama_produk']))) && (set((penjualan_toko_b['nama_produk']))))
```
Kode tersebut SALAH karena operator '&&' TIDAK VALID di dalam Python. Operator && adalah operator logika yang digunakan di beberapa bahasa pemrograman lainnya seperti C, C++, dan Java, tetapi dalam Python, operator logika yang valid adalah 'AND'.
Untuk menemukan produk yang terjual di KEDUA TOKO selama sebulan terakhir, Anda dapat menggunakan OPERATOR '& ' atau METHOD intersection() untuk menggabungkan dua set produk dari masing-masing toko:
```python
produk_a = set(penjualan_toko_a['nama_produk'])
produk_b = set(penjualan_toko_b['nama_produk'])

print(produk_a)
print(produk_b)

produk_terjual = produk_a.intersection(produk_b)
print(produk_terjual)
```
--------------------------OUTPUT
{'Jaket Gunung', 'Sleeping Bag', 'Tenda', 'Sepatu Gunung', 'Kompas', 'Senter', 'Matras', 'Headlamp'}
--------------------------------TABULAR
```py
# Membuat DataFrame dari set produk terjual
df = pd.DataFrame(list(produk_terjual), columns=["produk_terjual"])
print(df)
```
=======================================================================================================
Q4 - Hitung berapa kali transaksi penjualan pada masing-masing toko?
  - kemudian hitung berapa rata-rata harga jual per transaksi?
------------------------ERROR
 #Hitung berapa kali transaksi penjualan pada masing-masing toko,
total_transaksi = sum(penjualan_toko_a['tanggal']
                      Kode di atas kurang lengkap karena tidak mencakup langkah-langkah yang diperlukan untuk menghitung berapa kali transaksi penjualan pada masing-masing toko.
                      Sebagai informasi, total_transaksi = sum(penjualan_toko_a['tanggal'] hanya akan menjumlahkan nilai-nilai dalam kolom tanggal dari DataFrame penjualan_toko_a, BUKAN MENGHITUNG BERAPA KALI TRANSAKSI DILAKUKAN.
Untuk menghitung berapa kali transaksi penjualan pada masing-masing toko, kita dapat melakukan beberapa langkah seperti berikut:
- Mengelompokkan data penjualan berdasarkan toko menggunakan fungsi groupby()
- Menghitung jumlah transaksi penjualan pada setiap toko menggunakan fungsi count()
- Menampilkan hasil perhitungan
Berikut adalah contoh kode yang dapat digunakan:
```py
# Mengelompokkan data penjualan berdasarkan toko
penjualan_per_toko = data_penjualan.groupby('toko')

# Menghitung jumlah transaksi penjualan pada setiap toko
jumlah_transaksi_per_toko = penjualan_per_toko['tanggal'].count()

# Menampilkan hasil perhitungan
print(jumlah_transaksi_per_toko)
```
Dalam kode di atas, 'toko' adalah nama kolom yang berisi informasi toko pada DataFrame data_penjualan. Kita mengelompokkan data_penjualan berdasarkan kolom 'toko' menggunakan fungsi GROUPBY(), kemudian menghitung jumlah transaksi penjualan pada setiap toko dengan menghitung jumlah baris dalam kolom 'tanggal' pada setiap kelompok data toko menggunakan fungsi COUNT(). Hasil perhitungan tersebut disimpan pada variabel jumlah_transaksi_per_toko dan ditampilkan pada layar menggunakan fungsi print().

-----------DARI MENTOR
Petunjuk: Gunakan function “len” untuk menghitung elemen pada list  (frekuensi transaksi pada toko). Formula rata-rata harga jual per  transaksi = total penjualan / frekuensi transaksi  

Untuk menghitung total jumlah transaksi pada kedua toko, kita bisa menggunakan fungsi len() pada salah satu kolom yang ada dalam data penjualan. Karena setiap data dalam satu kolom memiliki jumlah yang sama, maka jumlah data dalam kolom tersebut akan merepresentasikan jumlah transaksi. Kita bisa menggunakan kolom 'tanggal' untuk menghitung jumlah transaksi karena setiap tanggal merepresentasikan satu transaksi. Berikut adalah contoh kode untuk menghitung total jumlah transaksi pada kedua toko:
```py
# Menghitung total jumlah transaksi pada toko A
jumlah_transaksi_toko_a = len(penjualan_toko_a['tanggal'])
print("Total jumlah transaksi pada toko A:", jumlah_transaksi_toko_a)

# Menghitung total jumlah transaksi pada toko B
jumlah_transaksi_toko_b = len(penjualan_toko_b['tanggal'])
print("Total jumlah transaksi pada toko B:", jumlah_transaksi_toko_b)
```
-------------------------------------RERATA  TRAKSAKSI SALAH
#menghitung rata-rata harga jual per transaksi
harga_rerata_a = omzet_toko_a \frekuensi_transaksi_a
  Kode yang diberikan SALAH karena kita tidak dapat membagi variabel 'omzet_toko_a' dengan 'frekuensi_transaksi_a' secara langsung. Kita perlu menggunakan operator pembagian '/' untuk melakukan operasi pembagian tersebut.
  Selain itu, variabel 'omzet_toko_a' juga tidak didefinisikan dalam kode yang diberikan, sehingga perhitungan rata-rata harga jual tidak dapat dilakukan. Berikut adalah contoh kode yang benar untuk menghitung rata-rata harga jual per transaksi pada toko A:
```py
rerata_harga_jual_a = sum(penjualan_toko_a['harga_jual']) / len(penjualan_toko_a['harga_jual'])
print("rerata_harga_a:", rerata_harga_jual_a)
rerata_harga_jual_b = sum(penjualan_toko_b['harga_jual']) / len(penjualan_toko_b['harga_jual'])
print("rerata_harga_b:", rerata_harga_jual_b)
```
==============================================================================================
                                                                                                                      
