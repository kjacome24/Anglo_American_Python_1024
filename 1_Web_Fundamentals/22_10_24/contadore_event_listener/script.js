
document.addEventListener("DOMContentLoaded", function () { ///




    let contador1 = document.querySelector("#contador1");
    let contador2 = document.querySelector("#contador2")
    let contador3 = document.querySelector("#contador3");

    let btn1 = document.querySelector("#btn1");
    let btn2 = document.querySelector("#btn2");
    let btn3 = document.querySelector("#btn3");

    btn1.addEventListener("click", function () { contar(this)});
    btn2.addEventListener("click", function () { contar(this)});
    btn3.addEventListener("click", function () { contar(this)});

    const contar = (elment) => { 
        if (elment.id === 'btn1'){
            let contador = contador1.innerText;
            contador++;
            contador1.innerText = contador;
        } else if (elment.id === 'btn2'){
            let contador = contador2.innerText;
            contador++;
            contador2.innerText = contador;
        }
        else if (elment.id === 'btn3'){
            let contador = contador3.innerText;
            contador++;
            contador3.innerText = contador;
        }
    }

});