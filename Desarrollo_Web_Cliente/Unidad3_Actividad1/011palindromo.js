function palindromo(cadena) {

    // Eliminar espacios, signos de puntuación, y convertir a minúsculas
    let cadenaLimpia = cadena.replace(/[^a-z0-9]/gi, '').toLowerCase();

    // Obtener la cadena invertida
    let cadenaInvertida = cadenaLimpia.split('').reverse().join(''); //split separa la cadena en un array de caracteres, reverse invierte el array, join une el array en una cadena

    // Comparar la cadena limpia con la invertida para saber si son iguales en ambos sentidos
    return cadenaLimpia === cadenaInvertida;
}

// Ejemplo de uso
let texto = "Ana";    
console.log("¿La cadena \"" + texto + "\" es un palíndromo? " + palindromo(texto)); 

