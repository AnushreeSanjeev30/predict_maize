// Example for Yield Prediction
async function predictYield() {
    const inputs = collectInputs(); // e.g., get SNPs and phenotype
    const response = await fetch('http://localhost:5000/predict_yield', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({features: inputs})
    });
    const result = await response.json();
    displayPrediction(result.prediction, result.confidence);
}
