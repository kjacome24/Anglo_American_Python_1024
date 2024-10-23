document.addEventListener("DOMContentLoaded", function () {

    // Select all buttons and counters
    let buttons = document.querySelectorAll(".btn");
    let counters = document.querySelectorAll(".counter");

    // Add event listeners to all buttons
    buttons.forEach((button, index) => {
        button.addEventListener("click", function () {
            let currentCounter = counters[index]; // Get corresponding counter
            let count = currentCounter.innerText; // Parse the current value
            currentCounter.innerText = ++count; // Increment the value and update
        });
    });

});
