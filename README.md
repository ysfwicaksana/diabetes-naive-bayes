# Diabetic Disease Prediction API

Ini adalah proyek prediksi penyakit diabetes menggunakan FastAPI dan scikit-learn.

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

6. **Testing Model**

   ```bash
   curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{
     "Usia": 60, 
     "Jenis_Kelamin": 1,
     "Riwayat_Keluarga": 1,
     "BMI": 25.5,
     "Tekanan_Darah": 1,
     "Gula_Darah": 0,
     "Kehamilan": 0,
     "Kebiasaan_Merokok": 1,
     "Aktifitas_Fisik": 1,
     "Pola_Tidur": 1
   }'
   
   # Response:
   # {
   #     "prediction": 0 => 0 : non diabetes / 1 : diabetes
   # }



