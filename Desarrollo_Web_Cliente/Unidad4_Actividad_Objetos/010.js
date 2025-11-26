function Coche(marca, modelo, año) {
    this.marca = marca;
    this.modelo = modelo;
    this.año = año;
}

let coche = new Coche("Ford", "Kuga", 2020);
let coche2 = new Coche("Toyota", "Corolla", 2021);
console.log(coche);
console.log(coche2);