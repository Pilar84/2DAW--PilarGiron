<script>
    let body = document.body;
    body.innerHTML = "&lt;!--" + body.tagName + "--&gt;";
    alert( body.firstChild.data ); // ¿qué hay aquí?
</script>


//El código muestra BODY porque se inserta un comentario con el nombre de la etiqueta y luego se lee el texto del nodo de comentario.

