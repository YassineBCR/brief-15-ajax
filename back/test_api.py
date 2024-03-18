from fastapi.testclient import TestClient
from api_models import app

client = TestClient(app)

def test_kmeans_endpoint():
    resp = client.get("/kmeans")
    assert resp.status_code == 200
    assert isinstance(resp.json(), float)

def test_dbscan_endpoint():
    resp = client.get("/dbscan")
    assert resp.status_code == 200
    assert isinstance(resp.json(), float)

def test_hierarchical_endpoint():
    resp = client.get("/hierarchical")
    assert resp.status_code == 200
    assert isinstance(resp.json(), float)
