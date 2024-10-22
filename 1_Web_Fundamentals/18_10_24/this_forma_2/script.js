var y = document.getElementById("miParrafo");
var x = document.getElementById("botonCambiar");

var z = document.getElementsByClassName("miparrafo2"); 


const cambio = (x) => {
    x.innerText = "¡Texto cambiado!";
    y.innerText = "¡Texto cambiado!";
    z[0].innerText = "¡Texto cambiado!";
    z[1].style.addclass = "miparrafo2";
};
