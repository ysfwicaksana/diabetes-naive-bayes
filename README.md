# FastAPI Classification Project

Ini adalah proyek klasifikasi data menggunakan FastAPI dan scikit-learn. Proyek ini menyediakan API untuk memprediksi kelas berdasarkan fitur yang diberikan.

## Persyaratan

Pastikan Anda memiliki versi Python 3.7 atau lebih baru terinstal di sistem Anda. Proyek ini juga memerlukan beberapa dependensi Python yang tercantum dalam `requirements.txt`.

## Instalasi

1. **Kloning Repository**

   Kloning repository dari GitHub:
   ```bash
   git clone [<repository-url>](https://github.com/ysfwicaksana/diabetes-naive-bayes.git)
   cd diabetes-naive-bayes
   
2. **Membuat dan Mengaktifkan Virtual Environment**

   Pada Windows:
   ```bash
   python -m venv myvenv
   myvenv\Scripts\activate

   Pada MacOS & Linux:
   ```bash
   python3 -m venv myvenv
   source myvenv/bin/activate
   
3. **Menginstall dependensi**
   
   ```bash
   pip install -r requirements.txt

5. **Jalankan aplikasi**

   ```bash
   uvicorn app.main:app --reload

   Setelah menjalankan server, API akan tersedia di http://127.0.0.1:8000. Anda dapat mengakses dokumentasi interaktif API di http://127.0.0.1:8000/docs atau http://127.0.0.1:8000/redoc.


