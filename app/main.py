# app/main.py
from fastapi import FastAPI
from app.routers import predict

app = FastAPI()

app.include_router(predict.router)

@app.get("/")
def index():
    return {"message": "Diabetic Disease Prediction API"}