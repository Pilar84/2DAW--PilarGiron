//Este bucle es infinito. Nunca termina, ¿por qué?
/* Porque la condición siempre es verdadera, ya que el numero decimal es 0.2
y al hacer la suma nunca llega a ser 10 y se sigue ejecutando */

let i = 0;
while (i != 10) {
i += 0.2;
}

/*
Función random(min, max):
Genera un número aleatorio de punto flotante entre min (incluido) y max (no incluido)
*/

function random(min, max) {
    return Math.random() * (max - min) + min;
}

// Ejemplos de uso
alert(random(1, 5));
alert(random(1, 5));
alert(random(1, 5));
