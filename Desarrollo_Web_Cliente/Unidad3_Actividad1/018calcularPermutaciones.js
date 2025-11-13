function calcularPermutaciones(array) {
  // Caso base: si solo hay un elemento, la única permutación es el mismo array
  if (array.length === 1) {
    return [array]; // Devuelve un array dentro de un array
  }

  const resultado = []; // Aquí vamos a guardar todas las permutaciones

  // Recorremos cada elemento del array
  for (let i = 0; i < array.length; i++) {
    const elemento = array[i]; // Tomamos un elemento

    // Creamos un array con todos los elementos menos el actual
    const resto = array.slice(0, i).concat(array.slice(i + 1));

    // Calculamos todas las permutaciones posibles del resto (recursión)
    const permutacionesResto = calcularPermutaciones(resto);

    // Para cada permutación del resto, agregamos el elemento actual al principio
    for (const perm of permutacionesResto) {
      resultado.push([elemento, ...perm]);
    }
  }

  return resultado; // Devolvemos todas las permutaciones encontradas
}

// Ejemplo de uso
const entrada = [1, 2, 3];
const salida = calcularPermutaciones(entrada);
console.log(salida);

