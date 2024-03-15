from fastapi import FastAPI, HTTPException
import pandas as pd
from function import kmeans_clustering, dbscan_clustering, hierarchical_clustering
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn
from sklearn.preprocessing import StandardScaler

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

csv_path = os.path.abspath("../data/mall_customers.csv")
feature_columns = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]

@app.post("/{model_name}")
async def clustering(model_name: str):
    if not os.path.exists(csv_path):
        raise HTTPException(status_code=400, detail="CSV file not found")

    data = pd.read_csv(csv_path)
    features = data[feature_columns]
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    if model_name == "kmeans":
        result = kmeans_clustering(features_scaled, k=5, n_init=10)
    elif model_name == "dbscan":
        result = dbscan_clustering(features_scaled, eps=0.5, min_samples=5)
    elif model_name == "hierarchical":
        result = hierarchical_clustering(features_scaled, n_clusters=5, linkage="ward")
    else:
        raise HTTPException(status_code=400, detail="Invalid model name")

    return result
if __name__ == "__main__":
    uvicorn.run(app)
