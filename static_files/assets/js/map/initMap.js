stateColorMapping = {}
var us_lat = 40.376;
var us_lng = -100.724;
var us_lat_lng = [28.3949, 84.1240];
var legend = L.control({position: 'bottomleft'});
var osmUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
var apiData;

$('document').ready(function () {
    map = L.map(document.getElementById('usMap'), {
        fullscreenControl: true, fullscreenControlOptions: {
            position: 'topright'
        }, center: us_lat_lng, zoom: 7.5, worldCopyJump: true, maxZoom: 18
    });

    L.tileLayer(osmUrl, {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);


    async function getMapPopUpData() {
        // apiData = await getApiData("api/state/");
        L.geoJSON(geoJsonFeature, {
            style: stateStyle,
            onEachFeature: onEachFeature
        }).addTo(map);
        // return apiData
    }
    getMapPopUpData()
})

function stateStyle(feature) {
    return {
        fillColor: feature.properties.color || "grey",
        weight: 2, opacity: 1, color: 'blue', dashArray: '10', fillOpacity: 0.7
    }

}

function onEachFeature(feature, layer) {
    layer.bindPopup(
        `<h5><strong>State: </strong> ${feature.properties.state}</h5>
                    <h4><strong>Total Number of Voters:</strong></h4>
                    <h5><strong> Male: </strong>10</h5>
                    <h5><strong> Female: </strong>20</h5>
                    <h5><strong> LGBTQIA+: </strong>30</h5>
                    <h4><strong>Age groups:</strong></h4>
                    <h5><strong> 0-18: </strong>10</h5>
                    <h5><strong> 18-40: </strong>10</h5>
                    <h5><strong> 40-60: </strong>20</h5>
                    <h5><strong> 60+:</strong>20</h5>
                    <h5><strong> Majority: </strong>60+</h5>
                    <h4><strong> Total Voters: </strong>60</h4>`);
}


