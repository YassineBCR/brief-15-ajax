from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from functions_models import kmeans_clustering, dbscan_clustering, hierarchical_clustering
import uvicorn

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
    silhouette_score_kmeans = kmeans_clustering(5, 10)
# return {"silhouette_score_kmeans": silhouette_score_kmeans}
    return silhouette_score_kmeans

@app.get("/dbscan")
async def perform_dbscan_clustering():
    dbscan_result = dbscan_clustering(0.5, 5)
    return dbscan_result

@app.get("/hierarchical")
async def perform_hierarchical_clustering():
    hierarchical_result = hierarchical_clustering(5, 'ward')
    return hierarchical_result


# Run the API with uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)