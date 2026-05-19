import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

model = joblib.load("churn_model.pkl")
model_columns = joblib.load("model_columns.pkl")

app = FastAPI()

class CustomerData(BaseModel):
    tenure: int
    monthlycharges: float
    totalcharges: float

@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API"}

@app.post("/predict")
def predict(data: CustomerData):
    input_data = pd.DataFrame([{
        "tenure": data.tenure,
        "monthlycharges": data.monthlycharges,
        "totalcharges": data.totalcharges
    }])

    for col in model_columns:
        if col not in input_data.columns:
            input_data[col] = 0

    input_data = input_data[model_columns]

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        result = "Likely to churn"
    else:
        result = "Not likely to churn"

    return {
        "prediction": result
    }