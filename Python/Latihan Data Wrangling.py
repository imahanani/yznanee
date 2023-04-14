Latihan Data Wrangling
Setelah merengkuh semua teori yang ada, kini saatnya kita praktik! Pada materi ini, kita akan belajar penerapan data wrangling dalam sebuah proyek analisis data sederhana.

Pada contoh proyek ini, kita akan menggunakan dataset DicodingCollection. Ia merupakan hasil modifikasi dari dataset Shopping Cart Database yang dipublikasi dalam platform kaggle. Proses modifikasi ini bertujuan untuk memastikan dataset yang digunakan cukup merepresentasikan semua masalah yang umum dijumpai di industri.

Sebagai permulaan, mari kita simak background story dari proyek ini.

Peringatan! 

Skenario dalam materi ini hanyalah fiktif belaka. Apabila terdapat kesamaan nama tokoh, perusahaan, ataupun produk, itu adalah kebetulan semata dan tidak ada unsur kesengajaan.



Background
Dicoding Collection atau sering disingkat DiCo merupakan sebuah perusahaan yang bergerak di bidang fashion. Ia memproduksi berbagai item fashion dan menjualnya melalui platform online. 

dos:1c183d6627f771f902fa1c5a86de6b2420230309133244.png

Sebagai perusahaan kekinian, DiCo menyadari betapa pentingnya data bagi perkembangan sebuah bisnis. Oleh karena itu, ia menyimpan semua history penjualan beserta informasi terkait produk dan customers dalam sebuah database. Database ini terdiri dari empat buah tabel, antara lain customers, orders, products, dan sales. 

Tabel customers: tabel ini menyimpan berbagai informasi terkait customer, seperti customer_id, customer_name, gender, age, home_address, zip_code, city, state, dan country.
Tabel orders: tabel ini menyimpan berbagai informasi terkait sebuah order yang terdiri dari order_id, customer_id, order_date, dan delivery_date.
Tabel products: tabel ini berisi berbagai informasi terkait sebuah produk, seperti product_id, product_type, product_name, size, colour, price, quantity, dan description.
Tabel sales: tabel ini mengandung informasi detail terkait penjualan, seperti sales_id, order_id, product_id, price_per_unit, quantity, dan total_price.
Nah, sebagai calon praktisi data profesional, Anda akan diminta untuk menganalisis seluruh data tersebut. So, apakah Anda siap untuk menjawab tantangan ini? Tentunya siap dong!


Tujuan
First of all, kita akan mulai proyek analisis data ini dengan menjalankan proses data wrangling terlebih dahulu. Proses ini memiliki tujuan antara lain

mengumpulkan seluruh data yang dibutuhkan;
menilai kualitas dari data yang telah dikumpulkan; dan
membersihkan data tersebut sehingga siap untuk dianalisis.


Alur Latihan
Berikut merupakan tahapan dalam latihan ini.

Tahap persiapan.
Tahap gathering data.
Tahap assessing data.
Tahap cleaning data.
Sudah siap? Yuk, kita mulai!



Persiapan
Sebelum mulai mengerjakan suatu proyek, terdapat beberapa hal yang harus disiapkan terlebih dahulu.

Pertama, siapkan environment untuk menjalankan proyek ini. Pada proyek latihan ini, Anda dapat menggunakan berbagai IDE seperti Jupyter Notebook atau Google Colaboratory (Google Colab). Jika menjalankan latihan ini melalui Jupyter Notebook, pastikan Anda telah menginstal seluruh library yang dibutuhkan, seperti numpy, pandas, scipy, matplotlib, dan seaborn.
Saran
Kami sangat menyarankan Anda untuk selalu membuat virtualenv baru pada setiap proyek. Hal ini untuk meminimalisasi masalah yang berhubungan dengan dependency pada library yang akan digunakan.

Membuat virtual environment menggunakan conda
Apabila menginstal Python melalui Anaconda ataupun miniconda, Anda dapat menggunakan conda sebagai package manager dan environment management system. Berikut merupakan tahapan dalam membuat virtual environment menggunakan conda.
1. 

Buka terminal atau PowerShell.

2.

Jalankan perintah berikut.

conda create --name main-ds python=3.9

3.

Aktifkan virtual environment dengan menjalankan perintah berikut.

conda activate main-ds

4.

Instal semua library yang dibutuhkan menggunakan perintah berikut.

pip install numpy pandas scipy matplotlib seaborn jupyter

5.

Buka jupyter-notebook dengan menjalankan perintah berikut.

jupyter-notebook .

6.

Buat sebuah folder baru bernama proyek_analisis_data. Folder tersebut akan menjadi directory utama dalam proyek ini. 

Membuat virtual environment menggunakan pipenv
Jika menginstal python melalui official home, Anda dapat menggunakan pip sebagai package manager dan pipenv sebagai environment management. Berikut merupakan tahapan dalam membuat virtual environment menggunakan pipenv.
1.

Buka terminal atau PowerShell.

2.

Buat sebuah folder baru bernama proyek_analisis_data dengan menjalankan perintah berikut.

mkdir proyek_analisis_data

3. 

Pindah ke folder terbaru tersebut menggunakan perintah berikut.

cd proyek_analisis_data

4.

Buat sebuah virtual environment dengan menjalankan perintah berikut.

pipenv install

5.

Aktifkan virtual environment dengan menjalankan perintah berikut.

pipenv shell

6.

Instal semua library yang dibutuhkan menggunakan perintah berikut.

pip install numpy pandas scipy matplotlib seaborn jupyter

7.

Buka jupyter-notebook dengan menjalankan perintah berikut.

jupyter-notebook .

Buat sebuah berkas baru bernama notebook.ipynb. Pada berkas inilah, seluruh proses analisis data akan dikerjakan.
Buka berkas notebook.ipynb.
Untuk memulai pengerjaan proyek ini, kita perlu memanggil semua library yang dibutuhkan. Berikut merupakan kode untuk melakukannya.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
Last but not least, siapkan sebuah camilan sebagai suplai energi selama mengikuti latihan ini.


Gathering Data
Setelah tahap persiapan selesai, kita bisa masuk ke tahap gathering data. Pada tahap ini, kita akan mengumpulkan semua data yang dibutuhkan. Beruntungnya data yang kita butuhkan telah tersedia dalam repository dataset Dicoding yang dapat diakses melalui tautan berikut: Dicoding Collection. 

Catatan:

Pada praktik yang umum dijumpai di industri, seluruh data tersebut diperoleh dari proses query database. Proses query ini umumnya dijalankan menggunakan perintah SQL. 

Seperti yang telah kita bahas sebelumnya, pada proyek latihan ini data yang akan kita gunakan terdiri dari 4 tabel. Oleh karena itu, pada tahap ini kita akan memuat (load) keempat tabel tersebut.

Memuat tabel customers
Data pertama yang harus kita muat ialah data dari tabel customers. Berikut merupakan kode untuk memuat tabel tersebut menjadi sebuah DataFrame.
customers_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/customers.csv")
customers_df.head()
Kode di atas akan menampilkan 5 baris pertama dari DataFrame customers_df seperti pada gambar di bawah ini.

dos:c19fd41f6ebdcd74875c289fb9818aa820230220172738.jpeg

Load tabel orders
Data selanjutnya yang harus kita muat ialah data dari tabel orders. Hal ini dapat dilakukan dengan menjalankan kode berikut.
orders_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/orders.csv")
orders_df.head()
Selain memuat tabel orders menjadi sebuah DataFrame, kode di atas juga akan menampilkan 5 baris pertama dari Dataframe tersebut.
dos:8032c58062e45a9492506ea32cf2ecc120230220172737.jpeg

Memuat tabel product
Tabel berikutnya yang harus kita muat ialah tabel product. Berikut merupakan kode yang dapat digunakan untuk membuat tabel product menjadi sebuah DataFrame bernama product_df.
product_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/products.csv")
product_df.head()
Kode di atas juga akan menampilkan lima baris pertama dari product_df.
dos:3cdae9acec30d05128693028c38f74cb20230220172738.jpeg

Load tabel sales
Last but not least, tabel terakhir yang harus kita muat ialah tabel sales. Berikut merupakan contoh kode untuk melakukannya.
sales_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/sales.csv")
sales_df.head()
Contoh kode di atas akan menghasilkan sebuah DataFrame bernama sales_df. Selain itu, ia juga akan menampilkan lima baris pertama dari DataFrame tersebut.
dos:362e67d61bcdc6a8b10e026a3f5a111b20230220172737.jpeg   
Oke, sekarang kita telah berhasil memuat semua data yang dibutuhkan. Tahap selanjutnya ialah menilai kualitas dari data tersebut.



Assessing Data
Sekarang kita masuk ke tahap kedua dalam proses data wrangling yaitu assessing data. Seperti yang telah kita bahas sebelumnya, pada proses ini kita akan menilai kualitas dari seluruh data yang akan digunakan. Penilaian ini bertujuan untuk melihat berbagai permasalahan yang ada dalam data tersebut.



Menilai Data customers_df
Data pertama yang akan kita nilai adalah customers_df. Sebagai permulaan, kita memeriksa tipe data data dari tiap kolom yang terdapat dalam customers_df. Proses ini dapat dilakukan menggunakan method info() seperti contoh kode berikut.

customers_df.info()
Kode di atas akan menampilkan informasi seperti gambar di bawah ini.

dos:19cae7214b45f20d40096e66e6bfc6ff20230221090151.png

Jika Anda perhatikan, tidak ada masalah dengan tipe data dari seluruh kolom tersebut. Akan tetapi, terdapat sedikit perbedaan pada jumlah data pada kolom gender. Hal ini menunjukkan adanya missing values pada kolom gender. Nah, untuk memastikan hal ini, jalankan kode berikut.

customers_df.isna().sum()
Kode di atas akan menampilkan informasi terkait jumlah missing values yang terdapat dalam setiap kolom seperti gambar berikut.

dos:aabacf58258cbbbf79b4c6529391c36920230221090250.png

Nah, gambar di atas menunjukkan bahwa terdapat 18 missing values pada kolom gender. Hal ini akan kita tangani pada tahap data cleaning nanti.

Masalah selanjutnya yang harus kita periksa ialah duplikasi data. Untuk memeriksa hal ini, kita bisa menjalankan kode berikut.

print("Jumlah duplikasi: ", customers_df.duplicated().sum())
Ketika menjalankan kode di atas, Anda akan menemukan bahwa terdapat 6 data yang terduplikat. Pada tahap data cleaning nanti, kita akan menghilangkan semua duplikasi tersebut.

Sekarang kita memeriksa parameter statistik dari kolom numerik yang terdapat dalam customers_df. Untuk mempermudah pemeriksaan, kita akan menggunakan method describe(). Method tersebut akan menampilkan ringkasan parameter statistik (mean, median, dll.) dari kolom numerik pada sebuah DataFrame. Berikut merupakan contoh penggunaannya.

customers_df.describe()
Kode di atas akan menampilkan ringkasan parameter statistik seperti berikut.

dos:8072626fabff9ea10312ddc90a6b693020230221090535.png

Jika diperhatikan, terdapat keanehan pada nilai maksimum yang terdapat pada kolom age. Ini kemungkinan besar terjadi karena adanya inaccurate value pada kolom tersebut. Masalah ini juga akan kita bersihkan dalam tahap cleaning data.



Menilai Data orders_df
Oke, selanjutnya kita akan menilai data pada orders_df. Seperti biasa, kita akan mulai dengan memeriksa tipe data dari tiap kolom menggunakan method info().

orders_df.info()
Berikut merupakan tampilan hasil yang diperoleh dari kode di atas.

dos:ac6782d702425299e5f585ab9b199f6f20230221090602.png

Jika Anda perhatikan, jumlah data pada orders_df telah lengkap atau dengan kata lain tidak ada missing value di dalamnya. Akan tetapi, terdapat kesalahan tipe data untuk kolom order_date & delivery_date. Kedua kolom tersebut harusnya direpresentasikan sebagai tipe data datetime, bukan object (ini digunakan untuk tipe data string).

Berikutnya, kita perlu memeriksa duplikasi dan ringkasan parameter statistik dari kolom numerik pada orders_df. Proses ini dilakukan dengan menjalankan kode berikut.

print("Jumlah duplikasi: ",orders_df.duplicated().sum())
orders_df.describe()
Berikut merupakan hasil yang diperoleh dari kode di atas.

dos:8e65e47bbf8ea688a388f19a40689f8820230221090653.png

Jika diperhatikan, tidak ada keanehan pada hasil tersebut. Ini menunjukkan tidak terdapat duplikasi dan keanehan nilai pada orders_df. 



Menilai Data product_df
Selanjutnya, kita akan menilai data pada product_df. Pertama, gunakan method info() untuk memastikan tipe data tiap kolom dalam product_df telah sesuai.

product_df.info()
Berikut merupakan output dari kode di atas.

dos:8aff3d11f9862f0c181cd15c76f4ffd920230221091929.png

Berdasarkan hasil tersebut, dapat disimpulkan bahwa tidak terdapat masalah pada tipe data tiap kolom dalam product_df.  Selain itu, jumlah datanya juga telah lengkap sehingga tidak ada missing value di dalamnya.

Hal berikutnya yang harus diperiksa ialah duplikasi dan ringkasan parameter statistik dari product_df. Berikut merupakan kode untuk melakukannya.

print("Jumlah duplikasi: ", product_df.duplicated().sum())
 
product_df.describe()
Kode di atas akan menghasilkan tampilan berikut. 

dos:de63315da1f2c7d964aad95fa76c542520230221092156.png

Berdasarkan gambar di atas, dapat dilihat bahwa terdapat 6 data yang terduplikasi pada product_df. Pada tahap cleaning data, kita akan menghapus duplikasi tersebut.



Menilai Data sales_df
Data terakhir yang harus kita nilai ialah sales_df. Sebagai permulaan, gunakan method info() untuk memeriksa tipe data dan jumlah data yang ada di dalam sales_df.

sales_df.info()
Berikut merupakan tampilan informasi yang diperoleh dari kode di atas.

dos:29ff78724a26e12c0f30612e6eb11abd20230221092927.png

Berdasarkan hasil di atas, tidak ada masalah pada tipe data tiap kolom dalam sales_df. Namun, terdapat keanehan pada jumlah data pada kolom total_price. Hal ini menunjukkan adanya missing value pada kolom tersebut. Untuk memastikannya, kita bisa menjalankan kode berikut.

sales_df.isna().sum()
Kode di atas akan menunjukkan jumlah missing value dari setiap kolom dalam sales_df. Berikut merupakan hasil yang kita peroleh.

dos:bacec396959a8aadba2074c8bb43fec920230221093037.png

Berdasarkan hasil di atas, dapat disimpulkan bahwa terdapat 19 missing value pada kolom total_price. Hal ini akan kita bersihkan pada tahap cleaning data.

Tahap selanjutnya ialah memeriksa duplikasi dan ringkasan parameter statistik dari sales_df. Berikut merupakan contoh kode untuk melakukannya.

print("Jumlah duplikasi: ", sales_df.duplicated().sum())
sales_df.describe()
Hasil keluaran dari kode di atas dapat Anda lihat di bawah ini.

dos:17b4e3c00e317bf4a09ced21f8a2204620230221093153.png

Hasil di atas menunjukkan bahwa tidak ada duplikasi pada slaes_df. Selain itu, ia juga menunjukkan tidak terdapat keanehan dalam ringkasan parameter statistik dari sales_df.

Oke, sampai tahap ini, kita telah berhasil mengidentifikasi berbagai masalah pada data yang telah kita kumpulkan. Berikut merupakan rangkumannya.


Tipe data

Missing value

Duplicate data

Inaccurate value

customer_df

-

Terdapat 18 missing values pada kolom gender.

Terdapat 6 data yang duplikat.

Terdapat inaccurate value pada kolom age.

orders_df

Terdapat kesalahan tipe data untuk kolom order_date & delivery_date.

-

-

-

product_df

-

-

Terdapat 6 data yang duplikat.

-

sales_df

-

Terdapat 19 missing value pada kolom total_price.

-

-



Cleaning Data
Nah, sekarang kita akan memasuki proses terakhir dalam data wrangling yaitu pembersihan atau cleaning data. Pada tahap ini, kita akan membersihkan berbagai masalah yang telah teridentifikasi dalam proses assessing data.



Membersihkan Data customers_df
Berdasarkan hasil proses assessing data, diketahui bahwa terdapat tiga masalah yang dijumpai dalam customer_df, yaitu duplicate data, missing value, dan inaccurate value. Pada tahap ini, kita akan membersihkan ketiga masalah tersebut.

Menghilangkan duplicate data
Masalah pertama yang akan kita tangani ialah duplicate data. Seperti yang telah kita pelajari sebelumnya, ketika menemukan duplikasi pada data, kita harus menghilangkan atau menghapus duplikasi tersebut. Nah, untuk melakukan hal ini, kita dapat memanfaatkan method drop_duplicates(). Berikut merupakan kode untuk menghapus duplikasi pada customer_df.
customers_df.drop_duplicates(inplace=True)
Setelah menjalankan kode di atas, periksa kembali apakah masih terdapat duplikasi pada data tersebut dengan menjalankan kode berikut.
print("Jumlah duplikasi: ", customers_df.duplicated().sum())
Jika proses penghapusan duplikasi berjalan lancar, kode di atas akan menghasilkan keluaran yang menunjukkan tidak adanya duplikasi pada customers_df.

Menangani missing value
Masalah berikutnya yang harus kita tangani ialah missing value pada kolom gender. Nah, secara umum terdapat tiga metode untuk mengatasi missing value yaitu dropping, imputation, dan interpolation. Untuk menentukan metode mana yang akan digunakan, kita perlu melihat data yang mengandung missing value tersebut menggunakan teknik filtering seperti berikut.
customers_df[customers_df.gender.isna()]
Kode di atas hanya akan menampilkan baris data yang memenuhi kondisi customers_df.gender.isna() atau dengan kata lain ia akan menampilkan baris data yang mengandung missing value pada kolom gender. Berikut merupakan tampilan baris data tersebut.
dos:d52ec67bb6bfedbc0fc7c2ecb0dc3dbd20230221093333.jpeg
Berdasarkan gambar di atas, dapat dilihat bahwa baris data tersebut masih mengandung banyak informasi penting sehingga sayang jika langsung dibuang. Oleh karena itu, pada kasus ini, kita akan menggunakan metode imputation untuk menangani missing value.

Pada metode imputation, kita akan menggunakan nilai tertentu untuk mengganti missing value. Musabab kolom gender merupakan kolom kategorik, kita akan menggunakan nilai yang dominan sebagai pengganti missing value tersebut. Gunakanlah method value_counts()untuk mengidentifikasi nilai yang dominan.
customers_df.gender.value_counts()
Kode di atas akan menghasilkan keluaran sebagai berikut.
dos:8734b29cd8fe2aaad27202f1c21038b520230221093329.jpeg
Berdasarkan hasil di atas, dapat diketahui bahwa nilai yang paling dominan dalam kolom gender ialah “Prefer not to say”. Nilai inilah yang selanjutnya akan kita gunakan sebagai pengganti missing value. Proses penggantian ini dapat dilakukan menggunakan method fillna()seperti contoh berikut.
customers_df.fillna(value="Prefer not to say", inplace=True)
Untuk memastikan proses di atas berjalan dengan semestinya, kita bisa menjalankan kembali kode untuk mengidentifikasi missing value seperti berikut.
customers_df.isna().sum()
Jika proses pembersihan missing value tersebut berhasil, Anda akan memperoleh hasil seperti berikut.
dos:30e5968031143c2bdcb3e96ca8ce045020230221093326.jpeg

Menangani inaccurate value
Oke, sekarang kita akan mengatasi masalah inaccurate value pada kolom age. Sebagai awal, kita perlu melihat data baris data yang mengandung inaccurate value tersebut (baris dengan nilai age maksimum). Hal ini dilakukan menggunakan teknik filter seperti contoh kode berikut.
customers_df[customers_df.age == customers_df.age.max()]
Kode di atas akan menampilkan baris data yang memiliki nilai age maksimum.
dos:c3e9f2a02a6645592ee468eeb3ff62c720230221093330.jpeg
Berdasarkan data tersebut, kita bisa berasumsi bahwa inaccurate value tersebut terjadi karena human error sehingga kelebihan memasukkan nilai nol. Oleh karena itu, gantilah dengan nilai 70. Proses ini dilakukan dengan memanfaatkan method replace()seperti contoh berikut.
customers_df.age.replace(customers_df.age.max(), 70, inplace=True)
Nah, untuk memastikan kode diatas berjalan sesuai harapan, jalankanlah kembali kode berikut.
customers_df[customers_df.age == customers_df.age.max()]
Upsi, ternyata masih ada invalid value lain yang terdapat dalam kolom age.
dos:3aaa95fde61e935ed34d496f58f6f53b20230221093332.jpeg
Penyebab kesalahan ini kemungkinan sama dengan sebelumnya, yaitu human error yang kelebihan memasukkan nilai nol. Untuk menangani hal ini, kita akan menggantinya dengan nilai 50.
customers_df.age.replace(customers_df.age.max(), 50, inplace=True)
Untuk memastikan kembali tidak terdapat inaccurate value pada customers_df, jalankanlah kode berikut.
customers_df.describe()
Kode di atas akan menghasilkan keluaran seperti berikut!
dos:fe21deb6b9df9e4587aa784c4bc39a4320230221093333.jpeg
Berdasarkan hasil tersebut dapat dilihat bahwa kolom age memiliki nilai maksimum yang cukup masuk akal. Selain itu, jika Ada perhatikan, nilai mean dan standard deviation ikut berubah setelah kita menangani inaccurate value tersebut.


Membersihkan Data orders_df
Oke, sekarang kita telah menyelesaikan semua permasalahan yang ada pada customers_df. Selanjutnya, kita akan mengatasi permasalahan pada orders_df. Berdasarkan proses assessing data sebelumnya, diketahui bahwa terdapat kesalahan tipe data untuk kolom order_date & delivery_date.

Untuk mengatasi masalah ini, kita akan mengganti tipe data pada kolom order_date & delivery_date menjadi datetime. Proses ini dapat dilakukan menggunakan function to_datetime() yang disediakan oleh library pandas. Berikut merupakan contoh kode untuk melakukannya.

datetime_columns = ["order_date", "delivery_date"]
 
for column in datetime_columns:
  orders_df[column] = pd.to_datetime(orders_df[column])
Kode di atas akan mengubah tipe data pada kolom order_date & delivery_date menjadi datetime. Untuk memastikan hal ini berjalan sesuai harapan, periksa kembali tipe data tersebut menggunakan method info().

orders_df.info()
Jika semua tahapan berjalan sesuai harapan, kode di atas akan menghasilkan keluaran seperti berikut.

dos:631dbd502dace0d79d752016bc6695b620230221093331.jpeg



Membersihkan Data product_df
Data berikutnya yang akan kita bersihkan ialah product_df. Sesuai hasil assessing data sebelumnya, kita mengetahui bahwa terdapat 6 data yang terduplikasi pada product_df. Untuk mengatasi hal ini, kita perlu membuang data yang sama tersebut menggunakan method drop_duplicates() seperti contoh berikut.

product_df.drop_duplicates(inplace=True)
Kode di atas akan menghapus semua data yang duplikat. Untuk memastikan kode tersebut berjalan sesuai harapan, jalankanlah kode berikut.

print("Jumlah duplikasi: ", product_df.duplicated().sum())
Jika proses penghapusan data yang duplikat berjalan dengan lancar, kode di atas akan menghasilkan keluaran seperti berikut “Jumlah duplikasi:  0”.



Membersihkan Data sales_df
Data selanjutnya yang perlu Anda bersihkan ialah sales_df. Berdasarkan hasil penilain data sebelumnya, diketahui bahwa terdapat 19 missing value pada kolom total_price. Untuk mengetahui proses penanganan missing value yang paling sesuai, kita perlu melihat terlebih dahulu baris data yang mengandung missing value tersebut. 

sales_df[sales_df.total_price.isna()]
Kode di atas akan menampilkan semua baris data yang memiliki missing value pada kolom total_price seperti pada gambar berikut.
dos:d474ce99c1c1fb9fc2afea4bf4d7ff3320230221102514.jpeg

Berdasarkan tampilan data tersebut, kita menemukan bahwa nilai total_price merupakan hasil perkalian antara price_per_unit dan quantity. Kita dapat menggunakan pola ini untuk menangani missing value pada kolom total_price. Berikut merupakan contoh penerapan kode untuk melakukannya.

sales_df["total_price"] = sales_df["price_per_unit"] * sales_df["quantity"]
Kode di atas akan mengatasi seluruh missing value serta memastikan nilai pada kolom total_price telah sesuai. Untuk memastikan hal ini, Anda dapat memeriksa kembali jumlah missing value pada sales_df menggunakan kode berikut.

sales_df.isna().sum()
Jika proses sebelumnya berjalan lancar, Anda akan menemukan hasil seperti berikut.

dos:a1782aae8c1d178a0be4c787687088d620230221093331.jpeg

Phew …, itulah segenap proses data wrangling untuk menyiapkan data sebelum dianalisis. Bagaimana menurut Anda? Proses data wrangling ternyata cukup menantang bukan? Namun, perlu Anda ingat bahwa di balik tantangan tersebut, tahapan ini akan sangat membantu kita untuk membuat hasil analisis yang berkualitas.

Catatan

Anda dapat mengakses proyek lengkap melalui tautan berikut: proyek data wrangling.

Pada materi selanjutnya, kita akan membahas berbagai hal terkait data understanding. Apakah Anda sudah siap untuk menghadapi tantangan baru? Nah, sebelum masuk ke materi berikutnya, terdapat kuis dengan 4 soal yang harus Anda selesaikan terlebih dahulu. So, tetap semangat!
