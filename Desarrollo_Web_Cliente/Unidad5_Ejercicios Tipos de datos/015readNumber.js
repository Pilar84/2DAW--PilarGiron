/*
readNumber pide un número al visitante hasta que ingrese uno válido.
Si cancela o deja vacío, devuelve null.
*/

function readNumber() {
    while (true) {
        let input = prompt("Ingresa un número:");

        if (input === null || input === "") return null; // canceló o vacío
        let num = Number(input);
        if (!isNaN(num)) return num; // es un número válido
    }
}

// Uso:
let numero = readNumber();
alert("Número ingresado: " + numero);
