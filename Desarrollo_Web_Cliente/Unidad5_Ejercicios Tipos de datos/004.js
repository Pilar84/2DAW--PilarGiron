/*Crea una variable con el valor 3.14159. Utiliza las funciones Math.round(),
Math.ceil() y Math.floor() para redondear este número. Muestra cada resultado y
explica las diferencias.*/

let pi = 3.14159;

redondeo_hacia_arraba= Math.ceil(pi);
console.log("Redondeo hacia arriba: " + redondeo_hacia_arraba);

redondeo_hacia_abajo= Math.floor(pi);
console.log("Redondeo hacia abajo: " + redondeo_hacia_abajo);

redondeo_entero_mas_cercano= Math.round(pi);
console.log("Redondeo hacia el entero mas cercano: " + redondeo_entero_mas_cercano);
