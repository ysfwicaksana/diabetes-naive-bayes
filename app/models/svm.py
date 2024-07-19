import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).parent.parent.parent / "data" / "diabetes_svm.joblib"

def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

def predict(input_data):
    return model.predict([input_data])