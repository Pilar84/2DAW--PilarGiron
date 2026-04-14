/*
Aquí está el documento con la tabla y el formulario. 
¿Cómo encontrar?… 
La tabla con id="age-table". 
Todos los elementos labeldentro de la tabla (debería haber 3). 
El primer td en la tabla (con la palabra “Age”). 
El form con name="search". 
El primer input en ese formulario. 
El último input en ese formulario.
*/

// La tabla con id="age-table"
const ageTable = document.getElementById('age-table');
console.log(ageTable);

// Todos los elementos label dentro de la tabla (debería haber 3)
const labelsInTable = ageTable.querySelectorAll('label');
console.log(labelsInTable);

// El primer td en la tabla (con la palabra “Age”)
const firstTd = ageTable.querySelector('td');
console.log(firstTd);

// El form con name="search"
const searchForm = document.querySelector('form[name="search"]');
console.log(searchForm);

// El primer input en ese formulario
const firstInput = searchForm.querySelector('input');
console.log(firstInput);

// El último input en ese formulario
const inputs = searchForm.querySelectorAll('input');
const lastInput = inputs[inputs.length - 1];
console.log(lastInput);



