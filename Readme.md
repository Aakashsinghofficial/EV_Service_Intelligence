\# EV Service Intelligence Platform



An end-to-end Machine Learning platform for predicting EV service outcomes.



\## Business Problem



EV service centers need to estimate service cost, turnaround time, and delay risk before completing a service visit.



This project uses vehicle, battery, service, workshop, technician, parts, and warranty information to generate actionable predictions for EV service operations.



\## Machine Learning Targets



| Target | ML Problem | Business Output |

|---|---|---|

| Repair Cost | Regression | Predicted repair cost |

| Turnaround Time (TAT) | Regression | Predicted service duration in days |

| Delay Risk | Binary Classification | Delay probability and HIGH/LOW risk |







\## Project Architecture



```text

Raw EV Service Data

&#x20;       |

&#x20;       v

Data Preparation \& Feature Engineering

&#x20;       |

&#x20;       v

Machine Learning Models

&#x20;       |

&#x20;       +-------------------+

&#x20;       |                   |

&#x20;       v                   v

&#x20;Repair Cost Model       TAT Model

&#x20;       |                   |

&#x20;       +---------+---------+

&#x20;                 |

&#x20;                 v

&#x20;            Delay Model

&#x20;                 |

&#x20;                 v

&#x20;            Saved Models

&#x20;                 |

&#x20;                 v

&#x20;              FastAPI

&#x20;             /       \\

&#x20;            /         \\

&#x20;       /health      /predict

&#x20;            \\         /

&#x20;             \\       /

&#x20;              Docker




## API

The trained machine learning models are served through a FastAPI application.

### Endpoints

#### GET `/health`

Checks whether the API is running and whether all trained models are loaded.

Example response:

```json
{
  "status": "healthy",
  "models_loaded": true
}


POST /predict

Accepts EV service-visit information and returns:

Predicted repair cost
Predicted turnaround time
Delay probability
Delay risk

Example response:

{
  "Predicted_Repair_Cost": 2016.71,
  "Predicted_TAT_Days": 0.47,
  "Delay_Probability": 0.03,
  "Delay_Risk": "LOW"
}


API Documentation

When running locally:

http://127.0.0.1:8000/docs

Swagger UI provides interactive API testing.



## Docker

The FastAPI application is containerized using Docker for reproducible deployment.

### Build Docker Image

```bash
docker build -t ev-service-intelligence .


Run Container:docker run -d -p 8000:8000 --name ev-service-api ev-service-intelligence

Check Running Container : docker ps

View Container Logs:docker logs ev-service-api

Stop Container : docker stop ev-service-api

Start Container Again : docker start ev-service-api




## Project Structure

```text
EV_Service_Intelligence/
│
├── App/
│   └── app.py
│
├── Data/
│   └── raw EV service dataset
│
├── Models/
│   ├── delay_model.pkl
│   ├── repair_cost_model.pkl
│   └── tat_model.pkl
│
├── Notebook/
│   └── ML development notebooks
│
├── SRC/
│
├── Dockerfile
├── .dockerignore
├── .gitignore
├── Requirements.txt
└── Readme.md

