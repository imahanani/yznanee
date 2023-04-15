Open powershell to create Venv

``` python --version ^Python 3.9.13^

``` conda create --name bike-sharing python=3.9.13 #membuat anama venv

```conda update -n base -c defaults conda #to update conda unto the latest version (recommended by system)

```conda activate bike-sharing #aktivasi venv
``` conda deactive #deaktivasi venv

```pip install numpy pandas scipy matplotlib seaborn jupyter #install library yang dibutuhkan (proses wrangling saat ini) 

```jupyter notebook #membuka notebook jupyter .ipynb

(otomatis masuk ke Jupyter web) Buat folder baru di Jupyter sebagai MAIN DIRECTORY. Aku kasih nama Dico-Bike-Sharing-Project

Bikin berkas baru, namanya Bike-SBiharing

Buka berkas di Jupyter Notebooknya, lalu coding semua tahapan analisis. 

Dimulai dengan memanggil semua Librari yang sudah di install ke venv di paling awal tadi (power shell). 
```import numpy as np
```import pandas as pd
```import matplotlib as plt
```import seaborn as sn

^persiapan selesai^
Then kita masuk ke Gathering process! Lets gooooooo!!

Load semua CSV file yang digithub. Ada 2 table: day & hour

```day_df = pd.read_csv(https://raw.githubusercontent.com/imahanani/yznanee/main/Project/day.csv)
day_df.head() #load day_df

```hour_df= pd.read_csv('https://raw.githubusercontent.com/imahanani/yznanee/main/Project/hour.csv')
hour_df.head()

^tahapan load udah, lanjut ke assessing^ WRANGLING, gais :)

```day_df.info() #type tiap kolom
```day_df.isna().sum()  #cek missiong value NaN
```print("Total Duplicates: ", day_df. duplicated().sum()  #jumlah duplikat
```day_df.describe() #ringkasan parameter statistik
         
#mau lihat bentuk tabular tiap table dong

         
^ini baru day_df ya^, sekarang ke hour_df
Karena isna nol dan type data dirasa sudah ok, maka lanjut ke EDA

   
```day_df.desribe(incude='all') #rangkuman parameter statistik

```day_df.groupby(by='mnth').agg({
  'instant': 'nunique',
  'temp': ['max', 'min', 'mean', 'std']
}) #grouping berdasarkan 'mnth' dan memanggil kolom 'instant' dan 'temp' |row: 'month' column: 'instant' dan 'temp'
  
```day_df.groupby(by='season').instant.nunique().sort_values(ascending=False)  #persebaran data by season | ERROR: ValueError: operands could not be broadcast together with shapes (188,) (178,) 

          SEK YA ISTIRAHAT
         



