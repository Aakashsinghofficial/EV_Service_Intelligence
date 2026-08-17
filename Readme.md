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
