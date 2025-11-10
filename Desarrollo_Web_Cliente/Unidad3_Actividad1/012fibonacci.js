function fibonacci(numero) {
    if (numero <= 0) {
        return []; // devuelve lista vacia
    } else if (numero === 1) {
        return [0]; // devuelve el primer número de Fibonacci
    } else if (numero === 2) {
        return [0, 1]; // devuelve los dos primerps números de Fibonacci
    }   
    let secuencia = [0, 1]; // Inicializa la secuencia con los dos primeros números
    for (let i = 2; i < numero; i++) {
        // Calcula el siguiente número sumando los dos anteriores
        let siguienteNumero = secuencia[i - 1] + secuencia[i - 2];
        secuencia.push(siguienteNumero); // Agrega el siguiente número a la secuencia
    }
    return secuencia; // Retorna la secuencia completa
}

// Ejemplo de uso
let cantidad = 10;    
console.log("Los primeros " + cantidad + " números de la secuencia de Fibonacci son: " + fibonacci(cantidad));      
