/* =========================================================================
   EJERCICIOS DOM - TECHSTORE
   Completa el código debajo de cada enunciado.
========================================================================= */

// EJERCICIO 1: Actualizar el contador del carrito.
// Selecciona todos los botones con la clase 'btn-comprar'.
// Recórrelos y añade un evento de 'click' a cada uno.
// Cada vez que se haga click, el número dentro del span con id 'contador-carrito' debe sumar 1.


// 1. Selecciona el elemento del contador y los botones de compra
// 2. Añade el evento click a los botones
// TU CÓDIGO AQUÍ:

let contadorCarrito = 0;
//seleccionamos elemento contador y botones de compra
const contador = document.getElementById('contador-carrito');
const botones = document.querySelectorAll('.btn-comprar');
//recorremos los botones y añadimos el evento click
botones.forEach(boton => {
   boton.addEventListener('click', () => {
      //subamos 1 al contador cada vez que se haga click
      contadorCarrito++;
      contador.textContent = contadorCarrito;
   });
});


// -------------------------------------------------------------------------
// EJERCICIO 2: Modo Oscuro (Manipulación de Clases).
// Selecciona el botón con id 'btn-tema'.
// Al hacer click en él, debes alternar (toggle) la clase 'modo-oscuro' en el elemento <body>.
// Si el body tiene la clase, cambia el texto del botón a "Modo Claro". Si no, a "Modo Oscuro".

// TU CÓDIGO AQUÍ:
//seleccionamos el boton con id btn-tema
const btnTema = document.getElementById('btn-tema');
//añadimos el evento click
btnTema.addEventListener('click', () => {
   //alternamos la clase modo-oscuro en el body
   document.body.classList.toggle('modo-oscuro');
   //cambiamos el texto del boton
   if (document.body.classList.contains('modo-oscuro')) {
      btnTema.textContent = 'Modo Claro';
   } else {
      btnTema.textContent = 'Modo Oscuro';
   }
});



// -------------------------------------------------------------------------
// EJERCICIO 3: Formulario y Eventos por defecto (Prevenir recarga).
// Selecciona el formulario de la newsletter (id 'form-newsletter').
// Escucha el evento 'submit'.
// 1. Evita que la página se recargue (preventDefault).
// 2. Obtén el valor del input del email.
// 3. Muestra un mensaje en el párrafo con id 'mensaje-suscripcion' que diga: "¡Gracias por suscribirte, [EMAIL]!".
// 4. Limpia el input del email.

// TU CÓDIGO AQUÍ:

//seleccionamos el formulario
const formNewsletter = document.getElementById('form-newsletter');
const mensaje = document.getElementById('mensaje-suscripcion');
//escuchamos el evento submit
const inputEmail = document.getElementById('email-input');
formNewsletter.addEventListener('submit', (e) => {
   //evitamos que la pagina se recargue
   e.preventDefault();
   //obtenemos el valor del input
   const email = inputEmail.value;
   //mostramos el mensaje
   mensaje.textContent = `¡Gracias por suscribirte, ${email}!`;
   //limpiamos el input
   inputEmail.value = '';
});



// -------------------------------------------------------------------------
// EJERCICIO 4: Creación de Nodos en el DOM.
// Queremos mostrar una notificación temporal cuando alguien añade algo al carrito.
// Modifica la lógica del Ejercicio 1 (o crea una nueva función aquí) para que, al hacer click en "Añadir al carrito":
// 1. Se cree un elemento <div>.
// 2. Se le asigne la clase 'alerta-exito' (ya definida en CSS).
// 3. Su texto sea "Producto añadido correctamente".
// 4. Se inserte dentro del div con id 'contenedor-mensajes'.
// 5. Usa setTimeout para eliminar este div del DOM pasados 3 segundos.

// TU CÓDIGO AQUÍ:
// creamos el elemento div
const div = document.createElement('div');
//le asignamos la clase alerta-exito
div.classList.add('alerta-exito');
//le asignamos el texto
div.textContent = 'Producto agregado correctamente';
//lo insertamos dentro del div con id contenedor-mensajes
document.getElementById('contenedor-mensajes').appendChild(div);
//usamos setTimeout para eliminar el div del DOM pasados 3 segundos
setTimeout(() => {
   div.remove();
}, 3000);



// -------------------------------------------------------------------------
// EJERCICIO 5: Navegación por el DOM y eliminación de elementos.
// Selecciona todos los botones con la clase 'btn-eliminar'.
// Al hacer click en uno de ellos, debes eliminar el producto de la pantalla.
// Pista: El botón está dentro de un <article>. Usa `parentElement` para seleccionar el artículo completo y luego el método `remove()`.

// TU CÓDIGO AQUÍ:



// -------------------------------------------------------------------------
// EJERCICIO 6: El Intercambiador de Vistas (Toggle de Atributos).
// Al hacer clic en la imagen de un producto, debe ocurrir lo siguiente:
// 1. Intercambiar el valor del atributo 'src' con el del atributo 'data-img-alt'.
//    (Pista: guarda el src actual en una variable temporal antes de cambiarlo).
// 2. Alternar (toggle) la clase CSS 'img-enfocada' en la propia imagen.
// 3. Extra: Haz que aparezca un pequeño texto flotante que diga "Vista detalle" 
//    sobre la imagen solo cuando esté seleccionada.

// TU CÓDIGO AQUÍ:



// -------------------------------------------------------------------------
// EJERCICIO EXTRA (Reto): Destacar producto.
// Al pasar el ratón ('mouseenter') por encima de una tarjeta de producto (<article>), 
// añádele la clase 'destacado'.
// Al quitar el ratón ('mouseleave'), quítale la clase 'destacado'.

// TU CÓDIGO AQUÍ:


// -------------------------------------------------------------------------
// EJERCICIO 7: Efecto Zoom (MouseEnter y MouseLeave).
// Queremos que cuando el usuario pase el ratón sobre la imagen de un producto,
// esta se agrande suavemente.
// 1. Selecciona todas las imágenes con la clase 'producto-img'.
// 2. Recórrelas y añade dos eventos a cada una:
//    - 'mouseenter': Añade la clase CSS 'img-agrandada'.
//    - 'mouseleave': Elimina la clase CSS 'img-agrandada'.
// Pista: Usa `event.target` o `this` dentro de la función del evento para referirte a la imagen concreta.

// TU CÓDIGO AQUÍ: