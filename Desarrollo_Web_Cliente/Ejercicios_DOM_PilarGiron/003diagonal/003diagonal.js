/*      
Seleccionar todas las celdas diagonales Escribe el código para pintar todas las 
celdas diagonales de rojo. Necesitarás obtener todas las <td> de la <table> y 
pintarlas usando el código: 
// td debe ser la referencia a la celda de la tabla 
td.style.backgroundColor = 'red'; 

*/
// Selecciona la tabla
const tabla = document.querySelector('table');
// Obtiene todas las filas de la tabla
const filas = tabla.rows;

// Recorre las filas
for (let i = 0; i < filas.length; i++) {
    // Selecciona la celda de la diagonal (misma fila y columna)
    const celdaDiagonal = filas[i].cells[i];
    // Aplica la clase roja a la celda diagonal 
    celdaDiagonal.classList.add("red");
}

