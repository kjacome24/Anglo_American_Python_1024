const turnOff = (element) => {
    if (element.innerText === "Off") {
        element.style.backgroundColor = "green";
        element.innerText = "On";
    } else {
        element.style.backgroundColor = "gray";
        element.innerText = "Off";
    }}