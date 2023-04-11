Menggunakan branching di dalam Python
```py
Generation_by_Age = {
    'Generation' : ['Gen Z','Millennials','Gen X','Boomers II (a/k/a Generation Jones)*','Boomers I*','Post War','WWII'],
    'Born' : ['1997-2012', '1981-1996', '1965-1980', '1955-1964', '1946-1954', '1928-1945', '1922-1927'],
    'Current Ages' : ['11-26', '17-42', '43-58', '59-68', '69-77', '78-95', '96-101'],   
}
Generation_by_Age
```
```py
import pandas as pd
# Membuat DataFrame
df_Generation_by_Age = pd.DataFrame(Generation_by_age)
# Menampilkan tabel
print("Generation_by_Age")
print(df_Generation_by_Age)
```
---------------------ERROR
```
Age = 31
if Age in '17-42':
    print('Generation', Millennial)
```
TypeError: 'in <string>' requires string as left operand, not int
  
ERROR MESSAGE tersebut mengindikasikan bahwa Anda mencoba untuk menggunakan operator 'in' pada sebuah nilai yang seharusnya berupa tipe data string, namun Anda malah memberikan nilai bertipe int (integer).
Contohnya, jika Anda menuliskan kode seperti ini:
```PY
x = 5
if x in 10:
    print("Nilai x ada dalam angka 10")
```
Maka akan muncul error yang sama dengan pesan: "TypeError: 'in <string>' requires string as left operand, not int". Karena operator 'in' memerlukan string sebagai operand kiri (left operand) dan bukan integer.
Untuk mengatasi error tersebut, pastikan Anda memberikan nilai yang sesuai dengan tipe data yang diharapkan oleh operator 'in'. Jika Anda ingin mencari nilai pada angka 10, maka Anda bisa menuliskan kode seperti ini:
```Py
x = 5
if x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print("Nilai x ada dalam angka 10")
```
Dalam contoh tersebut, kita membuat sebuah list dengan nilai 1 hingga 10, dan memeriksa apakah nilai x terdapat di dalam list tersebut.
=================================================================
Q1 Buat kondisi yang memenuhi semua kondisi dari tabel di atas untuk variabel “X”. jika tahun kelahiran tidak ada di dalam tabel, print “out of range” ?
```py

