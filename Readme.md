# EV Service Intelligence Platform

An end-to-end Machine Learning platform for predicting EV service outcomes.

The system predicts:

- Repair Cost — Regression
- Turnaround Time (TAT) — Regression
- Delay Risk — Classification

## Business Problem

EV service centers need to estimate repair cost, service turnaround time, and potential delays before completing a service visit.

This platform uses vehicle, battery, service, workshop, technician, parts, and warranty information to generate actionable predictions.

## ML Targets

| Target | Problem Type | Output |
|---|---|---|
| Repair Cost | Regression | Predicted repair cost |
| TAT | Regression | Predicted turnaround time in days |
| Delay Risk | Classification | Delay probability + LOW/HIGH risk |

## Project Architecture

Raw EV Service Data
        ↓
Data Preparation & Feature Engineering
        ↓
Machine Learning Models
        ↓
Saved Model Artifacts
        ↓
FastAPI
        ↓
Docker
        ↓
Render
        ↓
Public Prediction API

## Models

Three trained models are used:

- `repair_cost_model.pkl`
- `tat_model.pkl`
- `delay_model.pkl`

## API

### Health Check

`GET /health`

Returns the API and model loading status.

Example:

```json
{
  "status": "healthy",
  "models_loaded": true
}
Prediction

POST /predict

The API accepts service-visit information and returns:

{
  "Predicted_Repair_Cost": 2016.71,
  "Predicted_TAT_Days": 0.47,
  "Delay_Probability": 0.03,
  "Delay_Risk": "LOW"
}
Example Input
{
  "Visit_Number": 3,
  "Vehicle_Model": "Nexon EV",
  "Vehicle_Age_at_Service": 4,
  "Battery_Age_at_Service": 3,
  "Battery_Health_at_Service": 82,
  "Battery_Replaced": false,
  "Issue_Family": "Brake",
  "Exact_Issue": "Brake Pad Wear",
  "Parts_Required": true,
  "Parts_Available": true,
  "Part_Ordered": false,
  "Expected_Part_ETA_Days": 0,
  "Active_Jobs_On_Arrival": 8,
  "Workshop_Utilization": 0.55,
  "Day_Type": "Weekday",
  "Technician_Experience_Years": 5,
  "Repair_Complexity": 2,
  "Base_Labor_Hours": 2.5,
  "Technician_Efficiency": 0.9,
  "Effective_Labor_Hours": 2.25,
  "Warranty_Status": "Active",
  "Warranty_Covered": true,
  "Expected_TAT_Days": 1.2
}
Deployment

The application is containerized using Docker and deployed as a FastAPI web service.

Deployment stack:

Python
Scikit-learn
FastAPI
Uvicorn
Docker
GitHub
Render
Deployment Validation

The deployed API was validated using:

Health endpoint
Swagger/OpenAPI documentation
Realistic prediction request
HTTP 200 response
Successful loading of all three ML models
Project Structure
EV_Service_Intelligence/
│
├── App/
│   └── app.py
│
├── Data/
│   └── ev_service_history_raw.csv
│
├── Models/
│   ├── repair_cost_model.pkl
│   ├── tat_model.pkl
│   └── delay_model.pkl
│
├── Notebook/
│   ├── 01_dataset_generation.ipynb
│   ├── 02_EDA.ipynb
│   ├── 03_Feature_Engineering.ipynb
│   ├── 04_Model_Selection.ipynb
│   ├── 05_Repair_Cost.ipynb
│   ├── 06_Shap.ipynb
│   ├── 07_TAT_Model.ipynb
│   ├── 08_TAT_Tuning.ipynb
│   ├── 09_Delay_Model.ipynb
│   ├── 10_Delay_Tuning.ipynb
│   ├── 11_Model_Audit.ipynb
│   └── 12_Inference_Pipeline.ipynb
│
├── Dockerfile
├── Requirements.txt
├── .dockerignore
├── .gitignore
└── Readme.md
Live API

Public API:

https://ev-service-intelligence.onrender.com

Swagger documentation:

https://ev-service-intelligence.onrender.com/docs

Health check:

https://ev-service-intelligence.onrender.com/health



### One correction I intentionally made


The example uses:


```json
"Part_Ordered": false

not

"Parts_Ordered": false

because your actual ServiceRequest schema uses Part_Ordered.
