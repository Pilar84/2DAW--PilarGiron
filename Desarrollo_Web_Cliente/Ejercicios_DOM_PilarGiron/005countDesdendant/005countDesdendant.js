/*
Hay un árbol estructurado como ul/li anidado. 
Escribe el código que para cada <li> muestra: 
¿Cuál es el texto dentro de él (sin el subárbol)? 
El número de <li> anidados: todos los descendientes, incluidos los 
profundamente anidados.
*/

// Selecciona todos los elementos <li> en el documento
const items = document.querySelectorAll('li');

// Recorre cada elemento <li>
items.forEach(item => {

    // Obtiene el texto dentro del <li> sin hijos
    const texto = item.firstChild.textContent.trim();

    // Cuenta el número de <li> anidados dentro del <li> actual
    const descendientes = item.querySelectorAll('li').length;

    // Muestra el texto y el número de descendientes
    console.log(texto + ": " + descendientes);

});

