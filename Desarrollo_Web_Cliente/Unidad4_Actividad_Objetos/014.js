//crear clase CuentaBancaria con encapsulacion usando propiedades privadas
class CuentaBancaria {
    #saldo = 0;
    constructor(nombreTitular, saldoInicial) {
        this.nombreTitular = nombreTitular;
        this.#saldo = saldoInicial;
    }

    //obtener saldpo
    obtenerSaldo() {
        return this.#saldo;
    }
    //depositar monto
    depositar(monto) {
        if (monto > 0) {
            this.#saldo += monto;
            console.log(`Deposito realizado. Nuevo saldo: ${this.#saldo}EUR`);
        } else {
            console.log("El monto debe ser mayor que 0.");
        }
    }

    //retirar monto
    retirar(monto) {
        if (monto <= this.#saldo) {
            this.#saldo -= monto;
            console.log(`Retiro realizado. Nuevo saldo: ${this.#saldo}EUR`);
        } else {
            console.log("Saldo insuficiente.");
        }
    }

}

let cuenta = new CuentaBancaria("Pilar", 1000);
console.log(cuenta.obtenerSaldo());
cuenta.depositar(500);
cuenta.retirar(200);

//comprueba que no es posible acceder a la propiedad privada
//console.log(cuenta.#saldo);