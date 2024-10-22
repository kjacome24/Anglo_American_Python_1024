let contador = 0;

document.getElementById("likeButton").addEventListener("click", function() {
    contador++;
    document.getElementById("likeButton").innerText = contador + " me gusta";
    document.getElementById("likeButton").style.backgroundColor = "blue";

});


let contador2 = 0;

document.getElementsByClassName("I_dont_like")[0].addEventListener("click", function() {
    contador2++;
    document.getElementsByClassName("I_dont_like")[0].innerText = contador2 + " no me gusta";
    document.getElementsByClassName("I_dont_like")[0].style.backgroundColor = "red";
});