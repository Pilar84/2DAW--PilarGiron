function contarCaracteres(cadena) {
    if (typeof cadena !== "string") {
        return "La entrada debe ser una cadena de texto";
    }

    let contador = {};

    for (let i = 0; i < cadena.length; i++) {
        let letra = cadena[i];
        if (contador[letra]) {
            contador[letra] = contador[letra] + 1;
        } else {
            contador[letra] = 1;
        }
    }

    return contador;
}

// ejemplo de uso
let texto = "Buenos días";
console.log(contarCaracteres(texto));

