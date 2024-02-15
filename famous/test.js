let menuicn = document.querySelector(".menuicn"); 
let nav = document.querySelector(".navcontainer"); 

menuicn.addEventListener("click", () => { 
	nav.classList.toggle("navclose"); 
})
document.addEventListener("DOMContentLoaded", function() {
    // Add event listener to the logout button
    const logoutButton = document.querySelector(".logout");
    logoutButton.addEventListener("click", function() {
        // Redirect to the login page
        window.location.href = "famous\login.html"; // Replace "/path/to/login/page.html" with the actual path to your login page
    });
});
