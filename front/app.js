document.getElementById('submit-btn').addEventListener('click', () => {
    const selectedModel = document.getElementById('model-select').value;
  
    // Mettez à jour le chemin d'accès au fichier CSV ici
    const csv_path = '../data/mall_customers.csv'; // Chemin d'accès relatif
    // const csv_path = '/path/to/your/csv/file/mall_customers.csv'; // Chemin d'accès absolu
  
    const data = {
      csv_path: csv_path,
      feature_columns: ['Age', 'Annual Income (k$)', 'Spending Score (1-100)'],
    };
  
    fetch(`http://localhost:8000/${selectedModel}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
      console.log(result);
      document.getElementById('result').innerText = `Silhouette Score: ${result.silhouette_score}`;
    })
    .catch(error => {
      console.error('Error:', error);
    });
  });
  