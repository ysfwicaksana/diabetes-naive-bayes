from fastapi import APIRouter
from pydantic import BaseModel
from app.models.svm import predict as model_predict
from app.schemas.prediction import PredictRequest, PredictResponse

router = APIRouter()

@router.post('/predict', response_model=PredictResponse)
def predict(request: PredictRequest):
    
    # Extract features from the request
    features = [
        request.Usia,
        request.Jenis_Kelamin,
        request.Riwayat_Keluarga,
        request.BMI,
        request.Tekanan_Darah,
        request.Gula_Darah,
        request.Kehamilan,
        request.Kebiasaan_Merokok,
        request.Aktifitas_Fisik,
        request.Pola_Tidur
    ]

    # Make prediction using your model
    prediction = model_predict(features)

    # Return the prediction
    return PredictResponse(prediction=prediction[0])