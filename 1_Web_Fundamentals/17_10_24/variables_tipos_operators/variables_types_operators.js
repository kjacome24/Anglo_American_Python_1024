console.log("Hello World");

// Variables
const name = "John";
const age = 30;
const isCool = true;
const rating = 4.5;
const x = null;
const y = undefined;
let z;

console.log(typeof name);
console.log(typeof age);
console.log(typeof isCool);
console.log(typeof rating);
console.log(typeof x);
console.log(typeof y);
console.log(typeof z);

const ax = y + age;
console.log(ax);

// Template Strings
console.log(`My name is ${name} and I am ${age}`);

// String Methods
const s = "Hello World";
console.log(s.length);
console.log(s.toUpperCase());
console.log(s.toLowerCase());
console.log(s.substring(0, 5));
console.log(s.substring(0, 5).toUpperCase());
console.log(s.split(""));




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

console.log(promedio  ) ;

console.log(cost_per_day.length);