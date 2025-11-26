let persona={
    nombre: "Ana",
    edad: 28,
    trabajo: "Ingeniera"
};

//recorremos con un for para mostrar las claves y valores
for (let clave in persona) {
    console.log(clave + ": " + persona[clave]);
}