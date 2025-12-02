/*Crea un objeto que represente un estudiante con las siguientes propiedades:
nombre, edad, carrera. Agrega un método al objeto que muestre la información del
estudiante en la consola. Luego, cambia la propiedad edad y vuelve a mostrar la
información.*/

let estudiante = {
    nombre: "Pilar",
    edad: 40,
    carrera: "Desarrollo Web",

    info: function () {
        console.log(`Nombre del estudiante: ${this.nombre} , Edad: ${this.edad} , Carrera: ${this.carrera}`);
    }

};



estudiante.info()
estudiante.edad = 30
estudiante.info()