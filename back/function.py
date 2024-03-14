import pandas as pd
import numpy as np
from sklearn.cluster import KMeans,DBSCAN,AgglomerativeClustering
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler



csv_path = '../data/mall_customers.csv'
feature_columns = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']

#KMEANS
k = 5
n_init = 10
#DBSCAN
eps = 0.5
min_samples = 5
#Hierarchical
n_clusters = 5
linkage = 'ward'

def kmeans_clustering(csv_path, feature_columns, k=5, n_init=10):
    data = pd.read_csv(csv_path)
    features = data[feature_columns]
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    kmeans = KMeans(n_clusters=k, n_init=n_init, random_state=42)
    kmeans.fit(features_scaled)
    silhouette_score_kmeans = silhouette_score(features_scaled, kmeans.labels_)
    print("KMEANS SCORE  : ", silhouette_score_kmeans)
    result = {
        'silhouette_score': silhouette_score_kmeans,
        'kmeans_model': kmeans,
        'scaler_model': scaler
    }

    return result
result = kmeans_clustering(csv_path, feature_columns, k, n_init)


def dbscan_clustering(csv_path, feature_columns, eps=0.5, min_samples=5):
    data = pd.read_csv(csv_path)
    # Préparation des données
    features = data[feature_columns]
    # Normalisation des données
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    # Entraînement du modèle DBSCAN
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    dbscan.fit(features_scaled)
    # Calcul du score de silhouette (bien que la silhouette ne soit pas le meilleur score pour DBSCAN)
    silhouette_score_dbscan = silhouette_score(features_scaled, dbscan.labels_)
    # Imprimer le score de silhouette
    print("DBSCAN Score : ", silhouette_score_dbscan)
    result = {
        'silhouette_score': silhouette_score_dbscan,
        'dbscan_model': dbscan,
        'scaler_model': scaler
    }

    return result
result = dbscan_clustering(csv_path, feature_columns, eps, min_samples)

def hierarchical_clustering(csv_path, feature_columns, n_clusters=5, linkage='ward'):
    # Chargement des données
    data = pd.read_csv(csv_path)

    # Préparation des données
    features = data[feature_columns]

    # Normalisation des données
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # Entraînement du modèle de clustering hiérarchique
    hc = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage)
    hc.fit(features_scaled)

    # Calcul du score de silhouette
    silhouette_score_hc = silhouette_score(features_scaled, hc.labels_)

    # Imprimer le score de silhouette
    print("Hierarchical Score : ", silhouette_score_hc)

    result = {
        'silhouette_score': silhouette_score_hc,
        'hc_model': hc,
        'scaler_model': scaler
    }

    return result

result = hierarchical_clustering(csv_path, feature_columns, n_clusters, linkage)