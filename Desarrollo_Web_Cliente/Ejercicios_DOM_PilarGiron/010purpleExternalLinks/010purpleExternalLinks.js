/*Tenemos un elemento DOM vacio elem y un string text. ¿Cuáles de estos 3 
comandos harán exactamente lo mismo? Pon un ejemplo. 
elem.append(document.createTextNode(text)) 
elem.innerHTML = text 
elem.textContent = text*/

//Los tres comandos harán exactamente lo mismo,siempre que el string text no contenga etiquetas HTML.
//Ejemplo de HTML
<div id="elem"></div>

//Ejemplo de JavaScript
const elem = document.getElementById('elem');
const text = "Hola Mundo";

//opcion 1
elem.append(document.createTextNode(text));

//opcion 2
elem.innerHTML = text;

//opcion 3
elem.textContent = text;

//Resutado: Los tres comandos insertarán el texto "Hola Mundo" dentro del div con id "elem".


/*
Este ejercicio compara tres formas de insertar texto en el DOM.

Si el texto es plano:
- createTextNode
- innerHTML
- textContent
hacen exactamente lo mismo.

Si el texto contiene HTML:
- innerHTML lo interpreta
- los otros lo muestran como texto literal

Por eso no siempre son iguales.
*/




