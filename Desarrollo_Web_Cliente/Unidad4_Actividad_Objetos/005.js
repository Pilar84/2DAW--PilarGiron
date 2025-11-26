let persona={
    nombre: "Ana",
    edad: 28,
    trabajo: "Ingeniera"
};

//comprobamos is la propiedad nombre existe en el objeto persona
//devuelve true si existe
console.log("nombre" in persona);

//comprobamos si la propiedad apellido existe en el objeto persona
//devuelve false si no existe
console.log("apellido" in persona);

