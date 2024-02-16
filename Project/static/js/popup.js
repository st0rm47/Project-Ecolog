// Function to handle the API call and show the popup
function handleApiSignal() {
    // Code to handle the API call and show the popup
    fetch('http://your-flask-app-ip:5000/api/open-popup', {
        method: 'POST'
    })
    .then(response => {
        if (response.ok) {
            return response.text();
        }
        throw new Error('API call failed');
    })
    .then(data => {
        console.log(data);
        showPopup(); // Show the popup when API call is successful
    })
    .catch(error => {
        console.error(error);
    });
}

// Show the popup initially
showPopup();
