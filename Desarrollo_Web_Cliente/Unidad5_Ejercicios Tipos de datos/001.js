/*Declara una variable que almacene un número. A continuación, convierte este
número a tipo string y muestra ambos valores en la consola utilizando
console.log(). También convierte el string de nuevo a tipo numérico y muestra el
resultado*/

let num = 10;
let numStr = num.toString();
console.log("Resultado tipo String->El numero es: " + numStr);
let num2 = parseInt(numStr);
console.log("Resultado tipo Number->El numero es: " + num2);