// Algoritmo de Prueba - Samir Caizapasto
// Objetivo: Mostrar errores simples (sintáctico y semántico)

void main() {
  var nombre = "Samir";
  var edad = 22;
  print(nombre);
  print(edad);

  // Lógica correcta
  var numero = 5 + 3;
  print(numero);

  // Para demostrar el error SINTÁCTICO descomenta las dos líneas siguientes:
   var numero = (5 + 3;
   print(numero);
}

void errorSemantico() {
  // ERROR SEMÁNTICO con línea explícita
  print(total);
  break;
}

void loopOk() {
  for (var i = 0; i < 3; i = i + 1) {
    print(i);
  }
}
