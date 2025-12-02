/*
Función random(min, max):
Genera un número aleatorio de punto flotante entre min (incluido) y max (no incluido)
*/

function random(min, max) {
    return Math.random() * (max - min) + min;
}

// Ejemplos de uso
alert(random(1, 5));
alert(random(1, 5));
alert(random(1, 5));
