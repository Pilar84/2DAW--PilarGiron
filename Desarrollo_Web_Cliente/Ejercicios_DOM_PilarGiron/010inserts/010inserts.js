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



