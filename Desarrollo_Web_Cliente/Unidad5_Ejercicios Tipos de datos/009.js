/*Dado el siguiente array de números [10, 20, 30, 40, 50], utiliza el método reduce()
para obtener la suma total de los elementos. Después, modifica el código para
obtener el producto de todos los números.*/

let numeros = [10, 20, 30, 40, 50];

//el acumulador se inicializa con 0 en la suma
let suma = numeros.reduce(function(acumulador, numero) {
    return acumulador + numero;
}, 0);

console.log("Suma: " + suma);

//aqui el acumulador se inicializa con 1 en el producto
let producto = numeros.reduce(function(acumulador, numero) {
    return acumulador * numero;
}, 1);

console.log("Producto: " + producto);


