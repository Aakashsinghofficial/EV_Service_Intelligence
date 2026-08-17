# EV Service Intelligence Platform

An end-to-end Machine Learning platform for predicting EV service outcomes.

## Problem

EV service centers need to estimate repair cost, turnaround time, and delay risk before completing a service visit.

## ML Targets

| Target | Type | Output |
|---|---|---|
| Repair Cost | Regression | Predicted cost |
| TAT | Regression | Predicted service time |
| Delay Risk | Classification | Probability + LOW/HIGH risk |

## Architecture

```text
EV Service Data
      ↓
EDA & Feature Engineering
      ↓
ML Models
      ↓
FastAPI
      ↓
Docker
      ↓
Render
      ↓
Public API
```

## Models

```text
Repair Cost Model
      ↓
repair_cost_model.pkl

TAT Model
      ↓
tat_model.pkl

Delay Risk Model
      ↓
delay_model.pkl

SHAP
      ↓
Model Explainability
```

## API

```text
GET /health
      ↓
API & Model Health Check

POST /predict
      ↓
EV Service Input
      ↓
ML Predictions
      ↓
Repair Cost + TAT + Delay Risk
```

## Deployment

```text
FastAPI
   ↓
Docker
   ↓
GitHub
   ↓
Render
   ↓
Public API
```

## Live API

```text
API
↓
https://ev-service-intelligence.onrender.com

Swagger
↓
https://ev-service-intelligence.onrender.com/docs

Health Check
↓
https://ev-service-intelligence.onrender.com/health
```

## Tech Stack

```text
Python
Pandas
NumPy
Scikit-learn
SHAP
FastAPI
Docker
GitHub
Render
```

## Status

```text
ML Models          ✓
FastAPI            ✓
Docker             ✓
Cloud Deployment   ✓
Public API         ✓

STATUS: DEPLOYED & LIVE 🚀
```
