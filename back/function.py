import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import os

csv_path = os.path.abspath("../data/mall_customers.csv")
feature_columns = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]

def load_and_preprocess_data(csv_path, feature_columns):
    data = pd.read_csv(csv_path)
    features = data[feature_columns]
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    return features_scaled

def kmeans_clustering(features_scaled, k=5, n_init=10):
    kmeans = KMeans(n_clusters=k, n_init=n_init, random_state=42)
    kmeans.fit(features_scaled)
    labels = kmeans.labels_
    silhouette_score_kmeans = silhouette_score(features_scaled, labels)

    return silhouette_score_kmeans

def dbscan_clustering(features_scaled, eps=0.5, min_samples=5):
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    dbscan.fit(features_scaled)
    labels = dbscan.labels_
    silhouette_score_dbscan = silhouette_score(features_scaled, labels)

    return silhouette_score_dbscan

def hierarchical_clustering(features_scaled, n_clusters=5, linkage='ward'):
    hc = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage)
    hc.fit(features_scaled)
    labels = hc.labels_
    silhouette_score_hc = silhouette_score(features_scaled, labels)

    return silhouette_score_hc