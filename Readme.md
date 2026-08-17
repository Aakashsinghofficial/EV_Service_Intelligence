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


