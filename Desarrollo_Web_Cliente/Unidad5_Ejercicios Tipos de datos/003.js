/*Crea un array que contenga tres nombres de frutas. Realiza las siguientes
operaciones:
Añade una fruta al final del array.
Elimina el primer elemento del array.
Muestra el array resultante y el número de elementos que contiene.*/

let frutas = ["platano", "fresa", "pera"];
console.log("Array original: " + frutas);


frutas.push("manzana"); 
console.log("Añadimos manzana al final del array: " + frutas); 

frutas.shift(); 
console.log("Eliminamos el primer elemento: " + frutas); 

console.log("Array resultante: " + frutas);
console.log("Números de elementos: " + frutas.length);