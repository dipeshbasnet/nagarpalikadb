var labels;
var curveValues;
$('document').ready(function () {
    renderChart();
})

async function renderChart() {
    await displayLineGraph("chart-monthly-sales","api/v1/analytics/month-wise-registration/")
    await displayPieChart("business-type-chart","api/v1/analytics/type-of-business/")
}