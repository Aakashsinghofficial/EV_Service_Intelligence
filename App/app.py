from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path


# ============================================================
# 1. PROJECT PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================================
# 2. LOAD TRAINED ML MODELS
# ============================================================

repair_model = joblib.load(
    BASE_DIR / "Models" / "repair_cost_model.pkl"
)

tat_model = joblib.load(
    BASE_DIR / "Models" / "tat_model.pkl"
)

delay_model = joblib.load(
    BASE_DIR / "Models" / "delay_model.pkl"
)


# ============================================================
# 3. FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="EV Service Intelligence API",
    description="ML API for EV service prediction",
    version="1.0.0"
)


# ============================================================
# 4. INPUT DATA SCHEMA
# ============================================================

class ServiceRequest(BaseModel):
    Visit_Number: int
    Vehicle_Model: str
    Vehicle_Age_at_Service: int
    Battery_Age_at_Service: int
    Battery_Health_at_Service: float
    Battery_Replaced: bool
    Issue_Family: str
    Exact_Issue: str
    Parts_Required: bool
    Parts_Available: bool
    Part_Ordered: bool
    Expected_Part_ETA_Days: float
    Active_Jobs_On_Arrival: int
    Workshop_Utilization: float
    Day_Type: str
    Technician_Experience_Years: float
    Repair_Complexity: int
    Base_Labor_Hours: float
    Technician_Efficiency: float
    Effective_Labor_Hours: float
    Warranty_Status: str
    Warranty_Covered: bool
    Expected_TAT_Days: float


# ============================================================
# 5. HOME ENDPOINT
# ============================================================

@app.get("/")
def home():
    return {
        "message": "EV Service Intelligence API is running"
    }


# ============================================================
# 6. HEALTH CHECK
# ============================================================

@app.get("/health")
def health_check():

    models_loaded = (
        repair_model is not None
        and tat_model is not None
        and delay_model is not None
    )

    return {
        "status": "healthy" if models_loaded else "unhealthy",
        "models_loaded": models_loaded
    }

# ============================================================
# 7. PREDICTION ENDPOINT
# ============================================================

@app.post("/predict")
def predict_service(request: ServiceRequest):

    # Convert validated request into DataFrame
    input_data = request.model_dump()

    input_df = pd.DataFrame(
        [input_data]
    )

    # --------------------------------------------------------
    # Repair Cost Prediction
    # --------------------------------------------------------

    predicted_repair_cost = repair_model.predict(
        input_df
    )[0]

    # --------------------------------------------------------
    # TAT Prediction
    # --------------------------------------------------------

    predicted_tat = tat_model.predict(
        input_df
    )[0]

    # --------------------------------------------------------
    # Delay Risk Prediction
    # --------------------------------------------------------

    delay_probability = delay_model.predict_proba(
        input_df
    )[0, 1]

    delay_risk = (
        "HIGH"
        if delay_probability >= 0.50
        else "LOW"
    )

    # --------------------------------------------------------
    # Final Business Output
    # --------------------------------------------------------

    return {
        "Predicted_Repair_Cost": float(
            round(predicted_repair_cost, 2)
        ),
        "Predicted_TAT_Days": float(
            round(predicted_tat, 2)
        ),
        "Delay_Probability": float(
            round(delay_probability, 3)
        ),
        "Delay_Risk": delay_risk
    }