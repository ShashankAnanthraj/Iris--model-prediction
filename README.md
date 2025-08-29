# Iris Classifier API (FastAPI + Docker)

A minimal example of training a scikit-learn model and serving it using FastAPI. 
The Docker image trains the model during build for demo convenience.

## Prerequisites
- Python 3.10+ (for local dev)
- Docker Desktop
- Git + GitHub account
- VS Code (recommended) with Python extension

## Run locally (without Docker)
```bash
# 1) Create a virtual environment (optional but recommended)
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 2) Install dependencies and train
pip install --upgrade pip
pip install -r requirements.txt
python train.py   # creates model.joblib

# 3) Start the API
uvicorn app:app --reload
# Visit http://127.0.0.1:8000 and http://127.0.0.1:8000/docs
```

Test a prediction:
```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d @sample_request.json
```

## Build & run with Docker
```bash
# Build (trains the model inside the image)
docker build -t iris-api:1.0 .

# Run the container
docker run --rm -p 8000:8000 iris-api:1.0

# In a new terminal, test:
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d @sample_request.json
```

## Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit: Iris FastAPI + Docker"
git branch -M main

# Create a new empty repo on GitHub named iris-fastapi-docker (no README)
git remote add origin https://github.com/<your-username>/iris-fastapi-docker.git
git push -u origin main
```

## Notes
- Training during `docker build` is for demo simplicity; in real projects, train offline and copy only the artifact.
- If scikit-learn fails to install on `python:3.11-slim`, uncomment the `apt-get` lines in the Dockerfile.
- Explore interactive docs at `/docs` once the server is running.
```
