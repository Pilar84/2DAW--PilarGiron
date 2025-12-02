/*
Función ucFirst:
Devuelve un string con la primera letra en mayúscula
*/

function ucFirst(str) {
    if (!str) return ""; // si el string está vacío, devuelve vacío
    return str[0].toUpperCase() + str.slice(1);
}

// pedimos datos para probarlo
let input = prompt("Ingresa un nombre en minuscula: ");
alert("El nombre con la primera letra en mayúscula es: " + ucFirst(input));
 
