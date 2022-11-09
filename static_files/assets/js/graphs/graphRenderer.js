var labels;
var curveValues;
$('document').ready(function () {
    renderChart();
})

async function renderChart() {
    await displayLineGraph("chart-monthly-sales","http://127.0.0.1:8000/api/v1/analytics/month-wise-registration/")
    await displayPieChart("business-type-chart","http://127.0.0.1:8000/api/v1/analytics/month-wise-registration/")
}