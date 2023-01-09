// Initialize and add the map
function initMap() {
    // The location of your site
    const site = { lat: -25.344, lng: 131.031 };
    // The map, centered at site
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 4,
        center: site,
    });
    // The marker, positioned at site
    const marker = new google.maps.Marker({
        position: site,
        map: map,
    });
}
