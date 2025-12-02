/*Dado el siguiente array de números [3, 7, 2, 8, 1, 4, 10], realiza las siguientes
operaciones:
Encuentra el valor más alto y más bajo del array utilizando Math.max() y
Math.min().
Utiliza un bucle for para sumar todos los elementos del array.*/

let numeros = [3, 7, 2, 8, 1, 4, 10];

let maximo = Math.max(...numeros);
console.log("Máximo: " + maximo);
let minimo = Math.min(...numeros);
console.log("Mínimo: " + minimo);

let suma = 0;
for (let i = 0; i < numeros.length; i++) {
    suma=suma+numeros[i];
}

console.log("Suma: " + suma);