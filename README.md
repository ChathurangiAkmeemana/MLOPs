README.txt

Title: FastAPI ML Model Deployment with GitHub Actions & Docker

PROJECT DESCRIPTION:
This project involves building a machine learning model to predict diabetes. The CI pipeline is managed using GitHub Actions, and the model is containerized using Docker.

====================================================

PREREQUISITES:
- Python 3.x

====================================================

STEP-BY-STEP GUIDE

1. SETUP PROJECT LOCALLY:
-----------------------------------
a. Clone the GitHub repository:
   git clone https://github.com/ChathurangiAkmeemana/MLOPs


====================================================

2. SAVE MODEL USING PICKLE:
-----------------------------------


====================================================

3. DOCKERIZE THE APPLICATION:
-----------------------------------
a. Create a `Dockerfile` in root:

docker run https://hub.docker.com/repository/docker/kavi12345678/diabetes-model
# Run the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

