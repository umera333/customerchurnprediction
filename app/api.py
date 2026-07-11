from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Load model
model = joblib.load("models/best_model.pkl")
model_columns = joblib.load("models/model_columns.pkl")

app = FastAPI(
    title="Customer Churn Prediction API",
    version="1.0"
)

# Input schema
class Customer(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float


@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API is running"}


@app.post("/predict")
def predict(customer: Customer):

    input_df = pd.DataFrame([customer.dict()])

    # Convert categorical features
    input_df = pd.get_dummies(input_df)

    # Add missing columns
    for col in model_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Keep same order
    input_df = input_df[model_columns]

    prediction = model.predict(input_df)[0]

    probability = float(model.predict_proba(input_df)[0][1])

    result = "Likely to Churn" if prediction == 1 else "Not Likely to Churn"

    return {
        "prediction": result,
        "probability": round(probability, 4)
    }