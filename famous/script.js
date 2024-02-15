function toggleSlider(sectionId) {
    var slider = document.getElementById(sectionId);
    if (slider.style.display === "none") {
        slider.style.display = "block";
    } else {
        slider.style.display = "none";
    }
}

var hamburger = document.getElementById("hamburger");
hamburger.addEventListener("click", function() {
    toggleSlider("slider");
});
