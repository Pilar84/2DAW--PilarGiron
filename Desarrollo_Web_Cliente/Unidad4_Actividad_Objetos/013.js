//creamos clase animal
class Animal {
    constructor(nombre) {
        this.nombre = nombre
    }
    //metodo hacer sonido
    hacerSonido() {
         console.log(`${this.nombre} está haciendo un sonido.`);

    }
}

//creamos la clase hija Perro que extienda de Animal
class Perro extends Animal {
    constructor(nombre, raza) {
        super(nombre)
        this.raza = raza
    }
    //modifco el metodo hacer sonido
    hacerSonido() {
        console.log(`${this.nombre} está ladrando.`);
    }
    //metodo que muestre el nombre y la raza
    info(){
        console.log(`${this.nombre} es un ${this.raza}`);
    }
}

let miPerro=new Perro("Rex","Pastor Aleman")
miPerro.hacerSonido()
miPerro.info()

