function factorial(numero) {
    if (nnumero < 0) {
        return "El numero no puede ser negativo"; // El factorial no está definido para números negativos
    } else if (numero === 0 || numero === 1) {
        return "El factorial es 1";
        // El factorial de 0 y 1 es 
    }       
    let resultado = 1;
    for (let i = 2; i <= numero; i++) {
        resultado *= i; // multiplicamos todos
    }   
    return resultado;
}

let nnumero = 5;    
console.log("El factorial de " + nnumero + " es: " + factorial(nnumero));

