console.log("JS loaded successfully");

const form = document.getElementById('insuranceForm');
const resultDiv = document.getElementById('result');

const history = [];

// Chart.js setup
const ctx = document.getElementById('chargesChart').getContext('2d');
const chartData = {
    labels: [],
    datasets: [
        {
            label: 'Predicted Charges',
            data: [],
            borderColor: 'purple',
            backgroundColor: 'rgba(139, 92, 246, 0.3)',
            fill: true
        },
        {
            label: 'Average Charges',
            data: [],
            borderColor: 'orange',
            backgroundColor: 'rgba(251, 191, 36, 0.3)',
            fill: true
        }
    ]
};
const chargesChart = new Chart(ctx, {
    type: 'line',
    data: chartData,
    options: { responsive: true }
});

function updateHistory(prediction) {
    history.unshift(prediction);
    if(history.length > 5) history.pop();

    const tbody = document.querySelector('#historyTable tbody');
    tbody.innerHTML = '';
    history.forEach((pred, index) => {
        const row = `<tr>
                        <td class="border border-purple-300 px-2 py-1">${index+1}</td>
                        <td class="border border-purple-300 px-2 py-1">${pred.toFixed(2)}</td>
                     </tr>`;
        tbody.innerHTML += row;
    });
}

function updateChart(prediction) {
    chartData.labels.push(`Pred ${chartData.labels.length+1}`);
    chartData.datasets[0].data.push(prediction);
    const avgCharge = 13279.12; // dataset mean
    chartData.datasets[1].data.push(avgCharge);

    if(chartData.labels.length > 5){
        chartData.labels.shift();
        chartData.datasets[0].data.shift();
        chartData.datasets[1].data.shift();
    }
    chargesChart.update();
}

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    resultDiv.innerHTML = "Predicting... ⏳";

    const formData = new FormData(form);
    const data = {};
    formData.forEach((value, key) => { data[key] = value });

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if(result.prediction !== undefined){
            resultDiv.innerHTML = `Predicted Charges: $${result.prediction.toFixed(2)}`;
            updateHistory(result.prediction);
            updateChart(result.prediction);
        } else if(result.error){
            resultDiv.innerHTML = `Error: ${result.error}`;
        }

    } catch (error) {
        resultDiv.innerHTML = "Error predicting charges ❌";
        console.error(error);
    }
});
