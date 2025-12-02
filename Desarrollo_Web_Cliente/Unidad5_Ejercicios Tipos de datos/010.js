/*Crea un objeto que represente una empresa con las siguientes propiedades:
• nombre (string)
• ubicacion (objeto con pais, ciudad)
• empleados (array de objetos que representen empleados con propiedades
nombre y puesto)
Realiza las siguientes operaciones:
• Muestra la ciudad de la empresa.
• Añade un nuevo empleado al array.
• Muestra la lista de empleados en la consola.*/

let empresa = {
    nombre: "PilarGiron",
    ubicacion: {
        pais: "España",
        ciudad: "Córdoba"
    },
    empleados: [
        { nombre: "Empleado 1", puesto: "jefe" },
        { nombre: "Empleado 2", puesto: "programador" },
        { nombre: "Empleado 3", puesto: "secretaria" }
    ]
};

//mostrar ciudad empresa
console.log("Ciudad de la empresa: " + empresa.ubicacion.ciudad);

//añadir empleado
empresa.empleados.push({ nombre: "Empleado 4", puesto: "diseñador" });

//mostrar empleados
console.log(empresa.empleados);