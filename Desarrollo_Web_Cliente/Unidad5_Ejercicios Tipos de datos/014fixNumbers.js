/*¿Por qué 6.35.toFixed(1) == 6.3? Según la documentación Math.round y toFixed
redondean al número más cercano: 0..4 hacia abajo mientras 5..9 hacia arriba.
Por ejemplo: alert( 1.35.toFixed(1) ); // 1.4
En el ejemplo similar que sigue, ¿por qué 6.35 es redondeado a 6.3, y no a 6.4?
alert( 6.35.toFixed(1) ); // 6.3

Por la precisión limitada de los decimales en binario. Internamente 6.35 es un poco menor, así que se redondea hacia abajo.

¿Cómo redondear 6.35 de manera correcta?
Multiplicar antes de redondear y luego dividir, como el siguiente ejemplo
*/

alert( 6.35 * 10 ); // 63.5
alert( Math.round(63.5) / 10 ); // 6.4

