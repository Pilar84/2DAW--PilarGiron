<script>
    let body = document.body;
    body.innerHTML = "&lt;!--" + body.tagName + "--&gt;";
    alert( body.firstChild.data ); // ¿qué hay aquí?
</script>


/*El código muestra BODY porque se inserta un comentario con el nombre de la etiqueta y luego se lee el texto del nodo de comentario.

Ese texto se inserta dentro de un comentario <!-- BODY -->.

El primer hijo del body pasa a ser un nodo comentario,
y su propiedad .data devuelve el texto del comentario.

Por eso el alert muestra: BODY.
*/

