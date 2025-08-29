from fastapi import FastAPI
from pydantic import BaseModel, conlist
import joblib
import numpy as np

class IrisFeatures(BaseModel):
    # Order: sepal_length, sepal_width, petal_length, petal_width
    features: conlist(float, min_items=4, max_items=4)

app = FastAPI(title="Iris Classifier API", version="1.0.0")

# Load the trained model artifact (created by train.py)
artifact = joblib.load("model.joblib")
model = artifact["model"]
class_names = artifact["class_names"]

@app.get("/")
def root():
    return {
        "message": "Iris Classifier API. POST /predict with 'features': [sepal_len, sepal_wid, petal_len, petal_wid]"
    }

@app.post("/predict")
def predict(payload: IrisFeatures):
    X = np.array([payload.features])
    probs = model.predict_proba(X)[0].tolist()
    pred_idx = int(np.argmax(probs))
    return {
        "predicted_class_index": pred_idx,
        "predicted_class_name": class_names[pred_idx],
        "probabilities": {class_names[i]: float(probs[i]) for i in range(len(class_names))}
    }
