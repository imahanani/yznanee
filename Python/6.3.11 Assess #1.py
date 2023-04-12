Buat program yang bisa memeriksa apakah angka dari 2 hingga 100 merupakan bilangan prima

```py
#index python n hingga n(-1)
for x in range(2, 101):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                print(x, "bukan bilangan prima")
                break
        else:
            print(x, "adalah bilangan prima")
    else:
        print(x, "bukan bilangan prima")
```

STEP BY STEP

1. Pertama, kita menggunakan perulangan for untuk mengiterasi angka dari 2 hingga 100 dengan sintaks for x in range(2, 101):.

2. Setelah itu, kita menggunakan kondisi if x > 1: untuk mengecek apakah angka x lebih besar dari 1. Jika iya, maka program akan melanjutkan ke langkah 3. Jika tidak, maka program akan langsung keluar dari blok if dan mencetak "bukan bilangan prima" dengan menggunakan sintaks print(x, "bukan bilangan prima").

3. Di dalam blok if, kita menggunakan perulangan for lagi dengan sintaks for i in range(2, x): untuk mengiterasi angka dari 2 hingga angka sebelum x. Ini dilakukan untuk mengecek apakah ada bilangan selain 1 dan dirinya sendiri yang bisa membagi habis x.

4. Selanjutnya, kita menggunakan kondisi if (x % i) == 0: untuk mengecek apakah angka x bisa dibagi habis dengan bilangan i. Jika iya, maka artinya x bukan bilangan prima dan program akan langsung keluar dari blok if dengan menggunakan sintaks break. Jika tidak, maka program akan melanjutkan ke langkah 5.

5. Setelah perulangan for di dalam blok if selesai, kita menggunakan blok else dengan sintaks else: untuk mencetak "adalah bilangan prima" dengan menggunakan sintaks print(x, "adalah bilangan prima"). Blok else ini akan dijalankan jika perulangan for di dalam blok if selesai tanpa menemukan bilangan selain 1 dan dirinya sendiri yang bisa membagi habis x.

6. Jika kondisi if x > 1: pada langkah 2 tidak terpenuhi, maka program akan langsung keluar dari blok if dan mencetak "bukan bilangan prima" dengan menggunakan sintaks print(x, "bukan bilangan prima"). Ini dilakukan untuk menangani kasus ketika x kurang dari atau sama dengan 1.

Dengan langkah-langkah tersebut, program dapat mengecek apakah angka dari 2 hingga 100 adalah bilangan prima atau bukan.

