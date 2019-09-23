###  Credit Scoring Approval - API Deployment 📚 

- Pada Repository ini, terdiri dari code dan dataset untuk melakukan Model Deployment menggunakan **`Anaconda Prompt`** dan **`localhost`**
- Deployment kali ini menggunakan web **framework Flask**.

### Requirements
#### Tambahan module/package dari materi hari ini,
#### Wajib install `pip install flask-restplus`

```
1. Flask==0.12
2. Jinja2==2.9.5
3. numpy==1.13.1
4. scikit-learn==0.18.1
5. scipy==0.18.1
6. flask-restplus
```
================================================================================

### Code dan Dataset

- Dataset diambil dari [Kaggle](https://www.kaggle.com/brycecf/give-me-some-credit-dataset "Give Me Some Credit") | *"Give Me Some Credit*
- Model digunakan adalah model prediksi dengan model Gaussian Naive Bayes (`GaussianNB()`)
- Repository terdiri dari `app.py`, `requirements.txt`, `deploy.py`, dan `model.pkl`.

===============================================================================

### Dumping/Menyimpan File Pickle as Model

- Jalankan Anaconda Prompt dan ikuti prosedur di bawah ini:
  1. Pindahkan direktori aktif Anaconda Prompt ke folder repositori hasil extract repo ini.
  2. Jalankan dengan mengetik **`python app.py`** (ini bisa dikatakan **`testing model`**)
  3. Setelah itu, file .pkl akan terbentuk di folder yang sama.
  4. Setelah berhasil, jalankan **`python deploy.py`**
  
=============================================================================== 

### Akses Deployed Model di http://localhost:5000 (Default)

- Langkah selanjutnya, anda bisa melanjutkan proses dengan mengetikkan `localhost:5000` di web anda (rekomendasi Google Chrome)
- Setelah itu akan tampil halaman interaktif yang bisa teman-teman akses seperti berikut ini,
![Langkah 1](https://github.com/buildGather/ADSB2-Iykra/blob/master/Use%20Case%20-%20API%20Credit%20Scoring/Process/1.PNG)
- Setelah itu teman-teman bisa klik tulisan **`Penerimaan Kredit - Credit Approval`** sehingga muncul tampilan sebagai berikut,
![Langkah 2](https://github.com/buildGather/ADSB2-Iykra/blob/master/Use%20Case%20-%20API%20Credit%20Scoring/Process/2.PNG)
- Lalu, sila teman-teman klik tulisan hijau tersebut untuk membuka form pengisian data prediksi, tampilan seperti berikut ini,
![Langkah 3](https://github.com/buildGather/ADSB2-Iykra/blob/master/Use%20Case%20-%20API%20Credit%20Scoring/Process/3.PNG)
- Berikutinya, teman-teman bisa mulai dengan klik tulisan **`Try it Out`**
![Langkah 4](https://github.com/buildGather/ADSB2-Iykra/blob/master/Use%20Case%20-%20API%20Credit%20Scoring/Process/4.PNG)
- Langkah selanjutnya teman-teman bisa mulai mengisi data untuk prediksi kredit scoring dengan ketentuan yang akan saya tuliskan bawah ini
![Langkah 5](https://github.com/buildGather/ADSB2-Iykra/blob/master/Use%20Case%20-%20API%20Credit%20Scoring/Process/5.PNG)
  - `Rasio Total Tagihan dibagi Limit` rentang 0 sampai dengan satu (**float**), contoh 0.67
  - `Usia` bilangan bulat (**integer**)
  - `Jumlah Terlambat 30-59 Hari` (**integer**) -> Berapa kali terlambat? 1 apabila 1 kali, 2 apabila 2 kali, dst
  - `Rasio Hutang` rentang 0 sampai dengan 1 (**float**), contoh 0.54
  - `Pendapatan per Bulan` (**integer**)
  - `Hutang Tertanggung` (**integer**) -> jumlah hutang yang dimiliki, misalnya hutang kpr dan mobil, ditulis 2 (dua)
  - `Jumlah Terlambat 90 Hari` (**integer**) -> Berapa kali terlambat? 1 apabila 1 kali, 2 apabila 2 kali, dst
  - `Aset Pribadi` (**integer**) -> Berapa jumlah aset yang dimiliki?
  - `Jumlah Terlambat 60-89 Hari` (**integer**) -> Berapa kali terlambat? 1 apabila 1 kali, 2 apabila 2 kali, dst
  - `Jumlah Tanggungan Keluarga` (**integer**)

- Setelah itu, teman-teman bisa klik **`Execute`** untuk menampilkan hasil prediksinya
![Langkah 6](https://github.com/buildGather/ADSB2-Iykra/blob/master/Use%20Case%20-%20API%20Credit%20Scoring/Process/6.PNG)
- Selanjutnya, hasil prediksi bisa dilihat pada bagian bawah kotak hitam seperti berikut ini,
![Langkah 7](https://github.com/buildGather/ADSB2-Iykra/blob/master/Use%20Case%20-%20API%20Credit%20Scoring/Process/7.PNG)

**SELESAI!**

=============================================================================== 

### Interpretasi Hasil

- Ketika hasil menunjukan 'Pengajuan Kredit Pemohon Ditolak' Maka orang tersebut dapat diperkirakan akan gagal menanggung kredit dengan kriteria-kriteria dari model prediksi.
- Ketika hasil menunjukan 'Pengajuan Kredit Pemohon Diterima' Maka orang tersebut dapat diperkirakan dapat menanggung kredit dengan kriteria-kriteria dari model prediksi.
