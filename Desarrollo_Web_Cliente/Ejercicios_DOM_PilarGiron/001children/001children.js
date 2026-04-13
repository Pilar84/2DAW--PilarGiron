/*
Para cada una de las siguientes preguntas, da al menos una forma de cómo 
acceder a ellos: 
• ¿El nodo <div> del DOM? 
• ¿El nodo <ul> del DOM? 
El segundo <li> (con Peter Parker)?
*/

// Para acceder al nodo <div> del DOM
document.getElementsByTagName('div')[0]; // Usando getElementsByTagName

// Para acceder al nodo <ul> del DOM
document.body.children[0].children[1]; // Usando children

// Para acceder al segundo <li> (con Peter Parker)
document.getElementsByTagName('li')[1]; // Usando getElementsByTagName





