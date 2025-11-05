function esPar(numero) {
    if (numero % 2 === 0) {
        return true;
    } else{
        return false;
    }
}
console.log("El número 4 es par: "  +  esPar(4)); // true
console.log("El numero 7 es impar: "  + esPar(7)); // false

