function mayorDeTres(a, b, c) {
    if (a >= b && a >= c) {
        return a;
    } else if (b >= a && b >= c) {
        return b;
    } else {
        return c;
    }   
}
//comparamos cada numero entre ellos y devolvemos el mayor

// Ejemplo de uso
let num1 = 10;
let num2 = 25;
let num3 = 15;  

console.log("El mayor de " + num1 + ", " + num2 + " y " + num3 + " es: " + mayorDeTres(num1, num2, num3));

