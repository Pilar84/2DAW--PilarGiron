/* =========================================================================
   EJERCICIOS DOM - THE SOCIAL HUB
   ========================================================================= */

// 1. EDITAR PERFIL
// Al hacer click en 'btn-editar-perfil', usa un prompt para preguntar el nuevo nombre.
// Actualiza el texto de 'nombre-usuario' con el resultado.
// TU CÓDIGO AQUÍ:


// 2. CONTADOR DE CARACTERES
// Mientras el usuario escribe en 'post-texto', actualiza el span 'char-count'.
// El formato debe ser "X / 150". 
// Pista: usa el evento 'input' y la propiedad .length del valor del textarea.
// TU CÓDIGO AQUÍ:


// 3. BOTÓN SEGUIR/DEJAR DE SEGUIR
// Al pulsar 'btn-seguir', si el botón dice "Siguiendo":
// - Cambia el texto a "Seguir".
// - Cambia la clase a "no-siguiendo".
// - Resta 1 al contador de seguidores ('count-seguidores').
// Si dice "Seguir", haz lo contrario.
// TU CÓDIGO AQUÍ:


// 4. PUBLICAR UN POST (CREACIÓN DE NODOS)
// Al hacer click en 'btn-publicar':
// 1. Crea un nuevo <article> con la clase 'post'.
// 2. Añade dentro el HTML necesario (puedes usar innerHTML para simplificar).
// 3. El contenido del post debe ser lo que el usuario escribió en el textarea.
// 4. Insértalo al principio de 'lista-posts' usando prepend().
// 5. Limpia el textarea y el contador de caracteres.
// TU CÓDIGO AQUÍ:


// 5. SISTEMA DE LIKES (DELEGACIÓN DE EVENTOS)
// Crea una función para que al pulsar cualquier botón 'btn-like':
// - Se añada/quite la clase 'liked'.
// - Se sume o reste 1 al número que hay en el span de dentro.
// TU CÓDIGO AQUÍ:


// 6. ELIMINAR NOTIFICACIONES
// Al hacer click en el icono de notificaciones ('notificaciones'),
// pon el número de 'num-notificaciones' a 0 y oculta el círculo rojo (o el span).
// TU CÓDIGO AQUÍ:


// 7. BORRAR POSTS
// Haz que el botón 'btn-borrar' elimine el post completo al hacer click.
// (Ten en cuenta que para los nuevos posts creados dinámicamente, 
// deberás asignar el evento al crearlos o usar delegación).
// TU CÓDIGO AQUÍ: