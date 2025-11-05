function contarVocales(cadena) {   
    let contador = 0;
    let vocales = ['a','e','i','o','u','A','E','I','O','U','á','é','í','ó','ú','Á','É','Í','Ó','Ú']; // ponemos las vocales con tilde también, incluyendo mayúsculas y minúsculas en una lista

    for (let i = 0; i < cadena.length; i++) {//recorremos cad elemento de la lista
        if (vocales.includes(cadena[i])) {//comprobamos si el elemento actual está en la lista de vocales
            contador++;
        }   
    } 
    return contador;
}  
console.log(contarVocales("Bienvenido a Entorno Cliente"));