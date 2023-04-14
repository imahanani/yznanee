NUMPY
NumPy (singkatan dari numerical Python)
#menginstal NumPy menggunakan package manager seperti pip ataupun conda.
- pip install numpy
- conda install numpy
#memanggil dan menggunakan library NumPy 
import numpy as np
array_1 = np.array([2, 3, 6, 5])
array_1

PANDAS
Pandas menyediakan data structure bernama DataFrame
#menginstal pandas 
- pip install pandas
- conda install pandas
#memanggil pandas dan membuat sebuah DataFrame
import pandas as pd
data = {
    'Name': ['Lulu', 'Lala', 'Lili'], 
    'Age': [23, 45, 46]
}

SCIPY
SciPy (Scientific Python) untuk kebutuhan komputasi saintifik.
#menginstal SciPy
- pip install scipy
- conda install scipy
#memastikan proses instalasi berhasil.
import scipy
 
print(scipy.__version__)


MATPLOTLIB
URL: https://matplotlib.org/stable/gallery/index.html
Matplotlib menyediakan banyak object dan method yang memungkinkan kita membuat visualisasi data statis, animated, dan interaktif
#Instalasi
- pip install matplotlib
- conda install matplotlib
#memastikan keberhasilan instalasi
import matplotlib
 
print(matplotlib.__version__)


SEABORN
URL: https://seaborn.pydata.org/examples/index.html
Seaborn merupakan library Python yang spesifik digunakan untuk membuat visualisasi data yang atraktif dan informatif. Library ini memanfaatkan matplotlib untuk menampilkan grafik visualisasi data.
#instalasi
- pip install seaborn
- conda install seaborn
#cek keberhasilan instalasi
import seaborn as sns
 
print(sns.__version__)


#nilai mean menggunakan NumPy
import numpy as np
 
jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
jumlah_kucing.mean()

#memperoleh nilai median dari suatu data
import numpy as np
 
jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
np.median(jumlah_kucing)

#menghitung nilai mode
import numpy as np
from scipy import stats
 
jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
mode_jumlah_kucing = stats.mode(jumlah_kucing)[0][0]
 
#menghitung parameter range menggunakan library NumPy
import numpy as np
 
jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
range = jumlah_kucing.max() - jumlah_kucing.min()
print(range)

#menghitung IQR menggunakan library NumPy
import numpy as np
 
jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
iqr = np.percentile(jumlah_kucing, 75) - np.percentile(jumlah_kucing, 25)
print(iqr)

#menghitung nilai variance
import numpy as np
import pandas as pd
 
jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
jumlah_kucing_series = pd.Series(jumlah_kucing)
jumlah_kucing_series.var()

#menggunakan library pandas untuk menghitung standard deviation
import numpy as np
import pandas as pd
 
jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
jumlah_kucing_series = pd.Series(jumlah_kucing)
jumlah_kucing_series.std()


WRANGLING

#Pandas menyediakan sebuah function read_csv()untuk membaca berkas CSV.
import pandas as pd
 
df = pd.read_csv("data.csv", delimiter=",")

#Pandas juga menyediakan function read_excel() untuk membaca berkas data dengan format XLSX atau XLS. 
import pandas as pd
 
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")

#JSON memiliki struktur data yang mirip seperti data structure dictionary dalam Python yang terdiri dari pasangan keys dan values. function read_json()untuk membaca berkas data berformat JSON.
import pandas as pd
 
df = pd.read_json("data.json")

#HyperText Markup Language merupakan sebuah markup language standar yang digunakan untuk merancang tampilan sebuah dokumen/halaman di web browser. function read_html()
import pandas as pd
 
url = "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list"
df = pd.read_html(url)[0]

# XML. Ia merupakan singkatan dari Extensible Markup Language, function read_xml()
import pandas as pd
 
df = pd.read_xml("https://www.w3schools.com/xml/books.xml")

#SQL database. pandas menyediakan tiga function 
# read_sql_table()untuk membaca SQL database table dan mempresentasikannya ke dalam bentuk pandas DataFrame
import pandas as pd
import sqlalchemy as sqla
 
db = sqla.create_engine("sqlite:///mydata.sqlite")
 
pd.read_sql_table("table_name", db)

#read_sql_query()untuk membaca SQL query dan mempresentasikannya ke dalam bentuk pandas DataFrame.
import pandas as pd
import sqlalchemy as sqla
 
db = sqla.create_engine("sqlite:///mydata.sqlite")
 
pd.read_sql_query("SELECT * FROM table_name", db)

#read_sql()untuk membaca SQL query atau table dan mempresentasikannya ke dalam bentuk pandas DataFrame.
import pandas as pd
import sqlalchemy as sqla
 
db = sqla.create_engine("sqlite:///mydata.sqlite")
 
pd.read_sql("SELECT * FROM table_name", db)

#merge(). Ia dapat digunakan untuk menggabungkan dua buah DataFrame.
import pandas as pd
 
product_df = pd.read_csv("product.csv")
orders_df = pd.read_csv("orders.csv")
 
new_order_df = pd.merge(
    left=product_df,
    right=orders_df,
    how="inner",
    left_on="product_id",
    right_on="product_id"
)
Kode di atas akan menghasilkan sebuah DataFrame baru yang hanya mengambil nilai yang bersesuaian dari kedua DataFrame (product_df dan orders_df) tersebut. Proses ini dilakukan dengan menyesuaikan nilai pada kolom product_id yang berperan sebagai primary key dari product_df dan foreign key dari orders_df.  


#Missing Value karena adanya nilai yang hilang dari sebuah data dan biasanya direpresentasikan sebagai nilai NaN dalam library pandas. Library pandas menyediakan sebuah method bernama isnull() atau isna() untuk mengidentifikasi missing value dalam sebuah DataFrame. Keduanya sering dipadukan dengan method sum()untuk menghitung total missing value pada setiap kolom dalam sebuah DataFrame.
import pandas as pd
product_df = pd.read_csv("product.csv")
 
products_df.isnull().sum()

#method duplicated()untuk mengidentifikasi apakah terdapat duplikasi pada sebuah DataFrame. 
import pandas as pd
 
url = "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list"
df = pd.read_html(url)[0]
df.duplicated().sum()

#mengidentifikasi outlier menggunakan IQR method
import numpy as np
 
q25, q75 = np.percentile(data, 75), np.percentile(data, 25)
iqr = q75 - q25
cut_off = iqr * 1.5
minimum, maximum = q25 - cut_off, q75 + cut_off
 
outliers = [x for x in data if x < minimum or x > maximum]

#menghapus seluruh baris atau kolom yang memiliki missing value
import pandas as pd
 
products_df = pd.read_csv("product.csv")
 
products_df.dropna(axis=0, inplace=True)

#mengganti missing value pada kolom age
import pandas as pd
 
data=pd.read_csv('employee_data.csv')
 
data.age.fillna(value=data.age.mean(), inplace=True)

#menggunakan method interpolate().
import pandas as pd
 
data=pd.read_csv('bbca_index.csv')
 
data.close_price.interpolate(method='linear', limit_direction='forward', inplace=True)


OUTLIER
#menghapus seluruh baris yang mengandung outlier
import pandas as pd
 
df = pd.read_csv("data.csv")
 
Q1 = (df['TotalCharges']).quantile(0.25)
Q3 = (df['TotalCharges']).quantile(0.75)
IQR = Q3 - Q1
 
maximum = Q3 + (1.5*IQR)
minimum = Q1 - (1.5*IQR)
 
kondisi_lower_than = df['TotalCharges'] < maximum
kondisi_more_than = df['TotalCharges'] > minimum
 
df.drop(df[kondisi_lower_than].index, inplace=True)
df.drop(df[kondisi_more_than].index, inplace=True)

#mengganti outlier dengan nilai tertentu
method mask() yang disediakan oleh library pandas. Method tersebut menerima parameter cond sebagai kondisi untuk memfilter nilai outlier.

df = pd.read_csv("data.csv")
 
Q1 = (df['TotalCharges']).quantile(0.25)
Q3 = (df['TotalCharges']).quantile(0.75)
IQR = Q3 - Q1
 
maximum = Q3 + (1.5*IQR)
minimum = Q1 - (1.5*IQR)
 
kondisi_lower_than = df['TotalCharges'] < maximum
kondisi_more_than = df['TotalCharges'] > minimum
 
df.maks(cond=kondisi_more_than, maximum, axis=1, inplace=True)
df.mask(cond=kondisi_lower_than, minimum, axis=1, inplace=True)


#drop_duplicates() untuk menghilangkan duplikasi 
import pandas as pd
 
df = pd.read_csv("data.csv")
df.drop_duplicates(inplace=True)















#contoh kode untuk membuat grafik histogram dari data jumlah kucing peliharaan pegawai Dicoding.
import numpy as np
import matplotlib.pyplot as plt
 
jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
plt.hist(jumlah_kucing, bins=4)
plt.show()

#Library pandas method untuk menghitung skewness dari sebuah data
import numpy as np
import pandas as pd
 
jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
jumlah_kucing_series = pd.Series(jumlah_kucing)
jumlah_kucing_series.skew()


#Library Pandas telah menyediakan sebuah method untuk menghitung korelasi antar feature dalam sebuah DataFrame.
import pandas as pd
 
sample_data = {
    'name': ['John', 'Alia', 'Ananya', 'Steve', 'Ben'],
    'age': [24, 22, 23, 25, 28],  
    'communication_skill_score': [85, 70, 75, 90, 90],
    'quantitative_skill_score': [80, 90, 80, 75, 70]
}
 
df = pd.DataFrame(sample_data)
 
df.corr()

#menghitung covariance antar feature dalam sebuah DataFrame
import pandas as pd
 
sample_data = {
    'name': ['John', 'Alia', 'Ananya', 'Steve', 'Ben'],
    'age': [24, 22, 23, 25, 28],  
    'communication_skill_score': [85, 70, 75, 90, 90],
    'quantitative_skill_score': [80, 90, 80, 75, 70]
}
 
df = pd.DataFrame(sample_data)
 
df.cov()




 
