# filename: app.py
from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()
model = joblib.load('diabetes_model.pkl')

@app.get("/")
def read_root():
    return {"message": "Diabetes prediction model"}

@app.post("/predict/")
def predict(data: list):
    prediction = model.predict([np.array(data)])
    return {"prediction": prediction[0]}
