Dataset: https://github.com/dicodingacademy/dicoding_dataset/tree/main/DicodingCollection

Consist of 4 Tables:
- Customers
- Orders
- Products
- Sales

Aims:
- Collect needed data
- Assessing collected data
- Cleaning to ready-to-use data

Steps:
- Preparation
- Gathering
- Assesing
- Cleaning


=============================================(I USE ANACONDA)
1. Preparation 

A. Created Virtual Environment
  1. Open terminal/PowerSheell 
                Me: Check Python versin firstly
                   ```py
                    python -V
                    ```
                 Output on PowwerShell: Python 3.9.13
  2.  RUN: 
```py
conda create --name main-ds python=3.9.13
```
      Me: saya ubah codenya supaya lebih personal
    ```py
    conda create --name yz-nanee python=3.9.13
    ```
    
Kode "conda create --name main-ds python=3.9.13" adalah perintah untuk membuat lingkungan virtual bernama "main-ds" menggunakan perangkat lunak Conda. Lingkungan virtual ini akan menggunakan Python versi 3.9.13.

Dengan membuat lingkungan virtual, pengguna dapat mengisolasi dan mengelola paket-paket Python dan dependensinya secara terpisah untuk setiap proyek. Ini memungkinkan pengguna untuk mempertahankan versi paket yang berbeda pada lingkungan virtual yang berbeda tanpa mempengaruhi proyek lain di mesin yang sama.

Output:
==> WARNING: A newer version of conda exists. <==
  current version: 22.9.0
  latest version: 23.3.1
Proceed ([y]/n)? y 
      Me: y then click enter
 To activate this environment, use
#
#     $ conda activate yz-nanee
      me:of course just follow above command
    
 3. Activate Virtual Environment: conda activate yz-nanee
 4. Install all libraries that we need. RUN:
 ```py
  pip install numpy pandas scipy matplotlib seaborn jupyter
  ```
  Kode "pip install numpy pandas scipy matplotlib seaborn jupyter" adalah perintah untuk menginstal beberapa paket Python yang umum digunakan dalam analisis data, yaitu:

NumPy: library untuk melakukan operasi numerik pada array dan matriks dalam Python
Pandas: library untuk melakukan manipulasi, analisis, dan pemrosesan data dalam Python
SciPy: library untuk melakukan komputasi ilmiah dan teknik dalam Python
Matplotlib: library untuk membuat grafik dan visualisasi data dalam Python
Seaborn: library untuk membuat visualisasi data yang lebih menarik dan informatif dalam Python
Jupyter: aplikasi web untuk membuat notebook interaktif yang dapat digunakan untuk melakukan eksplorasi data, analisis, dan visualisasi
Dengan menginstal paket-paket ini, pengguna dapat mulai bekerja dengan Python untuk melakukan analisis data dan membuat visualisasi yang menarik dan informatif.

Note: pastikan SPASI setiap nama library, case senditif

 5. Open notebook , RUN on powerShell
    jupyter-notebook
  --Will authomatically open the notebook (web based)
 6. Create Folder Name that will be my main directory upon this Wrangling Project.
E.g: proyek_analisis_data
  Me: Dico-Data-Scrutiny
 7. Create file under the name e.g notebook.ipynb
Me: scrutiny.ipynb
  
.py dan .ipynb adalah dua jenis format file yang berbeda dalam bahasa pemrograman Python.
Format file .py adalah file script Python standar yang berisi kode Python. File .py dapat dieksekusi dengan menjalankan perintah "python nama_file.py" pada terminal atau prompt perintah.
Sementara itu, format file .ipynb adalah format file notebook Jupyter. File .ipynb berisi kode Python yang diatur dalam sel-sel dan dapat mencakup teks, gambar, dan output yang dihasilkan dari eksekusi kode. Notebook Jupyter digunakan untuk analisis data interaktif, visualisasi data, dan pembelajaran mesin.
Dalam format file .ipynb, kita dapat mengeksekusi kode Python pada setiap sel secara terpisah dan melihat hasilnya secara interaktif, sambil mempertahankan konteks dan outputnya. Hal ini memungkinkan pengguna untuk membuat laporan interaktif dan dokumentasi yang menarik dan berguna.
Dalam format file .py, kode Python dieksekusi secara langsung dari atas ke bawah tanpa mempertimbangkan konteks atau output sebelumnya. Format file ini umumnya digunakan untuk membuat aplikasi atau program Python yang sederhana atau kompleks.



