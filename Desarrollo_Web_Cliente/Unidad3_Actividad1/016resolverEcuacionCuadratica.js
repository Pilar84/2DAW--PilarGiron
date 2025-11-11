function resolverEcuacionCuadratica (a, b, c) {
    if (a === 0) {
        return "El coeficiente 'a' no puede ser cero en una ecuación cuadrática.";
    }

    //calcular el discriminante, es decir, lo que está dentro de la raíz cuadrada
    let discriminante = (b ** 2) - (4 * a * c);

    //si el discriminante es negativo, no hay soluciones reales
    if (discriminante < 0) {
        return "No hay soluciones reales.";
    }

    //aplicar la fórmula cuadrática
    let sqrtDiscriminante = Math.sqrt(discriminante);//calcular la raíz cuadrada del discriminante
    let x1 = (-b + sqrtDiscriminante) / (2 * a);//usa el signo positivo para la primera solución
    let x2 = (-b - sqrtDiscriminante) / (2 * a);   //usa el signo negativo para la segunda solución 

    //devuelver las soluciones
    return { x1, x2 };
}


// ejemplo de uso
console.log(resolverEcuacionCuadratica(1, -3, 2)); 
console.log(resolverEcuacionCuadratica(1, 2, 1));  
console.log(resolverEcuacionCuadratica(1, 0, 1));   


    