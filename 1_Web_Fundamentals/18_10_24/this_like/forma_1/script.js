let contador = 0;

document.getElementById("likeButton").addEventListener("click", function() {
    contador++;
    document.getElementById("likeButton").innerText = contador + " me gusta";
});


