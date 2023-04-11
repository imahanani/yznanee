Control Flow Statement pada Python

KONSEP BRACHING

Method 'if', satu kondisi
```py
n=85
if n>= 70: #kondisi terpenuhi
  print("Selamat! Anda Lulus")
MENGHASILKAN OUTPUT

n=61
if n>= 70: #kondisi terpenuhi
  print("Selamat! Anda Lulus")
  TIDAK MENGHASILKAN OUTPUT APAPUN
```

Method 'if else', dua kondisi
```py
n=85
if n>= 70:
  print("Selamat! Anda lulus")
else:
  print("Maaf, Anda belum lulus")
```

Method 'if, elif, else) u/ lebih dari 2 kondisi
```py
if n>=90:
    print("Nilai Anda A")
elif n>=80:
    print("Nilai Anda B")
elif n>=70:
    print("Nilai Anda C")
else:
    print("Maaf, Anda belum lulus")
```
    
LOOPING (FOR LOOP)
#for #while

```py
#list suhu dalam C
celcius = [25, 30, 35, 40, 45]
#konversi suhu dari C ke F
for x in celcius:
    fahrenheit = (x*9/5)+32
    print('='*20)
    print("Suhu dalam C:", x, "derajat")
    print("Suhu dalam F:", fahrenheit, "derajat")
```

CARA KEDUA, DISIMPAN KE VARIABEL BARU DENGAN FUNGSI "append"
```py
celcius = [25, 30, 35, 40, 45]
f = []
for x in celcius:
    convert = (x*9/5) + 32
    f.append(convert)
f
```

CARA KE3
```py
celcius = [25, 30, 35, 40, 45]
f = [(x*9/5) + 32 for x in celcius]
f
```

for LOOP + BRANCHING , jika input bernilai minus '-' (x absolut NOL), program muncul pesan 'error'

CARA PERTAMA
```py
celcius = [-400, -325, 0, 10, -5, 15]
f = []

for x in celcius:
    if x >= -273.15:
        convert = (x*9/5)+32
        f.append(convert)
    else:
        print("error: suhu (x) di bawah absolute nol")
f
```
CARA KEDUA
```py
celcius = [-400, -325, 0, 10, -5, 15]
f = [(x*9/5) + 32 for x in celcius if x >= -273.15]
f
```

WHILE LOOP while
```py
# i adalah nilai yang akan diulang
i = 1
while i <= 5:
    print(i)
    i += 1 
# tanda " +=" berfungsi menjumlahkan angka iterasi ke angka sebelumnya
```
WHILE LOOP + BRANCHING
```py
#menjumlahkan hanya bilangan genap.  %2 = 0










  
  
  
