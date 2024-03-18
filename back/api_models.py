from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from functions_models import kmeans_clustering, dbscan_clustering, hierarchical_clustering

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/kmeans")
async def perform_kmeans_clustering():
    try:
        silhouette_score_kmeans = kmeans_clustering(5, 10)
        return silhouette_score_kmeans
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/dbscan")
async def perform_dbscan_clustering():
    try:
        dbscan_result = dbscan_clustering(0.5, 5)
        return dbscan_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/hierarchical")
async def perform_hierarchical_clustering():
    try:
        hierarchical_result = hierarchical_clustering(5, 'ward')
        return hierarchical_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the API with uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
