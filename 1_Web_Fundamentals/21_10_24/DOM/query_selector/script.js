// Los dos van a seleccionar la etiqueta hl
var h1 = document.querySelector("h1");
var title = document.querySelector("#title");

var logoImg = document.querySelector(".nav img");



const changePage = () => {
    title.innerHTML = "Nuevo titulo";
    h1.innerHTML = "Nuevo titulo";
    logoImg.src = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png";
    logoImg.alt = "Google Logo";
}
