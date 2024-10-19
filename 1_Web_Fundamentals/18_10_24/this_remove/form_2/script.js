const hide = (element) => {
    element.remove();
};

// Add event listeners for each image
document.getElementById("ninja_negro").addEventListener("click", function() {
    hide(this);
});

document.getElementById("ninja_blue").addEventListener("click", function() {
    hide(this);
});

document.getElementById("ninja_green").addEventListener("click", function() {
    hide(this);
});

