from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from function import kmeans_clustering, dbscan_clustering, hierarchical_clustering
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8001",  # Ajoutez l'origine de votre application frontend ici
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ClusteringData(BaseModel):
    feature_columns: list[str]
csv_path = "../data/all_customers.csv"

@app.post("/{model_name}")
async def clustering(model_name: str, data: ClusteringData):
    csv_path = data.csv_path
    feature_columns = data.feature_columns

    if not os.path.exists(csv_path):
        raise HTTPException(status_code=400, detail="CSV file not found")

    if model_name == "kmeans":
        k = 5
        n_init = 10
        result = kmeans_clustering(csv_path, feature_columns, k, n_init)
    elif model_name == "dbscan":
        eps = 0.5
        min_samples = 5
        result = dbscan_clustering(csv_path, feature_columns, eps, min_samples)
    elif model_name == "hierarchical":
        n_clusters = 5
        linkage = "ward"
        result = hierarchical_clustering(csv_path, feature_columns, n_clusters, linkage)
    else:
        raise HTTPException(status_code=400, detail="Invalid model name")

    return result

if __name__ == "__main__":
    uvicorn.run(app)


