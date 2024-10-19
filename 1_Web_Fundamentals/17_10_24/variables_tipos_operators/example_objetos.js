const cost_per_day = {
    Monday: 100,
    Tuesday: 200,
    Wednesday: 300,
    Thursday: 400,
    Friday: 500,
    Saturday: 600,
    Sunday: 700
}


let promedio = 0;
for (let day in cost_per_day) {
    console.log(`${day}: ${cost_per_day[day]}`);
    promedio += cost_per_day[day];
}
promedio = promedio/Object.keys(cost_per_day).length;
console.log(promedio); 



let frutas = [
    "manzana",
    "pera",
    "uva",
    "sandia",
    "melon",
    "platano",
    "mango",
    "fresa",
    "kiwi",
    "naranja"
]

frutas.shift();

console.log(frutas);


const suma = (a,b) => a+b;

console.log(suma(1,2))


// --------------------------------------------

var hamburguesaClasica = {
    "pan": "pan de hamburguesa",
    "carne": "carne de res",
    "queso": "cheddar",
    "extras": ["lechuga", "tomate", "cebolla", "pepinillos"]
};

console.log(
    hamburguesaClasica.pan
);


var hamburguesaClasica = {
    "pan": "pan de hamburguesa",
    "carne": "carne de res",
    "queso": "cheddar",
    "extras": ["lechuga", "tomate", "cebolla", "pepinillos"]
};

console.log(
    hamburguesaClasica.pan
);



var hamburguesaClasica = {
    "pan": "pan con semillas de sésamo",
    "carne": "carne de res 100%",
    "queso": "queso cheddar",
    "extras": ["lechuga", "tomate", "cebolla", "salsa especial"],
    "infoHamburguesa": function() {
        console.log("Pan: " + this.pan);
        console.log("Carne: " + this.carne);
        console.log("Queso: " + this.queso);
        console.log("Extras: " + this.extras.join(", "));
    }
}

// Ahora, con solo una línea, ¡podemos obtener todos los detalles de nuestra hamburguesa clásica!
hamburguesaClasica.infoHamburguesa();






/////////////////////////////////Examples with objects

function sandwichFactory(pan, proteína, queso, salsas) {
    var sandwich = {};
    sandwich.pan = pan;
    sandwich.proteína = proteína;
    sandwich.queso = queso;
    sandwich.salsas = salsas;
    return sandwich;
}
    
var s1 = sandwichFactory("trigo", "pavo", "provolone", ["mostaza", "cebolla frita", "rúcula"]);
console.log(s1);

// ----------------------------------------

const pizzaOven = (crustType, sauceType, cheeses, toppings ) => ({crustType, sauceType, cheeses, toppings});

let ADeliciusPizza = pizzaOven("Thick Crust", "Marinara Sauce", "Mozzarela", ["Garlic Paste", "Mayo"] )

console.log(ADeliciusPizza)


