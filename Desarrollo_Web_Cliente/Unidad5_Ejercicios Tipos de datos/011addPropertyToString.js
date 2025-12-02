/*¿Puedo agregar una propiedad a un string?: Considera el siguiente código:
Qué piensas: ¿funcionará? ¿Qué mostrará? ¿Por qué?*/

/* En JavaSCript no se puede agregar propiedades a un string directamente.Tendria que crear 
un objeto y agregar la propiedad.
Por tanto este codigo no funcionará y mostrara undefined, porque no se puede agregar 
propiedades a un string directamente.*/

let str = "Peter";
str.test = 5;
alert(str.test);



