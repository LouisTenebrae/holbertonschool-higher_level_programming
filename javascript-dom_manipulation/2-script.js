addEventListener("DOMContentLoaded", function () {
    // Get red_header element
    const redHeaderElement = document.querySelector("#red_header");

    function elementAddClass() {
        // Get element an add a class
        document.querySelector("header").classList.add("red");
    }
    // add event
    redHeaderElement.addEventListener("click", elementAddClass);
});