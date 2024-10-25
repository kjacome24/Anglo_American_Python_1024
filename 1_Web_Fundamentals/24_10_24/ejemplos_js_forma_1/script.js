document.addEventListener('DOMContentLoaded', function() {
    /**Ejemplo selector */
    const select = document.querySelector('#select');
    const choosen = document.querySelector('#choosen');

    select.addEventListener('change', function() {
        choosen.innerText = this.value;
    });

    //////**** ejemplo input*/
    const input = document.querySelector('#input');
    const input_text = document.querySelector('#input_text');

    input.addEventListener('input', function() {
        input_text.innerText = this.value;
    });

    //****input form and button */
    const input_form = document.querySelector('#input_form');
    const btn = document.querySelector('#btn');
    const input_text2 = document.querySelector('#input_text2');

    btn.addEventListener('click', function() {
        input_text2.innerText = input_form.value;
    });

    //****hoover */
    const hoover_text = document.querySelector('#hoover_text');

    hoover_text.addEventListener('mouseover', function() {
        this.innerText = 'Mouse por dentro';
        this.style.backgroundColor = 'green';
    });

    hoover_text.addEventListener('mouseout', function() {
        this.innerText = 'Mouse por fuera';
        this.style.backgroundColor = 'red';
    });

    ////**Eliminar banner */
    const div5 = document.querySelector('#div5');
    const btn_cookies = document.querySelector('#btn_cookies');

    btn_cookies.addEventListener('click', function() {
        div5.remove();
    });

    //**Foco */
    const focus_input = document.querySelector('#focus_input');
    const focus_text = document.querySelector('#focus_text');

    focus_input.addEventListener('focus', function() {
        focus_text.innerText = 'Foco en el input';
    });

    //**Doble Clic */
    const doble_click_btn = document.querySelector('#doble_click_btn');
    const doble_click_text = document.querySelector('#doble_click_text');

    doble_click_btn.addEventListener('dblclick', function() {
        doble_click_text.innerText = "Tu has dado doble clic"; 
    });

});