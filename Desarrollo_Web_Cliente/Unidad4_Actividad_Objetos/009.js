let persona={
    nombre: "Ana",
    edad: 28,
    trabajo: "Ingeniera"
};

function saludar() {
    console.log(`Hola, soy ${this.nombre} y tengo ${this.edad} años`);
}

saludar.call(persona)
    