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

## Models

- `repair_cost_model.pkl` — Repair Cost
- `tat_model.pkl` — Turnaround Time
- `delay_model.pkl` — Delay Risk

SHAP was used for model explainability.

## API

### `GET /health`

Checks API and model status.

### `POST /predict`

Returns:

```json
{
  "Predicted_Repair_Cost": 2016.71,
  "Predicted_TAT_Days": 0.47,
  "Delay_Probability": 0.03,
  "Delay_Risk": "LOW"
}

## Deployment

Built with **FastAPI + Docker** and deployed on **Render**.

Deployment was validated using both `/health` and realistic `/predict` requests.

## Live API

**API:** https://ev-service-intelligence.onrender.com

**Swagger:** https://ev-service-intelligence.onrender.com/docs

## Tech Stack

Python • Pandas • NumPy • Scikit-learn • SHAP • FastAPI • Docker • GitHub • Render

## Status

**Deployed and Live 🚀**
