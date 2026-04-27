/* =========================================================================
   EJERCICIOS DOM - THE SOCIAL HUB
   ========================================================================= */

// 1. EDITAR PERFIL
// Al hacer click en 'btn-editar-perfil', usa un prompt para preguntar el nuevo nombre.
// Actualiza el texto de 'nombre-usuario' con el resultado.
// TU CÓDIGO AQUÍ:

document.getElementById('btn-editar-perfil').addEventListener('click', () => {
   const nuevoNombre = prompt('Introduce tu nuevo nombre');

   if (nuevoNombre && nuevoNombre.trim() !== '') {
      document.getElementById('nombre-usuario').textContent = nuevoNombre;
   }
});


// 2. CONTADOR DE CARACTERES
// Mientras el usuario escribe en 'post-texto', actualiza el span 'char-count'.
// El formato debe ser "X / 150".
// Pista: usa el evento 'input' y la propiedad .length del valor del textarea.
// TU CÓDIGO AQUÍ:

const textarea = document.getElementById('post-texto');
const charCount = document.getElementById('char-count');

textarea.addEventListener('input', () => {
   const caracteres = textarea.value.length;
   charCount.textContent = `${caracteres} / 150`;

   if (caracteres > 150) {
      textarea.value = textarea.value.slice(0, 150);
   }
});


// 3. BOTÓN SEGUIR/DEJAR DE SEGUIR
// Al pulsar 'btn-seguir', si el botón dice "Siguiendo":
// - Cambia el texto a "Seguir".
// - Cambia la clase a "no-siguiendo".
// - Resta 1 al contador de seguidores ('count-seguidores').
// Si dice "Seguir", haz lo contrario.
// TU CÓDIGO AQUÍ:

document.getElementById("btn-seguir").addEventListener("click", (e) => {
   const btn = e.target;
   const contador = document.getElementById("count-seguidores");

   let seguidores = parseInt(contador.textContent);

   if (btn.classList.contains("siguiendo")) {
      // Dejar de seguir
      btn.classList.remove("siguiendo");
      btn.classList.add("no-siguiendo");
      btn.textContent = "Seguir";
      contador.textContent = seguidores - 1;
   } else {
      // Seguir
      btn.classList.remove("no-siguiendo");
      btn.classList.add("siguiendo");
      btn.textContent = "Siguiendo";
      contador.textContent = seguidores + 1;
   }
});



// 4. PUBLICAR UN POST (CREACIÓN DE NODOS)
// Al hacer click en 'btn-publicar':
// 1. Crea un nuevo <article> con la clase 'post'.
// 2. Añade dentro el HTML necesario (puedes usar innerHTML para simplificar).
// 3. El contenido del post debe ser lo que el usuario escribió en el textarea.
// 4. Insértalo al principio de 'lista-posts' usando prepend().
// 5. Limpia el textarea y el contador de caracteres.
// TU CÓDIGO AQUÍ:

document.getElementById('btn-publicar').addEventListener('click', () => {
   const textarea = document.getElementById('post-texto');
   const charCount = document.getElementById('char-count');
   const texto = textarea.value.trim();

   if (!texto) return;

   const post = document.createElement('article');
   post.classList.add('post');

   post.innerHTML = `
      <div class="post-header"><strong>@dev_master</strong> ahora</div>
      <div class="post-content">${texto}</div>
      <div class="post-actions">
         <button class="btn-like">❤️ <span class="likes-count">0</span></button>
         <button class="btn-borrar">Eliminar</button>
      </div>
   `;

   document.getElementById('lista-posts').prepend(post);

   textarea.value = '';
   charCount.textContent = '0/150';
});
// 5. SISTEMA DE LIKES (DELEGACIÓN DE EVENTOS)
// Crea una función para que al pulsar cualquier botón 'btn-like':
// - Se añada/quite la clase 'liked'.
// - Se sume o reste 1 al número que hay en el span de dentro.
// TU CÓDIGO AQUÍ:

document.getElementById('lista-posts').addEventListener('click', (e) => {

   // ❤️ LIKE
   if (e.target.classList.contains('btn-like')) {
      const btn = e.target;
      const span = btn.querySelector('.likes-count');

      let likes = Number(span.textContent);

      if (btn.classList.contains('liked')) {
         btn.classList.remove('liked');
         span.textContent = likes - 1;
      } else {
         btn.classList.add('liked');
         span.textContent = likes + 1;
      }
   }
});


// 6. ELIMINAR NOTIFICACIONES
// Al hacer click en el icono de notificaciones ('notificaciones'),
// pon el número de 'num-notificaciones' a 0 y oculta el círculo rojo (o el span).
// TU CÓDIGO AQUÍ:

document.getElementById('notificaciones').addEventListener('click', () => {
   const num = document.getElementById('num-notificaciones');

   num.textContent = '0';
   num.style.display = 'none';
});


// 7. BORRAR POSTS
// Haz que el botón 'btn-borrar' elimine el post completo al hacer click.
// (Ten en cuenta que para los nuevos posts creados dinámicamente,
// deberás asignar el evento al crearlos o usar delegación).
// TU CÓDIGO AQUÍ:

document.getElementById('lista-posts').addEventListener('click', (e) => {

   if (e.target.classList.contains('btn-borrar')) {
      const post = e.target.closest('.post');
      if (post) post.remove();
   }

});