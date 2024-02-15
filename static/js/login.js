// Get the form element
const loginForm = document.getElementById('loginForm');

// Add an event listener to the form for the submission
loginForm.addEventListener('submit', function (event) {
  // Prevent the default form submission
  event.preventDefault();

  // Get the username and password values
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  // Get the error message element
  const errorMessage = document.getElementById('errorMessage');

  // Check if the username and password match the specified values
  if (username === 'admin' && password === 'password') {
      window.location.href = 'dashboard.html'; // Redirect to the dashboard page
  } else {
    // Display an error message
    errorMessage.innerText = 'Invalid username or password';
  }
});

// Function to toggle password visibility
function togglePasswordVisibility() {
  const passwordInput = document.getElementById('password');
  const eyeIcon = document.querySelector('.eye-icon');

  if (passwordInput.type === 'password') {
    passwordInput.type = 'text';
    eyeIcon.innerHTML = '&#128064;'; // Show an open eye icon
  } else {
    passwordInput.type = 'password';
    eyeIcon.innerHTML = '&#128065;'; // Show a closed eye icon
  }
}
