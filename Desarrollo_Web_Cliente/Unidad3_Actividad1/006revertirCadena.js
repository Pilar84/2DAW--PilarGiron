function revertirCadena(cadena) {

    let cadenaRevertida = '';//inicializamos una variable vacía para almacenar la cadena revertida

    for (let i = cadena.length - 1; i >= 0; i--) {//recorremos la cadena de atras hacia adelante
        cadenaRevertida += cadena[i];//acumulamos cada caracter 
    }       
    return cadenaRevertida;
}

console.log(revertirCadena("Mi nombre es Pilar")); 




