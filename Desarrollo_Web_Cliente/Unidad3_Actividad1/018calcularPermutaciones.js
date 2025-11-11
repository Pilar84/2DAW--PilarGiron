function calcularPermutaciones(array) {
  if (array.length === 1) {
    return [array]; // Caso base: solo un elemento
  }

  const resultado = [];

  for (let i = 0; i < array.length; i++) {
    // Tomamos el elemento actual
    const elemento = array[i];

    // Creamos un array sin el elemento actual
    const resto = array.slice(0, i).concat(array.slice(i + 1));

    // Generamos todas las permutaciones del resto
    const permutacionesResto = calcularPermutaciones(resto);

    // Añadimos el elemento actual a cada permutación del resto
    for (const perm of permutacionesResto) {
      resultado.push([elemento, ...perm]);
    }
  }

  return resultado;
}

// Ejemplo de uso
console.log(calcularPermutaciones([1, 2, 3]));


