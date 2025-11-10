function combinaciones(cadena) {
    let resultados = [];

    // recorrer todos los caracteres
    for (let i = 0; i < cadena.length; i++) {
        for (let j = i + 1; j <= cadena.length; j++) {
            resultados.push(cadena.slice(i, j));
        }
    }

    return resultados;
}

// ejemplo de uso
let texto = "Pilar";
console.log(combinaciones(texto));