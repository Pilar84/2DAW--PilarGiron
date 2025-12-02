/*
Función randomInteger(min, max):
Devuelve un número entero aleatorio entre min y max, ambos incluidos.
*/

function randomInteger(min, max) {
    // Math.random() -> 0..1
    // Multiplicamos por (max - min + 1) para incluir max
    // Math.floor para redondear hacia abajo
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Ejemplos de uso
alert(randomInteger(1, 5));
alert(randomInteger(1, 5));
alert(randomInteger(1, 5));