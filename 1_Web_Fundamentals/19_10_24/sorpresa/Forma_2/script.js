
    let contador1 = document.querySelector("#contador1");
    let contador2 = document.querySelector("#contador2");
    let contador3 = document.querySelector("#contador3");

    // Function is now global


const contar = (element) => { 
    if (element.id === 'btn1'){
        let contador = contador1.innerText ;// Convert to number
        contador++;
        contador1.innerText = contador;
    } else if (element.id === 'btn2'){
        let contador = contador2.innerText; // Convert to number
        contador++;
        contador2.innerText = contador;
    } else if (element.id === 'btn3'){
        let contador = contador3.innerText ;// Convert to number
        contador++;
        contador3.innerText = contador;
    }
};
