import pandas as pd
import numpy as np
from sklearn.cluster import KMeans,DBSCAN,AgglomerativeClustering
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler



# Load data and prepare features
csv_path = '../data/Mall_Customers.csv'
data = pd.read_csv(csv_path)
# Rename columns
data = data.rename(columns={'CustomerID': 'customer_ID', 'Gender': 'gender', 'Age': 'age','Annual Income (k$)': 'annual_income', 'Spending Score (1-100)': 'spending_score'})
# Map gender to 0 and 1
data['gender'] = data['gender'].map({'Male': 0, 'Female': 1})
feature_columns = ['age', 'gender', 'annual_income', 'spending_score']
# to standardize the numerical features in other columns
scaler = StandardScaler()
features_scaled = scaler.fit_transform(data[feature_columns])


def kmeans_clustering(k, n_init):
    # Entraînement du modèle DBSCAN
    kmeans = KMeans(n_clusters=k, n_init=n_init, random_state=42)
    kmeans.fit(features_scaled)
    # Calcul du score de silhouette
    silhouette_score_kmeans = silhouette_score(features_scaled, kmeans.labels_)
    return silhouette_score_kmeans


def dbscan_clustering(eps, min_samples):
    # Entraînement du modèle DBSCAN
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    dbscan.fit(features_scaled)
    # Calcul du score de silhouette (bien que la silhouette ne soit pas le meilleur score pour DBSCAN)
    silhouette_score_dbscan = silhouette_score(features_scaled, dbscan.labels_)
    return silhouette_score_dbscan


def hierarchical_clustering(n_clusters, linkage):
    # Entraînement du modèle de clustering hiérarchique
    hc = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage)
    hc.fit(features_scaled)
    # Calcul du score de silhouette
    silhouette_score_hc = silhouette_score(features_scaled, hc.labels_)
    return silhouette_score_hc

