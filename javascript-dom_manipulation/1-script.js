addEventListener("DOMContentLoaded", function () {
    // Function to change color 
    function changeColor() {
        document.querySelector("header").style.color = "#FF0000";
    }

    // Get the div element
    const divRedHeader = document.querySelector("#red_header");

    // Add the click event
    divRedHeader.addEventListener("click", changeColor);
});