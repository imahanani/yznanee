Menggunakan branching di dalam Python
# LINE 1
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
Q1 Buat kondisi yang memenuhi semua kondisi dari tabel di atas untuk variabel “X”. jika tahun kelahiran tidak ada di dalam tabel, print “out of range”? 
#if elif else (method)
```py
tahun_lahir = '2001'
tahun_lahir = int(2001) # konversi tahun_lahir menjadi integer
if tahun_lahir in range(1997, 2013):
print("Anda termasuk dalam generasi Gen Z dengan rentang usia 11-26")
elif tahun_lahir in range(1981, 1997):
print("Anda termasuk dalam generasi Millennials dengan rentang usia 17-42")
elif tahun_lahir in range(1965, 1981):
print("Anda termasuk dalam generasi Gen X dengan rentang usia 43-58")
elif tahun_lahir in range(1955, 1965):
print("Anda termasuk dalam generasi Boomers II (a/k/a Generation Jones)* dengan rentang usia 59-68")
elif tahun_lahir in range(1946, 1955):
print("Anda termasuk dalam generasi Boomers I* dengan rentang usia 69-77")
elif tahun_lahir in range(1928, 1946):
print("Anda termasuk dalam generasi Post War dengan rentang usia 78-95")
elif tahun_lahir in range(1922, 1928):
print("Anda termasuk dalam generasi WWII dengan rentang usia 96-101")
else:
print("out of range")
``` 
#HASIL MASIH ERROR
 File"C:\Users[USERNAME]\AppData\Local\Temp\ipykernel_9648\1316560416.py", line 4
    print("Anda termasuk dalam generasi Gen Z dengan rentang usia 11-26")
    ^
IndentationError: expected an indented block

MENTOR : sama ini ada tambahan, di line 2 bisa diganti `tahun_lahir = int(tahun_lahir)`
```py
tahun_lahir = '2001'
tahun_lahir = int(tahun_lahir) # konversi tahun_lahir menjadi integer
```

MASIH SALAH
```
if x in range (1997, 2013):
    print("Anda Gen Z usia 11-26")
    elif x in range (1981, 1997):
        print("Anda Gen Millennials usia 17-42")
        elif x in range (1965, 1981):
            print("Anda GenX usia 43-58")
            elif x in range (1955, 1965):
                print("Anda  Boomers II (a/k/a Gen Jones)* usia 59-68)
                      elif x in range (1946, 1955):
                      print("Anda Gen Boomers I* usia 69-77")
                      elif x in range (1928, 1946):
                      print("Anda Gen Post War usia 78-95")
                      elif x in range (1922,1928):
                      print("Anda Gen WWII usia 96-101")
                      else:
                      print("out of range")
```
Beberapa kesalahan yang diperbaiki adalah:

Menambahkan variabel x untuk menentukan usia yang ingin dikategorikan.
Menghapus spasi ekstra di dalam fungsi range().
Menambahkan spasi setelah elif pada baris ke-3 dan setelah print() pada baris ke-7 hingga ke-13.
Menambahkan tanda kutip pada string pada baris ke-7 dan ke-9.
Menambahkan tanda kurung kurawal pada string pada baris ke-7 dan ke-9.
Menambahkan tanda kurung pada baris ke-10 hingga ke-18.
Menambahkan spasi pada baris ke-10 hingga ke-18.
Menambahkan : pada baris ke-10 hingga ke-18.
Menambahkan indentasi pada setiap baris yang berada di dalam blok percabangan if-elif-else.
Menambahkan string out of range pada blok else.
                      
SETELAH PERBAIKAN KODE
                      
```PY
                      x = # usia Anda

if x in range(1997, 2013):
    print("Anda Gen Z usia 11-26")
elif x in range(1981, 1997):
    print("Anda Gen Millennials usia 27-42")
elif x in range(1965, 1981):
    print("Anda GenX usia 43-58")
elif x in range(1955, 1965):
    print("Anda Boomers II (a/k/a Gen Jones)* usia 59-68")
elif x in range(1946, 1955):
    print("Anda Gen Boomers I* usia 69-77")
elif x in range(1928, 1946):
    print("Anda Gen Post War usia 78-95")
elif x in range(1922, 1928):
    print("Anda Gen WWII usia 96-101")
else:
    print("out of range")
```
#OUTPUT SUDAH SESUAI HARAPAN "Anda Gen Z usia 11-26"

==================================================================
ERROR LAGIIII
```py
                      x = 1925
if x > 1922 and x <= 1927:
    print("WWII")
    elif x > 1928 and x <= 1945:
        print("Post War")
        elif x > 1945 and x <= 1954:
            print("Boomer I")
            elif x > 1954 and <=1964:
                print("Boomer II")
                elif x > 1965 and <= 1980:
                    print("Gen X")
                    elif x > 1980 <= 1996:
                        print("Millennials")
                        elif x > 1996 and <= 2012:
                            print(Gen Z)
                            else:
                                print(out of range)
```
There are TWO SYNTAX ERRORS in the code:
- The indentation is incorrect. The elif statements should be aligned with the if statement, not with the print statements.
- The print statement for "Gen Z" is missing quotes around the string.

CARA KEDUA YANG BENAR
```py
                      x = 1925
if x > 1922 and x <= 1927:
    print("WWII")
elif x > 1928 and x <= 1945:
    print("Post War")
elif x > 1945 and x <= 1954:
    print("Boomer I")
elif x > 1954 and x <= 1964:
    print("Boomer II")
elif x > 1965 and x <= 1980:
    print("Gen X")
elif x > 1980 and x <= 1996:
    print("Millennials")
elif x > 1996 and x <= 2012:
    print("Gen Z")
else:
    print("out of range")
```
#output : WWII                      
                      
                      
                      
                      
