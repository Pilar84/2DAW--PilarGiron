//selecciona todos los enlaces
const enlaces = document.querySelectorAll('a');

//recorre cada enlace y muestra su href
enlaces.forEach(enlace => {
    console.log(enlace.getAttribute('href'));
});

//comprueba si es un enlace externo
if (href.includes("://") && !href.startsWith("http://internal.com")) {
    // Cambia el color a purple
    link.style.color = "purple";
}

/*
Este ejercicio pinta de color purple los enlaces externos.

Un enlace es externo si:
- Su href contiene ://
- No empieza por http://internal.com

Se recorren todos los <a> y se cambia el estilo
solo a los que cumplen esas condiciones.
*/



