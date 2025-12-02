/*Crea una variable que almacene la fecha y hora actual usando el constructor
Date(). Luego, realiza las siguientes acciones:
Muestra el año actual.
Extrae y muestra el día de la semana (como texto, no número).*/

let fecha = new Date();
//devuelve el año actual
console.log("Año actual: " + fecha.getFullYear());
//devuelve el dia de la semana, localizacion español y formato largo
console.log("Día de la semana: " + fecha.toLocaleDateString('es-ES', {weekday: 'long'}));