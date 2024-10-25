    // Ejemplo selector
    let choosen = document.querySelector('#choosen');

    const showCar = (element) => {
        choosen.innerText = element.value;
    };

    // Ejemplo input

    let input_text = document.querySelector('#input_text');
    const updateInput = (element) => {
        input_text.innerText = element.value;
    };

    // Ejemplo input y botón

    let input_text2 = document.querySelector('#input_text2');
    const submitForm = () => {
        input_text2.innerText = input_form.value;
    };

    // Hoover

    const hoverIn = (element) => {
        element.innerText = 'Mouse por dentro';
        element.style.backgroundColor = 'green';
    };

    const hoverOut = (element) => {
        element.innerText = 'Mouse por fuera';
        element.style.backgroundColor = 'red';
    };

    // Eliminar banner
    let div5 = document.querySelector('#div5');

    const acceptCookies = () => {
        div5.remove();
    };

    // Foco
    let focus_text = document.querySelector('#focus_text');
 
    const focusInput = () => {
        focus_text.innerText = 'Foco en el input';
    };

    // Doble Clic
 
    let doble_click_text = document.querySelector('#doble_click_text');
 
    const doubleClick = () => {
        doble_click_text.innerText = "Tú has dado doble clic";
    };
