function buscarSubsecuenciaMasLarga(cadena1, cadena2) {
    // Caso base: si alguna cadena está vacía, la subsecuencia es vacía
    if (cadena1.length === 0 || cadena2.length === 0) {
        return "";
    }

    // Tomamos el último carácter de cada cadena
    const ultimo1 = cadena1[cadena1.length - 1];
    const ultimo2 = cadena2[cadena2.length - 1];

    // Si los últimos caracteres coinciden
    if (ultimo1 === ultimo2) {
        // Incluimos este carácter en la subsecuencia y seguimos con el resto de las cadenas
        return buscarSubsecuenciaMasLarga(
            cadena1.slice(0, -1), // cadena1 sin el último carácter
            cadena2.slice(0, -1)  // cadena2 sin el último carácter
        ) + ultimo1;
    } else {
        // Si no coinciden, probamos dos opciones:
        // 1. Ignorar el último carácter de la primera cadena
        const opcion1 = buscarSubsecuenciaMasLarga(cadena1.slice(0, -1), cadena2);//slice toma una parte de la cadena desde el índice 0 hasta el índice -1 (sin incluir el último carácter)
        // 2. Ignorar el último carácter de la segunda cadena
        const opcion2 = buscarSubsecuenciaMasLarga(cadena1, cadena2.slice(0, -1));
        
        // Devolvemos la opción más larga
        return opcion1.length > opcion2.length ? opcion1 : opcion2;
    }
}

// Ejemplo de uso:
const cadena1 = "ABCBDAB";
const cadena2 = "BDCAB";

const resultado = buscarSubsecuenciaMasLarga(cadena1, cadena2);

console.log(`La subsecuencia común más larga es: "${resultado}"`); 

