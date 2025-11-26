usuario1={
    nombre: "Pilar",
    edad: 40,
    email: "pilar@pilar.com"
    }

//clonacion superficial
let usuario2=Object.assign({},usuario1)
usuario2.edad=50
usuario2.nombre="Maria"
console.log(usuario1.edad)
console.log(usuario2.edad)  
console.log(usuario1.nombre)
console.log(usuario2.nombre)

