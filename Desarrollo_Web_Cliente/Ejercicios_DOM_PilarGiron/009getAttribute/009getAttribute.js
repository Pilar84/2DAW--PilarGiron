//selecciona el div
const div = document.querySelector('div');

//obtiene el valor del atributo data-widget-name
const value = div.getAttribute('data-widget-name');

//muestra el valor en la consola
console.log(value);


/*
Este ejercicio obtiene el valor de un atributo data-*.

El atributo data-widget-name tiene el valor "menu".
Se usa getAttribute o dataset para leerlo.

El texto "Elige el género" es el contenido del div,
no el valor del atributo.
*/
