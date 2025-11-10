function esPrimo(numero) {
    if (numero <= 1) {
        return false; // Los números menores o iguales a 1 no son primos
    }
    for (let i = 2; i < numero; i++) {
        if (numero % i === 0) {
            return false; // Si encuentra algun nuemero que al dividirlo el resto es 0, no es primo
        }   
    }
    return true; // No se encontraron divisores, es primo
}
// Verificamos si un número es primo comprobando divisores desde 2 hasta la raíz cuadrada del número

// Ejemplo de uso
let numero =10;    
console.log("¿El número " + numero + " es primo? " + esPrimo(numero));

