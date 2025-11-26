const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let carrito = {};

rl.question("Introduce el nombre del producto1: ", function(producto1) {
  rl.question("Cantidad de " + producto1 + ": ", function(cantidad1) {
    carrito[producto1] = parseInt(cantidad1, 10);

    rl.question("Introduce el nombre del producto2: ", function(producto2) {
      rl.question("Cantidad de " + producto2 + ": ", function(cantidad2) {
        carrito[producto2] = parseInt(cantidad2, 10);

        rl.question("Introduce el nombre del producto3: ", function(producto3) {
          rl.question("Cantidad de " + producto3 + ": ", function(cantidad3) {
            carrito[producto3] = parseInt(cantidad3, 10);

            console.log("Carrito final:", carrito);
            rl.close();
          });
        });
      });
    });
  });
});
