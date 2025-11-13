function evaluarExpresionMatematica(expresion) {
  // Quitamos espacios
  expresion = expresion.replace(/\s+/g, '');

  // Función recursiva para evaluar expresiones
  function evaluar(tokens) {
    let numeros = [];
    let operadores = [];

    // Convertimos la cadena en tokens de números y operadores
    let i = 0;
    while (i < tokens.length) {
      const char = tokens[i];

      if (char === '(') {
        // Buscamos el paréntesis que cierra
        let contador = 1;
        let j = i + 1;
        while (contador > 0) {
          if (tokens[j] === '(') contador++;
          if (tokens[j] === ')') contador--;
          j++;
        }
        // Evaluamos el contenido dentro del paréntesis
        const subResultado = evaluar(tokens.slice(i + 1, j - 1));
        numeros.push(subResultado);
        i = j; // Saltamos los paréntesis
      } else if (!isNaN(char) || char === '.') {
        // Leemos número completo
        let numStr = char;
        i++;
        while (i < tokens.length && (!isNaN(tokens[i]) || tokens[i] === '.')) {
          numStr += tokens[i];
          i++;
        }
        numeros.push(parseFloat(numStr));
      } else if ('+-*/'.includes(char)) {
        operadores.push(char);
        i++;
      } else {
        i++;
      }
    }

    // Multiplicación y división primero
    for (let k = 0; k < operadores.length; k++) {
      if (operadores[k] === '*' || operadores[k] === '/') {
        let resultado = operadores[k] === '*' ? numeros[k] * numeros[k + 1] : numeros[k] / numeros[k + 1];
        numeros.splice(k, 2, resultado);
        operadores.splice(k, 1);
        k--; // Ajustamos índice
      }
    }

    // Ahora suma y resta
    let resultadoFinal = numeros[0];
    for (let k = 0; k < operadores.length; k++) {
      if (operadores[k] === '+') resultadoFinal += numeros[k + 1];
      if (operadores[k] === '-') resultadoFinal -= numeros[k + 1];
    }

    return resultadoFinal;
  }

  return evaluar(expresion.split(''));
}

// Prueba
const entrada = "3 + (2 * (1 + 5)) / 2";
console.log(evaluarExpresionMatematica(entrada)); 
