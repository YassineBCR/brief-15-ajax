async function sendClusteringRequest(modelName) {
  const response = await fetch(`http://localhost:8000/${modelName}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      csvPath: '../data/mall_customers.csv',
      featureColumns: ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']
    })
  });

  if (response.ok) {
    const result = await response.json();
    console.log(result);

    // Sélectionnez l'élément HTML où vous souhaitez afficher les résultats
    const resultElement = document.getElementById('result');

    // Mettez à jour le contenu de l'élément HTML avec les résultats
    resultElement.innerHTML = `
      <h3>Silhouette Score: ${result.silhouette_score}</h3>
      <h4>Cluster Centers:</h4>
      <pre>${JSON.stringify(result.cluster_centers, null, 2)}</pre>
      <h4>Labels:</h4>
      <pre>${JSON.stringify(result.labels, null, 2)}</pre>
    `;
  } else {
    console.error('Error:', response.status, response.statusText);
  }
}

// Appeler la fonction avec le nom du modèle en paramètre
sendClusteringRequest('kmeans');