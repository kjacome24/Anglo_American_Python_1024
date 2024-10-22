// Los dos van a seleccionar la etiqueta hl
var p = document.querySelector("p");
var title = document.querySelector("#title");
var logoImg = document.querySelector(".nav img");



const changePage = () => {
    title.innerHTML = "Nuevo titulo";
    h1.innerHTML = "Nuevo titulo";
    logoImg.src = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png";
    logoImg.alt = "Google Logo";
}


const cloud = () => {
    title.innerText = "Cloudy";
    p.innerText = "The weather is cloudy";
    logoImg.src = "img/some_clouds.png";
    logoImg.alt = "Cloud logo";
}


const rain = () => {
    title.innerText = "Rainy";
    p.innerText = "The weather is rainy";
    logoImg.src = "img/some_rain.png";
    logoImg.alt = "Rain logo";
}

const sun = () => {
    title.innerText = "Sunny";
    p.innerText = "The weather is sunny";
    logoImg.src = "img/some_sun.png";
    logoImg.alt = "Sun logo";
}