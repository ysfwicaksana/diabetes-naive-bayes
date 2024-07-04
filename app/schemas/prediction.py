from pydantic import BaseModel

class PredictRequest(BaseModel):
    Usia: int
    Jenis_Kelamin: int
    Riwayat_Keluarga: int
    BMI: float
    Tekanan_Darah: float
    Gula_Darah: float
    Kehamilan: int
    Kebiasaan_Merokok: int
    Aktifitas_Fisik: int
    Pola_Tidur: int

class PredictResponse(BaseModel):
    prediction: int