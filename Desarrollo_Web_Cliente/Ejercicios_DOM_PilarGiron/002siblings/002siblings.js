/*
Si elem – es un elemento nodo arbitrario del DOM… 
• ¿Es cierto que elem.lastChild.nextSibling siempre es null? 
• ¿Es cierto que elem.children[0].previousSibling siempre es null ? 
Demuéstralo. 
*/

/*• ¿Es cierto que elem.lastChild.nextSibling siempre es null? 
 Si es cierto que elem.lastChild.nextSibling siempre es null, 
 porque lastChild devuelve el último nodo hijo del elemento, y nextSibling devuelve el siguiente nodo hermano.*/


/*¿Es cierto que elem.children[0].previousSibling siempre es null ?
<<<<<<< HEAD
No es falso, porque children[0] devuelve el primer nodo hijo del elemento, y previousSibling devuelve cualquier tipo de nodo hermano anterior, incluyendo nodos de texto o comentarios.*/
=======
No es falso, porque children[0] devuelve el primer nodo hijo del elemento, y previousSibling devuelve cualquier tipo de nodo.*/
>>>>>>> optativa-semana1
const elem = document.getElementById('elem');

//lastChild.nextSibling, devuelve null
console.log("elem.lastChild:", elem.lastChild);
console.log("elem.lastChild.nextSibling:", elem.lastChild.nextSibling);

//demostración lógica
if (elem.lastChild.nextSibling === null) {
    console.log("Es cierto que elem.lastChild.nextSibling siempre es null");
}

//children[0].previousSibling
console.log("elem.children[0]:", elem.children[0]);
console.log("elem.children[0].previousSibling:", elem.children[0].previousSibling);

//comparación correcta

console.log(
    "elem.children[0].previousElementSibling:",
    elem.children[0].previousElementSibling
);


