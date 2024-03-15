from fastapi import FastAPI
from function import kmeans_clustering, dbscan_clustering, hierarchical_clustering, load_and_preprocess_data, csv_path, feature_columns
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn

app = FastAPI()

origins = [
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

@app.get("/kmeans")
async def kmeans():
    features_scaled = load_and_preprocess_data(csv_path, feature_columns)
    result = kmeans_clustering(features_scaled, k=5, n_init=10)
    return {"silhouette_score": result}

@app.get("/dbscan")
async def dbscan():
    features_scaled = load_and_preprocess_data(csv_path, feature_columns)
    result = dbscan_clustering(features_scaled, eps=0.5, min_samples=5)
    return {"silhouette_score": result}

@app.get("/hierarchical")
async def hierarchical():
    features_scaled = load_and_preprocess_data(csv_path, feature_columns)
    result = hierarchical_clustering(features_scaled, n_clusters=5, linkage="ward")
    return {"silhouette_score": result}

if __name__ == "__main__":
    uvicorn.run(app)
