document.addEventListener("DOMContentLoaded", function() { ////** Esta linea se asegura de cargar los elementos del DOM antes de ejecutar el codigo de JS */




const turnOff = (element) => {
    if (element.innerText === "Off") {
        element.style.backgroundColor = "green";
        element.innerText = "On";
    } else {
        element.style.backgroundColor = "gray";
        element.innerText = "Off";
    }}

document.getElementById("btn1").addEventListener("click", function() {
    turnOff(this);
});

document.getElementById("btn2").addEventListener("click", function() {
    turnOff(this);
}
);

document.getElementById("btn3").addEventListener("click", function() {
    turnOff(this);
}
);


});