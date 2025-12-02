/*Crea un array de objetos que represente una lista de productos, cada uno con
propiedades como nombre, precio, disponible. Filtra los productos que estén
disponibles y cuyo precio sea menor a 20 euros. Luego, transforma el array
resultante para mostrar solo los nombres de los productos.*/

let productos = [
    { nombre: "Pendientes", precio: 5.50, disponible: true },
    { nombre: "Pulseras", precio: 25, disponible: true },
    { nombre: "Collares", precio: 15, disponible: false },
    { nombre: "Anillos", precio: 4.80, disponible: true },
  ];
  
  let productosDisponibles = productos.filter(function(producto) {
    return producto.disponible && producto.precio < 20;
  });
  
  let nombresProductos = productosDisponibles.map(function(producto) {
    return producto.nombre;
  });
  
  console.log(nombresProductos);