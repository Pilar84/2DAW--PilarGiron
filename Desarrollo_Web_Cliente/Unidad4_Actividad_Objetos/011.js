

let id = Symbol("id");
let empleado={
    [id]: 1,
    nombre: "Ana",
    edad: 28,
    trabajo: "Ingeniera"
};
//COMPROBAMOS QUE NO MUUESTRA EL ID, LO IGNORA
for (let clave in empleado) {
    console.log(clave + ": " + empleado[clave]);
}