// Función que genera una frase aleatoria
function generarFraseAleatoria(palabras) {
  // Selecciona una palabra aleatoria de un array
  function palabraAleatoria(array) {
    const indice = Math.floor(Math.random() * array.length);
    return array[indice];
  }

  // Tomamos una palabra de cada categoría
  const sustantivo = palabraAleatoria(palabras.sustantivos);
  const verbo = palabraAleatoria(palabras.verbos);
  const adjetivo = palabraAleatoria(palabras.adjetivos);

  // Formamos la frase de manera coherente
  const frase = `El ${sustantivo} ${verbo} ${adjetivo}.`;

  return frase;
}

// Ejemplo de uso
const palabras = {
  sustantivos: ["gato", "perro", "ratón", "elefante"],
  verbos: ["salta", "corre", "duerme", "come"],
  adjetivos: ["rápido", "lento", "grande", "pequeño"]
};

console.log(generarFraseAleatoria(palabras)); // Ej: "El elefante duerme lento."
console.log(generarFraseAleatoria(palabras)); // Ej: "El gato corre rápido."