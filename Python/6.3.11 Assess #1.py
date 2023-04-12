# Tugasmu adalah menulis program Python untuk melihat apakah suatu angka merupakan bilangan prima atau bukan. Buat program yang bisa memeriksa apakah angka dari 2 hingga 100 merupakan bilangan prima pada python

CARA PERTAMA. Berikut adalah program Python untuk memeriksa apakah angka dari 2 hingga 100 merupakan bilangan prima:
```py
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(2, 101):
    if is_prime(i):
        print(i, "adalah bilangan prima")
    else:
        print(i, "bukan bilangan prima")
```
# Program di atas menggunakan fungsi is_prime() untuk memeriksa apakah suatu angka bilangan prima atau bukan. Fungsi tersebut akan mengembalikan nilai True jika angka tersebut adalah bilangan prima, dan False jika bukan.
# Selanjutnya, program menggunakan perulangan for untuk memeriksa angka dari 2 hingga 100. Jika suatu angka merupakan bilangan prima, maka program akan mencetak "adalah bilangan prima", dan jika bukan, program akan mencetak "bukan bilangan prima".

CARA KEDUA. menggunakan if, elif, dan else untuk mengecek apakah suatu bilangan merupakan bilangan prima atau bukan. Berikut adalah contoh kode program Python yang menggunakan if, elif, dan else untuk mengecek bilangan prima dari 2 hingga 100:
```py
for num in range(2, 101):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "bukan bilangan prima")
                break
        else:
            print(num, "adalah bilangan prima")
    else:
        print(num, "bukan bilangan prima")
```
Pada program di atas, kita menggunakan perulangan for untuk mengiterasi angka dari 2 hingga 100. Kemudian, kita menggunakan if untuk mengecek apakah angka tersebut lebih besar dari 1, karena bilangan prima harus lebih besar dari 1. Jika angka tersebut lebih kecil atau sama dengan 1, maka kita langsung mengeluarkan output "bukan bilangan prima".

Selanjutnya, kita menggunakan perulangan for di dalam if untuk mengiterasi angka dari 2 hingga angka sebelumnya (num - 1). Jika kita menemukan bilangan yang bisa membagi habis angka tersebut, maka kita mengeluarkan output "bukan bilangan prima" dan keluar dari perulangan dengan break. Jika perulangan selesai tanpa mengeluarkan output, maka angka tersebut merupakan bilangan prima dan kita mengeluarkan output "adalah bilangan prima".

Terakhir, jika angka kurang dari atau sama dengan 1, maka kita langsung mengeluarkan output "bukan bilangan prima" tanpa melakukan pengecekan.
