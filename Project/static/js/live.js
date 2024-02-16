// Set device status
document.getElementById('status').textContent = 'Status: Active';

// Set current date and time
setInterval(() => {
    const now = new Date();
    document.getElementById('time').textContent = 'Time: ' + now.toLocaleTimeString();
    document.getElementById('date').textContent = 'Date: ' + now.toLocaleDateString();
}, 1000);

// Set location and map
navigator.geolocation.getCurrentPosition((position) => {
    document.getElementById('location').textContent = 'Location: ' + position.coords.latitude + ', ' + position.coords.longitude;
    var map = L.map('map').setView([position.coords.latitude, position.coords.longitude], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
    L.marker([position.coords.latitude, position.coords.longitude]).addTo(map);

    // Fetch forest data
    fetch(`https://data-api.globalforestwatch.org/forest?lat=${position.coords.latitude}&lng=${position.coords.longitude}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('forestStatus').textContent = 'Latitude: ' + position.coords.latitude + ', Longitude: ' + position.coords.longitude + '\n' + JSON.stringify(data, null, 2);
        });
});

function logout() {
    window.location.href = '/logout';
}
function dashboard() {
    window.location.href = '/dashboard';
}