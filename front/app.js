document.getElementById("run-button").addEventListener("click", async () => {
  const modelSelect = document.getElementById("model-select");
  const modelName = modelSelect.value;
  await sendClusteringRequest(modelName);
});

async function sendClusteringRequest(modelName) {
  const response = await fetch(`http://127.0.0.1:8000/${modelName}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (response.ok) {
    const result = await response.json();
    console.log(result);

    const resultElement = document.getElementById("result");

    resultElement.innerHTML = `Silhouette Score: ${result}`;
  } else {
    console.error("Error:", response.status, response.statusText);
  }
}
