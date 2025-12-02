/*
Función checkSpam:
Devuelve true si el string contiene 'viagra' o 'XXX' (sin importar mayúsculas/minúsculas)
*/

function checkSpam(str) {
    let lowerStr = str.toLowerCase(); // convertimos todo a minúsculas
    return lowerStr.includes("viagra") || lowerStr.includes("xxx");
}

// Ejemplos de uso
alert(checkSpam("compra ViAgRA ahora")); // true
alert(checkSpam("xxxxx gratis"));        // true
alert(checkSpam("coneja inocente"));     // false