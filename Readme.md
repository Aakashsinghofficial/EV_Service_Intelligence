# EV Service Intelligence Platform

An end-to-end Machine Learning platform designed to predict key EV service outcomes before a service visit is completed.

The platform predicts:

- Repair Cost
- Turnaround Time (TAT)
- Delay Risk

The project covers the complete ML lifecycle from data generation and analysis to model development, explainability, API development, Docker containerization, and cloud deployment.

---

## Business Problem

EV service centers need to estimate repair cost, service turnaround time, and potential delays before completing a service visit.

This platform uses vehicle, battery, service, workshop, technician, parts, and warranty information to generate actionable predictions that can support service planning and operational decision-making.

### Potential Business Users

- Service Center Managers
- Workshop Operations Teams
- Service Advisors
- Parts & Supply Teams
- After-Sales Teams

---

## ML Objectives

| Prediction | ML Problem | Business Output |
|---|---|---|
| Repair Cost | Regression | Predicted repair cost |
| Turnaround Time (TAT) | Regression | Predicted service duration in days |
| Delay Risk | Binary Classification | Delay probability and LOW/HIGH risk |

---

## Key Features

The prediction system uses information related to:

- Vehicle characteristics
- Vehicle age
- Battery age and health
- Battery replacement
- Service visit history
- Issue family and exact issue
- Parts requirement and availability
- Parts ordering status
- Expected parts ETA
- Workshop utilization
- Active jobs on arrival
- Technician experience
- Technician efficiency
- Repair complexity
- Labor hours
- Warranty status
- Warranty coverage
- Day type

---

## Project Workflow

```text
Raw EV Service Data
        |
        v
Data Preparation
        |
        v
Exploratory Data Analysis
        |
        v
Feature Engineering
        |
        v
Model Selection
        |
        +-------------------+
        |                   |
        v                   v
 Repair Cost Model       TAT Model
        |                   |
        +---------+---------+
                  |
                  v
             Delay Model
                  |
                  v
             Model Audit
                  |
                  v
         Inference Pipeline
                  |
                  v
               FastAPI
                  |
                  v
               Docker
                  |
                  v
               Render
                  |
                  v
        Public Prediction API

## Machine Learning Models

Three trained model artifacts are used:

```text
Models/
├── repair_cost_model.pkl
├── tat_model.pkl
└── delay_model.pkl


The trained models are loaded by the FastAPI application during application startup.

---

## Model Explainability

SHAP was used to understand model predictions and identify important factors influencing the outputs.

The analysis focuses on operational factors such as:

- Battery health
- Vehicle age
- Battery age
- Workshop utilization
- Active jobs
- Technician experience
- Repair complexity
- Labor hours
- Parts availability
- Expected parts ETA

This helps connect model predictions with operational decision-making.

---

## API

The trained models are exposed through a FastAPI REST API.

### Health Check

`GET /health`

Used to verify that the API is running and that all trained models have loaded successfully.

Example response:

```json
{
  "status": "healthy",
  "models_loaded": true
}
