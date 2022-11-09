async function getApiData(url) {
    const response = await fetch(url, {
        method: "GET"
    });
    const apiData = await response.json();
    return apiData
}