usuario1={
    nombre: "Pilar",
    edad: 40,
    email: "pilar@pilar.com"
    }
//aqui hacemos copia por referencia
let usuario2=usuario1

usuario2.edad=50
console.log(usuario1.edad)
console.log(usuario2.edad)
