function filtrarPares(array_numeros) {
    return array_numeros.filter(function(numero) {
        return numero % 2 === 0; // Devuelve true si el número es par
    });
}
array_numeros=[1,2,3,4,5,6,7,8,9,10]; // Ejemplo de array de números    
console.log("Números pares en el array: " + filtrarPares(array_numeros));

