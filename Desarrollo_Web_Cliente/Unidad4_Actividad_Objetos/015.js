//creamos la clase Vehiculo con la propiedad marca
class Vehiculo {
    constructor(marca) {
        this.marca = marca;
    }
    //metodo arrancar
    arrancar() {
        console.log(`El vehiculo de la marca ${this.marca} está arrancando.`);
    }
}
//clase hija llamada Coche
class Coche extends Vehiculo {
    constructor(marca, modelo) {
        super(marca);
        this.modelo = modelo;
    }

    //sobreescribimos el metodo arrancar
    arrancar() {
        console.log(`El coche de la marca ${this.marca} y modelo ${this.modelo} está arrancando.`);
    }
    //metodo detener
    detener() {
        console.log(`El coche de la marca ${this.marca} y modelo ${this.modelo} está detenido.`);
    }
}

let coche = new Coche("Toyota", "Corolla");
coche.arrancar();
coche.detener();